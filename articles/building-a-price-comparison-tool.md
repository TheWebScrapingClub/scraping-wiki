---
type: article_summary
title: 'Hands on #3: Building a price comparison tool with Nimble APIs'
slug: building-a-price-comparison-tool
canonical_url: https://www.scraping.club/p/building-a-price-comparison-tool
publish_date: '2023-06-15'
visibility: free
topics:
- proxies
description: Hands-on test of Nimble's Browser and E-commerce APIs for a price monitoring tool, tracking the Nike Air Jordan 1 Mid across countries and on Walmart.
source_hash: 0fc7994f173fff25
---

# Hands on #3: Building a price comparison tool with Nimble APIs

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-06-15 (free to read). **[Read the full article](https://www.scraping.club/p/building-a-price-comparison-tool?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Brands care about price consistency. The same pair of shoes at different prices in different places undermines the price a brand declares, and the effect is stronger in luxury. Online, customers compare across the brand site, marketplaces and third-party retailers, so monitoring those prices is a real business need and a typical web scraping use case. Nike, which pushed direct-to-consumer and now also works with selected retailers, is our example.

We built a small price monitoring tool around the Nike Air Jordan 1 Mid, using Nimble as the data layer. First we set a baseline by scraping Nike's own site in several countries and colors with the Nimble Browser inside a Scrapy project, then normalized prices to USD to look at geo pricing. Then we moved to wholesalers, using the Nimble E-commerce API on Walmart search results and its marketplace sellers. I also say what I think of both products and where they still need work.

## What's inside

- Why the Nike site is harder than the scraper: some countries put all colors on one page, Canada has one page per color, and Saudi Arabia uses different product IDs.
- Where the schema.org data on the product page was enough, and why we parsed what the API returned.
- A proxy authentication quirk with the Nimble Browser that needed a custom Scrapy middleware.
- How the Amazon side would work, and what I saw when I tried the E-commerce API outside the US.

**In the full article:** The Scrapy project and the requests script on GitHub, the geo pricing table by country, the Walmart seller output and my full assessment of the Browser and E-commerce APIs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-a-price-comparison-tool?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
