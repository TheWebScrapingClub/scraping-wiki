---
type: article_summary
title: Scraping Akamai protected websites
slug: scraping-akamai-protected-website
canonical_url: https://www.scraping.club/p/scraping-akamai-protected-website
publish_date: '2023-07-06'
visibility: premium
topics:
- akamai
- proxies
- antibot
- browser-automation
description: How to scrape Zalando's 1.3 million products despite Akamai Bot Manager, using a Scrapy spider, adjusted headers and Smartproxy datacenter proxies on AWS.
source_hash: 1f4515d8b5305e7c
---

# Scraping Akamai protected websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-07-06 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-akamai-protected-website?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Zalando is one of the main European fashion e-commerce sites, with 1.3 million items from 6300+ brands. It is listed on the Frankfurt Stock Exchange, so its assortment and discount levels work as an early signal for market research in apparel. That is why many people try to scrape it. It is not easy: the catalog is huge and the site sits behind Akamai Bot Manager.

I start with how Akamai scores traffic and how to spot it on a target, through Wappalyzer and the cookies it sets. Then we build a simple Scrapy spider with human-like headers, fed with more than 260 pre-scraped category URLs, and run it first locally and then on a server. The server run gets blocked after a few requests, and I explain what I think triggers it. My solution starts from the cheapest option, Smartproxy datacenter proxies plugged into Scrapy through the advanced-scrapy-proxies package, and I close on the cost side.

## What's inside

- How Bot Manager scores requests from 0 to 100 and why each website can react differently to the same scraper.
- Two quick checks for Akamai: the Wappalyzer extension and the _abck and ak_bmsc cookies.
- Why the same spider behaves differently on a home connection and on a cloud server, and why blocks appear only after a few calls.
- How the input is split into category URLs so executions can be spread across different machines.

**In the full article:** The full spider code, the Scrapy headers and proxy settings, the run command, the results of the AWS execution and the cost breakdown of the setup.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-akamai-protected-website?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
