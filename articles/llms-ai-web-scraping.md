---
type: article_summary
title: About LLMs, AI and Web Scraping
slug: llms-ai-web-scraping
canonical_url: https://www.scraping.club/p/llms-ai-web-scraping
publish_date: '2024-06-02'
visibility: free
topics:
- industry-overview
description: 'Pierluigi Vinciguerra and ML engineer Marco Vinciguerra on LLMs for web scraping: HTML parsing vs access, data quality, hallucinations and ScrapeGraphAI.'
source_hash: 3f20088153a2e104
---

# About LLMs, AI and Web Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-02 (free to read). **[Read the full article](https://www.scraping.club/p/llms-ai-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

After the ScrapeGraphAI tests in The Lab, I still had open questions about using LLMs for scraping. GPT 3.5 Turbo gave plausible but wrong data on medium pages. GPT-4o did better, with TripAdvisor parsed correctly on a minimal prompt. An LLM only covers the parsing half of the job. If the target is heavily protected, most of the project time goes into reaching the HTML, so the gain from smarter parsing shrinks.

Since I'm not an AI expert, I put these questions to Marco Vinciguerra, ML engineer and teaching assistant at Università degli Studi di Bergamo. We looked at data quality for use cases where accuracy and timeliness matter, such as dynamic pricing and inventory tracking. We also covered why a hallucinated value is harder to catch than a broken selector, and how general-purpose models compare with models built for scraping. Finally, we looked at ScrapeGraphAI's Generate Scraper Node and what it means for response times in production.

## What's inside

- Why TripAdvisor worked with a minimal prompt while an e-commerce site needed an elaborate prompt reworked several times, and whether training data explains it.
- How LLM failures differ from the two states of a classic selector, working or broken, and why consistency over time becomes a problem.
- How to catch errors in LLM output with the same checks we use in standard scraping, such as tests on the scraper or at the end of the pipeline.
- Why 10 seconds per request is a problem at scale and how generating selectors with an LLM changes that trade-off.

**In the full article:** Marco's full answers on general-purpose versus scraping-specific models, the reasoning on the Generate Scraper Node and the trade-offs of AI-generated selectors in a Scrapy workflow.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/llms-ai-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
