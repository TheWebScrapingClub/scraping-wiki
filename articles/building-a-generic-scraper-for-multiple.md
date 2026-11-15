---
type: article_summary
title: Building a generic scraper for multiple websites
slug: building-a-generic-scraper-for-multiple
canonical_url: https://www.scraping.club/p/building-a-generic-scraper-for-multiple
publish_date: '2024-11-03'
visibility: free
topics:
- akamai
- datadome
- cloudflare
- llm-scraping
description: One scraper per site or one generic scraper for ten e-commerce sites, comparing Schema.org markup with the Zyte API against Datadome and Akamai.
source_hash: c2991cdbf827df45
---

# Building a generic scraper for multiple websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-11-03 (free to read). **[Read the full article](https://www.scraping.club/p/building-a-generic-scraper-for-multiple?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

On any project with many websites, the same doubt comes up: dedicated scrapers or one generic scraper. I have always built a dedicated one per site, even as standards like Schema.org spread for SEO reasons. With LLM-powered scraping tools around, I wanted to check whether that habit still holds. The test case is ten e-commerce sites and one fixed output: product code, full and final price with currency code, category, item URL, main image URL and name.

We first checked what Schema.org Product markup gives us on real product pages. Then we looked at LLM-based tools such as Skyvern, ScrapeGraph AI and Firecrawl. For the test we used the Zyte API on sites behind Datadome, Akamai, Cloudflare and Kasada. The scraper has two functions, product navigation and product detail, and the pool includes infinite scroll, "view more" buttons and odd discount layouts.

## What's inside

- Schema.org Product fields are optional and not constrained, and we show real pages from Dolce e Gabbana and Yoox where a price field is incomplete.
- What a third-party tool must deliver to replace custom parsers: a fixed output schema, a way to correct wrong LLM output, and anti-bot bypass.
- Why the brand field matters on multi-brand sites, and how a custom output schema could cut the number of API calls.
- Why the pool mixes famous multi-brand sites with lesser-known mono-brand ones, and why it is harsher than the basket most projects will have.

**In the full article:** Test results per site, the findings on pagination, brand and category fields, the full list of the ten targets with their protections, and the generic-scraper code in the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-a-generic-scraper-for-multiple?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
