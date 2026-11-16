---
type: article_summary
title: 'The Lab #57: Improving your Playwright scraper and avoid CDP detection'
slug: playwright-stealth-cdp
canonical_url: https://www.scraping.club/p/playwright-stealth-cdp
publish_date: '2024-07-26'
visibility: premium
topics:
- browser-automation
- datadome
- antibot
- cloudflare
description: How CDP detection flags Playwright, Puppeteer and Selenium scrapers, and what it takes to make an existing Playwright scraper pass without a rewrite.
source_hash: 0a44ab13804c0a16
---

# The Lab #57: Improving your Playwright scraper and avoid CDP detection

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-26 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/playwright-stealth-cdp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A Playwright, Puppeteer or Selenium scraper that got past your target's anti-bot may stop working after a new anti-bot version. In our community it seems common with Cloudflare and Akamai, though I only have gut feeling, no data. One recent technique, described by Datadome, detects CDP (Chrome DevTools Protocol) usage. It targets the protocol all these frameworks use to drive Chromium, not the quirks of one framework.

We check how to tell whether a test page like BrowserScan already uses CDP detection and run a standard Playwright installation against it. Then I explain what has to change: switching browsers or using an anti-detect one does not touch the signal, so the fix belongs in the automation library. I mention Nodriver as one that already handles it, then move to patching an existing Playwright scraper without rewriting it.

## What's inside

- A manual check for whether a test page knows CDP detection: open it normally, reload it with dev tools open, and compare the two verdicts.
- Why CDP detection is more generic than fingerprinting a single framework, and why that also covers anti-detect tools.
- The specific CDP command the Playwright library sends and the fix has to stop sending.
- Why Nodriver is only mentioned and not tested: I am stuck on a dependencies loop on my Mac.

**In the full article:** The library that makes the Playwright scraper pass the CDP test, the example code in folder 57 of the GitHub repository, and the BrowserScan screenshots.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/playwright-stealth-cdp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
