---
type: article_summary
title: 'The Lab #55: Checking your browser fingerprint'
slug: browser-fingerprinting-test-online
canonical_url: https://www.scraping.club/p/browser-fingerprinting-test-online
publish_date: '2024-07-04'
visibility: premium
topics:
- browser-fingerprinting
- browser-automation
- scraping-infra
- antibot
description: How browser fingerprints expose scrapers, which attributes anti-bots check, and how to benchmark a Playwright setup against a real browser, locally and on AWS.
source_hash: fdece5c443fe93ae
---

# The Lab #55: Checking your browser fingerprint

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-04 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/browser-fingerprinting-test-online?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Reverse engineering works against a single anti-bot, but it breaks every time the solution changes. Human-like bots last longer, as long as the headful browser carries a fingerprint that looks like a real user's. Anti-bots have plenty to inspect: the latest Chrome exposes more than 8k browser APIs. Inconsistent attributes, odd API usage and headless traces are what give scrapers away.

We use the device and browser info page built by Antoine Vastel, head of research at Datadome, as a benchmark. I start from my own fingerprint on a desktop Mac as the reference. Then we compare plain Playwright with Chromium, Playwright with Chrome and some camouflage options, and the same script running on an AWS machine. The last step is injecting a fingerprint with Browserforge.

## What's inside

- Fingerprinting versus cookies: persistence, uniqueness and evasion resistance on one side, accuracy, regulation and usability trade-offs on the other.
- Three ways anti-bots use fingerprints: inconsistencies between attributes, API usage patterns (Canvas, WebGL, XMLHttpRequest) and headless browser detection.
- A list of the attributes that matter, including audio, video and camera device counts and the WebGL renderer, and why servers stand out on them.
- Why headers are the easy part to mimic, even in Scrapy, and the device information section is where scrapers get caught.

**In the full article:** The run_playwright_vanilla and run_chrome test functions, the benchmark screenshots for each setup, the Browserforge section and the 55.FINGERPRINT-TEST folder in the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/browser-fingerprinting-test-online?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
