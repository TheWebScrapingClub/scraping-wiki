---
type: article_summary
title: The Kallax Index - Scraping Ikea websites
slug: ikea-scraping-kallax
canonical_url: https://www.scraping.club/p/ikea-scraping-kallax
publish_date: '2022-10-20'
visibility: free
topics:
- http-clients
description: Scraping the price of one IKEA Kallax bookshelf across 61 country sites to see how far local prices drift, and what multi-country scraping breaks along the way.
source_hash: f5c43e3d75fab259
---

# The Kallax Index - Scraping Ikea websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-10-20 (free to read). **[Read the full article](https://www.scraping.club/p/ikea-scraping-kallax?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

The Big Mac Index assumes the same burger should cost the same everywhere. Most retail doesn't work that way: production site, logistics, taxes, duties and currency moves all change the final price. IKEA is a good example. It sells in 61 countries, mostly manufactures far from where it sells, and has a bestseller available everywhere, the Kallax bookshelf.

We used the white 77x77cm Kallax as a price index and scraped it from every IKEA country site. There is no official list of localizations, so mapping the sites was manual and tedious. The same item turned out to carry different product codes in some regions, and 14 country sites run on a different tech stack, with no common API. I built the scraper in Scrapy around the internal search API and filled the remaining countries by hand. Then we put the output in a Google Spreadsheet with currency conversion to compare prices.

## What's inside

- How we found the internal product search API with the Chrome network tools, and what the JSON gives back
- Why some sites use a different stack, from local development teams in greater China and Japan to staggered software rollouts
- Why the currency ISO code in the API response saved us a data standardization step
- Where currency conversion belongs in a real pipeline, and what a large price gap can signal

**In the full article:** The product codes per region, the list of countries on each website variant, the API endpoint format, the Scrapy scraper on GitHub, the Google Spreadsheet with the results and the price range we measured.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/ikea-scraping-kallax?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
