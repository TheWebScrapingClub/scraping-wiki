---
type: article_summary
title: 'THE LAB #1: Scraping data from an app'
slug: the-lab-1-scraping-data-from-an-app
canonical_url: https://www.scraping.club/p/the-lab-1-scraping-data-from-an-app
publish_date: '2022-09-04'
visibility: premium
topics:
- industry-overview
description: 'How to scrape product data from a mobile app with no web interface: intercept its API calls with Fiddler Everywhere, then replicate them in a Scrapy spider.'
source_hash: 8a4c79b410b4b4eb
---

# THE LAB #1: Scraping data from an app

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-09-04 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-1-scraping-data-from-an-app?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most of what I write about is extracting data from websites. Sometimes the target is an app with no web interface, or the website is too complex to scrape and the app may be another door to the same data. We cannot read the app's source code, so the only option is to intercept the requests it sends to its servers and replicate them in our scraper.

In this first post of THE LAB we used Fiddler Everywhere as a man-in-the-middle between a phone and the app's servers. We set up HTTPS decryption and routed the phone's traffic through our computer as a proxy. The target was the Off White app, even though the brand has a website. We opened the app, browsed a catalog section, found the API call that returns product data, and rebuilt it in a Scrapy project with the headers we read in Fiddler. Then we mapped the JSON structure to Item fields.

## What's inside

- Why Fiddler can also reveal hidden calls to external services an app makes after installation, not only the data endpoints.
- Closing background apps on the phone before the test to cut noise in the captured requests.
- Which headers we removed from the replicated request and why: Accept, Accept-Encoding and Cookie.
- The Bearer token copied from Fiddler expires after a few hours, so getting it dynamically is left as a next step.

**In the full article:** The Fiddler screenshots of the captured requests, the Scrapy spider, settings and Item class code, the header list, and the JSON output we parsed and checked against the scraped items.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-1-scraping-data-from-an-app?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
