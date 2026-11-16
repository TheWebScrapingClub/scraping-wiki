---
type: article_summary
title: 'THE LAB #77: Building a Web Scraping Knowledge Assistant with RAG'
slug: ingest-web-data-rag-llm
canonical_url: https://www.scraping.club/p/ingest-web-data-rag-llm
publish_date: '2025-02-27'
visibility: premium
topics:
- industry-overview
description: 'Building a RAG assistant on scraped data: fine-tuning vs RAG, local vs API LLM, and scraping The Web Scraping Club with Firecrawl into Pinecone.'
source_hash: 8b3028213d3da1ad
---

# THE LAB #77: Building a Web Scraping Knowledge Assistant with RAG

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-02-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/ingest-web-data-rag-llm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most companies that use web data stop at the first layer: scraped files go into a warehouse and analysts build dashboards on top. LLMs suggest a different way to use that data, asking questions in natural language instead of hunting for the right dashboard. I've seen too many dashboards that disagree with each other, so the idea appeals to me. The open problem is hallucinations: if you can't see the number behind an answer, can you trust it?

In this Lab we start an end-to-end project on the articles of this newsletter. We compare fine-tuning and Retrieval-Augmented Generation for adding custom knowledge to an LLM, and weigh a local open-source model against a hosted API. We then scrape the whole blog with Firecrawl, starting from the Substack sitemap and getting Markdown back. Pinecone is the vector database we picked for retrieval. A second post in the series will cover the rest of the build.

## What's inside

- Pros and cons of fine-tuning and RAG, including privacy, update cost and the fact that a fine-tuned model cannot cite its sources.
- Why fine-tuning and RAG can be combined, for example tuning for tone while RAG supplies the changing knowledge.
- The trade-offs of local models such as LLaMA 2, Mistral and Falcon against OpenAI's API, and why the retrieval layer stays the same either way.
- Why the sitemap is the starting point for Firecrawl instead of a blind crawl.

**In the full article:** The Python script in the paywalled GitHub repository, the Firecrawl setup and the Pinecone choice are in the full article, and the web app build is left to the next Lab.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/ingest-web-data-rag-llm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
