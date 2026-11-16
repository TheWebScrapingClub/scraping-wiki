---
type: article_summary
title: Three web scraping tools just discovered on GitHub
slug: three-web-scraping-tools-just-discovered
canonical_url: https://www.scraping.club/p/three-web-scraping-tools-just-discovered
publish_date: '2023-10-08'
visibility: free
topics:
- http-clients
- cloudflare
description: 'Three GitHub finds for scraping: ASN to audit proxy IPs, curl_cffi for browser-like TLS fingerprints from Python, and fake-useragent for User Agent rotation.'
source_hash: e89f76fd74fce582
---

# Three web scraping tools just discovered on GitHub

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-10-08 (free to read). **[Read the full article](https://www.scraping.club/p/three-web-scraping-tools-just-discovered?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Once a month I browse GitHub at random, looking for repositories that could be useful for scraping work. This time three of them stood out, each aimed at a different weak point: knowing what a proxy IP really is, getting past TLS fingerprinting without a browser, and rotating User Agents without writing the logic yourself.

We look at ASN, an OSINT command line tool that bundles several IP lookups into one command. I used it on a well-known public DNS IP and on one taken from a free proxy list. Then curl_cffi, the Python binding for curl_impersonate, which I was skeptical about because it does no JavaScript handling. I tried it on a luxury retail site protected by Cloudflare, where plain curl gets blocked. Last is fake-useragent, an old technique in a better package than it looks. I also say where each tool fits and which problems I plan to try it on.

## What's inside

- What ASN reports for an IP: type (data center or not), reputation, geolocation, and where the IPQualityScore data comes from.
- How ASN helps when a spider is blocked on a different machine or when the proxy location differs from what the target sees.
- Why I expected curl_cffi to fail without JavaScript handling, and how plain curl compares with curl_impersonate at the handshake level.
- How fake-useragent filters by browser family and by each string's usage percentage.

**In the full article:** The ASN output screenshots for both IPs, the curl_cffi snippet with the target URL and the result on Cloudflare, and the two fake-useragent configuration examples.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/three-web-scraping-tools-just-discovered?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
