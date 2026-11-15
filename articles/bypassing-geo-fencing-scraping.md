---
type: article_summary
title: Bypassing Geo-fencing While Scraping
slug: bypassing-geo-fencing-scraping
canonical_url: https://www.scraping.club/p/bypassing-geo-fencing-scraping
publish_date: '2024-03-22'
visibility: premium
topics:
- proxies
- browser-automation
- scraping-infra
description: 'How websites use IP and browser geolocation to geo-fence content, and the ways to get around it while scraping: residential proxies, Scrapoxy, and Playwright.'
source_hash: 1acb17d41463d814
---

# Bypassing Geo-fencing While Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-22 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-geo-fencing-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Geo-fencing decides what a user can see from their location, which is estimated from the IP address and the browser's APIs. For a scraper this means region-specific prices, different catalogs, or a login wall where other countries get open access. If your target does this, you get partial or wrong data unless you control where you appear to be.

We start with what a site can read from an IP, using IPinfo on an AWS address, and with the EU Geo-blocking Regulation and what it does not cover. Then we go through the ways around geo-fencing, from the most expensive to the free ones. We compare a Smartproxy residential proxy in the US, tested on italist.com, with Scrapoxy running datacenter IPs on your own cloud accounts, and with setting the browser location in Playwright, as we did on Lowe's. Past the paywall there is a real-world case, plus a warning on proxies used in a browser that is not patched correctly.

## What's inside

- What an IP lookup returns beyond the city: ASN, company, carrier and privacy flags such as hosting, VPN and proxy.
- Where the EU Geo-blocking Regulation 2018/302 stops, for example copyright-protected content like streaming.
- Why Scrapoxy is cost-effective on large sites, and the condition that the target must not block datacenter proxies.
- The WebRTC leak that appears when a proxy is used on a browser that is not correctly patched.

**In the full article:** The Scrapy settings for Scrapoxy, the Playwright geolocation code for the Lowe's example, the paid-section case where we circumvent a site's geo-fencing, and the WebRTC leak test.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-geo-fencing-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
