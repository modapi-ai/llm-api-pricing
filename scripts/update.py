"""Rebuild data/models.json, data/models.csv and the README tables from https://modapi.ai/api/pricing.

Usage: python scripts/update.py
No API key is needed; the pricing endpoint is public. Prices are USD per 1M tokens,
rounded to 4 significant digits as shown on https://modapi.ai/pricing. For models with
tiered pricing (by context length), the entry tier is used. A model keeps its `updated`
date until its price changes, so the files only change when a price does.
If any price changed, a commit message describing the changes is written to .commit-msg.
"""
import csv
import datetime
import io
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = "https://modapi.ai/api/pricing"
SKIP_VENDORS = {"TypeSafe", "Ollama"}
SKIP_MODEL_WORDS = ("embedding", "rerank")
VENDOR_LABEL = {"Moonshot AI": "Moonshot (Kimi)", "Z.ai": "Zhipu (GLM)", "Alibaba Cloud": "Alibaba (Qwen)"}
SEARCH = {"Anthropic": "claude", "Google": "gemini", "xAI": "grok", "Moonshot (Kimi)": "kimi",
          "Zhipu (GLM)": "glm", "Alibaba (Qwen)": "qwen", "OpenAI": "gpt", "Xiaomi": "mimo"}
UTM = "utm_source=github&utm_medium=referral&utm_campaign=offsite_seo"
TIER = re.compile(r"p\s*\*\s*([\d.]+)\s*\+\s*c\s*\*\s*([\d.]+)")
FIELDS = ["vendor", "model", "input", "output", "updated"]
START, END = "<!-- pricing:start -->", "<!-- pricing:end -->"


def sig4(v):
    return float(f"{v:.4g}")


def price(m, group_ratio):
    groups = [g for g in (m.get("enable_groups") or []) if g.startswith("LLM_")]
    ratio = min(group_ratio.get(g, 1) for g in groups)
    hit = TIER.search(m.get("billing_expr") or "")
    if hit:
        i, o = float(hit.group(1)), float(hit.group(2))
    elif m.get("model_ratio") is not None:
        i = m["model_ratio"] * 2
        o = i * (m.get("completion_ratio") or 1)
    else:
        return None
    return sig4(i * ratio), sig4(o * ratio)


def fetch():
    req = urllib.request.Request(URL, headers={"User-Agent": "llm-api-pricing-updater"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    vendors = {v["id"]: v["name"] for v in data["vendors"]}
    rows = []
    for m in data["data"]:
        if not any(g.startswith("LLM_") for g in (m.get("enable_groups") or [])):
            continue
        if any(w in m["model_name"] for w in SKIP_MODEL_WORDS):
            continue
        vendor = vendors.get(m.get("vendor_id"), "Other")
        if vendor in SKIP_VENDORS:
            continue
        p = price(m, data["group_ratio"])
        if p is None:
            continue
        rows.append({"vendor": VENDOR_LABEL.get(vendor, vendor), "model": m["model_name"],
                     "input": p[0], "output": p[1]})
    return rows


def fmt(v):
    return f"${v:g}" if v >= 0.0001 else f"${v:.4g}"


def readme_tables(rows):
    by_vendor = {}
    for r in rows:
        by_vendor.setdefault(r["vendor"], []).append(r)
    out = []
    for vendor in sorted(by_vendor, key=lambda v: (-len(by_vendor[v]), v)):
        items = sorted(by_vendor[vendor], key=lambda r: r["model"])
        q = SEARCH.get(vendor, vendor.split(" ")[0].lower())
        out += [f"### {vendor}", "",
                f"{len(items)} models · live prices: [modapi.ai/pricing?search={q}](https://modapi.ai/pricing?search={q}&{UTM})", "",
                "| Model | Input $/1M | Output $/1M |", "|---|---:|---:|"]
        out += [f"| `{r['model']}` | {fmt(r['input'])} | {fmt(r['output'])} |" for r in items]
        out.append("")
    return "\n".join(out)


def main():
    today = datetime.date.today().isoformat()
    json_path, csv_path, readme = ROOT / "data/models.json", ROOT / "data/models.csv", ROOT / "README.md"
    old = {}
    if json_path.exists():
        old = {(r["vendor"], r["model"]): r for r in json.loads(json_path.read_text())["models"]}
    rows, changes = [], []
    for r in fetch():
        prev = old.pop((r["vendor"], r["model"]), None)
        if prev and (prev["input"], prev["output"]) == (r["input"], r["output"]):
            r["updated"] = prev["updated"]
        else:
            r["updated"] = today
            if prev:
                changes.append(f"- {r['model']}: input {fmt(prev['input'])} -> {fmt(r['input'])}, "
                               f"output {fmt(prev['output'])} -> {fmt(r['output'])}")
            elif json_path.exists():
                changes.append(f"- added {r['model']}: {fmt(r['input'])} / {fmt(r['output'])}")
        rows.append(r)
    changes += [f"- removed {m}" for (_v, m) in sorted(old)]
    rows.sort(key=lambda r: (r["vendor"], r["model"]))

    json_path.write_text(json.dumps({"source": URL, "unit": "USD per 1M tokens", "models": rows}, indent=1) + "\n")
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    csv_path.write_text(buf.getvalue())
    text = readme.read_text()
    head, rest = text.split(START, 1)
    _old_tables, tail = rest.split(END, 1)
    readme.write_text(f"{head}{START}\n{readme_tables(rows)}{END}{tail}")

    msg = ROOT / ".commit-msg"
    if changes:
        msg.write_text(f"Update prices {today}\n\n" + "\n".join(changes) + "\n")
    elif msg.exists():
        msg.unlink()
    print(f"{len(rows)} models, {len(changes)} changes")


if __name__ == "__main__":
    main()
