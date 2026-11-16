---
type: article_summary
title: 'The Lab #52: Scraping with LLMs and ScrapeGraphAi - part 1'
slug: scraping-with-llms-scrapegraphai
canonical_url: https://www.scraping.club/p/scraping-with-llms-scrapegraphai
publish_date: '2024-05-30'
visibility: premium
topics:
- industry-overview
description: Testing ScrapeGraphAI with GPT-3.5-turbo on Net-A-Porter, and why general-purpose LLMs are a risky fit for web scraping where accuracy matters.
source_hash: fcbc43bbbd4e4e0c
---

# The Lab #52: Scraping with LLMs and ScrapeGraphAi - part 1

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-05-30 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-with-llms-scrapegraphai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

The dream of every web scraper is a tool that scrapes any website with no maintenance when the code changes. LLMs are sold as that tool, and I use ChatGPT daily as the intern I can't afford to pay, for low-risk tasks. Scraping has a different risk profile. Prompts take trial and error, every test is flaky, and nobody can check every scraped page by hand.

We tested ScrapeGraphAI, a Python library that scrapes with LLMs. Llama on my 4-year-old MacBook Pro could not complete any scraping, so I used GPT-3.5-turbo. With SmartScraperGraph we ran two tests on Net-A-Porter: a category listing, where numeric fields like price must be exact, and a single product page with qualitative fields such as description, color and material composition. We compared the output with the live pages and repeated the listing run the next day.

## What's inside

- Why Zyte and Nimble build scraping-specific models, and how locating data in the HTML differs from guessing the next word.
- The five graph types in ScrapeGraphAI and why SmartScraperGraph fits single pages.
- Why a prompt that works today may not work next month, and what that means when no human checks the results.
- How the prompts are written field by field, with rules for product code, full price, price and currency.

**In the full article:** Prompts and Python scripts for both tests, the screenshots comparing the output with the real Net-A-Porter pages, and the results of each run.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-with-llms-scrapegraphai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
