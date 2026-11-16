---
type: article_summary
title: 'THE LAB 33: Fingerprinting at different connection layers'
slug: the-lab-33-fingerprinting-at-different
canonical_url: https://www.scraping.club/p/the-lab-33-fingerprinting-at-different
publish_date: '2023-11-30'
visibility: premium
topics:
- cloudflare
- browser-fingerprinting
- antibot
- akamai
description: 'Fingerprinting happens at several layers: IP, TCP, TLS, HTTP headers and browser APIs. How we test each one on our scrapers and forge a coherent fingerprint.'
source_hash: aad45953cf927df8
---

# THE LAB 33: Fingerprinting at different connection layers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-30 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-33-fingerprinting-at-different?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Fingerprinting has been a recurring topic here because it can decide whether a scraping project works or fails. It does not happen in one place. A target can look at your IP address and its reputation, at the TCP packet fields that point to an operating system, at the TLS handshake, at the HTTP headers and at the Web APIs exposed by the browser.

We walk through these layers one by one: IP, TCP, TLS, HTTP and browser. For each, I show what the target can read and how we can test our own scraper, using IP lookup endpoints, nmap, the Incolumitas TCP classifier and the browserleaks TLS API. Then we look at forging a fingerprint layer by layer with Scrapy and Scrapy-impersonate, and why the headers must stay coherent with the browser we mimic. For TCP, I don't know of a package that spoofs it.

## What's inside

- Where IP reputation comes from: spam and botnet lists, government ranges and published datacenter lists, and why proxy providers compete on the quality of their pools.
- Which TCP/IP fields give away the operating system, such as initial TTL and window size, and how nmap OS detection uses them.
- How JA3 hashes the order of the TLS ciphers into a string that is compared against legitimate ones.
- Two ways to set headers in Scrapy, globally in the settings or on each request, and why the browser layer adds hundreds of built-in APIs to the picture.

**In the full article:** The nmap output, the Incolumitas classifier result from my MacBook, the Scrapy headers code and the Scrapy-impersonate spider that queries the browserleaks API.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-33-fingerprinting-at-different?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
