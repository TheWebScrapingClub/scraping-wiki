---
type: article_summary
title: 'Algolia and web scraping: an introduction'
slug: algolia-and-web-scraping-an-introduction
canonical_url: https://www.scraping.club/p/algolia-and-web-scraping-an-introduction
publish_date: '2023-12-10'
visibility: free
topics:
- http-clients
description: An introduction to Algolia, the search-as-a-service behind many sites, and how to scrape its API endpoint, with the Michelin Guide starred restaurants as the ex
source_hash: a048d02d98fef3cf
---

# Algolia and web scraping: an introduction

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-10 (free to read). **[Read the full article](https://www.scraping.club/p/algolia-and-web-scraping-an-introduction?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Many sites load their lists and search results from Algolia, a hosted search service, instead of rendering them in the HTML. For scraping this is good news. The endpoint returns JSON, it puts less load on the site, and the scraper is faster to write and more stable than one that parses raw HTML.

We cover what Algolia is and how its requests are built: the agent, API key and application ID in the URL, plus a payload that changes with the implementation. We compare two cases, the Hacker News search and the Michelin Guide, which uses instantsearch. Then we scrape all the starred restaurants of the Michelin Guide. We find the request in the browser's network tab, replicate it and paginate through the results with a Scrapy spider split in two functions. The data was also used by Martina Pugliese of Doodling Data for charts on Michelin stars by country.

## What's inside

- How the Hacker News search payload differs from the Michelin Guide instantsearch payload, and what parameters like typoTolerance and minProximity do.
- How to isolate the right request in the browser: Fetch/XHR filter, clearing the tab before reload, and the difference between copy as cURL and copy all as cURL.
- Why pagination is simple here: only the page attribute changes between requests.
- Two snapshots of the output, taken around the 2024 Michelin Guide update, were used for Martina's analysis of stars by country.

**In the full article:** The full Scrapy code for the call_api and get_data functions, the complete cURL request and payloads, the annotated screenshots of the network tab, and the link to the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/algolia-and-web-scraping-an-introduction?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
