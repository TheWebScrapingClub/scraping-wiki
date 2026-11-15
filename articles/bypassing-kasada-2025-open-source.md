---
type: article_summary
title: 'THE LAB #76: Bypassing Kasada With Open Source Tools In 2025'
slug: bypassing-kasada-2025-open-source
canonical_url: https://www.scraping.club/p/bypassing-kasada-2025-open-source
publish_date: '2025-02-13'
visibility: premium
topics:
- browser-automation
- cloudflare
- browser-fingerprinting
description: How to detect Kasada and test open-source Playwright setups against Canadagoose.com in 2025, without paying for an unblocking service.
source_hash: 7f77b158b6f13085
---

# THE LAB #76: Bypassing Kasada With Open Source Tools In 2025

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-02-13 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-kasada-2025-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada, the Australian anti-bot company, is a protection every professional scraper meets sooner or later, and paid unblocking services carry a price tag that is not for every pocket. Some say generating a valid token is enough. I don't think that is the best route when you need data soon: reverse engineering a commercial solution takes time, and you restart after every change in the anti-bot software. I prefer a human-like request that mixes with the real traffic of the site. It is slower because it needs browser automation, but more ethical than hundreds of requests per second.

This continues our series on open-source bypasses, after Cloudflare Turnstile. The target is Canadagoose.com. We show how to tell that a site runs Kasada, then we test three open-source setups built on Playwright and a modified browser, starting from a plain Playwright and Brave baseline and moving to Patchright.

## What's inside

- Wappalyzer data can be stale, so I double check in the network tab with "preserve log" ticked and look for a 429 followed by a normal load.
- The x-kpsdk access control headers on the following calls are the second sign that Kasada is in front of the site.
- Why I often use Brave in these examples: it adds noise to the WebGL fingerprint, though it is not a real anti-detect browser.
- What Patchright changes compared to standard Playwright, and why the GitHub repositories that try to compute the Kasada token are not my preferred approach.

**In the full article:** Scripts for each test, the result for each of the three tools on Canadagoose.com, and the 76.KASADA2025 folder of The Lab GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-kasada-2025-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
