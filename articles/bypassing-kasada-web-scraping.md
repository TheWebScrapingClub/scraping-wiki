---
type: article_summary
title: Bypassing Kasada for web scraping 2024 edition
slug: bypassing-kasada-web-scraping
canonical_url: https://www.scraping.club/p/bypassing-kasada-web-scraping
publish_date: '2024-01-25'
visibility: premium
topics:
- browser-automation
- anti-detect-browsers
- cloudflare
- antibot
description: How Kasada's 429 challenge and fingerprinting work, and a first attempt at scraping public prices from Canada Goose with undetected-chromedriver.
source_hash: 33024916d8ec8750
---

# Bypassing Kasada for web scraping 2024 edition

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-01-25 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-kasada-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada is a niche anti-bot with a different approach from the others we have covered. It works like a firewall: it collects hundreds of data points from the browser, applies some AI, and decides whether the request goes through. The first request gets a 429 challenge. If the fingerprint looks like a human browsing, we are redirected to the URL, otherwise we see a white page. Scrapers without a JavaScript rendering engine, like Scrapy, are cut out by default.

Our target is Canada Goose, where we want public prices. We approached it with three tools, starting with undetected-chromedriver. The scraper loads the home page, collects the product categories, scrolls each one to the bottom because of the infinite scroll, then extracts the product data. Along the way I recap what Selenium and webdrivers do and why options like headless mode matter against Kasada.

## What's inside

- Kasada's core business is fraud prevention, so login and purchase checks are likely stricter. We stay on what is visible when browsing public data.
- Selenium, ChromeDriver, GeckoDriver and EdgeDriver explained, and what undetected-chromedriver changes compared to the standard chromedriver.
- Why the scraper has to handle infinite scroll before extracting anything from a category page.
- The cookie popup on first load and how we collect the category URLs as input for the second part of the scraper.

**In the full article:** The full scraper code for all three solutions, the browser options as we set them, the category and product extraction logic, and the results of each tool against Kasada.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-kasada-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
