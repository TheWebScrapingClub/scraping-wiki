---
name: selenium-headless-chrome-detection
type: entity
category: anti-bot
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-detecting-headless-chrome-selenium-2024.md
---

# Selenium/Headless Chrome Detection

## What it is

This project presents four efficient techniques designed to detect bots that utilize Selenium running in both headless and non-headless Chrome environments. These methods are effective for identifying automated browser instances.

## How it works

The detection techniques rely on analyzing various browser and JavaScript artifacts. One method involves checking the user agent HTTP headers or the `navigator.userAgent` in JavaScript to identify user agents linked to Headless Chrome, such as those containing `HeadlessChrome/126.0.6478.114`.

Other techniques include detecting the presence of the `HeadlessChrome` substring within the `sec-ch-ua` header, checking if `navigator.webdriver` is set to `true` in JavaScript, and detecting side effects resulting from the Chrome DevTools Protocol (CDP).

## TWSC experience

Not yet tested by TWSC.

## Related

* [cdp-detection](../concepts/cdp-detection.md)
* [browser-fingerprinting](../concepts/browser-fingerprinting.md)
* [puppeteer](../entities/puppeteer.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/detecting-headless-chrome-selenium-2024](https://deviceandbrowserinfo.com/learning_zone/articles/detecting-headless-chrome-selenium-2024)
