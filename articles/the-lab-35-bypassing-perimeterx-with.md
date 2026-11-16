---
type: article_summary
title: 'The Lab #35: Bypassing PerimeterX with Python and Playwright'
slug: the-lab-35-bypassing-perimeterx-with
canonical_url: https://www.scraping.club/p/the-lab-35-bypassing-perimeterx-with
publish_date: '2023-12-21'
visibility: premium
topics:
- browser-automation
- captcha
- tls-fingerprinting
- browser-fingerprinting
description: 'How PerimeterX (now Human Scraping Defense) works and two ways to scrape Neiman Marcus product prices past it: hRequests and Playwright with Brave.'
source_hash: 9420dd17c9049785
---

# The Lab #35: Bypassing PerimeterX with Python and Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-21 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-35-bypassing-perimeterx-with?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

PerimeterX, now Human Scraping Defense, is one of the best known anti-bot solutions on the market. It combines behavioral analysis, predictive detection and several kinds of fingerprinting, with machine learning deciding who looks like a bot. When it does, it serves a challenge or blocks the IP. For anyone scraping a protected e-commerce site, a plain HTTP client rarely gets far, and the real question is which layer of the stack gives you away.

We picked Neiman Marcus as the target and tried to collect product prices from its category pages. First we checked how the site delivers listing data, because that decides how few requests we need. Then we worked through two solutions: a Scrapy spider built on hRequests, run with a rotating residential proxy and error handling for the Human Captcha, and a browser setup with Playwright and Brave.

## What's inside

- The four defense categories: IP monitoring, HTTP headers, fingerprinting (browser, HTTP/2, TLS) and CAPTCHA with behavioral analysis.
- Why Wappalyzer showing PerimeterX made us drop a standard Scrapy strategy.
- How the first listing page and the following pages deliver product data, and why the category ID is all we need.
- Why changing the IP is not enough after a failed challenge, and what has to be reset.

**In the full article:** The full hRequests Scrapy spider code, the proxy and session handling logic, the Playwright with Brave setup and the results of both runs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-35-bypassing-perimeterx-with?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
