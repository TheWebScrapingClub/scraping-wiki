---
type: article_summary
title: 'THE LAB #88: Fuel Your Content Machine with LLM Scraping'
slug: fuel-obsidian-with-llms
canonical_url: https://www.scraping.club/p/fuel-obsidian-with-llms
publish_date: '2025-07-03'
visibility: premium
topics:
- llm-scraping
- proxies
- residential-proxies
description: Building a daily web scraping press review with ScrapeGraphAI and Firecrawl, with LLM summaries saved as Markdown notes in an Obsidian vault.
source_hash: 5ad2157a59da2854
---

# THE LAB #88: Fuel Your Content Machine with LLM Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-07-03 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/fuel-obsidian-with-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Finding fresh ideas for a corporate blog or a newsletter means checking dozens of sites by hand, and that gets tedious fast. I wanted a daily web scraping press review that tells me what the industry is publishing, without writing a custom scraper for every source I add.

We built a pipeline that collects the URLs of the latest posts from two sources: a Black Hat World search on fingerprinting and the WebScraping.pro blog. ScrapeGraphAI and Firecrawl, both driven by a prompt and an output schema, return a short summary, tags and the link for each post. Each result becomes a Markdown note in the vault, and I decide whether to keep it, discard it or read it later. I also explain what a second brain is and why Obsidian's Markdown files suit programmatic notes.

## What's inside

- Why the Black Hat World search and the WebScraping.pro sitemap need different ways of finding new URLs, and how links already processed are skipped.
- What we ask the LLM to return for each post: a short summary, tags and the URL for the full read.
- How each Obsidian note is laid out, and how the keep, discard or read-later review works as a first-pass filter.
- Why LLM scraping fits this use case: hundreds of sources without hundreds of custom article scrapers.

**In the full article:** Scripts for both sources, the ScrapeGraphAI and Firecrawl calls with their prompts and schemas, the note-generation code and a screenshot of the resulting Obsidian notes.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/fuel-obsidian-with-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
