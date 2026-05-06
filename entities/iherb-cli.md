---
name: iherb-cli
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - SeverinAlexB-iherb-cli.md
---

# iherb-cli

## What it is

A Rust command-line tool for querying product data from iHerb using a headless browser. Designed for both AI agents and humans — clean commands, Markdown output, no API key required.

## How it works

iHerb uses Cloudflare anti-bot protection, so simple HTTP requests are blocked. iHerb-cli uses a headless Chromium browser (via the Chrome DevTools Protocol) to load pages like a real user. Data extraction uses multiple strategies with automatic fallback:

1. **JSON-LD** structured data embedded in the page
2. **JavaScript globals** (`window.PRODUCT_DETAILS`, etc.)
3. **`__NEXT_DATA__`** — iHerb's Next.js server-side data
4. **DOM scraping** — CSS selector-based extraction as a last resort

This layered approach keeps the tool working even when iHerb changes their page structure.

## TWSC experience

Not yet tested by TWSC.

## Related

- [Cloudflare](../entities/cloudflare.md)
- [playwright](../entities/playwright.md)


## Sources

- [https://github.com/SeverinAlexB/iherb-cli](https://github.com/SeverinAlexB/iherb-cli)
