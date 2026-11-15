---
type: article_summary
title: 'Change detection for web scraping: tools and techniques'
slug: change-detection-for-web-scraping
canonical_url: https://www.scraping.club/p/change-detection-for-web-scraping
publish_date: '2023-10-15'
visibility: free
topics:
- proxies
description: 'How to deal with website changes in scraping pipelines: HTML and tech stack changes, selector best practices, and two tools for change detection.'
source_hash: c065d32310e20008
---

# Change detection for web scraping: tools and techniques

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-10-15 (free to read). **[Read the full article](https://www.scraping.club/p/change-detection-for-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

With web scraping we have no control over the data source. Unlike internal pipelines, where data contracts and similar practices exist, we usually learn that a website changed only when our scraper stops working. If the delivery deadline is tight, there may be no time to fix it.

We split the changes to expect into two groups: HTML modifications and tech stack changes, such as a new or different anti-bot solution. Then we cover how to write scrapers that survive them: the website's API, the JSON the framework embeds in the page, and selectors kept as generic as possible. Refresh frequency also matters, because a weekly or monthly run leaves more days in which a change can go unnoticed. For monitoring between runs, we look at Wappalyzer for detecting the tech stack and anti-bot, and changedetection.io for watching HTML with selectors, including what each costs and what I have or haven't tested in production.

## What's inside

- Why changes in fashion retail are partly predictable, around new collections, discount seasons and Black Friday, and why those are only soft signals.
- Why a framework change is treated as an HTML change.
- How refresh frequency, daily or intraday versus weekly or monthly, changes how fast we notice a break.
- How changedetection.io handles selectors, proxies for anti-bot protected sites, a visual editor and alerts through messaging platforms.

**In the full article:** The XPath example, the names of the embedded JSON objects for React and Next.js, the Wappalyzer API cost, the changedetection.io pricing and my notes on using both tools.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/change-detection-for-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
