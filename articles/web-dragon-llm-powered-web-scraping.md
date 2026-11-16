---
type: article_summary
title: Web DRAGON - LLM-powered web scraping on a distributed cloud
slug: web-dragon-llm-powered-web-scraping
canonical_url: https://www.scraping.club/p/web-dragon-llm-powered-web-scraping
publish_date: '2023-12-19'
visibility: free
topics:
- browser-automation
- captcha
description: 'Web scraping on Salad''s residential GPU network: Playwright crawler, Qdrant vector search and a Zephyr 7B LLM extracting product data from Harrods.'
source_hash: 87286c23dc64fb29
---

# Web DRAGON - LLM-powered web scraping on a distributed cloud

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-12-19 (free to read). **[Read the full article](https://www.scraping.club/p/web-dragon-llm-powered-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Web scraping at scale keeps hitting the same two walls. Many sites block datacenter IPs and fingerprint anything that doesn't look like a home user, and selector-based scrapers break whenever the layout changes. Salad's network of residential gaming PCs offers an answer to both: real home traffic, and GPUs that can run an LLM to parse pages instead of HTML selectors and regexes.

I asked Bob Miles and Shawn Rushefsky from Salad to build a pipeline on that network. It has three stages: crawling, search indexing and LLM inference. The crawler runs Playwright with Chromium and Playwright Stealth, fed by a crawling service. Pages are chunked, embedded with Text Embeddings Inference and BAAI/bge-large-en-v1.5, and stored in Qdrant. For each field, we retrieve the relevant chunks and ask Zephyr 7B, served by Text Generation Inference, in a RAG setup. The test target is Harrods.com.

## What's inside

- How the crawling service hands out each URL only once, stays on the entry domain and respects a maximum depth.
- Why the chunker keeps meta tags and embedded JSON scripts next to the visible text, and why it uses NLTK tokenization instead of splitting on whitespace.
- Why the prompt must follow the model's chat template, and how we render it from the Jinja template since we don't use transformers directly.
- What changes in compute cost and per-site tuning when an LLM replaces selectors, and how the inference servers make swapping models easy.

**In the full article:** Code for the crawler, chunking, embedding, Qdrant indexing and retrieval, the architecture diagrams, the chat template setup, and the crawl success rates and per-page processing times from the Harrods run.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-dragon-llm-powered-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
