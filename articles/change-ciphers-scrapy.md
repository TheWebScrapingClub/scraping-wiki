---
type: article_summary
title: 'THE LAB #6: Changing Ciphers in Scrapy to avoid bans by TLS Fingerprinting'
slug: change-ciphers-scrapy
canonical_url: https://www.scraping.club/p/change-ciphers-scrapy
publish_date: '2022-11-08'
visibility: premium
topics:
- tls-fingerprinting
- cloudflare
description: How TLS fingerprinting identifies scrapers from the cipher suites in the client Hello message, and how to change the ciphers Scrapy sends to avoid bans.
source_hash: 45a3cddc3ca2f6cf
---

# THE LAB #6: Changing Ciphers in Scrapy to avoid bans by TLS Fingerprinting

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-11-08 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/change-ciphers-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Advanced anti-bot solutions work on three levels: behavioral, browser and HTTP. A question on our Discord server led me to the HTTP level, where TLS fingerprinting lets a server profile your client before it requests a single page. The fingerprint is built from the Hello message, which carries the supported TLS version and the cipher suites. Chrome, Safari and Scrapy on the same machine each send a different list, so a default Scrapy connection is easy to spot and block.

We start from the TCP handshake and the Hello message, then compare the cipher lists sent by Chrome on a Mac, Safari and Scrapy. We also point to the JA3 and TS1 algorithms described in the LWT Hiker post. The goal is to change the ciphers Scrapy sends, so its connection stops standing out from a real browser.

## What's inside

- How the SYN, SYN/ACK and ACK exchange leads to the Hello message where the fingerprint data is sent.
- Why the "client random" and the TLS version matter less than the order and number of ciphers when comparing clients.
- The server uses the ciphers together with other parameters, so the cipher list alone does not tell the whole story.
- Where JA3 and TS1 come from and why LWT Hiker is the reference for going deeper.

**In the full article:** The Scrapy code and settings used to change the ciphers, the countermeasures section, and the full cipher lists for Chrome, Safari and Scrapy side by side.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/change-ciphers-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
