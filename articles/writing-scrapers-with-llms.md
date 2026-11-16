---
type: article_summary
title: 'Writing scrapers with LLMs: GPT4, LLama3.1, Mistral compared'
slug: writing-scrapers-with-llms
canonical_url: https://www.scraping.club/p/writing-scrapers-with-llms
publish_date: '2024-09-06'
visibility: premium
topics:
- browser-automation
- proxies
description: Where LLM-powered scraping tools help and where they don't, tested by asking GPT4, Llama3.1 and Mistral to write scrapers with ScrapeGraph-AI.
source_hash: 9b6548b230d2b8e6
---

# Writing scrapers with LLMs: GPT4, LLama3.1, Mistral compared

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-09-06 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/writing-scrapers-with-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

LLM-powered scraping tools are everywhere, so expectations need setting first. Without an anti-bot in the way, they can write a scraper, heal it when the site changes, or return the data directly. They cannot read the network tab for internal APIs, bypass anti-bot systems, handle proxies, or beat a Scrapy or Playwright scraper on cost and speed. So today I see their best use as a junior programmer: they write the first draft, we review it and deploy.

We ran the tests with ScrapeGraph-AI, which lets us swap models by changing a few parameters. We asked GPT4, Llama3.1 and Mistral to write scrapers for different types of websites, starting with GitHub: given a user profile, list all its repositories. We picked it because the models have most likely seen its structure in training. Same task and output schema for every model, with BeautifulSoup as the library.

## What's inside

- Why an LLM cannot return data that lives only in an internal API, such as inventory levels missing from the HTML.
- Why running an LLM extraction costs more than Python selectors: once the selectors exist, parsing is free, while tokens are not.
- How we set up ScriptCreatorGraph with a prompt that asks for exception handling and a schema that defines the output fields.
- Why any judgment on these models ages fast, and how this follows up on my earlier ScrapeGraph-AI test.

**In the full article:** Generated scraper code and JSON output for each model, the prompts and schemas we used, and the per-model results on GitHub and the other target websites.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/writing-scrapers-with-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
