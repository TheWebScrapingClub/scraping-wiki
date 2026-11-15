---
type: article_summary
title: How to start with Scrapy and Playwright - Part 1
slug: basic-scrapy-configuration
canonical_url: https://www.scraping.club/p/basic-scrapy-configuration
publish_date: '2024-11-17'
visibility: free
topics:
- browser-automation
- proxies
- tls-fingerprinting
description: 'Part 1 of a Scrapy and Playwright setup guide: the Scrapy settings that make a spider less detectable, from headers and cookies to throttling and proxies.'
source_hash: ed0dae0988b7c05c
---

# How to start with Scrapy and Playwright - Part 1

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-11-17 (free to read). **[Read the full article](https://www.scraping.club/p/basic-scrapy-configuration?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy and Playwright are the two libraries I would pick when starting a Python scraping project from scratch in 2024. Scrapy is the framework, Playwright drives real browsers. Selenium is still popular, but I find Playwright easier and faster for writing a scraper.

This first part covers the Scrapy side. A plain spider is usually enough when the target has no advanced anti-bot and only checks request headers, TLS fingerprinting or the number of requests from one IP. We went through the settings that matter in those cases: default headers and User Agent, cookie handling, request throttling and proxy usage. I also tell a story about old scrapers that stopped working for a reason I did not expect, and how we fixed them. The Playwright configuration for being less detectable comes in part two.

## What's inside

- Why the default Scrapy headers and User Agent flag your requests as a scraper right away, and where to copy realistic ones from.
- How Scrapy passes cookies between requests, and why that matters when a site issues a clearance cookie.
- Two ways to throttle: the Auto Throttle options and a fixed delay, with concurrency limits per domain and per IP.
- Setting a proxy on single requests versus the middleware approach, and what the difference means for proxy costs.

**In the full article:** The settings.py snippets for headers, cookies, throttling and proxies, the browser Fetch export used to copy headers, and the proxy middleware packages we compare.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/basic-scrapy-configuration?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
