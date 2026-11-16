---
type: article_summary
title: How to scrape Datadome protected websites (early 2023 version)
slug: how-to-scrape-datadome-2023
canonical_url: https://www.scraping.club/p/how-to-scrape-datadome-2023
publish_date: '2023-04-14'
visibility: premium
topics:
- datadome
- browser-automation
- antibot
- captcha
description: Testing free Playwright setups with Chrome, Firefox and Brave against Datadome on Footlocker.it, plus how to detect Datadome and what bypassing it costs.
source_hash: 9ee17b53b7644101
---

# How to scrape Datadome protected websites (early 2023 version)

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-04-14 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-scrape-datadome-2023?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Datadome is gaining popularity as an anti-bot solution, and it shows up on large sites you may need in a project. It combines device fingerprinting, behavior analysis and machine learning, so a basic Scrapy spider with no JavaScript rendering has no chance. Bypassing it has a cost, especially when several big websites are involved. This is the third post in our anti-bot series, after Kasada and Cloudflare.

We start with how to recognize Datadome on a target, then test free open-source tools against Footlocker.it, aiming at the men's shoes product list page. We ran Playwright with Chrome, Firefox and Brave, both on a local machine and on a VM in a datacenter, and tried a package that simulates human mouse movements. We close with the cost trade-off between headful browsers and commercial APIs called from a simple Scrapy spider.

## What's inside

- Three ways to spot Datadome: Wappalyzer, the cookie set on the first response, and the slider challenge you can get in Incognito mode.
- python_ghost_cursor simulates human mouse movements with Bezier curves, and it only works with Chrome.
- Each browser setup was run from both a local environment and a datacenter VM, since results vary with target configuration and environment.
- Headful browsers need more CPU and memory, while commercial APIs charge per call but cut the cost of the machines hosting the scrapers.

**In the full article:** The scraper code and screenshots for each Playwright setup, and the result per browser and environment on Footlocker.it.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-scrape-datadome-2023?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
