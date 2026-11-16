---
type: article_summary
title: The costs of web scraping
slug: the-costs-of-web-scraping
canonical_url: https://www.scraping.club/p/the-costs-of-web-scraping
publish_date: '2022-09-11'
visibility: free
topics:
- proxies
- scraping-infra
description: 'A cost comparison of AWS, Azure and Google Cloud for web scraping: micro and medium VMs, storage for archived HTML, and per-GB proxy pricing.'
source_hash: 1363a9be6cfc4b3a
---

# The costs of web scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-09-11 (free to read). **[Read the full article](https://www.scraping.club/p/the-costs-of-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloud computing made large-scale scraping cheaper, but not cheap, and sites keep getting harder to scrape. At Databoutique.com we use about 500k VM hours of different sizes every month, so the choice of provider shows up directly in the bill. Storage and proxies add their own line items, and they grow faster than most teams expect.

I benchmarked the top 3 cloud providers by market share, picking the cheapest availability zone for each. We compared a micro-sized VM for a simple Scrapy spider, calculated over 10,000 hours of use, and a medium-sized VM with enough RAM for a full headful browser. Then we matched four storage tiers across the three providers and looked at what it costs to keep the HTML of every run. For proxies, I used Bright Data and Oxylabs as examples of per-GB billing. I close with what this means for burn rate before a dataset has any commercial value.

## What's inside

- How I built comparable configurations across the three providers, using the smallest machine that still runs Scrapy.
- Why Google's per-operation storage charges change the comparison, and why I excluded redundancy options.
- A worked example of archiving HTML for a 500k-page site read daily, with gzip and 30 days of retention.
- The questions that decide proxy cost: geo-targeting, request limits per IP and the strength of the anti-bot defenses.

**In the full article:** The price tables for micro and medium VMs and for the four storage tiers, the provider rankings, the storage calculation for the 500k-page site and the Bright Data and Oxylabs pricing screenshots.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-costs-of-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
