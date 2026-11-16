---
type: article_summary
title: 'THE LAB #73: How to Bypass Cloudflare in 2025'
slug: how-to-bypass-cloudflare-turnstile
canonical_url: https://www.scraping.club/p/how-to-bypass-cloudflare-turnstile
publish_date: '2025-01-23'
visibility: premium
topics:
- cloudflare
- browser-automation
- antibot
- captcha
description: How Cloudflare Turnstile works, why reverse engineering falls short, and the open-source tools we tested on an Indeed.com page in 2025.
source_hash: 0b9a022b5ced4884
---

# THE LAB #73: How to Bypass Cloudflare in 2025

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-23 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-bypass-cloudflare-turnstile?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Sooner or later every scraper meets Cloudflare, and Statista gives it about 80% of the bot protection market. My gut feeling is that the number is overestimated, but the problem stays the same: we need a way past it. On the Burger King reviews page on Indeed.com, Turnstile runs a back-and-forth of POST requests with encrypted payloads, most likely our browser fingerprint. Then it hands out a clearance cookie, valid for six months in this case.

I explain why reverse engineering that process, as Cloudscraper tried, teaches a lot but is a poor way to run a real project. Then I cover the alternative of behaving like a real browser, with genuine fingerprints in Playwright or Puppeteer, which is what anti-detect browsers do. Finally we test open-source tools on the same Indeed page: Playwright, Cloudscraper and Botasaurus. The same test with commercial tools comes in the following months.

## What's inside

- Why reverse engineering is an unfair game: every anti-bot needs its own process, and each update sends us back almost to the start.
- Where fingerprint matching stops being enough: strict anti-bot rules that add keyboard and mouse behavior tracking.
- The setup of the Playwright test: a local Brave instance with masking arguments and no stealth library added.
- The state of Cloudscraper, whose repository has not been updated for two years.

**In the full article:** Scripts for each tool, the result of each test on the Indeed page, the Botasaurus section and the 73.CLOUDFLARE folder of the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-bypass-cloudflare-turnstile?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
