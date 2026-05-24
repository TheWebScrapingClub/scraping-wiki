---
name: beautiful-code-screenshots-codeshot
type: entity
category: tool
first_seen: 2026-05-24
last_updated: 2026-05-24
sources:
  - drmadmeow-up-railway-app.md
---

# Beautiful Code Screenshots (CodeShot)

## What it is

CodeShot is an API toolkit designed for developers and AI agents that facilitates code screenshotting, website scraping, and link preview generation. It provides a single REST API endpoint for various functionalities, including generating code images, extracting text from URLs, and retrieving Open Graph metadata.

## How it works

The tool operates via a REST API, allowing users to interact with features like code screenshotting, web scraping, and link preview generation using a single API key. For code screenshots, a POST request to `/v1/screenshot` accepts code, language, theme, and preset parameters to return an image.

Other web tools are accessible through dedicated endpoints: `POST /v1/webshot` captures a full-page or viewport screenshot as a PNG, `POST /v1/scrape` extracts clean markdown or text from a URL, and `POST /v1/preview` retrieves Open Graph and Twitter Card metadata for link previews.

## TWSC experience

Not yet tested by TWSC.

## Related

* [crawl4ai](../entities/crawl4ai.md)
* [lucidextractor](../entities/lucidextractor.md)
* [browser-use](../entities/browser-use.md)


## Sources

- [https://drmadmeow.up.railway.app/](https://drmadmeow.up.railway.app/)
