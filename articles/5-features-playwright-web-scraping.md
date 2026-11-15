---
type: article_summary
title: 5 Playwright useful features for web scraping
slug: 5-features-playwright-web-scraping
canonical_url: https://www.scraping.club/p/5-features-playwright-web-scraping
publish_date: '2023-09-30'
visibility: free
topics:
- browser-automation
- antibot
- browser-fingerprinting
description: 'Five Playwright features useful for scraper design: network interception, video recording, iFrame handling, geolocation and timezone overrides, device emulation'
source_hash: a22693a636f71c9a
---

# 5 Playwright useful features for web scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-09-30 (free to read). **[Read the full article](https://www.scraping.club/p/5-features-playwright-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Playwright is built for web testing and automation, not for scraping. It drives Chromium, Firefox and WebKit, though, so it works when a real browser is needed to get past anti-bots. Some of its features fit scraper design better than you would expect from a testing framework, and a few of them are painful to reproduce in Selenium.

I picked five that I find useful when building bots: network interception, video recording of a browser context, iFrame handling, geolocation and timezone overrides, and device emulation. For each one we wrote a short Python example and ran it against a real target or a test page, such as an Italian real estate portal, a browser leaks page for geolocation and a fingerprint test page for device emulation. The list is not exhaustive. I also say where a feature falls short for a modern anti-bot fingerprint, and where I am still stuck myself.

## What's inside

- How to log every network call a page makes without opening the browser's network tab, and how to alter headers at runtime.
- Video recording of a headless run, and the problem I still have with empty video files.
- Selecting an iFrame by name or URL and querying its content with ordinary selectors.
- Why device emulation only partly covers the fingerprint checks used by anti-bot systems.

**In the full article:** The Python code for each of the five features, the iFrame test page, the geolocation and timezone comparison, the iPhone 13 Pro device parameters and my closing comparison with Selenium.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/5-features-playwright-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
