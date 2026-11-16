---
type: article_summary
title: Testing the Bright Data Web Unblocker proxy
slug: testing-bright-data-unblockler-cloudflare
canonical_url: https://www.scraping.club/p/testing-bright-data-unblockler-cloudflare
publish_date: '2023-03-09'
visibility: free
topics:
- proxies
- cloudflare
- datadome
- browser-automation
description: A test of Bright Data Web Unblocker as a proxy for a Scrapy spider, against Datadome, Cloudflare, Kasada, F5 and PerimeterX on five retail sites.
source_hash: d3a7d965ddb26560
---

# Testing the Bright Data Web Unblocker proxy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-03-09 (free to read). **[Read the full article](https://www.scraping.club/p/testing-bright-data-unblockler-cloudflare?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Bright Data Web Unblocker is an API sold as a way to scrape even the most protected websites. It plugs into a scraper like a normal proxy, and the vendor lists what happens behind it: per-IP rate limits, user emulation, device imitation, referrer calibration, honeypot detection and random delays between requests. That is easy to claim. What matters is whether it gets a plain HTTP scraper past real anti-bot systems without Playwright or Selenium.

We built a plain Scrapy spider that fetches 10 product pages from each of five retail sites, one per anti-bot: Datadome, Cloudflare, Kasada, F5 and PerimeterX. The spider without a proxy is the benchmark. We then ran it through Web Unblocker from a local machine and from a cloud VM, to see whether a server fingerprint leaks, and scored the outcome from 0 to 100.

## What's inside

- Which site stands in for each anti-bot, including a Cloudflare target with one of the strictest policies I've seen.
- How the score is built: a page counts only if the product string is found, across a local run and a server run.
- Why we repeated the test from a cloud VM instead of trusting the local result.
- The pricing caveat: per-GB billing versus billing per 1,000 requests, and what it means for large or low-budget projects.

**In the full article:** Result tables for the no-proxy, local and cloud runs, the proxy zone setup in Bright Data, the link to the test spider on GitHub, the final score and my pros and cons verdict.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/testing-bright-data-unblockler-cloudflare?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
