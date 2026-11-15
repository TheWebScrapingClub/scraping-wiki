---
type: article_summary
title: 'Web scraping from 0 to hero: creating our first Scrapy spider - Part 1'
slug: create-scrapy-spider-part-1
canonical_url: https://www.scraping.club/p/create-scrapy-spider-part-1
publish_date: '2023-12-17'
visibility: free
topics:
- cloudflare
- akamai
- datadome
- industry-overview
description: 'First lesson on writing a Scrapy spider: scoping a Valentino UK price scraper, checking for anti-bot, and extracting the product category links from the menu.'
source_hash: 9bfb5eed1263b8d4
---

# Web scraping from 0 to hero: creating our first Scrapy spider - Part 1

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-17 (free to read). **[Read the full article](https://www.scraping.club/p/create-scrapy-spider-part-1?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Before writing any code, a scraping project needs written requirements. That means a defined target website, a country, a refresh rate and a list of output fields. Skip this and you can't estimate costs or check whether the job is legal. I've had inquiries where the client couldn't name a single target site. Anti-bot detection comes next, because it decides which tool you use.

In this lesson of the free course we build a first, basic scraper on Valentino.com, UK version, a simple e-commerce site. We scoped it as a one-off project, listed the output fields, and checked which of them the product list pages expose. We ran Wappalyzer to look for anti-bot software, then created a Scrapy project, defined the items and generated a spider. Since Scrapy doesn't render pages, we read the raw HTML to find the menu links and wrote the first XPath selector to list the product categories.

## What's inside

- How to decide the refresh rate and why a one-off project costs differently from a daily or intra-daily one.
- Why we take fields from the product list pages instead of opening every product page, and which field is not exposed there.
- A trick for finding menu links in raw HTML when URLs may be relative: search for only the ending part of a known URL.
- What each file in a new Scrapy project does, and which ones we touch in this first lesson.

**In the full article:** The code for items.py and the spider, the Wappalyzer result on the target, the screenshots of the HTML and of the printed category list, and the link to the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/create-scrapy-spider-part-1?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
