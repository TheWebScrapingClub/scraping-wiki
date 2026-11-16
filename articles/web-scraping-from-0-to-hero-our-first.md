---
type: article_summary
title: 'Web Scraping from 0 to hero: our first scraper with Microsoft Playwright'
slug: web-scraping-from-0-to-hero-our-first
canonical_url: https://www.scraping.club/p/web-scraping-from-0-to-hero-our-first
publish_date: '2024-02-04'
visibility: free
topics:
- browser-automation
- antibot
description: A first Playwright scraper in Python for valentino.com, built on raw HTML and compared with the Scrapy version of the same job.
source_hash: eed85e1ade9f5ba7
---

# Web Scraping from 0 to hero: our first scraper with Microsoft Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-04 (free to read). **[Read the full article](https://www.scraping.club/p/web-scraping-from-0-to-hero-our-first?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy or Playwright? It depends on two things: anti-bot protection and content that only appears after JavaScript runs. If the data is in the HTML and the target has no anti-bot, Scrapy is the right choice. It's asynchronous, lightweight and built for scraping. Browser automation tools, Playwright included, are a last resort for sites that need a real browser.

In this lesson of Web Scraping from 0 to Hero we build our first Playwright scraper in Python. The target is valentino.com, the same site as the Scrapy spider, so the two codebases can be compared side by side. We set up the environment, choose between sync and async mode, and read the raw HTML instead of the rendered page. Playwright has no built-in parser, so we pick one from BeautifulSoup, lxml or Scrapy's HtmlResponse. Then we crawl from categories to product pages and write the output to a CSV file. We close with a comparison of the two tools on speed and resource use.

## What's inside

- How the sync and async APIs differ in Python, and why we chose sync for readability
- The rendered DOM and the raw HTML of the Valentino menu differ, and that decides which one we scrape
- Which HTML parsers can be paired with Playwright, and why we used Scrapy's HtmlResponse with XPath
- What we left out on purpose, such as pagination inside each subcategory, and what the next lesson covers

**In the full article:** The complete scraper code, the installation commands, the browser launch options, the XPath selectors and JSON parsing for the product pages, and the Scrapy vs Playwright execution time comparison.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-scraping-from-0-to-hero-our-first?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
