---
type: article_summary
title: Bypass Cloudflare with these web scraping tools
slug: bypass-cloudflare-browser-check
canonical_url: https://www.scraping.club/p/bypass-cloudflare-browser-check
publish_date: '2023-02-12'
visibility: free
topics:
- cloudflare
- browser-automation
- proxy-industry
description: 'Two ways to get past Cloudflare in scraping projects: Undetected Chromedriver with Selenium, and Playwright with Firefox, plus a few Playwright options.'
source_hash: d5b7c81164671313
---

# Bypass Cloudflare with these web scraping tools

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-12 (free to read). **[Read the full article](https://www.scraping.club/p/bypass-cloudflare-browser-check?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare is one of the best-known anti-bot solutions, and getting past it can be hard on any scraping project. I have written about it several times in past posts, so here I put the approaches in one place. There is no silver bullet. Even if there were, it would work only until the next release, and the whole thing stays a cat-and-mouse game.

We look at two setups. The first is Undetected Chromedriver, a Chromedriver version modified for scraping, paired with Selenium to drive Chromium-based browsers and extract data from nodes. The second is Playwright, where in the last 4-5 months Firefox has given me the best results on most Cloudflare-protected sites, in line with our Anti-Detect Anti-Bot matrix. For Playwright I also cover two options I found useful in practice, slow_mo and launch_persistent_context, and why they can matter to the anti-bot.

## What's inside

- Which browsers Undetected Chromedriver and Selenium can drive besides Chrome, including Brave and GoLogin.
- Why Playwright suits this work: it supports Chromium, WebKit and Firefox natively, with sync or async sessions depending on parallelism needs.
- A case where scrapers that worked from my laptop failed from data center VMs, and the single option that changed that.
- Why a browser profile with some history can help against an anti-bot, and the ethical baseline for treating target websites.

**In the full article:** The Undetected Chromedriver and Playwright code examples, the screenshots of the Cloudflare tests, and the exact slow_mo and persistent context setup.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypass-cloudflare-browser-check?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
