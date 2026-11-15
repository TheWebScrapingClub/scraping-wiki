---
type: article_summary
title: Using internal APIs call for web scraping more efficiently
slug: apis-in-web-scraping
canonical_url: https://www.scraping.club/p/apis-in-web-scraping
publish_date: '2025-09-28'
visibility: free
topics:
- http-clients
- api-scraping
- tls-fingerprinting
- proxies
description: How to scrape a site through the internal API calls its pages already make, when it works, when it doesn't, and a Yahoo Finance example with hrequests.
source_hash: 8d1b19f5268a2824
---

# Using internal APIs call for web scraping more efficiently

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-09-28 (free to read). **[Read the full article](https://www.scraping.club/p/apis-in-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most of the data on a page reaches the browser through API calls. Parsing HTML means chasing layout changes and anti-bot measures, while the endpoints behind the page return structured data and skip the rendering. Calling them directly is what I mean by API scraping.

We cover how to spot these endpoints in the Network tab, and which page behaviors usually point to them: pagination, filters, infinite scroll, single-page apps. We also look at where the approach breaks, with Trustpilot as a working case and Booking.com as one where the data is encrypted. A plain HTTP client is often not enough because of TLS fingerprinting, so we list clients that spoof it. Then we apply the method to historical NVDA data on Yahoo Finance using hrequests in Python, and close with pros and cons against traditional scraping.

## What's inside

- Which user interactions on a page tend to reveal a public endpoint: Load More buttons, in-page filters, pagination, SPAs.
- Why we stay away from authenticated API calls, both for legal reasons and because the requests tie your activity to your account.
- Why Node.js is left out of the TLS fingerprinting client list, and the workarounds available.
- The cons we have seen: partial data that calls for a hybrid approach, and endpoints that change more often than the DOM.

**In the full article:** The full hrequests script for the Yahoo Finance endpoint, the code that turns the JSON response into records, the table of TLS-spoofing HTTP clients and the side-by-side comparison table with traditional scraping.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/apis-in-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
