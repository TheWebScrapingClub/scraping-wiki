---
type: article_summary
title: Is web scraping becoming harder?
slug: is-web-scraping-becoming-harder
canonical_url: https://www.scraping.club/p/is-web-scraping-becoming-harder
publish_date: '2022-08-28'
visibility: free
topics:
- browser-automation
- browser-fingerprinting
- proxies
- datadome
description: 'Why web scraping is getting harder and costlier: active fingerprinting by anti-bot systems, and what it takes to make Playwright look like a real user.'
source_hash: 2bea7e0c4be0b0b6
---

# Is web scraping becoming harder?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-08-28 (free to read). **[Read the full article](https://www.scraping.club/p/is-web-scraping-becoming-harder?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

I have the feeling that web scraping is getting harder and more expensive, especially over the last 12 months. More sites with a larger budget now use advanced anti-bot solutions. They rely on AI to spot anomalous behavior and on active fingerprinting. At databoutique.com we scrape public data from major e-commerce sites, so browsing a catalog looks like normal user behavior and behavioral checks rarely hit us. Active fingerprinting is the real problem, and it pushed us to build a new toolkit and configuration for the hardest targets.

I explain the difference between passive and active fingerprinting, including browser and canvas fingerprints, and why Scrapy alone is no longer enough on these sites. We moved to Playwright with a real browser and measured how it looks to fingerprint tests such as CreepJS and incolumitas. We compared it with a normal Chrome baseline, step by step, adding a change at each run.

## What's inside

- How passive fingerprinting (headers plus IP) differs from active fingerprinting (JavaScript run on the client), and how anti-bot systems match the results against a catalogue of common installations.
- Why the navigator.webdriver flag matters and how its value differs between Chromium under Playwright and recent Chrome releases.
- Which public test sites we used to check a browser setup, and why CreepJS is the one I find clearest.
- A caveat on plugins that stop being maintained: an old stealth tool can look worse on strict tests, and we plan to release our own version.

**In the full article:** The Playwright code for each of the three runs, the annotated test screenshots against the Chrome baseline, and the detailed reading of what the stealth plugin changes and where it now falls short.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/is-web-scraping-becoming-harder?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
