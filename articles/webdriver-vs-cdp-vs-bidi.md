---
type: article_summary
title: 'WebDriver vs Chrome DevTools Protocol (CDP) vs WebDriver BiDi: How We Control Browsers'
slug: webdriver-vs-cdp-vs-bidi
canonical_url: https://www.scraping.club/p/webdriver-vs-cdp-vs-bidi
publish_date: '2026-02-01'
visibility: free
topics:
- browser-automation
- anti-detect-browsers
description: How WebDriver, Chrome DevTools Protocol and WebDriver BiDi control browsers under Selenium, Playwright and Puppeteer, and how they differ.
source_hash: cee7efdda5972f7e
---

# WebDriver vs Chrome DevTools Protocol (CDP) vs WebDriver BiDi: How We Control Browsers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-02-01 (free to read). **[Read the full article](https://www.scraping.club/p/webdriver-vs-cdp-vs-bidi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most of us have written dozens of scripts with Selenium, Playwright or Puppeteer without looking at what sits between the library and the browser. That layer is a browser automation protocol, and it decides what your scraper can see and control. It also decides how much driver management you inherit and whether your code works outside Chromium.

I go through the three protocols that matter: WebDriver, Chrome DevTools Protocol (CDP) and WebDriver BiDi. For each one I explain what it is, which components are involved, and what happens at a low level when a script issues a command like a click or a screenshot. I also list the libraries built on each protocol and cover some history, including Selenium 3's JSON Wire Protocol and Firefox's remote debugging. A comparison with pros and cons closes the technical part. Then I look at where Selenium, Puppeteer, Cypress and Playwright are heading, and whether BiDi replaces CDP.

## What's inside

- Why WebDriver needs a browser-specific driver server, and what changed with driver management in Selenium 4.10
- How CDP organizes its commands and events into domains, and why it runs over WebSocket
- Why Firefox and Safari have their own debug protocols, and what happened to Firefox's limited CDP support
- Why Puppeteer still uses CDP for Chrome even though BiDi is enabled by default for Firefox

**In the full article:** The step-by-step request flow for each protocol, the library tables for WebDriver and CDP, the side-by-side comparison with pros and cons, and my take on whether BiDi replaces CDP.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/webdriver-vs-cdp-vs-bidi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
