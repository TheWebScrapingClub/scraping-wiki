---
type: article_summary
title: 'THE LAB #99: HTTP Caching for Web Scraping'
slug: http-caching-scraping
canonical_url: https://www.scraping.club/p/http-caching-scraping
publish_date: '2026-03-05'
visibility: premium
topics:
- http-clients
- tls-fingerprinting
- proxy-industry
- proxies
description: HTTP conditional requests (ETag, If-None-Match, 304) can cut proxy bandwidth on recurring scrapes. We tested them on Shopify stores with curl_cffi.
source_hash: 66bcf7dfa35e16ff
---

# THE LAB #99: HTTP Caching for Web Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-03-05 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/http-caching-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In recurring scraping, a lot of the proxy bill goes on pages that have not changed since the last run. Take price monitoring across 50,000 product pages every hour: most of them show the same price as an hour ago, and we pay for identical bytes again and again. Anti-bot defenses have made each successful request more expensive, so the waste hurts more than it used to.

Solutions like changedetection.io or SimHash fingerprints exist, but you have to build and maintain the change detection yourself. HTTP already has a native mechanism: conditional requests, where the server answers 304 with an empty body. We explain how ETag and Last-Modified work, then write an audit function with curl_cffi that checks whether a target supports 304. We ran it on Shopify stores, testing product HTML pages, product JSON and catalog JSON endpoints, and measured the bandwidth saved. We also look at whether the same approach works with Scrapy.

## What's inside

- How the ETag and Last-Modified headers map to If-None-Match and If-Modified-Since, and what the server does with them.
- Why curl_cffi and TLS fingerprinting were needed, since some e-commerce targets would return 403 before caching could be tested.
- Why we focused on Shopify, and which three endpoint types we checked: product HTML, product JSON and catalog JSON.
- How the technique compares with changedetection.io and SimHash fingerprinting, which both need client-side change detection logic.

**In the full article:** The full audit code in the paying-users GitHub repo, the per-store measurements and the Scrapy integration are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/http-caching-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
