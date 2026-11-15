---
type: article_summary
title: Bypassing Perimeterx in 2023 with code and examples
slug: bypassing-perimeterx-2023
canonical_url: https://www.scraping.club/p/bypassing-perimeterx-2023
publish_date: '2023-08-17'
visibility: premium
topics:
- browser-automation
- captcha
- anti-detect-browsers
- antibot
description: 'How to detect PerimeterX on a site and get past it on Neimanmarcus.com with free tools: Undetected Chromedriver and Playwright on Firefox, Chrome and Brave.'
source_hash: 2fd0c172c4309d4b
---

# Bypassing Perimeterx in 2023 with code and examples

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-17 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-perimeterx-2023?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

PerimeterX, now part of Human, is one of the most widespread anti-bot solutions on the web. It combines fingerprinting on several layers, IP filtering and AI applied to behavioral analysis, so a scraper that only fixes one of these layers usually still gets blocked. Neimanmarcus.com is a good example of a target protected this way, and it shows the Press and Hold challenge many of you have already met.

We looked at how to recognize a PerimeterX-protected site, using Wappalyzer or a specific cookie. Then we tested free bypass options against Neimanmarcus.com: Undetected Chromedriver and Playwright, running Firefox, Chrome and Brave. We tried them locally and from a datacenter with proxies. We also looked at the behavioral side, with random pauses and scrolling between actions. These setups are a starting point, since every site configures the protection differently.

## What's inside

- How to spot PerimeterX from the Wappalyzer security section or from a cookie in the browser storage.
- Why I used Brave with Undetected Chromedriver instead of Chrome, and what it fixed.
- The Playwright option that slows execution down, and why I think it matters on a low-latency server connection.
- Differences between Playwright with Firefox and with Chromium, and which Chrome settings and persistent context the second one needs.

**In the full article:** The code of each scraper from the GitHub repository, the Playwright launch options for Firefox, Chrome and Brave, and the per-browser results on the Neimanmarcus category crawl.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-perimeterx-2023?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
