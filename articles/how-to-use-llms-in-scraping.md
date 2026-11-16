---
type: article_summary
title: Are LLMs capable of replacing traditional scrapers?
slug: how-to-use-llms-in-scraping
canonical_url: https://www.scraping.club/p/how-to-use-llms-in-scraping
publish_date: '2025-04-27'
visibility: free
topics:
- antibot
- industry-overview
description: 'Whether LLMs can replace traditional scrapers: where they fail on accuracy, cost and speed, and where they fit, tested on 100 URLs from 33 e-commerce sites.'
source_hash: 30ba58e308c846d7
---

# Are LLMs capable of replacing traditional scrapers?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-04-27 (free to read). **[Read the full article](https://www.scraping.club/p/how-to-use-llms-in-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Every conversation about scraping now includes AI, because the industry hopes LLMs will fix its old problem: scalability. With traditional scraping, every new website means a dedicated scraper in the codebase. Each one can break, and the more scrapers we maintain, the more people we need to fix them. This is the extended version of my talk at PragueCrawl, organized by Apify and Massive.

I split the work into two layers, getting past the anti-bot to retrieve the HTML and parsing it, and look at where LLMs could take over the parsing. We go through three limits: accuracy, cost and speed. Then we ran an experiment where LLMs fit best, scraping a large number of websites with just a few URLs each. We used the ScrapeGraphAI API on 100 product URLs from 33 e-commerce sites, with a fixed output schema. I close with where I think LLMs belong in a massive scraping pipeline.

## What's inside

- How the time split between anti-bot bypass and HTML parsing changes from site to site, and why it matters for scraper maintenance.
- Why identical prompts on identical HTML can return different answers, and the e-commerce case where the LLM picks the suggested product instead of the main one.
- What a tokenizer shows when you feed it the HTML of a real Italian e-commerce product page, and why per-token pricing hurts at scale.
- Why parallel calls do not remove the ceiling set by provider rate limits.

**In the full article:** The Pydantic output schema, the GitHub repository with the experiment, the success and error breakdown, the cost and timing figures, the token count and pricing comparator, and the link to my earlier post on using AI to speed up scraper development.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-use-llms-in-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
