---
name: kimurai
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - vifreefly-kimuraframework.md
---

# Kimurai

## What it is

Kimurai is a Ruby-based web scraping framework that uses AI to assist in data extraction. It allows users to write scrapers using a clean, AI-assisted Domain-Specific Language (DSL). Kimurai uses AI to generate selectors on the first request and caches them for subsequent requests, enabling fast and efficient data extraction without the need for per-request AI calls.

## How it works

1. On the first request, `extract` sends the HTML and your schema to an LLM, which generates XPath selectors and caches them in a file.
2. **All subsequent requests use cached XPath selectors — zero AI calls, pure fast Ruby extraction.**
3. Kimurai supports OpenAI, Anthropic, Gemini, or local LLMs via [Nukitori](https://github.com/vifreefly/nukitori).

Kimurai also works as a traditional scraper, supporting headless antidetect Chromium, Firefox, or simple HTTP requests.

## TWSC experience

Not yet tested by TWSC.

## Related

- [ai-scraping-assistants](../concepts/ai-scraping-assistants.md)
- [Anti-Detect Browsers](../concepts/anti-detect-browsers.md)
- [ML-Based Bot Detection](../concepts/ml-bot-detection.md)


## Sources

- [https://github.com/vifreefly/kimuraframework](https://github.com/vifreefly/kimuraframework)
