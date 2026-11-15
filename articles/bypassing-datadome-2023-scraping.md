---
type: article_summary
title: Bypassing Datadome with Web Scraping - End of 2023 Version
slug: bypassing-datadome-2023-scraping
canonical_url: https://www.scraping.club/p/bypassing-datadome-2023-scraping
publish_date: '2023-12-06'
visibility: premium
topics:
- datadome
- browser-automation
- antibot
- captcha
description: Testing Scrapy-impersonate and Playwright against Datadome on Footlocker UK at the end of 2023, and why behavioral analysis makes these projects a lottery ticke
source_hash: d73dcdb28ec5057c
---

# Bypassing Datadome with Web Scraping - End of 2023 Version

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-06 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-datadome-2023-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Datadome is one of the most advanced anti-bot solutions on the market and, in my opinion, the one that leans hardest on behavioral analysis. It combines TLS fingerprinting and AI, and its CAPTCHA can appear in the middle of a session, for scrapers and for human visitors alike. Starting a scraping project on a Datadome website is a lottery ticket. The outcome depends on how the solution is set up on that specific site, and you only find out at the end.

Our target is Footlocker UK, and I'm not sure we can scrape it. We skip plain Scrapy requests, since Datadome blocks them for sure, and start with Scrapy-impersonate, looping through three browsers to impersonate. Then we move to browser automation with Playwright and a real Chrome, going from the home page to a men's shoes category page, and look at what Datadome actually reacts to.

## What's inside

- Why Datadome's behavioral analysis can block a session halfway through, even for a human browsing the site.
- Why plain Scrapy requests are not worth testing against Datadome.
- How we set up Playwright with a persistent Chrome profile in headed mode, with pauses between page loads.
- The difference between a browser being flagged and its navigation pattern being flagged, and what that means for how you move between pages.

**In the full article:** The Scrapy-impersonate and Playwright code, the logs from each run, and our verdict on whether Footlocker UK can be scraped.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-datadome-2023-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
