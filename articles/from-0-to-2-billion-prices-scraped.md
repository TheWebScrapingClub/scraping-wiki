---
type: article_summary
title: From 0 to 2 Billion Prices scraped per months
slug: from-0-to-2-billion-prices-scraped
canonical_url: https://www.scraping.club/p/from-0-to-2-billion-prices-scraped
publish_date: '2022-08-06'
visibility: free
topics:
- proxies
- scraping-infra
description: How Databoutique.com went from 0 to 2 billion prices scraped per month, bootstrapped and with a minimal developer team, and the principles behind it.
source_hash: fa8aa9f4ce900101
---

# From 0 to 2 Billion Prices scraped per months

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-08-06 (free to read). **[Read the full article](https://www.scraping.club/p/from-0-to-2-billion-prices-scraped?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

At Databoutique.com we went from an empty database to 2 billion prices scraped per month. We did it bootstrapped and with a minimal team of developers, so costs and headcount had to stay low while volume grew. Both founders came from business intelligence consulting, and we started with one kind of data only: prices. Things are far from perfect and we made tons of mistakes along the way.

I wrote down the principles that guided our development, the notes I wish I had read before starting. They are thinking big from the start, keeping it simple, standardizing, building processes like LEGO bricks, and keeping an eye on everything. Together they cover our data model, our in-house Python ETLs, our scraper templates, the internal building blocks for cloud and proxies, and the monitoring we run to keep a small team productive.

## What's inside

- What we give up by choosing a simple, common data model: some customer requests for product-level detail.
- Why we built our own ETLs and logging instead of adding a third-party tool like Airflow.
- How a new website enters production: a scraper written from a template, pushed live, and scheduled with one line in a table.
- How we split process controls from data quality controls, and how we track cloud provider costs as a bootstrapped company.

**In the full article:** Our full reasoning on each of the five principles, the freelancer workflow for fixing a running scraper with its two human steps, the automatic issue routing, and the daily cloud cost report.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/from-0-to-2-billion-prices-scraped?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
