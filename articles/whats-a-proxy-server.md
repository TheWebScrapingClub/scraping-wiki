---
type: article_summary
title: What's a proxy server?
slug: whats-a-proxy-server
canonical_url: https://www.scraping.club/p/whats-a-proxy-server
publish_date: '2022-09-23'
visibility: free
topics:
- proxies
- residential-proxies
- scraping-infra
description: 'A primer on proxy servers for web scraping: why you need them, how they differ by anonymity, location and rotation, and where data center IPs get caught.'
source_hash: 079d5accb1a4b90a
---

# What's a proxy server?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-09-23 (free to read). **[Read the full article](https://www.scraping.club/p/whats-a-proxy-server?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Sooner or later a scraper needs a proxy. Websites geo-fence content by IP, cap requests per IP, run fingerprinting anti-bot software, or block the IP ranges of cloud providers outright. Each of these calls for a different kind of proxy, and picking the wrong one means blocks you can't explain.

We start from the definition of a proxy server and map four common scraping scenarios to the proxy that fits each. Then we go through the three features vendors and free lists use to sort proxies: anonymity level, location, and static versus rotating. To show how visible a data center IP is, I set up a Highly Anonymous Proxy on an EC2 instance and checked it against incolumitas.com, an IP API lookup and a TCP/IP fingerprint test, comparing it with my Mac browsing without a proxy. We close with free proxy lists and the main paid providers.

## What's inside

- The three anonymity levels (transparent, anonymous, elite) and which headers each one adds or leaves untouched
- Why residential and mobile proxies cost more than data center ones
- How a rotating proxy lets you configure a single endpoint while requests are routed to a pool in the background
- Why TCP handshake values can reveal the operating system and flag a request as coming from a server

**In the full article:** Screenshots of the IP API and TCP/IP fingerprint results for the EC2 proxy and for my Mac, the list of providers with links, and the free proxy list I point to.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/whats-a-proxy-server?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
