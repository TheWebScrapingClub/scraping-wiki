---
type: article_summary
title: 'THE LAB #93: scraping Booking.com using internal APIs'
slug: scraping-booking-using-apiss
canonical_url: https://www.scraping.club/p/scraping-booking-using-apiss
publish_date: '2025-09-19'
visibility: premium
topics:
- browser-automation
- http-clients
- proxies
- antibot
description: How to scrape Booking.com hotel data through its private GraphQL API with an HTTP client instead of Playwright, including the CSRF token step.
source_hash: 970c15ba4d58c166
---

# THE LAB #93: scraping Booking.com using internal APIs

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-09-19 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-booking-using-apiss?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Our previous Booking.com scraper used Playwright and parsed HTML elements. It works, but at scale you pay for it in CPU and memory, and scaling the operations gets painful. Booking's own internal calls return structured JSON, so there are no selectors to maintain and no browser to run.

We reverse-engineered Booking's private GraphQL API. We located the requests in the browser's Network panel while using the map view, looked at the payload and its operation names, and handled the CSRF token the endpoint requires. Then we rebuilt the call in Python with httpx over HTTP/2 and read the hotel fields straight from the JSON response. To cover a larger area, we point back to our evergreen grid technique, the same one we used for Zillow.

## What's inside

- Why the internal API beats HTML scraping: speed, lighter resource use, and data such as detailed pricing, availability and map coordinates.
- Which GraphQL operations to look for in the Network panel, and which parts of the payload you change (dates, bounding box, guests).
- Why the token expires, which errors signal it, and how to refresh it during a long session.
- The caveat that these endpoints are private and undocumented, so you do the homework yourself and still need proxies and rate limits.

**In the full article:** Python code for the token retrieval, the GraphQL request and the JSON parsing, the section on pagination and result limits, and the Scrapy and Camoufox scrapers in the paywalled GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-booking-using-apiss?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
