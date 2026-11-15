---
type: article_summary
title: Building a price comparison agent with the Oxylabs Web API
slug: building-a-price-comparison-oxylabs-web-api
canonical_url: https://www.scraping.club/p/building-a-price-comparison-oxylabs-web-api
publish_date: '2026-10-20'
visibility: free
topics:
- proxies
description: 'Tool of the Week: testing the Oxylabs Web API search and scrape endpoints by building a Claude price comparison agent that reads live shop prices in three count'
source_hash: aead064ec27de9a9
---

# Building a price comparison agent with the Oxylabs Web API

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-10-20 (free to read). **[Read the full article](https://www.scraping.club/p/building-a-price-comparison-oxylabs-web-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anyone who has built an AI agent that fetches live web data knows the problems with the standard fetch tool in the harness. Anti-bot systems block it, and a single page of raw HTML can bloat the context with useless markup. For a price check that is a real cost in tokens and in reliability.

For this Tool of the Week we tested the Oxylabs Web API, which has a search endpoint, a scrape endpoint and dedicated scrapers for sites like Amazon and Best Buy. We checked Markdown output, JavaScript rendering, geolocation, AI parsing and endpoint discovery on a Best Buy product page. Then we built a price comparison agent with Claude and the Anthropic Python SDK, using five thin tools of our own instead of the official MCP server. We ran it on the US, Italian and UK markets and looked at what it cost on both the Oxylabs and the LLM side.

## What's inside

- Why I wrote my own tool wrappers instead of using the official MCP server or the agent skills: visibility, control, tool descriptions and cost.
- How AI parsing with an OpenAPI schema behaves over repeated runs, and what the schema does and does not guarantee.
- How the agent reads endpoint discovery at runtime, and what the dedicated scrapers return compared with the generic one.
- In the UK run, a failing page, a wrong ASIN and a cut of the rendered Markdown changed time and token use.

**In the full article:** The full tool definitions, the system prompt, the loop code, the per-run tool call logs for the US, Italy and UK, the cost breakdown per run and the link to the GitHub repository with agent.py.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-a-price-comparison-oxylabs-web-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
