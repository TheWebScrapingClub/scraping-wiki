---
type: article_summary
title: The true costs of a web scraping project
slug: the-true-costs-of-a-web-scraping
canonical_url: https://www.scraping.club/p/the-true-costs-of-a-web-scraping
publish_date: '2023-11-25'
visibility: free
topics:
- scraping-infra
- antibot
- captcha
- proxies
description: A cost model for web scraping projects that compares building a scraper, buying a commercial solution and buying the data, for setup and monthly maintenance.
source_hash: 3572b8e80dfe15af
---

# The true costs of a web scraping project

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-25 (free to read). **[Read the full article](https://www.scraping.club/p/the-true-costs-of-a-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Whether you are a PM, an in-house developer or a freelancer, the first question on a new scraping project is the same: how much will it cost? Knowing the real costs is what lets you charge customers enough, stay inside a budget, and understand the unit economics of your scraping activity. Difficulty of the target, refresh frequency and how long the data is needed all change the answer.

I split the costs into two parts: getting the data once and maintaining the feed over time. For each part we compare three paths: building the scraper in-house, buying a commercial solution such as web unblockers or target-specific APIs, and buying pre-scraped data from marketplaces like Datarade, AWS Data Exchange and Databoutique.com. I built cost scenarios for small, medium and large websites, then looked at which path fits one-off needs and which fits long-running projects. There is also a spreadsheet to plug in your own numbers.

## What's inside

- Commercial solutions bill per GB of bandwidth or per request, which makes providers hard to compare, and each model suits a different kind of target.
- Maintenance of an in-house scraper is modeled as running costs (hardware, proxies, CAPTCHA solvers) plus time spent fixing a spider that breaks.
- With a commercial solution we no longer need resources for headful browsers, but the service cost recurs at every refresh.
- A bought dataset can be a starting point, for example a product catalog before scraping the images, but integration work on top can change the economics.

**In the full article:** The cost tables for each scenario and website size, the assumptions behind the hourly rate and monthly maintenance, and the link to the spreadsheet for testing your own scraping costs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-true-costs-of-a-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
