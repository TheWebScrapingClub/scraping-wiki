---
type: article_summary
title: Anti-bot technology and bypass articles
slug: post-archive-anti-bot-techniques
canonical_url: https://www.scraping.club/p/post-archive-anti-bot-techniques
publish_date: '2023-02-20'
visibility: free
topics:
- cloudflare
- proxy-industry
- antibot
- datadome
description: 'An index of Web Scraping Club posts on anti-bot systems: Cloudflare, Kasada, PerimeterX and Datadome, plus TLS fingerprinting and human-like mouse movements.'
source_hash: 4f6ddf0e3f257904
---

# Anti-bot technology and bypass articles

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-20 (free to read). **[Read the full article](https://www.scraping.club/p/post-archive-anti-bot-techniques?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

If you scrape at any real scale, anti-bot systems are the main obstacle. Cloudflare, Kasada, PerimeterX and Datadome each block in a different way, and a technique that worked last year often stops working. Search "Cloudflare bypass" and you find hundreds of articles and repositories, some of them selling a solution. What you need is a way to tell what works on real targets.

This page collects what I have written on the topic, mostly in THE LAB series, where we cover real-world use cases with code and an explanation of the methodology. The posts go through scraping Cloudflare-protected sites, including an early 2023 update, plus Kasada, PerimeterX, and Datadome combined with xsrf tokens. Other posts cover changing ciphers in Scrapy to avoid bans by TLS fingerprinting, bypassing Cloudflare with GoLogin and Playwright, human-like mouse movements with Bezier curves, and an anti-detect anti-bot matrix. One post starts from a plain Error 429 on an e-commerce site.

## What's inside

- Coverage is split by vendor: Cloudflare has several posts from 2022 to early 2023, while Kasada, PerimeterX and Datadome each have their own.
- Two posts deal with detection signals rather than a single vendor: TLS fingerprinting handled by changing ciphers in Scrapy, and mouse movement simulated with Bezier curves.
- The Datadome post combines the anti-bot with xsrf tokens, and the Kasada post starts from a 429 error seen in the browser's network tab.
- The anti-detect anti-bot matrix and the GoLogin post look at browser tooling against these protections.

**In the full article:** Code, methodology and test results for each target are only in the individual posts, along with the tool comparisons and the Cloudflare setup that was current in early 2023.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/post-archive-anti-bot-techniques?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
