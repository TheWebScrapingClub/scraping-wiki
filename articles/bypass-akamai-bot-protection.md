---
type: article_summary
title: 'THE LAB #85: Bypass Akamai Bot Protection by Chaining Proxies'
slug: bypass-akamai-bot-protection
canonical_url: https://www.scraping.club/p/bypass-akamai-bot-protection
publish_date: '2025-05-29'
visibility: premium
topics:
- akamai
- tls-fingerprinting
- proxies
- antibot
description: How to get past Akamai Bot Manager at the network level by chaining JA3Proxy for the TLS fingerprint with a rotating residential proxy, outside Scrapy.
source_hash: 3af34fceff916a86
---

# THE LAB #85: Bypass Akamai Bot Protection by Chaining Proxies

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-05-29 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypass-akamai-bot-protection?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

When a site turns on Akamai Bot Manager, my Scrapy scraper usually hangs and times out on the first request. Akamai checks several layers: TLS and JA3 fingerprint, HTTP/2 and header order, IP reputation, and behavioral scripts. The _abck and ak_bmsc cookies are the clearest sign it's there. Scrapy Impersonate is the common fix, but it locks you into Scrapy, makes proxy rotation awkward, lags behind new browser versions, and still isn't enough on the harder configurations.

We look at a setup that fixes the first two limits by chaining two proxies. JA3Proxy, built on uTLS, replays our traffic with a chosen browser TLS fingerprint, so any HTTP client can use it. A rotating residential proxy sits upstream and handles IP reputation. Before the setup, I explain what a TLS fingerprint is and how JA3 is built. I also say plainly what this approach does not cover: Akamai's JavaScript sensor and behavioral checks.

## What's inside

- How a JA3 string is composed from TLS version, ciphers, extensions, curves and curve formats, and why it gets hashed.
- Why changing the User-Agent is not enough and the TLS handshake itself has to change.
- What JA3Proxy leaves untouched: HTTP headers and browser behavior still have to be set by the client.
- Why Scrapy Impersonate struggles with HTTPS proxies and with retries on proxy failures.

**In the full article:** The JA3Proxy setup guide, the scripts in the private GitHub repository folder 85.AKAMAI-JA3PROXY, and the code example for chaining it with a residential proxy.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypass-akamai-bot-protection?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
