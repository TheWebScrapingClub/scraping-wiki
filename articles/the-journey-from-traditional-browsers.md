---
type: article_summary
title: From Traditional Browsers to AI-Powered Web Scraping
slug: the-journey-from-traditional-browsers
canonical_url: https://www.scraping.club/p/the-journey-from-traditional-browsers
publish_date: '2023-06-11'
visibility: free
topics:
- browser-automation
- nlp-ml
- antibot
- proxies
description: A guest post by Nimble's CEO on why headless browsers fall short against anti-bot systems and how an AI fingerprinting engine and a from-scratch browser respond
source_hash: 92453118a475ae6e
---

# From Traditional Browsers to AI-Powered Web Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-06-11 (free to read). **[Read the full article](https://www.scraping.club/p/the-journey-from-traditional-browsers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Selenium, Puppeteer and Playwright made scraping at scale possible, and then anti-bot vendors learned to spot them. Blocks got more frequent, fingerprint leaks got harder to plug, and the browsers ate compute. Teams ended up patching all the time instead of working on the data.

This guest post comes from Uriel Knorovich, CEO at Nimble, so it is the vendor's view of the problem. He describes Nimble Browser, built from scratch instead of on top of Chromium, and the AI fingerprinting engine that picks fingerprints by matching them against profiles of the target sites. He then shows how the browser is used through Nimble APIs, with residential proxies, NLP parsing and page interactions, and lists the use cases Nimble sees: e-commerce, marketing and brand protection.

## What's inside

- Which fingerprint parameters the engine claims to control, from operating system and fonts to sub-pixel hinting and GPU stats.
- The two datasets behind the model, fingerprints and website profiles, and why the second was harder to collect.
- Why Nimble chose to write a browser from scratch instead of building on Chromium.
- How Nimble Lab and a real-time browser update system are meant to react when a block is detected.

**In the full article:** The sample Nimble Web API request on an Amazon product page, with its geolocation and click-and-wait page interaction, plus the full description of the training and browser update process.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-journey-from-traditional-browsers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
