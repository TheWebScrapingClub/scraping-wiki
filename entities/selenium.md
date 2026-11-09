---
name: selenium
type: entity
category: browser
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-bypass-api-vs-headless-browser.md
---

# Selenium

## What it is

Selenium is an open-source framework used for automating web browsers. It allows users to write scripts that interact with web pages as a real user would, enabling tasks such as form submission, navigation, and data extraction. It is commonly employed in web scraping and testing scenarios.

## How it works

Selenium operates by controlling a web browser through a WebDriver interface. This interface translates commands from the Selenium script into actions performed by the browser. For web scraping, Selenium is often used in a "headless" mode, meaning the browser runs without a graphical user interface, making it more efficient for automated tasks.

The source document mentions that headless browsers like Selenium are used to render challenges presented by bot detection systems, mimicking real user interactions to bypass these defenses. However, this approach can be slower and more resource-intensive compared to dedicated bypass APIs.

## TWSC experience

Not yet tested by TWSC.

## Related

- [selenium-headless-chrome-detection](../entities/selenium-headless-chrome-detection.md)
- [playwright](../entities/playwright.md)
- [puppeteer](../entities/puppeteer.md)


## Sources

- [https://takionapi.tech/blog/bypass-api-vs-headless-browser](https://takionapi.tech/blog/bypass-api-vs-headless-browser)
