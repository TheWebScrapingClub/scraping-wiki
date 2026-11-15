---
type: article_summary
title: 'THE LAB #3: Scraping Cloudflare protected websites'
slug: cloudflare-how-to-scrape
canonical_url: https://www.scraping.club/p/cloudflare-how-to-scrape
publish_date: '2022-09-27'
visibility: premium
topics:
- cloudflare
- antibot
- tls-fingerprinting
- human-behavior-emulation
description: 'Scraping Cloudflare-protected sites: how its anti-bot checks work and three different solutions for brownsfashion.com, antonioli.eu and ssense.com.'
source_hash: 7afdbf46b72b799d
---

# THE LAB #3: Scraping Cloudflare protected websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-09-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/cloudflare-how-to-scrape?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare is one of the toughest anti-bot protections to bypass in a scraping project. Anyone with some experience has met its challenge screen at least once. It checks the connection passively and the browser actively. It also queries the browser for automation tools and watches what happens on the page, so a bot has many ways to give itself away.

There is no silver bullet, so I did not look for a single recipe. We took three targets, brownsfashion.com, antonioli.eu and ssense.com, and built three similar but not identical solutions, with the methodology behind each. As always, we scraped only public product price data, without logging in, at a speed that does not harm the business of the target website.

## What's inside

- The passive layer (TCP, TLS and HTTP fingerprinting) and the active layer (Canvas fingerprinting and CAPTCHAs), and what each means for a scraper
- Cloudflare is also a DDoS mitigation, distributed DNS and CDN provider, and anti-bot protection is only one of its services
- The on-page monitoring, mouse movements included, that can make a bot detectable even after it passes the first checks
- Why one setup does not fit all three sites, and where the three solutions differ

**In the full article:** The code for the three scrapers, the methodology applied to each site, and the results on brownsfashion.com, antonioli.eu and ssense.com.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/cloudflare-how-to-scrape?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
