---
type: article_summary
title: 'The Great Web Unblocker Benchmark: Kasada edition'
slug: web-unblocker-test-kasada
canonical_url: https://www.scraping.club/p/web-unblocker-test-kasada
publish_date: '2024-06-18'
visibility: free
topics:
- cloudflare
- browser-automation
description: Benchmark of seven web unblockers against Kasada on canadagoose.com, measuring success rate, scraping time and cost with the same Scrapy spider.
source_hash: 0cb73984656eed93
---

# The Great Web Unblocker Benchmark: Kasada edition

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-18 (free to read). **[Read the full article](https://www.scraping.club/p/web-unblocker-test-kasada?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada is one of the hardest anti-bots to bypass, and it is not on the radar of most unblocker vendors the way Cloudflare is. If you scrape a Kasada-protected site, you need to know whether delegating the bypass to a web unblocker works and what it costs in time and money compared with building your own scraper and browser automation.

This is the second episode of the Great Web Unblocker Benchmark. We pointed one simple Scrapy spider at canadagoose.com: the homepage and 100 product URLs. We ran seven unblockers: Bright Data, Infatica, NetNut, Oxylabs, Smartproxy, ZenRows and Zyte API. Each got a score out of 100, with the elapsed time measured by Scrapy and the cost of the successful pages. A 200 status was not enough. The page also had to parse, because Kasada can return an empty HTML. Vendors did not see the results in advance.

## What's inside

- Pricing models differ: pay-per-GB, pay-per-request, credits and dynamic pricing. They change what a run costs on pure HTML pages.
- Two unblockers failed, each in a different way: one stopped at the homepage with the typical Kasada error, the other returned 200 on every page without usable HTML.
- Among the unblockers that passed, scores were close, so execution time and cost separated them.
- NetNut's unblocker is a recent product and its price is undisclosed, so we could not compare its cost with the others.

**In the full article:** The per-vendor results with success scores, execution times and costs, the recap table, and the final ranking by score, speed and price.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-unblocker-test-kasada?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
