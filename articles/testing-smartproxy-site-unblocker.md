---
type: article_summary
title: 'Hands On #4: Testing the new Smartproxy Site Unblocker'
slug: testing-smartproxy-site-unblocker
canonical_url: https://www.scraping.club/p/testing-smartproxy-site-unblocker
publish_date: '2023-07-13'
visibility: free
topics:
- cloudflare
- datadome
- antibot
description: A hands-on test of Smartproxy's Site Unblocker API against Datadome, Cloudflare, Kasada, F5 and PerimeterX, using a plain Scrapy spider on 50 URLs.
source_hash: 4dafb4d6d39cb4ba
---

# Hands On #4: Testing the new Smartproxy Site Unblocker

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-07-13 (free to read). **[Read the full article](https://www.scraping.club/p/testing-smartproxy-site-unblocker?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Smartproxy has added Site Unblocker to its services, a "super API" that promises proxy rotation, geo-targeting, JavaScript rendering, fingerprint and session management behind a single call. Like the other unblocker APIs we've looked at, it claims to make our life easier. The practical question is whether it actually gets past the anti-bots we meet in production.

We ran the same benchmark we use for the other unblocker APIs. A plain Scrapy spider requests 10 pages from each of 5 websites, one per anti-bot: Datadome, Cloudflare, Kasada, F5 and PerimeterX. It records the status code and a page string to confirm the real page loaded. We ran it three ways: with no unblocker as a baseline, with Site Unblocker returning raw HTML, and with JavaScript rendering enabled. Each run was scored from 0 to 100 on a local machine and on a server. I also cover the Scrapy integration, pricing, pros and cons, and a final rating.

## What's inside

- The baseline spider without the unblocker is scored 0, so every later result is measured against a scraper that retrieves nothing.
- Each run is checked with an XPath-extracted field from the product page, so a 200 status code on a challenge page does not count as a success.
- Switching on JavaScript rendering takes a change to the request parameters, and we compare it with the raw HTML run.
- Sticky sessions, geotargeting and custom cookies are available by tweaking headers, and the pricing model has a drawback for occasional users.

**In the full article:** The per-anti-bot results of the three runs, the Scrapy spider setup and its GitHub repository, the request parameters, the pricing figures and the final score with the full list of pros and cons.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/testing-smartproxy-site-unblocker?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
