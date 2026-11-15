---
type: article_summary
title: 'The Lab #53: Bypassing AWS WAF'
slug: bypassing-aws-waf-scraping
canonical_url: https://www.scraping.club/p/bypassing-aws-waf-scraping
publish_date: '2024-06-06'
visibility: premium
topics:
- scraping-infra
- browser-automation
- http-clients
- antibot
description: AWS WAF challenges and the aws-waf-token cookie, tested on Traveloka's flight search API with plain Scrapy and with Scrapy plus Playwright.
source_hash: d49edcd0e4b4c0c9
---

# The Lab #53: Bypassing AWS WAF

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-06 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-aws-waf-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A community member asked how to get past AWS WAF to scrape an API endpoint. Wappalyzer does not flag it, but the aws-waf-token session cookie gives it away. A challenge runs in the background at the start of the session to validate your browser, and its payload is opaque. Reverse engineering it is slow and needs constant updates, so I prefer mimicking a human on a legit hardware and software stack, which survives anti-bot releases longer.

Our target is Traveloka, a flights and hotels aggregator for the APAC market. We looked at the flight search request in curl, worked out which cookies the endpoint needs, and then built two scrapers: plain Scrapy with a realistic set of headers, and Scrapy combined with Playwright through the scrapy-playwright library, where a headful browser collects the cookies and Scrapy handles the parallel requests.

## What's inside

- What a WAF does and how AWS WAF checks your browser once, then lets you keep browsing until the cookie expires.
- Which of the seven cookies on the Traveloka request can be set to fixed values and which are assigned to the browser session.
- Why the HTML of the offers page is useless for fares, since they come from the API response.
- How long the aws-waf-token stays valid on Traveloka, and what that means for how often you need a browser session.

**In the full article:** Full code for both scrapers in the 53.AWS_WAF folder of the Lab repository, the Scrapy run results, and the cookie hand-off from Playwright to Scrapy.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-aws-waf-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
