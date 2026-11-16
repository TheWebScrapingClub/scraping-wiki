---
type: article_summary
title: 'The Framework That Won''t Quit: Scrapy''s Continued Relevance in Data Extraction'
slug: scrapy-ten-years-of-scraping-framework
canonical_url: https://www.scraping.club/p/scrapy-ten-years-of-scraping-framework
publish_date: '2025-05-18'
visibility: free
topics:
- browser-automation
- proxies
- data-analysis
- human-behavior-emulation
description: 'Why Scrapy is still relevant: its Twisted core, modular architecture, middlewares and pipelines, and how it fits JavaScript sites, proxies and LLMs.'
source_hash: 3a8628417d6775ab
---

# The Framework That Won't Quit: Scrapy's Continued Relevance in Data Extraction

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-05-18 (free to read). **[Read the full article](https://www.scraping.club/p/scrapy-ten-years-of-scraping-framework?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Web scraping reinvents itself every couple of years. New frameworks appear, anti-bot systems get harder, APIs are the promised land, and now LLMs promise to automate everything. In that noise Scrapy looks venerable, so I asked myself whether it still belongs in a modern stack. My answer is yes, and the reason is its architecture, not inertia.

I walk through the design choices that keep it useful. We start from the asynchronous core built on Twisted and its Reactor, set against hand-built asyncio and AIOHTTP code around Requests, BeautifulSoup or Selenium. Then come the modular components, the middlewares and Item Pipelines, and the settings for throughput and politeness. Last, I look at how Scrapy works with JavaScript-heavy sites, proxy and anti-detection setups, and LLM-based processing, including where it falls short on its own.

## What's inside

- Why overlapping the waits for two requests matters, and what a synchronous flow costs you when one request fails.
- What each Scrapy component is responsible for, and what that separation means for debugging, unit testing and teamwork on large projects.
- Practical uses for Downloader Middlewares, Spider Middlewares and Item Pipelines, from custom retry logic and proxy handling to deduplication and multiple storage destinations.
- Scrapy does not run client-side JavaScript, so I compare Splash with Playwright or Puppeteer workers and Scrapy as crawl orchestrator, then cover the API cost and latency caveats of LLMs in pipelines.

**In the full article:** Sync and async request flow diagrams, the Scrapy architecture diagram, the full lists of throttling and concurrency settings, links to the Splash, Playwright and Puppeteer plugins, and my video interview with Shane Evans of Zyte.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapy-ten-years-of-scraping-framework?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
