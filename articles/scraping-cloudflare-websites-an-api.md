---
type: article_summary
title: Scraping Cloudflare websites using an API
slug: scraping-cloudflare-websites-an-api
canonical_url: https://www.scraping.club/p/scraping-cloudflare-websites-an-api
publish_date: '2024-07-21'
visibility: free
topics:
- cloudflare
- datadome
- antibot
- industry-overview
description: Testing PixelWhisperer, a solo developer's unblocker API still in preview, against Cloudflare, Akamai, Datadome, PerimeterX and Kasada with a Scrapy spider.
source_hash: 55c6e024060b438f
---

# Scraping Cloudflare websites using an API

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-21 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-cloudflare-websites-an-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Unblocker APIs are usually commercial products from companies with budget and headcount. This one is different. PixelWhisperer, a cybersecurity expert who runs the Web Scraping and Data Extraction Discord server and the Scraping wiki, built an unblocker API on his own. It is not public yet, and I got a preview to test. The practical question is how a solo project compares with commercial solutions against the anti-bots that matter most in production.

We tested it from a Scrapy spider that sends each target URL to the API and gets the HTML back. Cloudflare was tested on the US version of Indeed.com, with 10 remote job search URLs. Akamai was tested on 10 URLs from Zalando.com. We then ran the same approach against Datadome, PerimeterX and Kasada, with Hermes.com and Crunchbase.com among the targets. The integration is a plain API call with the target URL and an API key.

## What's inside

- Why Cloudflare came first: it is the most widespread anti-bot, and probably where PixelWhisperer put most of his effort.
- For Datadome, we looked at Hermes.com beyond the homepage, including product pages.
- For PerimeterX on Crunchbase.com, we also followed the guidelines from The Lab article on bypassing PerimeterX.
- The API is still a work in progress, and PixelWhisperer is looking for beta testers through his Discord server.

**In the full article:** The Scrapy spider code and the repository folder, plus the success rates per anti-bot and the site-by-site results on Datadome, PerimeterX and Kasada.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-cloudflare-websites-an-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
