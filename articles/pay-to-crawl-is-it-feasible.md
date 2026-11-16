---
type: article_summary
title: 'Cloudflare Pay to Crawl: is it something feasible?'
slug: pay-to-crawl-is-it-feasible
canonical_url: https://www.scraping.club/p/pay-to-crawl-is-it-feasible
publish_date: '2025-08-24'
visibility: free
topics:
- cloudflare
- legal-ethics
- antibot
- proxies
description: 'Cloudflare''s Pay per Crawl and default AI crawler blocking: whether the economics work for site owners and for the AI companies that would pay.'
source_hash: 13aca7ee25470da3
---

# Cloudflare Pay to Crawl: is it something feasible?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-24 (free to read). **[Read the full article](https://www.scraping.club/p/pay-to-crawl-is-it-feasible?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare introduced Pay per Crawl and began blocking AI crawlers by default. The buzz covers little of how AI companies actually scrape. Their budgets are unlike anything we saw before, and site owners pay for the infrastructure that absorbs the load. LLM answers also send fewer people to the original page, even for sites ranking first on Google. Paying per crawl sounds good in theory.

I ran the idea through a simple model: a small bike repair guide site, a per-request price and a few AI companies crawling it. Then I questioned two assumptions behind it, using Google's index size to size the scraping volume and Bright Data's Web Unlocker as the alternative AI companies already have. I also cover Databoutique.com as a different model, and bot detection through Cloudflare's report on Perplexity and a LinkedIn post by Antoine Vastel.

## What's inside

- Garry Tan's report that Cloudflare blocked AI crawlers on the YCombinator domain without him noticing.
- The costs on the owner's side beyond the fees: running Cloudflare itself and the cut taken by the payment platform used in the beta.
- The tension between a price attractive to AI companies and a price worth collecting for the site owner.
- Why whitelisting LLM user agents without checking IPs is a weak setup, given how easy it is to change a user agent.

**In the full article:** The full revenue calculation for the bike repair site, the estimate of yearly AI request volume behind it, the price comparison with the Bright Data unblocker and the Databoutique model in more detail.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/pay-to-crawl-is-it-feasible?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
