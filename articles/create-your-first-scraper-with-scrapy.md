---
type: article_summary
title: 'How to Create Your First Web Scraper with Scrapy: A Step-by-Step Tutorial'
slug: create-your-first-scraper-with-scrapy
canonical_url: https://www.scraping.club/p/create-your-first-scraper-with-scrapy
publish_date: '2023-08-06'
visibility: free
topics:
- proxies
- browser-automation
- residential-proxies
- proxy-industry
description: A beginner tutorial on building a first Scrapy spider against quotes.toscrape.com, with a bonus step on routing requests through a proxy middleware.
source_hash: 64abbd833c5cad99
---

# How to Create Your First Web Scraper with Scrapy: A Step-by-Step Tutorial

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-06 (free to read). **[Read the full article](https://www.scraping.club/p/create-your-first-scraper-with-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy is my first choice for websites with no anti-bot. It is asynchronous, handles pagination, cookies and user agents out of the box, and can render JavaScript through Splash, though Splash won't help against sophisticated anti-bots. If you are new to it, the hard part is seeing how the pieces fit together before you write any code.

We start from the architecture: spiders, engine, Twisted, middlewares, Items and the built-in storage options. Then we build a first scraper on quotes.toscrape.com in six steps, from installing Scrapy and generating the project to defining the item, writing XPath selectors, following the next-page link and exporting to JSON. I explain why I keep selectors as short as possible and why the last page needs special handling. A bonus step shows how to plug a proxy into the project with the advanced-scrapy-proxies package, using Oxylabs Web Unblocker as the example.

## What's inside

- How the Scrapy architecture diagram maps to what you actually write: spiders, items and middlewares.
- Why I choose XPath over CSS selectors in this example, and why shorter selectors break less often.
- How pagination works with a callback loop, and what happens on the last page when the next-page selector is missing.
- The proxy modes of advanced-scrapy-proxies and how to keep credentials out of the proxy list file.

**In the full article:** The full code for the items file, the spider and the pagination, the settings and launch parameters for the proxy middleware, the list of proxy modes and the link to the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/create-your-first-scraper-with-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
