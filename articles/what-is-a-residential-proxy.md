---
type: article_summary
title: What is a residential proxy?
slug: what-is-a-residential-proxy
canonical_url: https://www.scraping.club/p/what-is-a-residential-proxy
publish_date: '2024-03-13'
visibility: free
topics:
- proxies
- residential-proxies
- antibot
- datadome
description: What residential proxies are, how static and rotating ones work, how they compare with datacenter, ISP and mobile proxies, and how sites detect them.
source_hash: 44e6cfa39338d489
---

# What is a residential proxy?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-13 (free to read). **[Read the full article](https://www.scraping.club/p/what-is-a-residential-proxy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Residential proxies send your requests through IP addresses that ISPs assign to real households, so traffic looks like it comes from an ordinary home connection. For scraping, that is the difference between getting blocked on a datacenter range and getting through. The catch is that residential IPs cost more, can be slower, and are not invisible.

I cover how residential networks work, including peer-to-peer pools such as Packetstream and ProxyRack, and the split between static and rotating proxies. Then I compare them with datacenter, ISP and mobile proxies on anonymity, speed, reliability and cost. The last part looks at the other side: how websites and security vendors spot proxy traffic. That means ASN checks, IP databases like IP2Proxy and IPQualityScore, IP reputation, behavioral and fingerprint analysis, reverse DNS, and machine learning models that combine all these signals.

## What's inside

- Why ISP proxies sit between datacenter and residential, and the subnet risk that comes with them
- Why mobile proxies are the hardest to detect, with carrier-grade NAT as the reason, and where they fall short
- How a timezone mismatch between the proxy IP and the browser gives you away
- Why a residential IP does not protect you if your request pattern looks suspicious

**In the full article:** The detailed comparison of each proxy type on anonymity, speed, reliability and cost, the full list of detection methods with the tools behind them, and the partner proxy deals.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/what-is-a-residential-proxy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
