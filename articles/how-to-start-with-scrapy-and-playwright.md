---
type: article_summary
title: How to start with Scrapy and Playwright - Part 2
slug: how-to-start-with-scrapy-and-playwright
canonical_url: https://www.scraping.club/p/how-to-start-with-scrapy-and-playwright
publish_date: '2024-11-24'
visibility: free
topics:
- browser-automation
- antibot
- proxies
- residential-proxies
description: How to tell when Scrapy is not enough, which tool fits each major anti-bot, and how to set up Playwright manually to reduce its detection surface.
source_hash: bd0e4c2e116c7f74
---

# How to start with Scrapy and Playwright - Part 2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-11-24 (free to read). **[Read the full article](https://www.scraping.club/p/how-to-start-with-scrapy-and-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy is enough for sites with little or no anti-bot protection. When a modern anti-bot kicks in, you usually need a browser automation tool like Playwright. A Scrapy spider has no JavaScript engine, so a simple JS challenge exposes it. Scrapy-splash does not fix that. The catch is that a browser gives anti-bots more to look at: behavior, device fingerprint, IP consistency and JavaScript execution.

We start with detecting the tech stack of the target using the Wappalyzer extension. Then I share the rule of thumb I apply to PerimeterX, Akamai, Cloudflare, Kasada and Datadome on e-commerce sites, matching each to a mix of Scrapy, Playwright, Camoufox, proxies and web unblockers. The rest covers manual Playwright configuration: a real Chromium-based browser instead of the bundled one, a persistent context, launch arguments and slow_mo. We also look at why this manual approach is becoming obsolete.

## What's inside

- The four groups of signals a browser exposes to anti-bots: behavior analysis, device fingerprinting, IP tracking and JavaScript challenges.
- Why I prefer a real Chromium-based browser such as Chrome, Edge or Brave, and why I use a persistent context that keeps cookies between runs.
- Which common launch arguments reduce automation signals, and the caveat that overusing some of them can raise suspicion.
- Two reasons the manual setup falls short: anti-bots can detect Playwright through the CDP protocol, and some fingerprint properties need patching Playwright itself.

**In the full article:** The full mapping of each anti-bot to its tooling, the Playwright code snippets for the persistent context and slow_mo, and the detailed list of launch arguments with my notes on each are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-start-with-scrapy-and-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
