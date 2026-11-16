---
type: article_summary
title: Understanding the Role of the X-Forwarded-For Header in Proxies
slug: x-forwarded-for-header-proxies
canonical_url: https://www.scraping.club/p/x-forwarded-for-header-proxies
publish_date: '2025-09-14'
visibility: free
topics:
- proxies
- human-behavior-emulation
- akamai
- tls-fingerprinting
description: What the X-Forwarded-For header is, who sets it, and how to check whether your scraping proxy leaks your real IP to the target server.
source_hash: 8250867aeed35e4c
---

# Understanding the Role of the X-Forwarded-For Header in Proxies

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-09-14 (free to read). **[Read the full article](https://www.scraping.club/p/x-forwarded-for-header-proxies?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Your proxy server may be adding an X-Forwarded-For header to every request. That header carries the original client IP, and sometimes the chain of proxies in between. If your real IP ends up in it, the target can rate limit you, track you and apply geo-restrictions, and the proxy has done nothing for your anonymity.

I explain how the header works, with a walkthrough of a request passing through a transparent proxy and a load balancer. I also cover the standard Forwarded header and which kinds of proxies tend to set these headers. Then we test it in practice. A short Python script sends a request through a proxy to the HttpBin /anything endpoint, and we compare what comes back from a transparent proxy and from an elite one. The aim is a quick check you can run on any proxy before trusting it with a scraper.

## What's inside

- How X-Forwarded-For is built hop by hop, with a worked example of a client, a transparent proxy and a load balancer
- Why X-Forwarded-For is non-standard but more widely used than the standard Forwarded header, and why the same logic applies to both
- Which proxies usually set the header: test proxies, free public proxies and corporate proxies that log client IPs
- What to read in the HttpBin response: the origin field, the X-Forwarded-For header and other giveaways such as Via

**In the full article:** The Python script for the proxy anonymity test, the HttpBin response screenshots for the transparent and elite proxies, and the comparison tables of the two headers and of the proxy types.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/x-forwarded-for-header-proxies?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
