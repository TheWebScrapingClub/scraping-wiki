---
type: article_summary
title: Bypassing Akamai in H&M website using Proxidize
slug: bypassing-akamai-proxidize
canonical_url: https://www.scraping.club/p/bypassing-akamai-proxidize
publish_date: '2023-08-03'
visibility: free
topics:
- proxies
- akamai
- residential-proxies
- proxy-industry
description: Scraping H&M product detail pages behind Akamai with a Scrapy spider on four Proxidize mobile dongles, plus a cost comparison with datacenter, residential and m
source_hash: 2a26e4acb5966a6a
---

# Bypassing Akamai in H&M website using Proxidize

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-03 (free to read). **[Read the full article](https://www.scraping.club/p/bypassing-akamai-proxidize?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Our earlier Akamai test on Zalando worked with datacenter proxies because we scraped product list pages. That kept requests low and the proxy bill under five dollars per run. Product detail pages are a different case. H&M has more than 20k items, listed under several categories, so a full run goes past 100k requests and uses about ten GB. Akamai bans IPs temporarily after a few requests, so the proxy setup matters as much as the spider.

We tested Proxidize, a hardware and software system for running your own fleet of mobile proxies. I installed it in my office with four working dongles, since one SIM would not work. The harder part was making Scrapy cope with a tiny pool whose IPs rotate often. We used a Scrapy spider with the advanced-scrapy-proxies package and tuned rotation on the Proxidize side. Then we compared the cost per GB and the one-year total cost of ownership against other proxy types.

## What's inside

- How Proxidize is built: a mini PC server, a USB rack and modems, and the path a request takes from your scraper to the target and back.
- Practical setup issues: buying SIMs yourself, mixing carriers, and the onboarding call to open the router ports.
- Why the Proxidize proxy pool address does not work as a load balancer with so few modems, and what a retry does to the request meta.
- Limits of the solution: all IPs sit in one country, the hardware needs stable power and network, and the Proxidize server is a single point of failure.

**In the full article:** The Scrapy settings and spider code, the Proxidize rotation configuration, the proxy list setup on S3, the pricing tables and the one-year cost scenarios by GB volume.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-akamai-proxidize?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
