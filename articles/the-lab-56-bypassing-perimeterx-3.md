---
type: article_summary
title: 'The Lab #56: Bypassing PerimeterX 3'
slug: the-lab-56-bypassing-perimeterx-3
canonical_url: https://www.scraping.club/p/the-lab-56-bypassing-perimeterx-3
publish_date: '2024-07-11'
visibility: premium
topics:
- browser-automation
- antibot
- cloudflare
- datadome
description: How to recognize PerimeterX (HUMAN Bot Defender) by its cookies and network calls, and a first set of scraping tests against Crunchbase's public pages.
source_hash: 8811d948f3f7836d
---

# The Lab #56: Bypassing PerimeterX 3

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-11 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-56-bypassing-perimeterx-3?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

PerimeterX, now part of HUMAN Security, sits with Cloudflare, Datadome and Kasada among the main anti-bot solutions. It protects sites like Crunchbase, Zillow and SSense. Before writing a scraper you need to know what you are facing: Sensor, Detector and Enforcer, the Press and Hold challenge or ReCAPTCHA on top, and Hype Sale for sensitive areas like checkout.

We start by recognizing it from its cookies and the domains it calls in the network tab. Then we pick a target protected only by PerimeterX 3, with the _px3 cookie and no other anti-bot, and that target is Crunchbase. We stay on public pages and leave the logged-in content alone. We look at how the site behaves in an incognito browser, then test a Scrapy spider with scrapy-impersonate and Playwright with Chrome on a local Mac, from a clean home IP.

## What's inside

- How to check a site for PerimeterX with Wappalyzer, and why its result needs a second check.
- Why Hype Sale uses slower, heavier challenges and can only cover a small part of a website.
- Why Crunchbase was chosen as the test target, and where we draw the line on paywalled data and Terms of Service.
- How the order of page visits in a manual incognito session shapes the design of the scraper.

**In the full article:** The Scrapy spider and Playwright code, the GitHub folder 56.PERIMETERX3, the second Playwright attempt and the working setup for Crunchbase are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-56-bypassing-perimeterx-3?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
