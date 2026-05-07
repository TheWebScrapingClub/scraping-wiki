---
name: wick
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - getwick-dev.md
---

# Wick

## What it is

Wick is an open-source tool that allows AI agents to access web pages as if they were real browsers. It runs as a lightweight local service on your machine, handling requests using the same technology real browsers use. This ensures that the requests appear indistinguishable from those made by a human user, bypassing anti-bot systems and providing clean, structured markdown output.

## How it works

Wick runs as a local service on your machine, handling requests using the same networking technology as real browsers. This means that when your AI agent needs to fetch a page, Wick ensures that the request looks like it is coming from a real user, with your own IP and cookies. The result is that websites cannot detect the request as being automated, allowing your agent to access the page without issues such as 403 errors or CAPTCHA walls.

## TWSC experience

Not yet tested by TWSC.
## Related

- [Undetected-Chromedriver](../entities/undetected-chromedriver.md)
- [Playwright](../entities/playwright.md)
- [Cdp-Detection](../concepts/cdp-detection.md)


## Sources

- [https://getwick.dev](https://getwick.dev)
