---
type: article_summary
title: Reading StockX’s internal API with the Decodo Web Data API
slug: reading-stockxs-internal-api-decodo-web-data-api
canonical_url: https://www.scraping.club/p/reading-stockxs-internal-api-decodo-web-data-api
publish_date: '2026-11-18'
visibility: free
topics:
- proxies
- antibot
- cloudflare
description: Testing the Decodo Web Data API on StockX and eBay Italy for a LEGO price comparison, reading StockX's internal GraphQL calls with the xhr parameter.
source_hash: 2da1e2149f09bb34
---

# Reading StockX’s internal API with the Decodo Web Data API

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-11-18 (free to read). **[Read the full article](https://www.scraping.club/p/reading-stockxs-internal-api-decodo-web-data-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

After paying three different prices for the same DUPLO set (airport, LEGO site, supermarket), I wondered whether there is still room for LEGO resellers who buy on one website and sell on another. To answer it we need prices from StockX and eBay, and both sit behind anti-bots. That makes them a good battleground for the new Decodo Web Data API.

We tested /scrape, /search and /map through a thin Python client that logs every call. On StockX we used the xhr parameter on the LEGO collectibles list sorted by highest bid, to read the internal API calls behind the page instead of parsing HTML. On eBay Italy we ran one search for each set number found on StockX, read price and condition from the result cards, and checked how the API behaves when the target pushes back. We also looked at what each configuration costs.

## What's inside

- How the four endpoints are priced per 1,000 successful requests, depending on proxy pool and JavaScript rendering, and which three we used.
- What the xhr response contains, why you still have to find the right call among the analytics and ad requests, and what the geo parameter changes in the market StockX shows.
- How the API reports a failed scrape and a browser-check page, and what ends up billed in each case.
- Why eBay needs a custom parser: there is no ready template for it among the Decodo target templates.

**In the full article:** The complete client, StockX and eBay scripts and parser code, the per-run call counts and success rates, the dashboard comparisons, the cost figures and the LEGO price dataset built from the two sources.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/reading-stockxs-internal-api-decodo-web-data-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
