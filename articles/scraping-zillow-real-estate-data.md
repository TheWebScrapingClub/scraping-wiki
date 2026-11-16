---
type: article_summary
title: 'THE LAB #81: Scraping Zillow for fun and profit'
slug: scraping-zillow-real-estate-data
canonical_url: https://www.scraping.club/p/scraping-zillow-real-estate-data
publish_date: '2025-04-17'
visibility: premium
topics:
- industry-overview
description: Scraping Zillow listings through its internal search API, and using square tiling to get past the 20-page, roughly 820-listing cap on results.
source_hash: 826507e38733efb9
---

# THE LAB #81: Scraping Zillow for fun and profit

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-04-17 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-zillow-real-estate-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Real estate was the first market we targeted at Re Analytics, and Zillow is one of the biggest targets in the US. Its listings are public and structured, and the site covers over 110 million properties. The catch is that a search never shows more than 20 pages of results, about 820 listings. Query a whole state and most of it stays hidden behind that cap.

We start from how Zillow's map-based search works and use the Network tab to find the internal search API behind it. We look at the searchQueryState payload, with its map bounds, region selection and the wants parameter, and at what the JSON returns for each listing. Then we get around the pagination cap with square tiling, splitting areas recursively until each tile fits under the limit. New York State is the working example, followed by a read of zillow_with_grids.py.

## What's inside

- Why we filter by state instead of stacking many filters, and how the region identifier changes from one state to another.
- What each listing carries in the JSON response: the zpid, price, coordinates, beds and baths.
- Why tiling only subdivides where needed: sparse rural areas need few requests, while dense cities get split much deeper.
- Why real estate sites hold thousands of results no human ever sees, and how that shapes the way we design the scraper.

**In the full article:** The zillow_with_grids.py script with its walkthrough, the request payload screenshots, and the 81.ZILLOW folder in the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-zillow-real-estate-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
