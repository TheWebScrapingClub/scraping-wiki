---
type: article_summary
title: How to Scrape E-Commerce Websites With Python
slug: scraping-amazon-aliexpress-api
canonical_url: https://www.scraping.club/p/scraping-amazon-aliexpress-api
publish_date: '2024-07-23'
visibility: free
topics:
- data-analysis
description: A Python tutorial on scraping Amazon search results and an AliExpress product page with Oxylabs' E-Commerce Scraper API, parsed into a pandas DataFrame.
source_hash: 87cdbd4cd5d8372e
---

# How to Scrape E-Commerce Websites With Python

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-23 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-amazon-aliexpress-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Market analysts scrape e-commerce sites for market research, trend analysis and pricing new products. The practical issue is that every platform has its own page types, and keeping parsers and anti-bot handling alive across them takes time. A managed API that returns parsed data cuts a lot of that work.

We built two small scrapers in Python with Oxylabs' E-Commerce Scraper API, a partner of the newsletter. The first takes a search query on Amazon and returns the list of products. The second reads a single product page on AliExpress through the universal_ecommerce source. We use Requests to call the API and pandas to hold and export the results. I cover how Amazon is handled through dedicated data sources while other shops need only a product URL, which parameters are mandatory in the payload, and which fields we pull from the parsed response.

## What's inside

- Amazon is supported through dedicated source keys, one per page type, while other shops go through a single universal source.
- Only the source and query parameters are mandatory in the Amazon search payload. Domain, start page, number of pages and the parse flag are optional.
- The Amazon scraper extracts title, ASIN, price and URL into a DataFrame, then exports to CSV and JSON.
- The AliExpress example reads title, price with currency, and description from the parsed product page.

**In the full article:** The full payload parameter table, the complete Python code for both scrapers, the list of Amazon data sources and the output screenshots for each run.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-amazon-aliexpress-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
