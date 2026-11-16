---
type: article_summary
title: 'THE LAB #78: Building a Web Scraping Knowledge Assistant with RAG - Part2'
slug: web-scraping-assistant-gpt
canonical_url: https://www.scraping.club/p/web-scraping-assistant-gpt
publish_date: '2025-03-07'
visibility: premium
topics:
- industry-overview
description: 'How to improve a Pinecone knowledge base built from a scraped newsletter: markdown cleaning, three chunking strategies, and a query and answer flow with GPT-4o.'
source_hash: 4d29b641675de572
---

# THE LAB #78: Building a Web Scraping Knowledge Assistant with RAG - Part2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-03-07 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/web-scraping-assistant-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In part one we scraped this newsletter with Firecrawl and loaded the posts into a Pinecone VectorDB. After release I kept querying it and the results did not satisfy me, so I tried to improve the data ingestion. With RAG, retrieval quality depends on what you put in the index. A whole article in a single entry makes it hard to match one concept to a user query.

We worked on three things. First, we cleaned the markdown that Firecrawl extracts before passing it to Pinecone. Second, we split the articles into chunks, first by fixed length and then by having GPT-4o rewrite each post paragraph by paragraph. That gave us three indexes built on the same input data. Finally, we covered the query side: embedding the prompt, the proximity search in Pinecone, a confidence threshold, and a fallback to GPT-4o general knowledge. The retrieved chunks then go into the prompt context to generate the answer.

## What's inside

- Why fixed-length chunking is approximate: the same paragraph can end up split across different chunks.
- The record structure shared by the three indexes: a vector field, a text field returned as output, and metadata used to cite the source articles.
- How a confidence threshold on the proximity score decides between using Pinecone results and falling back to GPT-4o general knowledge.
- Which of the three indexes I think gives the best answers, and why prompt engineering is the last step.

**In the full article:** The regex cleaning function, the retrieval and answer generation code, the two chunking scripts and the paid GitHub folder with the full set of scripts.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-scraping-assistant-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
