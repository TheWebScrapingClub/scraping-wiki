---
type: article_summary
title: Analyzing the cost of a web scraping project
slug: analyzing-cost-web-scraping
canonical_url: https://www.scraping.club/p/analyzing-cost-web-scraping
publish_date: '2024-06-16'
visibility: free
topics:
- proxies
- browser-automation
- antibot
- proxy-industry
description: 'A breakdown of web scraping project costs into setup, maintenance and per-usage, with three scenarios and two ways to cut them: make vs buy and VMs vs proxies.'
source_hash: b1fa7a6cb2b606cc
---

# Analyzing the cost of a web scraping project

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-16 (free to read). **[Read the full article](https://www.scraping.club/p/analyzing-cost-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Estimating what a scraping project will cost is hard because some variables are ours, like extraction frequency and scope, and others are not. An anti-bot raises running costs. A website that changes its HTML often raises maintenance costs. Before estimating anything, you need to know which cost you are dealing with.

We split the costs into three types: setup, maintenance and per-usage. Setup covers studying the target and coding the scraper, plus the wider pipeline and the legal assessment. Maintenance can match or exceed setup when a site changes radically. Per-usage covers proxies, unblockers, compute and anti-detect browsers. We then run three scenarios on Gucci.com, Hermes.com and Zalando.com to show which type dominates in each. Last, we look at two ways to cut costs: make versus buy, including buying data from a marketplace like Databoutique.com, and using virtual machines through Scrapoxy instead of datacenter proxies.

## What's inside

- Why the legal assessment belongs in setup cost, and why we focus on a single scraper rather than the whole pipeline.
- Why browser automation like Playwright costs more to run than Scrapy, and when you can skip it.
- How the size of the target changes the make versus buy decision when an unblocker is billed per usage.
- Why a fixed number of VMs behind Scrapoxy gives you IPs with unlimited bandwidth, unlike datacenter proxies billed per GB.

**In the full article:** The datacenter proxy price per GB used in the Zalando example, the explanation of how Scrapoxy routes requests across VMs, and the links to the unblocker benchmark and The Lab #41.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/analyzing-cost-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
