---
type: article_summary
title: 'Browser API: an introduction'
slug: browser-api-an-introduction
canonical_url: https://www.scraping.club/p/browser-api-an-introduction
publish_date: '2023-09-09'
visibility: free
topics:
- browser-automation
- anti-detect-browsers
- antibot
- cloudflare
description: 'Introduction to browser APIs and fingerprinting for scrapers: which attributes anti-bots read, from navigator.webdriver to hardware data, and how to check them.'
source_hash: 142852e2899a6158
---

# Browser API: an introduction

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-09-09 (free to read). **[Read the full article](https://www.scraping.club/p/browser-api-an-introduction?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Before building a scraper against a protected site, it pays to see what your browser stack tells the target. Every browser exposes hundreds of client-side API values about itself, its hardware and its user. Anti-bots read them, mix them with the IP and encode the result as a fingerprint. A scraper that looks wrong on this data gets blocked, however good its behavior is.

I start from what client-side APIs are and why they exist, then split the exposed information into three groups: location, browser and hardware. For location, the IP and the proxy provider decide everything. For the browser group, I use the navigator.webdriver flag as the example and run the Sannysoft test with Playwright with Chromium, Playwright with Chrome and undetected-chromedriver. For the hardware group, I cover why a scraper that works on your PC can fail from a datacenter even with residential proxies. I also look at Brave and anti-detect browsers such as GoLogin and Kameleo.

## What's inside

- How to inspect window.navigator in the developer console and compare your own browser with your Selenium or Chromium scraper.
- Why a scraper that passes every check on a local PC can still be blocked once deployed in a datacenter behind residential proxies.
- Why missing audio outputs on servers can work as a red flag, and how a customized hardware profile helped me with some Cloudflare-protected sites.
- The closing principles: mimic typical human setups, don't overload the target, and don't scrape personal or copyrighted data.

**In the full article:** Test code for Playwright and undetected-chromedriver on Sannysoft, the script that prints browser attributes programmatically, and the Sannysoft screenshots comparing each configuration.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/browser-api-an-introduction?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
