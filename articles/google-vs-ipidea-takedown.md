---
type: article_summary
title: 'Google vs IPIDEA: Anatomy of a Residential Proxy Takedown'
slug: google-vs-ipidea-takedown
canonical_url: https://www.scraping.club/p/google-vs-ipidea-takedown
publish_date: '2026-02-08'
visibility: free
topics:
- residential-proxies
- proxies
- proxy-industry
- cloudflare
description: Google's January 2026 takedown of IPIDEA, and what it shows about how residential proxy networks recruit devices, run their infrastructure and survive disruptio
source_hash: 585b4954c5795989
---

# Google vs IPIDEA: Anatomy of a Residential Proxy Takedown

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-02-08 (free to read). **[Read the full article](https://www.scraping.club/p/google-vs-ipidea-takedown?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Residential proxy networks need millions of consumer devices, and nobody gets that many people to share their connection knowingly without shortcuts. IPIDEA is the case that shows those shortcuts in detail. On January 28, 2026, Google Threat Intelligence Group announced the disruption of what it called one of the largest residential proxy networks in the world. Most people outside our industry had never heard of it, yet scrapers and threat actors use the same kind of infrastructure.

We use the takedown to look under the hood. We cover what Google did, how IPIDEA's SDKs, VPN apps and pre-infected devices enrolled IPs, and how its two-tier command-and-control system worked. We also look at the brands that hid a single network, why defenders cannot simply block residential exit nodes, and why the takedown is unlikely to end the network. We close with the economics of selling proxy bandwidth and what this means for those of us who buy it.

## What's inside

- How one SDK on a phone produces two products, residential on WiFi and mobile on 5G, and why mobile is priced higher.
- Why IPIDEA's 13 brands are storefronts for one pool, and how that compares with the handful of truly independent residential networks in the market.
- Antoine Vastel's verified IP counts per brand, and why he advises using them for risk scoring instead of direct blocking.
- Why infected devices stay infected after the C2 domains are seized, and what that means for a possible rebuild or rebrand.

**In the full article:** The list of the 13 brands, the SDK and VPN app names, the Tier One and Tier Two architecture, Vastel's per-brand IP counts and the cost and margin figures for proxy providers.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/google-vs-ipidea-takedown?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
