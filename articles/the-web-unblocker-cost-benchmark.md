---
type: article_summary
title: The Web Unblocker Cost Benchmark
slug: the-web-unblocker-cost-benchmark
canonical_url: https://www.scraping.club/p/the-web-unblocker-cost-benchmark
publish_date: '2023-12-24'
visibility: free
topics:
- cloudflare
- akamai
- industry-overview
description: Cost comparison of Bright Data, Infatica, Nimble, Oxylabs, Smartproxy and Zyte unblockers on two e-commerce scraping projects, pay-per-GB versus pay-per-request
source_hash: 6be3673d3ffda270
---

# The Web Unblocker Cost Benchmark

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-24 (free to read). **[Read the full article](https://www.scraping.club/p/the-web-unblocker-cost-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Success rate against a given target is not the only way to pick a "super API". The price of a project matters too, and comparing vendors is not simple because some bill pay-per-request and others pay-per-GB. Both metrics are hard to estimate before a project starts. If you already scrape the site and log well, the numbers get much clearer.

We collected the pricing models of Bright Data Web Unlocker, Infatica web scraper, Nimble Unblocker Proxy, Oxylabs Web Unblocker, Smartproxy Site Unblocker and Zyte API as of December 8th, 2023. We then picked one price per vendor and ran two cost benchmarks on real scraping volumes from our own stats. The first is the product list pages of Zalando, a high-GB, high-request job. The second is the product detail pages of Zara USA, where the ratio between GB and requests is very different. For Zyte, I asked their head of product marketing for help in choosing a price.

## What's inside

- Why Infatica's credit system is hard to read, and why we assumed render_js on every request to compare it with the others.
- How Bright Data's premium domain list affects the price, and why we kept the standard rate for Zara even though it is on that list.
- How Zyte's tiered pricing was reduced to one weighted average, using an internal study of the top 250,000 websites and its five clusters.
- Why the number of requests is easy to deduce from the target site while the number of GB is much harder, and what that means for a multi-provider setup.

**In the full article:** The price per vendor for each plan, the two cost tables for Zalando and Zara USA, the GB and request volumes behind them, and my closing conclusions on mixing providers.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-web-unblocker-cost-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
