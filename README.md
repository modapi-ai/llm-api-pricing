# LLM API Pricing

Per-token prices for GPT, Claude, Gemini, Grok, DeepSeek, Kimi, GLM, Qwen and other chat models, in USD per 1M input and output tokens. Every model below is served through one OpenAI-compatible API at `https://modapi.ai/v1`. The data is refreshed daily and is free to reuse under the MIT license.

- **Machine-readable data:** [`data/models.json`](data/models.json) and [`data/models.csv`](data/models.csv), with the fields `vendor`, `model`, `input`, `output`, `updated`.
- **Source:** the public pricing endpoint [`https://modapi.ai/api/pricing`](https://modapi.ai/api/pricing), which needs no API key. The live price list is at [modapi.ai/pricing](https://modapi.ai/pricing?utm_source=github&utm_medium=referral&utm_campaign=offsite_seo).
- **Update frequency:** a GitHub Action runs once a day and commits only when a price changes. The commit message lists every price that changed, so the [commit history](../../commits/main) is a price-change log.

## How prices are shown

- Prices are USD per 1M tokens, rounded to 4 significant digits, the same as modapi.ai/pricing.
- They are the lowest-priced LLM channel group a model is available on, usually the Standard group at vendor list price.
- Where a model has tiered pricing by context length, the entry tier is shown.
- `updated` is the date the model's price last changed in this dataset.
- Embedding and rerank models are not included.

## Prices by vendor

New here? Start with $20 in free credit. Top up $100, get up to $330 in LLM credit: [modapi.ai/campaigns](https://modapi.ai/campaigns?utm_source=github&utm_medium=referral&utm_campaign=offsite_seo).

<!-- pricing:start -->
### OpenAI

66 models · live prices: [modapi.ai/pricing?search=gpt](https://modapi.ai/pricing?search=gpt&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `gpt-3.5-turbo` | $1.05 | $3.15 |
| `gpt-3.5-turbo-1106` | $1 | $2 |
| `gpt-3.5-turbo-16k` | $6.3 | $12.6 |
| `gpt-4` | $30 | $60 |
| `gpt-4-1106-preview` | $10 | $30 |
| `gpt-4-turbo` | $10 | $30 |
| `gpt-4-turbo-2024-04-09` | $10 | $30 |
| `gpt-4.1` | $2 | $8 |
| `gpt-4.1-2025-04-14` | $2 | $8 |
| `gpt-4.1-mini` | $0.4 | $1.6 |
| `gpt-4.1-mini-2025-04-14` | $0.4 | $1.6 |
| `gpt-4.1-nano` | $0.1 | $0.4 |
| `gpt-4.1-nano-2025-04-14` | $0.1 | $0.4 |
| `gpt-4o` | $2.5 | $10 |
| `gpt-4o-2024-05-13` | $5 | $15 |
| `gpt-4o-2024-08-06` | $2.5 | $10 |
| `gpt-4o-2024-11-20` | $2.5 | $10 |
| `gpt-4o-mini` | $0.15 | $0.6 |
| `gpt-4o-mini-2024-07-18` | $0.15 | $0.6 |
| `gpt-5` | $1.25 | $10 |
| `gpt-5-2025-08-07` | $1.25 | $10 |
| `gpt-5-chat-latest` | $1.25 | $10 |
| `gpt-5-codex` | $1.25 | $10 |
| `gpt-5-mini` | $0.25 | $2 |
| `gpt-5-mini-2025-08-07` | $0.25 | $2 |
| `gpt-5-nano` | $0.05 | $0.4 |
| `gpt-5-nano-2025-08-07` | $0.05 | $0.4 |
| `gpt-5-pro` | $15 | $120 |
| `gpt-5-search-api` | $2.625 | $21 |
| `gpt-5-search-api-2025-10-14` | $2.625 | $21 |
| `gpt-5.1` | $1.25 | $10 |
| `gpt-5.1-2025-11-13` | $1.25 | $10 |
| `gpt-5.1-codex` | $1.25 | $10 |
| `gpt-5.2` | $1.75 | $14 |
| `gpt-5.2-codex` | $1.75 | $14 |
| `gpt-5.2-pro` | $21 | $168 |
| `gpt-5.3-codex` | $1.75 | $14 |
| `gpt-5.4` | $2.5 | $15 |
| `gpt-5.4-mini` | $0.75 | $4.5 |
| `gpt-5.4-mini-2026-03-17` | $0.75 | $4.5 |
| `gpt-5.4-nano` | $0.2 | $1.25 |
| `gpt-5.4-nano-2026-03-17` | $0.2 | $1.25 |
| `gpt-5.4-pro` | $30 | $180 |
| `gpt-5.4-pro-2026-03-05` | $30 | $180 |
| `gpt-5.5` | $5 | $30 |
| `gpt-5.5-pro` | $63 | $378 |
| `gpt-5.6-luna` | $0.2 | $1.2 |
| `gpt-5.6-sol` | $4 | $20 |
| `gpt-5.6-terra` | $2 | $12 |
| `gpt-6-astra` | $10 | $50 |
| `gpt-6-luna` | $0.1 | $0.5 |
| `gpt-6-sol` | $2 | $10 |
| `gpt-6.1-sol` | $2 | $10 |
| `gpt-6.1-terra` | $1 | $5 |
| `gpt-6.2-astra` | $8 | $40 |
| `gpt-6.2-sol` | $2 | $10 |
| `gpt-chat-latest` | $1.103 | $6.618 |
| `gpt-oss-120b` | $0.2328 | $0.931 |
| `o1` | $15 | $60 |
| `o1-2024-12-17` | $15 | $60 |
| `o3` | $2 | $8 |
| `o3-2025-04-16` | $2 | $8 |
| `o3-mini` | $1.1 | $4.4 |
| `o3-mini-2025-01-31` | $1.1 | $4.4 |
| `o4-mini` | $1.1 | $4.4 |
| `o4-mini-2025-04-16` | $1.1 | $4.4 |

### Alibaba (Qwen)

22 models · live prices: [modapi.ai/pricing?search=qwen](https://modapi.ai/pricing?search=qwen&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `qwen-flash` | $0.105 | $0.84 |
| `qwen-max` | $3.36 | $13.44 |
| `qwen-plus` | $0.4 | $1.2 |
| `qwen-plus-2025-12-01` | $0.84 | $2.52 |
| `qwen-plus-character` | $1.05 | $2.94 |
| `qwen-plus-latest` | $0.84 | $2.52 |
| `qwen3-30b-a3b-think` | $0.42 | $5.04 |
| `qwen3-coder-flash` | $0.63 | $3.15 |
| `qwen3-vl-plus` | $0.2 | $1.6 |
| `qwen3.5-122b-a10b` | $0.84 | $6.72 |
| `qwen3.5-27b` | $0.63 | $5.04 |
| `qwen3.5-35b-a3b` | $0.525 | $4.2 |
| `qwen3.5-397b-a17b` | $1.26 | $7.56 |
| `qwen3.5-plus` | $0.84 | $5.04 |
| `qwen3.5-plus-2026-02-15` | $0.84 | $5.04 |
| `qwen3.6-plus` | $1.05 | $6.3 |
| `qwen3.7-max` | $5.25 | $15.75 |
| `qwen3.8-max` | $2 | $6 |
| `qwen3.8-max-0902` | $2 | $6 |
| `qwen3.8-omni-flash` | $0.315 | $0.987 |
| `qwen4-max` | $3.15 | $9.45 |
| `qwq-32b` | $2.562 | $7.688 |

### Anthropic

15 models · live prices: [modapi.ai/pricing?search=claude](https://modapi.ai/pricing?search=claude&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `claude-fable-5` | $10 | $50 |
| `claude-fable-5-1` | $10 | $50 |
| `claude-fable-5-2` | $8 | $40 |
| `claude-haiku-4-5-20251001` | $1 | $5 |
| `claude-haiku-5-5` | $0.1 | $0.5 |
| `claude-opus-4-5-20251101` | $5 | $25 |
| `claude-opus-4-6` | $5 | $25 |
| `claude-opus-4-7` | $5 | $25 |
| `claude-opus-4-8` | $5 | $25 |
| `claude-opus-5` | $5 | $25 |
| `claude-opus-5-5` | $4 | $20 |
| `claude-sonnet-4-5-20250929` | $3 | $15 |
| `claude-sonnet-4-6` | $3 | $15 |
| `claude-sonnet-5` | $2 | $10 |
| `claude-sonnet-5-5` | $2 | $10 |

### Google

15 models · live prices: [modapi.ai/pricing?search=gemini](https://modapi.ai/pricing?search=gemini&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `gemini-2.5-flash` | $0.3 | $2.5 |
| `gemini-2.5-flash-lite` | $0.1 | $0.4 |
| `gemini-2.5-pro` | $1.25 | $10 |
| `gemini-3-flash-preview` | $0.5 | $3 |
| `gemini-3-pro-preview` | $2 | $12 |
| `gemini-3.1-flash-lite` | $0.25 | $1.5 |
| `gemini-3.1-flash-lite-preview` | $0.25 | $1.5 |
| `gemini-3.1-pro-preview` | $2 | $12 |
| `gemini-3.5-flash` | $1.5 | $9 |
| `gemini-3.5-flash-lite` | $0.3 | $2.5 |
| `gemini-3.6-flash` | $0.75 | $3.75 |
| `gemini-3.7-flash` | $0.75 | $3.75 |
| `gemini-3.8-flash` | $0.75 | $3.75 |
| `gemini-4-argon` | $4 | $20 |
| `gemini-4-hydrogen` | $3.15 | $15.75 |

### Zhipu (GLM)

11 models · live prices: [modapi.ai/pricing?search=glm](https://modapi.ai/pricing?search=glm&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `glm-4-airx` | $1.477 | $5.907 |
| `glm-4-flash` | $0.0848 | $0.3392 |
| `glm-4-long` | $0.1477 | $0.5907 |
| `glm-4.5` | $0.6 | $2.2 |
| `glm-4.5-air` | $0.1181 | $0.2953 |
| `glm-4.6` | $1.26 | $4.62 |
| `glm-5` | $1.24 | $5.582 |
| `glm-5.1` | $1.861 | $7.442 |
| `glm-5.2` | $2.94 | $9.24 |
| `glm-5.3` | $1.4 | $4.4 |
| `glm-5.3-flash` | $0.15 | $0.5 |

### xAI

8 models · live prices: [modapi.ai/pricing?search=grok](https://modapi.ai/pricing?search=grok&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `grok-4` | $3 | $15 |
| `grok-4-20-non-reasoning` | $1.25 | $2.5 |
| `grok-4-20-reasoning` | $1.25 | $2.5 |
| `grok-4.3` | $1.25 | $2.5 |
| `grok-4.5` | $2 | $6 |
| `grok-4.6` | $2 | $6 |
| `grok-4.7` | $2 | $6 |
| `grok-4.7-fast` | $4 | $12 |

### DeepSeek

7 models · live prices: [modapi.ai/pricing?search=deepseek](https://modapi.ai/pricing?search=deepseek&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `deepseek-v3` | $0.9512 | $3.875 |
| `deepseek-v3-1` | $0.7429 | $2.229 |
| `deepseek-v4-flash` | $0.63 | $2.52 |
| `deepseek-v4-flash-0731` | $0.8617 | $2.585 |
| `deepseek-v4-pro` | $2.772 | $8.316 |
| `deepseek-v4-pro-0813` | $1.32 | $3.96 |
| `deepseek-v4.1-flash` | $0.3 | $1.2 |

### Moonshot (Kimi)

6 models · live prices: [modapi.ai/pricing?search=kimi](https://modapi.ai/pricing?search=kimi&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `kimi-k2-0711-preview` | $0.775 | $3.1 |
| `kimi-k2.5` | $1.427 | $7.494 |
| `kimi-k2.6` | $1.995 | $8.4 |
| `kimi-k2.7-code` | $1.995 | $8.4 |
| `kimi-k3` | $3 | $15 |
| `kimi-k3.1-pro` | $2 | $10 |

### MiniMax

3 models · live prices: [modapi.ai/pricing?search=minimax](https://modapi.ai/pricing?search=minimax&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `MiniMax-M2.5` | $0.63 | $2.52 |
| `MiniMax-M3` | $0.63 | $2.52 |
| `MiniMax-M3.1-Flash` | $0.15 | $0.6 |

### Xiaomi

1 models · live prices: [modapi.ai/pricing?search=mimo](https://modapi.ai/pricing?search=mimo&utm_source=github&utm_medium=referral&utm_campaign=offsite_seo)

| Model | Input $/1M | Output $/1M |
|---|---:|---:|
| `mimo-v2.6-pro` | $0.9135 | $1.827 |
<!-- pricing:end -->

## Use any of these models with an OpenAI-compatible client

Create a key at [modapi.ai/keys](https://modapi.ai/keys?utm_source=github&utm_medium=referral&utm_campaign=offsite_seo), then point your client at `https://modapi.ai/v1`. Use a model ID from the tables as `model`. Existing OpenAI code works by changing `base_url` and the key.

### curl

```bash
curl https://modapi.ai/v1/chat/completions \
  -H "Authorization: Bearer $MODAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4.1-nano", "messages": [{"role": "user", "content": "Hello"}]}'
```

### Python (openai SDK)

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://modapi.ai/v1", api_key=os.environ["MODAPI_API_KEY"])
reply = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Hello"}],
)
print(reply.choices[0].message.content)
```

### Claude Code

Claude Code speaks Anthropic's Messages API rather than the OpenAI format, so it uses the Anthropic-format endpoint at the root URL:

```bash
export ANTHROPIC_BASE_URL="https://modapi.ai"
export ANTHROPIC_AUTH_TOKEN="your-modapi-api-key"
export ANTHROPIC_MODEL="claude-sonnet-5-5"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="claude-haiku-5-5"
claude
```

### Cursor

In **Cursor Settings → Models**, enter your ModAPI key as the **OpenAI API Key**, turn on **Override OpenAI Base URL** and set it to `https://modapi.ai/v1`, then add the model IDs you want to use. Custom API keys apply to chat and Cmd-K; Tab completion and some agent features still use Cursor's own models.

## Why a key per project helps

Each ModAPI key can have its own model allowlist, IP allowlist, spending quota, expiry date and channel group, so a key in a CI job or on a teammate's laptop can reach only what it should. There are no top-up fees or subscriptions.

## Run the update yourself

```bash
python scripts/update.py
```

It needs only the Python standard library.

## License

[MIT](LICENSE). The data is provided as is. Always check [modapi.ai/pricing](https://modapi.ai/pricing?utm_source=github&utm_medium=referral&utm_campaign=offsite_seo) before relying on a price.
