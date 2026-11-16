---
type: article_summary
title: Scraping Akamai-protected websites with Scrapy
slug: scraping-akamai-protected-websites
canonical_url: https://www.scraping.club/p/scraping-akamai-protected-websites
publish_date: '2024-05-19'
visibility: free
topics:
- akamai
- scraping-infra
- proxies
- browser-automation
description: Scraping Akamai Bot Manager sites such as Versace with a plain Scrapy spider, tested from a laptop and from AWS and Azure machines.
source_hash: 0e5636300a89460b
---

# Scraping Akamai-protected websites with Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-05-19 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-akamai-protected-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Akamai Bot Manager protects sites like Loewe, Versace, Zalando, NewBalance and Rakuten. In the Lab post on bearer tokens I got past it with a shortcut: I filled the cookie jar with Akamai cookies from my laptop browser. I meant to follow up with a how-to on getting that token automatically with Playwright before the Scrapy spider starts. Then our Versace scraper, untouched for years apart from XPath fixes, stopped working, and it took me a while to see why.

We rebuilt a simplified Versace spider that crawls product pages and scrapes only titles. I compare the old Scrapy settings with the updated ones, then run the spider on my laptop, on an AWS machine and on an Azure one, checking the IP with an ASN lookup. I also say what I make of the result for public data versus sensitive use cases.

## What's inside

- Why I reached for scrapy-impersonate and other workarounds first, and what that detour cost me
- What was wrong with the old scraper's User Agent and request headers, and why nobody on the team had looked at them
- How AWS, Azure and GCP differ for scraping in my experience, and my guess about the reason
- What the hardest Akamai sites I've met needed in practice, and why fraud protection may be a different story

**In the full article:** Settings.py files before and after with the full header set, the screenshots of each run, the ASN check on the cloud IP, and the list of Akamai sites where I repeated the test.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-akamai-protected-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
