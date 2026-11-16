---
type: article_summary
title: A Practical Guide to Web Data Extraction with LLMs and GPT Vision
slug: scraping-with-llms-gpt-vision
canonical_url: https://www.scraping.club/p/scraping-with-llms-gpt-vision
publish_date: '2025-07-27'
visibility: free
topics:
- browser-automation
- proxies
- residential-proxies
description: 'Three ways to scrape the same National Weather Service forecast page: BeautifulSoup selectors, Pydantic with GPT-4o, and screenshots read by GPT Vision.'
source_hash: 74d5d0cf475688cb
---

# A Practical Guide to Web Data Extraction with LLMs and GPT Vision

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-07-27 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-with-llms-gpt-vision?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A scraper that worked yesterday breaks today because someone renamed a class. Nested tables, like the infobox on the Wikipedia United States page, make it worse, since you end up writing complex logic around selectors that nobody guarantees will stay the same. The goal is to depend as little as possible on HTML structure and anchor only to the parts you expect to stay stable.

We took one target, the San Francisco seven-day forecast on forecast.weather.gov, and extracted day, temperature and overall description with three methods, all in Python. The first is the classic requests and BeautifulSoup scraper. The second sends only the relevant HTML to GPT-4o and uses Pydantic to define and validate the output schema. The third uses Selenium to screenshot and crop the forecast block, then passes the image to GPT Vision. We then look at what AI-based extraction costs and where it can go wrong.

## What's inside

- Why the nested infobox on the Wikipedia United States page is hard to scrape with plain selectors
- The only selector we kept in the LLM methods is the seven-day-forecast-list container, which we assume is stable
- What Pydantic adds to the LLM output: schema definition, validation and detailed error messages
- The caveats of AI scraping: per-request API cost, token optimization, and hallucinated or missing fields that call for human validation

**In the full article:** The full Python code for the three scrapers, the Pydantic models and prompts, the Selenium screenshot and cropping setup, the resulting CSV files for each method, and the complete list of caveats on cost and hallucinations.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-with-llms-gpt-vision?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
