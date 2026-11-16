---
type: article_summary
title: 'Web scraping from 0 to hero: creating our first Scrapy spider - Part 2'
slug: web-scraping-from-0-to-hero-creating
canonical_url: https://www.scraping.club/p/web-scraping-from-0-to-hero-creating
publish_date: '2024-01-07'
visibility: free
topics:
- industry-overview
description: 'Second part of building a Scrapy spider for Valentino.com: crawling category pages, request headers and cookies, XPath selectors, product JSON and output.'
source_hash: 04066353f6da84de
---

# Web scraping from 0 to hero: creating our first Scrapy spider - Part 2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-01-07 (free to read). **[Read the full article](https://www.scraping.club/p/web-scraping-from-0-to-hero-creating?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In the previous lesson we set up the Scrapy project for Valentino.com and wrote a spider that only printed the product category URLs. That is not a scraper yet. To get data out, the spider has to follow those URLs, reach every product page and map what it finds to the output fields we defined.

In this lesson we finish the spider and explain the code line by line. We turn the category URLs into requests with callbacks, then look at how headers and cookies are controlled from settings.py, including cookie debugging. For the product pages we cover XPath versus CSS selectors and why I prefer XPath. We also cover the difference between View Page Source and Inspect when you write selectors for Scrapy, which has no rendering browser. The product data sits in a JSON embedded in a script tag, so we extract and clean it, and use a selector only for the product name. Then we export the items to a file.

## What's inside

- Why View Page Source, not Inspect, is the right view when Scrapy has no rendering browser.
- Where default request headers and cookie behavior are configured, and how to watch the cookie jar change between requests.
- Why an embedded JSON is preferred over HTML selectors, and why this spider uses both anyway.
- A short note on how AI-based extraction tools may change selector maintenance, and the loss of control that could come with it.

**In the full article:** The full spider code, the headers configuration, the cookie debug log, the JSON extraction and cleaning expression, the field mapping and the export command, plus the link to the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-scraping-from-0-to-hero-creating?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
