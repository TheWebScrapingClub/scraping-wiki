---
type: article_summary
title: The Great Web Unblocker Benchmark - Cloudflare Edition
slug: cloudflare-web-unblocker-benchmark
canonical_url: https://www.scraping.club/p/cloudflare-web-unblocker-benchmark
publish_date: '2024-09-22'
visibility: free
topics:
- cloudflare
- antibot
- browser-automation
- proxies
description: Six web unblockers tested against Cloudflare on indeed.com with one Scrapy spider, compared on first-try success rate, speed and cost.
source_hash: 30ef990546555640
---

# The Great Web Unblocker Benchmark - Cloudflare Edition

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-09-22 (free to read). **[Read the full article](https://www.scraping.club/p/cloudflare-web-unblocker-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare is the most widespread anti-bot protection, so I expected every web unblocker to get past it. When you delegate the bypass to a third party instead of building a browser-based scraper, what counts is how often a request works on the first try, how long it takes and what the extraction costs. Pricing differs too: per GB, per request, credits, dynamic.

This is the Cloudflare episode of the Great Web Unblocker Benchmark. We pointed the same browserless Scrapy spider at indeed.com: it reads the homepage, then collects job URLs from the first 7 pages of the remote Python Developer search, around 100 URLs. We tested Bright Data, Infatica, Oxylabs, Smartproxy, ZenRows and Zyte API. A request counted only if the scraper parsed it, since Cloudflare can return an empty rendered page with a 200. Each unblocker got scores for success, speed and cost.

## What's inside

- The success score is 0 if an unblocker can't scrape the homepage or a single URL, otherwise it is the share of requests that worked on the first try.
- Speed is URLs parsed, retries included, divided by the seconds of the whole run, with 10 parallel threads each requesting 1 URL per second.
- Pricing details matter here: Bright Data charges more for domains on its premium list, Smartproxy lets you pick the payment metric, and ZenRows consumes more credits when JS rendering is needed.
- Vendors did not see results in advance, so I may have missed an option that solves the anti-bot, and I'll update the results if I did.

**In the full article:** Per-unblocker figures for items, requests, retries, seconds per request and cost, the recap table and the final ranking with my comments.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/cloudflare-web-unblocker-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
