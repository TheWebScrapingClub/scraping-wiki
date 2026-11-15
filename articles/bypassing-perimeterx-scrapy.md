---
type: article_summary
title: Bypassing PerimeterX without a browser automation tool
slug: bypassing-perimeterx-scrapy
canonical_url: https://www.scraping.club/p/bypassing-perimeterx-scrapy
publish_date: '2024-02-22'
visibility: premium
topics:
- cloudflare
- browser-automation
- anti-detect-browsers
- antibot
description: How to scrape PerimeterX-protected sites without Playwright, using a Scrapy-based approach, with two real-world examples and tips on detecting PerimeterX.
source_hash: 7d6cc8d983f4392a
---

# Bypassing PerimeterX without a browser automation tool

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-22 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-perimeterx-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

No anti-bot bypass works everywhere. Sites running the same anti-bot can set different protection levels, and even one site can protect some paths and leave others open. Booking.com is protected by PerimeterX (now Human Scraping Defense) on the website, while its internal APIs are not. Anti-bots mostly exist to stop fraud, like automated purchases of sneaker drops, not to stop responsible scraping of public data.

Two months ago we bypassed PerimeterX with Python and Playwright. A JS rendering engine is usually needed to solve anti-bot challenges, but it makes scraping slower and heavier on resources. So I asked whether one of the many open source tools on GitHub could replace it. I skipped the trials and errors and went straight to the one that worked, a Scrapy-based tool. We apply it to two real-world PerimeterX-protected websites. I also cover how to tell that a site uses PerimeterX before you start.

## What's inside

- How to detect PerimeterX on a target: the Wappalyzer Chrome extension and the cookies it sets.
- Why the Press and Hold CAPTCHA is not the only sign of PerimeterX.
- Why Booking.com is a good example of an anti-bot that protects the website but not its internal APIs, and the possible reasons.
- A pointer to the Web Scraping Wiki for deobfuscating and reverse engineering anti-bots.

**In the full article:** The name of the tool in context, its setup, the two PerimeterX-protected target websites with their scrapers, and the code in the paid GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-perimeterx-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
