---
type: article_summary
title: 'THE LAB #61: Evaluating your proxy provider'
slug: evaluating-proxy-providers-ips
canonical_url: https://www.scraping.club/p/evaluating-proxy-providers-ips
publish_date: '2024-09-12'
visibility: premium
topics:
- proxy-industry
- proxies
- antibot
description: 'How to evaluate a proxy provider beyond price: billing models by use case, plus a test of IP rotation and geolocation on three providers'' residential proxies.'
source_hash: ba7c57867364d070
---

# THE LAB #61: Evaluating your proxy provider

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-09-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/evaluating-proxy-providers-ips?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Proxies can become the first cost item for a web data company once you move from rotating datacenter IPs to unblockers or mobile ones. So price drives the choice, but it is not the only factor, and the cheapest plan depends on your case. API endpoints, raw HTML, sites with or without bot protection: each points to a different billing model and a different proxy type.

We look at when pay-per-GB or pay-per-request makes more sense, and when an unblocker is overkill. Then we check what price does not tell you. We ran 50 requests on rotating residential proxies in the USA and 50 in France for three providers: a top name, a less established brand and a low-cost player. We collected the exit IPs with the Ipify API and analyzed them with the ASN command line tool, looking at IP variety and geolocation. I also share the Proxy Provider Pricebook, the spreadsheet we use in consultancy work.

## What's inside

- Why pay-per-GB tends to fit API endpoints and pay-per-request tends to fit HTML downloads.
- Why an unblocker is overkill on sites with no protection, and why ISP or datacenter IPs rarely bypass bot protection.
- The checks beyond price: pool size against your request volume, proxy type coherence, and whether IPs are located where you asked.
- Why the test uses two countries of different sizes, the USA and France, and what we looked at in each IP: variety, location, reputation and type.

**In the full article:** The scripts for IP collection and the ASN commands, the geolocation reports for each provider, the per-provider rotation numbers and the remaining tests are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/evaluating-proxy-providers-ips?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
