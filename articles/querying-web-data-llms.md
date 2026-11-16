---
type: article_summary
title: 'THE LAB #86: Querying Web Data using GPT-Like Web Interface'
slug: querying-web-data-llms
canonical_url: https://www.scraping.club/p/querying-web-data-llms
publish_date: '2025-06-05'
visibility: premium
topics:
- industry-overview
description: A proof of concept for asking natural-language questions about a web-scraped Farfetch dataset on Amazon S3 through a GPT-like interface, as an alternative to BI
source_hash: 0ee6e19f5cf1715a
---

# THE LAB #86: Querying Web Data using GPT-Like Web Interface

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-06-05 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/querying-web-data-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Collecting web data is only the first step. The real work is getting something useful to the people who make decisions. Having built Data Warehouse and reporting systems early in my career, I know the pains are the same fifteen years later: hundreds of overlapping reports, each with different numbers, and a BI team that loses control of what gets distributed. Self-service BI was supposed to fix that, but in old-school companies people lack the time, skills or will to learn another tool.

In this episode of The Lab we build a proof of concept for a conversational alternative. We take a web-scraped Farfetch product dataset (names, categories, prices) bought from DataBoutique and stored on Amazon S3. The goal is to let anyone ask questions in natural language and get answers right away, with no hand-written SQL and no scrolling through CSVs. We put it together with LLM APIs and a few packages, as an AI data analyst sitting on top of the file.

## What's inside

- Why self-service BI tools like Looker did not deliver, and why friction in changing worker behavior matters more than tool quality.
- Where a conversational interface fits next to a small set of certified core reports instead of replacing them.
- The toolset behind the AI data analyst, and how it reads a dataset stored on Amazon S3.
- How a purchased web data file from DataBoutique becomes something a non-technical user can question.

**In the full article:** The full toolset list, the scripts in the private GitHub repository folder 86.AI-POWERED-BI, the setup of the AI data analyst and examples of the questions it answers on the Farfetch dataset.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/querying-web-data-llms?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
