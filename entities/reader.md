---
name: reader
type: entity
category: tool
first_seen: 2026-05-06
last_updated: '2026-05-07'
sources:
- vakra-dev-reader.md
- blog-why-i-built-reader.md
---

# Reader

## What it is

Reader is an open-source, production-grade web scraping engine built for LLMs. It provides a simple API for scraping and crawling the entire web, producing clean markdown output. The project aims to handle the complexities of anti-bot defenses, TLS fingerprinting, proxy management, and reliability issues that arise in production.

## How it works

Reader is built on top of Ulixee Hero, a headless browser designed for web scraping. It offers two main primitives: `scrape` and `crawl`. The `scrape` function allows you to scrape URLs and get clean markdown or HTML output, while the `crawl` function discovers and scrapes pages within a specified depth. Under the hood, Reader manages browser instances, anti-bot bypasses, proxy rotation, and other necessary tasks to ensure reliable and efficient scraping.

## TWSC experience

Not yet tested by TWSC.
## Related

- [Cloudflare](../entities/cloudflare.md)
- [Undetected-Chromedriver](../entities/undetected-chromedriver.md)
- [Scraping Infrastructure](../concepts/scraping-infrastructure.md)


## Sources

- [https://github.com/vakra-dev/reader](https://github.com/vakra-dev/reader)
