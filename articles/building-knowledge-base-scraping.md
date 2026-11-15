---
type: article_summary
title: 'THE LAB #101: Building an Internal Knowledge Base for Your Scraping Team'
slug: building-knowledge-base-scraping
canonical_url: https://www.scraping.club/p/building-knowledge-base-scraping
publish_date: '2026-04-02'
visibility: premium
topics:
- cloudflare
- browser-automation
- scraping-infra
- proxy-industry
description: 'How we built the internal knowledge base for our scraping team: markdown conversion, e5 embeddings and PostgreSQL with pgvector for searching 300 articles.'
source_hash: f69390bb7e9a51ca
---

# THE LAB #101: Building an Internal Knowledge Base for Your Scraping Team

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-04-02 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/building-knowledge-base-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Every scraping team ends up with the same mess. Someone documents a Cloudflare workaround in Notion, a teammate reinvents it three months later in a Google Doc, and the original page goes stale. The knowledge exists, but nobody can find it when it matters. At TWSC we have around 300 articles from four years, and Substack's archive search stopped being useful long ago.

We show the production system we built and use daily, after the FAISS proof of concept in THE LAB #77. Playwright pulls our own Substack posts, the Algolia API feeds Hacker News stories, and ScrapegraphAI, with Firecrawl as fallback, converts external URLs. Everything becomes markdown with YAML frontmatter, gets embedded with e5-large-v2 and lands in PostgreSQL with pgvector. We explain why markdown, how embeddings work, which chunking strategy performs better and what auto-tagging does for retrieval.

## What's inside

- When to build your own HTML-to-markdown converter and when to pay for extraction services, based on whether you control the source.
- Why metadata lives in frontmatter and is used for filtering, while only the content is embedded.
- Why we picked pgvector over a dedicated vector database, and which parts of the three-stage pipeline you can swap for Confluence or Qdrant.
- How we discover URLs from the sitemap, detect changes with lastmod and keep a logged-in Playwright session for premium posts.

**In the full article:** The code in the paying-users GitHub repository, the chunking comparison, the reasoning behind the e5-large-v2 choice, the auto-tagging setup and the Docker Compose layout.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-knowledge-base-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
