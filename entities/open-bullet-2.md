---
name: open-bullet-2
type: entity
category: tool
first_seen: 2026-05-07
last_updated: '2026-05-07'
sources:
- dbi-selenium-chrome-mode-open-bullet2.md
- dbi-analyze-open-bullet2-request-mode.md
- dbi-overview-open-bullet2.md
---

# Open Bullet 2

## What it is

Open Bullet 2 is a credential stuffing tool that can be used for web scraping and automation. It supports various modes, including Puppeteer and Selenium Chrome, which are used to create browser instances for interacting with web pages.

## How it works

First, you need to set the Chrome path for Selenium in the `**RuriLib Settings**` panel. Then, you create a new configuration and edit it using the `Stacker` panel. The configuration involves creating a browser instance using the `Selenium` function block, navigating to a specific URL, waiting for a short period, and executing JavaScript to retrieve the bot detection status and fingerprint.

## TWSC experience

Not yet tested by TWSC.

## Related

- [Puppeteer](../entities/puppeteer.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/selenium-chrome-mode-open-bullet2](https://deviceandbrowserinfo.com/learning_zone/articles/selenium-chrome-mode-open-bullet2)
