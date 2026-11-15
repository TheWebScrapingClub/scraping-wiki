---
type: article_summary
title: Bypassing Cloudflare with open source repositories
slug: bypassing-cloudflare-free-tools
canonical_url: https://www.scraping.club/p/bypassing-cloudflare-free-tools
publish_date: '2024-05-03'
visibility: premium
topics:
- cloudflare
- browser-automation
- anti-detect-browsers
- proxies
description: Open source ways to get past Cloudflare bot protection, from IP and environment tests to Scrapy Impersonate and Undetected Chromedriver, with caveats on each.
source_hash: c4aa8214665222c5
---

# Bypassing Cloudflare with open source repositories

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-05-03 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-cloudflare-free-tools?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

"How can I bypass Cloudflare?" is the question I see most in every scraping community, and it comes without context. Cloudflare has the biggest market share among anti-bot solutions, and installations differ in strictness. A fix that works on one protected site may do nothing on the next. Before picking a tool, you need to know why your scraper is blocked.

I start with the diagnosis: run the same scraper from a residential connection and from a server, then separate browserless setups such as Scrapy with Scrapy-impersonate from browser automation with Selenium or Playwright, where fingerprinting changes the picture. Then I look at the open source side. I recall our earlier tests of Undetected Chromedriver against Cloudflare and other anti-bots, and I pick three free solutions to try, starting with Scrapy Impersonate, which I still run in production. Results always depend on the running environment and on each site's rules.

## What's inside

- How to tell an IP reputation problem from a fingerprinting problem by changing where the scraper runs
- Why adding residential proxies is often enough for browserless scrapers but not for Selenium or Playwright
- What Undetected Chromedriver does and does not do, and why its maintainer limited the issue tracker
- Why no free tool works everywhere, given how much Cloudflare invests in R&D

**In the full article:** The three selected open source solutions with the reasoning behind each choice, and the code in the paid GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-cloudflare-free-tools?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
