---
type: article_summary
title: Build a RAG Application with ScraperAPI, Gemini, and FAISS
slug: build-a-rag-application-with-scraperapi
canonical_url: https://www.scraping.club/p/build-a-rag-application-with-scraperapi
publish_date: '2025-04-01'
visibility: free
topics:
- data-analysis
description: Build a RAG app that scrapes a product site with ScraperAPI, indexes it in FAISS, and answers questions with Gemini through a Streamlit interface.
source_hash: 41a61de6fefca605
---

# Build a RAG Application with ScraperAPI, Gemini, and FAISS

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-04-01 (free to read). **[Read the full article](https://www.scraping.club/p/build-a-rag-application-with-scraperapi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Finding a product on a shopping site usually means scrolling and paging through listings. We wanted to scrape the site once and ask it questions instead, like a bag within a given budget. Retrieval Augmented Generation fits this job: the LLM answers from the scraped data rather than from its pre-trained knowledge, which limits hallucinations. The catch is the input. Raw HTML needs cleaning before an LLM can use it.

We built a small app around ScraperAPI's LLM output feature, which returns the page as markdown. Gemini 1.5 Flash writes the answers, sentence-transformers produce the embeddings, FAISS handles similarity search, LangChain handles chunking, and Streamlit provides the interface and free hosting. We cover the three RAG stages first, then set up the keys and go through the app function by function.

## What's inside

- How retrieval, augmentation and generation each work, from embedding the chunks to building the final prompt.
- Why markdown output from the scraper saves cleaning work compared with parsing HTML and stripping tags and JavaScript.
- A custom embedding wrapper that lets a SentenceTransformer model plug into LangChain's FAISS vector store.
- How the augmented prompt combines retrieved context, the user question and the chat history before it goes to Gemini.

**In the full article:** The complete Streamlit app code, the scraping function with its ScraperAPI parameters, the Gemini prompt construction, and the project setup and API key steps.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/build-a-rag-application-with-scraperapi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
