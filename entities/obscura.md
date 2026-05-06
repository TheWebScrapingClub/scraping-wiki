---
name: obscura
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - h4ckf0r0day-obscura.md
---

# Obscura

## What it is

Obscura is a headless browser engine written in Rust, built for web scraping and AI agent automation. It runs real JavaScript via V8, supports the Chrome DevTools Protocol, and acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright.

## How it works

Obscura is designed for automation at scale, not desktop browsing. It offers several advantages over headless Chrome, including lower memory and binary sizes, built-in anti-detection features, faster page loads, and instant startup. It supports both Puppeteer and Playwright, making it a versatile tool for web scraping and AI agent automation.

| Metric       | Obscura      | Headless Chrome |
|--------------|--------------|------------------|
| Memory       | **30 MB**    | 200+ MB          |
| Binary size  | **70 MB**    | 300+ MB          |
| Anti-detect  | **Built-in** | None          |
| Page load    | **85 ms**    | ~500 ms          |
| Startup      | **Instant**  | ~2s              |
| Puppeteer    | **Yes**      | Yes              |
| Playwright   | **Yes**      | Yes              |

## TWSC experience

Not yet tested by TWSC.
## Related

- [playwright](../entities/playwright.md)
- [undetected-chromedriver](../entities/undetected-chromedriver.md)


## Sources

- [https://github.com/h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)
