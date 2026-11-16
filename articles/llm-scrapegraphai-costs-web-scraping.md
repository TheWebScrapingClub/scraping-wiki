---
type: article_summary
title: How LLMs are affecting the costs of web scraping
slug: llm-scrapegraphai-costs-web-scraping
canonical_url: https://www.scraping.club/p/llm-scrapegraphai-costs-web-scraping
publish_date: '2024-06-23'
visibility: free
topics:
- llm-scraping
- data-analysis
- industry-overview
description: How LLMs and ScrapeGraphAI change web scraping costs, from setup for non-experts to scraper maintenance, with a look at self-healing pipelines.
source_hash: d4c6fa1ef331ebd9
---

# How LLMs are affecting the costs of web scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-23 (free to read). **[Read the full article](https://www.scraping.club/p/llm-scrapegraphai-costs-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In the previous post we split the costs of a web scraping project into categories. Setup and maintenance are the two where LLMs look most promising. Setup is the barrier for people who need web data but have no scraping experience. Maintenance is the pain point for companies running many scrapers in production, where scaling gets expensive.

With Marco Vinciguerra, founder of ScrapeGraphAI, we looked at two scenarios. In the first, a journalist with a tech background needs some data and has no time to build a scraper, so we used the SmartScraperGraph module, which returns the data straight from a prompt. In the second, a company already runs scrapers in production. Sending every request to an LLM would be inefficient there, so we used the ScriptCreatorGraph, which writes the scraper instead of the data. We then sketched a futuristic scenario, self-healing web data pipelines, where QA failures trigger an LLM fix.

## What's inside

- How the SmartScraperGraph is built from four nodes: fetch, parse, a RAG store and answer generation with an LLM
- The model options for the answer step: OpenAI, Gemini, or a local model with Ollama
- Why sending every request to an LLM does not make sense for scrapers already in production
- How a QA check could trigger an LLM to rewrite selectors, and why only the easiest scrapers would see maintenance costs near zero

**In the full article:** Code examples for SmartScraperGraph, its parallel multi-source version and ScriptCreatorGraph, the graph diagrams, and our closing remarks on using LLMs in production today.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/llm-scrapegraphai-costs-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
