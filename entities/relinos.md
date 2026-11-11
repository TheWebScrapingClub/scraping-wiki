---
name: relinos
type: entity
category: tool
first_seen: 2026-11-11
last_updated: 2026-11-11
sources:
  - realsirjoe-relinos.md
---

# Relinos

## What it is

Relinos is a programmable browser that functions as a REST API, enabling users to render and interact with websites. It allows for the control of multiple browser instances and the extraction of structured data from web pages.

## How it works

Relinos utilizes browser automation to render web pages and execute actions defined in a JSON request. Users can specify interactions such as typing into fields, clicking elements, and navigating through pages. The tool supports defining extraction rules using XPath to pull specific data points from the rendered page.

It also includes features for handling pagination, caching results for a specified duration, and importing pre-defined routines and extractions from a registry for common websites.

## TWSC experience

Not yet tested by TWSC.
## Related

- [playwright](../entities/playwright.md)
- [puppeteer](../entities/puppeteer.md)
- [scrapy](../entities/scrapy.md)


## Sources

- [https://github.com/realsirjoe/relinos](https://github.com/realsirjoe/relinos)
