---
type: article_summary
title: 'THE LAB #28: Deep dive on inventory levels tracking'
slug: the-lab-28-deep-dive-on-inventory
canonical_url: https://www.scraping.club/p/the-lab-28-deep-dive-on-inventory
publish_date: '2023-09-28'
visibility: premium
topics:
- proxies
- akamai
- browser-automation
- residential-proxies
description: How to extract per-store inventory levels from Lowe's, a large US home improvement retailer, using an internal API result, Scrapy and Playwright.
source_hash: 6249d4d13d7a707c
---

# THE LAB #28: Deep dive on inventory levels tracking

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-09-28 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-28-deep-dive-on-inventory?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Lowe's is the second home improvement chain in the US, with more than 2100 stores and an assortment from furniture to animal care. Its inventory could say something about the company's profitability, about the brands it distributes and even part of the consumer price index. Like many retailers with a "pick up in store" option, the website has to know what is available in each store. Some sites show only a yes or no, others show exact quantities, and some keep the numbers inside internal API calls.

I found that Lowe's belongs to the last group. Wappalyzer showed Akamai as the only anti-bot, so we started with Scrapy and proxies. We split the job in two: a store list scraper, and a category crawler that works store by store. The category part was the hard one. It needed Playwright with browser contexts, a Brave instance and a way to switch the pickup store without a commercial tool. At the end I share my doubts about how to read this data.

## What's inside

- Plain residential proxy rotation was not enough for the store directory, so we used a web unblocker for that step.
- The website shows at most 25 pages per category, so the category must be small enough to fit under that limit.
- The API that returns the stock data could not be called directly, so the same data is read from the page HTML.
- Pagination had a quirk that returned stale data, and the final remarks question whether the numbers refer to a store or a central warehouse.

**In the full article:** The full Scrapy and Playwright code for the stores and category scrapers, the run commands, the store output format and the screenshots of the API response are in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-28-deep-dive-on-inventory?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
