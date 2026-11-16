---
type: article_summary
title: 'The Lab #54: Scraping from Algolia APIs'
slug: scraping-algolia-endpoints
canonical_url: https://www.scraping.club/p/scraping-algolia-endpoints
publish_date: '2024-06-21'
visibility: premium
topics:
- legal-ethics
description: How EndClothing loads its product lists through an Algolia search endpoint, how the request payload works, and what product data the JSON returns.
source_hash: 50b218d4c102215d
---

# The Lab #54: Scraping from Algolia APIs

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-21 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-algolia-endpoints?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Alex Lokhov at MapeZero showed how web data from a fashion marketplace can measure sustainability by brand, using the materials listed on product detail pages. The site he used, endclothing.com, is one of the hundreds we scrape at Re Analytics. It fits the idea behind Databoutique: the data is the same for everyone, yet every buyer pays to collect and refine it alone.

We started where we start with an e-commerce site, the network tab, checking how the product list pages paginate. On EndClothing the load more button calls an Algolia endpoint. We break down the URL, with its application ID and API key parameters, and the request payload that carries filters and page number. Then we look at the JSON returned per product and the use cases it supports: price monitoring, fabric and color analysis for ESG work, image collection for AI training, and stock-based sales tracking.

## What's inside

- How the Algolia URL breaks down: base host, API version, the indexes wildcard, and the agent, application ID and API key parameters.
- Why the payload carries four queries for a single category, and which parts of it we change to move across filters and pages.
- Which response fields cover prices per country, categories, description, sizes, colors, image galleries and stock, and which Databoutique data schemas match each use case.
- A caveat on using API keys and endpoints you find in the browser: terms of service of the target site and of Algolia still apply.

**In the full article:** Scraper code from the GitHub repository (folder 54.ALGOLIA-END), the full request payload and sample JSON response, and the build of the scraper itself.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-algolia-endpoints?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
