---
type: article_summary
title: 'Web Scraping from 0 to hero: data cleaning processes'
slug: web-data-quality-pipeline
canonical_url: https://www.scraping.club/p/web-data-quality-pipeline
publish_date: '2024-05-12'
visibility: free
topics:
- browser-automation
description: Two ways to clean and standardize scraped web data, inside the scraper or in a database after loading, with the pros and cons of each.
source_hash: 6643ef4ee20c69d4
---

# Web Scraping from 0 to hero: data cleaning processes

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-05-12 (free to read). **[Read the full article](https://www.scraping.club/p/web-data-quality-pipeline?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Getting the text out of the HTML is not the end of the job. A price can come with or without a thousands separator, with a comma or a dot, with or without a currency symbol. Descriptions carry new line characters, and country and currency codes change from site to site. If you want to compare extractions, you need a data cleaning and standardization process.

There are two places to put it: in the scraper, or in a database after loading. We walk through a data quality process for structured e-commerce data, from numeric and string cleaning to standardization and validation, up to publishing to the final user. We show it on a SQL database, using regular expressions and lookup tables for country codes. Then we look at the same steps embedded in a Python scraper, with a library like Price-Parser. We close by weighing the two approaches, especially when the number of scrapers grows.

## What's inside

- How a lookup table with two columns keeps country standardization maintainable, since the values you meet are many but finite.
- Which validation checks to run before publishing: e-mail format, valid product URLs, empty fields, unmapped values, and how to link them to alerts.
- Why standardization is the harder step inside the scraper, and the options for bringing the target values in.
- The cost of adding a database to your stack when you only scrape a few websites.

**In the full article:** The full step-by-step pipeline diagram, the lookup table example, the data quality checklist and the complete pros and cons comparison of the two approaches are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-data-quality-pipeline?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
