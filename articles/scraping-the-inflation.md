---
type: article_summary
title: Scraping The Inflation
slug: scraping-the-inflation
canonical_url: https://www.scraping.club/p/scraping-the-inflation
publish_date: '2024-12-03'
visibility: free
topics:
- industry-overview
description: Why scraping prices to measure inflation is hard, and why splitting raw data collection from index construction could work, with a survey of statistical offices
source_hash: 8f41bd47418c2afd
---

# Scraping The Inflation

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-03 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-the-inflation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Inflation is probably the most ambitious scraping target there is. Online prices are only a subset of what an economy spends, and nobody knows how representative they are. Validating them against manual or scanner-based collection takes long time series, and those are fragile because websites, assortments and product identifiers like EAN codes keep changing. On top of that, national statistics institutes publish their CPI baskets only as taxonomy updates, with no bar codes or retailer details, so nobody can replicate or improve the indices from the ground up.

I look at where the work gets stuck and why generative AI scrapers don't fix it at scale. I then propose splitting the quest in two: raw data acquisition, which should be a shared and syndicated effort, and index construction, which should be an open market with different skills. I size the gap between ISTAT's price quotations and what daily grocery scraping in Italy could produce. I also go through who has already tried this, from the Billion Prices Project to ISTAT, ONS, ECB, BIS and BLS.

## What's inside

- Why scraped price series lose value when retailers start showing EAN or bar codes, and how the COVID-19 shift in grocery assortments broke consistency.
- A luxury example, the Small Lady Dior bag in France, to show what sector-specific indices could capture that official baskets miss.
- What we saw with spider.cloud, Firecrawl and Jina.ai on large-scale collection, including the cost of fixing hallucinated prices.
- The limits of the approach: web scraping covers consumer prices and leaves out much of B2B services inflation.

**In the full article:** The back-of-the-envelope calculation comparing ISTAT's monthly price quotations with scraped grocery data, the full profiles of each institution's web scraping initiative with source links, and the Data Boutique angle.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-the-inflation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
