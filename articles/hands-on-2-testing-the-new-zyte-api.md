---
type: article_summary
title: 'Hands On #2: Testing the new Zyte Api'
slug: hands-on-2-testing-the-new-zyte-api
canonical_url: https://www.scraping.club/p/hands-on-2-testing-the-new-zyte-api
publish_date: '2023-04-06'
visibility: free
topics:
- cloudflare
- datadome
- antibot
- proxies
description: 'Hands On #2 tests Zyte API with a Scrapy spider against Datadome, Cloudflare, Kasada, F5 and PerimeterX, comparing raw HTML and browser rendering.'
source_hash: ed71bc7aff3b64bb
---

# Hands On #2: Testing the new Zyte Api

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-04-06 (free to read). **[Read the full article](https://www.scraping.club/p/hands-on-2-testing-the-new-zyte-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Zyte API is a hosted API that handles the anti-bot work for you. It covers proxy rotation and retries, automatic switching from data center to residential IPs, geolocation, a cookie jar, sticky IPs and a scriptable browser. Before paying for a tool like this, you want to see how it behaves on real targets, not on a marketing page. This is the second Hands On episode, it is not sponsored, and the opinions are mine.

We built a plain Scrapy spider that fetches 10 pages from each of five sites, one per anti-bot: Datadome, Cloudflare, Kasada, F5 and PerimeterX. We ran a baseline without Zyte, then Zyte API with raw HTML only, then with browser rendering. Each setup was scored from 0 to 100 on runs from a local machine and from a server. We plugged the API into Scrapy through the scrapy-zyte-api package. I close with pros, cons and a final rating.

## What's inside

- How the 0 to 100 score is built from two runs, one local and one from a server, over fifty hand-picked URLs.
- Why the spider checks a string on the page and not just the status code, so a 200 on a challenge page does not count as a success.
- What changes in the Scrapy setup when you move from raw HTML to browser rendering, and why that choice matters for cost on larger volumes.
- How the dashboard shows the cost of each request, and how the pricing commitment works once you go past the trial credit.

**In the full article:** The spider's settings, the result tables for each run and each anti-bot, the final rating with its reasoning, and the full pros and cons list.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/hands-on-2-testing-the-new-zyte-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
