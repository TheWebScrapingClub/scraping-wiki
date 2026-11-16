---
type: article_summary
title: 'THE LAB #92: scraping Depop in a cost-effective way'
slug: scraping-depop-cost-effective
canonical_url: https://www.scraping.club/p/scraping-depop-cost-effective
publish_date: '2025-08-29'
visibility: premium
topics:
- anti-detect-browsers
- antibot
- proxies
- cloudflare
description: 'Scraping Depop behind Cloudflare Bot Detection: a Camoufox browser approach compared with calling its internal API through ScraperAPI, with costs.'
source_hash: 99e263aa8cbfca39
---

# THE LAB #92: scraping Depop in a cost-effective way

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-29 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-depop-cost-effective?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Depop is a secondhand fashion marketplace with a catalog of over 30 million items, so it is a requested scraping target. It is also well protected: Cloudflare Bot Detection, configured in a restrictive way. The internal search API shows up easily in the browser's network tab, but replaying the request with cURL fails most of the time, even though no Cloudflare cookie is needed. Getting a response is only half the problem. At this size, the way you bypass the protection decides what a full snapshot costs.

We start with Camoufox, loading the men's category page and intercepting the API responses while scrolling. Then we put numbers on a full run: calls needed, execution time, AWS instance cost and proxy bandwidth, priced with our ProxyPrice calculator. After that we drop the browser, call the internal API through ScraperAPI, iterate it with Scrapy and compare the bill.

## What's inside

- Why a browser is called a bazooka to kill mosquitoes for this target, and the performance degradation that comes with loading many pages.
- How the API paginates with a cursor instead of a page number, and what the response metadata tells you about where to continue.
- Why the smallest AWS instance that can run a browser still matters in the cost estimate.
- How the credit cost per request changes when JavaScript rendering is not needed.

**In the full article:** The Camoufox and Scrapy scripts from the GitHub repository, the full cost breakdown for a complete catalog snapshot, and the walkthrough of the browserless Scrapy build.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-depop-cost-effective?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
