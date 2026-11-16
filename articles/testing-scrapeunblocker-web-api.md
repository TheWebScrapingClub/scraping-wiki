---
type: article_summary
title: Testing ScrapeUnblocker on Google and Shopee
slug: testing-scrapeunblocker-web-api
canonical_url: https://www.scraping.club/p/testing-scrapeunblocker-web-api
publish_date: '2026-10-27'
visibility: free
topics:
- http-clients
- antibot
- cloudflare
- akamai
description: A hands-on test of the ScrapeUnblocker anti-bot API on Google SERP, the Shopee and Shein plugins, with a look at data quality, pricing and Oxylabs Web API.
source_hash: 8ce27b2ebf3bd2fa
---

# Testing ScrapeUnblocker on Google and Shopee

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-10-27 (free to read). **[Read the full article](https://www.scraping.club/p/testing-scrapeunblocker-web-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Google keeps getting harder to scrape and now hides destination URLs. Shopee has custom bot protection, login requirements and strict geo controls. Shein is so costly to extract that it sometimes isn't economically viable. When ScrapeUnblocker asked me to test their API, these were the targets I wanted to see it on.

ScrapeUnblocker is a black box: you send a URL and it picks the route. We tested it as a customer would, with a plain requests client, one attempt per call and no retries, ten calls per target from Italy. We ran /serpApi on ten keywords across several countries, the Shopee plugin on search and product endpoints, and the Shein plugin plus the generic /getPageSource with parsed_data. We checked the returned data, not just the status codes. We also costed the run and compared the product with the Oxylabs Web API.

## What's inside

- How the billing works: one request is one credit, with no multiplier for JavaScript, and which failures are free and which are billed.
- What the /serpApi response contains beyond organic results: AI Overview, ads fields, and whether the result URLs are the real destinations.
- Where the Shopee and Shein data needs checking before it goes into a pipeline: price labels, filters that don't hold, missing fields and prices that differ between calls.
- How the catalog of dedicated scrapers overlaps with Oxylabs, and the trade-off between control over the route and predictable cost.

**In the full article:** The test client code, the per-target latency and success figures, the JSON examples for Google, Shopee and Shein, the price discrepancies found on Shein, the monthly cost estimates and the side-by-side table with Oxylabs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/testing-scrapeunblocker-web-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
