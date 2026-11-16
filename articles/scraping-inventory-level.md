---
type: article_summary
title: 'THE LAB #27: Scraping stock level data to estimate revenues'
slug: scraping-inventory-level
canonical_url: https://www.scraping.club/p/scraping-inventory-level
publish_date: '2023-09-14'
visibility: premium
topics:
- industry-overview
description: How stock levels exposed by fashion e-commerce sites, from out-of-stock flags to exact quantities, can be scraped and read as a proxy for online sales.
source_hash: 42098331e31b8aa8
---

# THE LAB #27: Scraping stock level data to estimate revenues

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-09-14 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-inventory-level?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

E-commerce pricing is public, factual data, and I have scraped hundreds of fashion sites over the years. Stock levels are a less obvious layer. Brands, stores and distributors have to talk to each other, so a site often shows what is left in the warehouse or in a store. That communication happens in your browser, which means we can extract it.

We look at two uses of this data. The first is out-of-stock analysis, which works on almost any site and needs a daily scraping run with no missed items. The second is sales estimation, for sites that expose the exact quantity somewhere in the code or in the API calls they make. We go through how to read changes in those quantities: returns, restocks, and end-of-season clearouts that are not sales. We also ask why such sensitive data sits in plain sight, and why hedge funds care about it. Industry knowledge is what makes the numbers readable.

## What's inside

- Why a missing item in a scrape can be mistaken for a sold-out one, and what that demands from the scraping process
- How a capsule collection that sells out in days is normal for some brands and a warning sign for others
- How to tell a return from a restock using a threshold tied to the sales volume of the site, with a worked stock sequence
- My guess on why internal warehouse APIs end up exposed on public sites, and why hedge funds buy this kind of data

**In the full article:** The two live examples on publicly traded companies' e-commerce sites, the way the stock data is extracted from each, and the rules used to turn stock movements into sales estimates.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-inventory-level?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
