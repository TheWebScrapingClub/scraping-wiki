---
type: article_summary
title: 'THE LAB #75: Building self healing scrapers with AI'
slug: building-self-healing-scrapers-with-gpt
canonical_url: https://www.scraping.club/p/building-self-healing-scrapers-with-gpt
publish_date: '2025-02-06'
visibility: premium
topics:
- browser-automation
- anti-detect-browsers
- proxies
description: A proof of concept that uses GPT-4o to fix a broken e-commerce scraper, given the old scraper, a target URL and the desired output structure.
source_hash: 9515b0dfeba23978
---

# THE LAB #75: Building self healing scrapers with AI

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-02-06 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/building-self-healing-scrapers-with-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Hundreds of scrapers in production means a steady stream of breakages and partial data, and every fix costs people and money. AI could help in two ways: returning data without a scraper, or generating and maintaining the scrapers. Browser agents suit one-off tasks but not a large catalog, because of cost, reliability and execution time. Generated scrapers fit big projects better, though a human still has to handle anti-bot changes and proxy choices.

I built a proof of concept that takes a broken scraper and a target URL and returns a fixed one. The target is an e-commerce product list page, with a fixed output structure to give the LLM context. We fetch the HTML with Camoufox, then send it to GPT-4o through the OpenAI SDK to isolate the sections holding the product data, whether in tags or JSON. That step took hours of prompt engineering.

## What's inside

- Why an LLM can't fix an arbitrary scraper from the website's code alone, and why the desired data structure has to be part of the context.
- How the system and user message roles work in the OpenAI chat API, and what each is used for in the extraction step.
- A practical cost: sending a full HTML page to the API required moving to Tier 2 of the OpenAI account, which cost more than 100 USD.
- A short rant on prompt engineering, which feels like playing slot machines, with different results even when nothing changes.

**In the full article:** The complete prompt, the GPT-4o extraction function, the Camoufox snippet and the later steps that write the XPATH selectors and fix the broken scraper.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-self-healing-scrapers-with-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
