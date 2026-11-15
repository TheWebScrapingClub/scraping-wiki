---
type: article_summary
title: How to Give Claude Real-Time Web Access With the Decodo MCP
slug: claude-decodo-mcp-how-to
canonical_url: https://www.scraping.club/p/claude-decodo-mcp-how-to
publish_date: '2026-06-07'
visibility: free
topics:
- captcha
- proxies
- data-analysis
- antibot
description: How to connect the Decodo MCP server to Claude Desktop so Claude can scrape the web in real time, with a Google search and an Amazon bestsellers example.
source_hash: 067cacf6e7511ef2
---

# How to Give Claude Real-Time Web Access With the Decodo MCP

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-06-07 (free to read). **[Read the full article](https://www.scraping.club/p/claude-decodo-mcp-how-to?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Surviving Cloudflare, CAPTCHAs and proxy rotation used to be the whole job. Now the second problem is plugging scraping into AI pipelines and agents, because bosses and clients want data in real time, structured, and often with some analysis on top. Until MCP arrived, that meant a lot of custom code and time.

We look at what MCP is and how the Decodo MCP server works as a scraping layer for AI agents on top of Decodo's Web Scraping API. Then we connect it to Claude Desktop and run two examples. The first is a Google search taken from the Decodo documentation. The second asks Claude to pull Amazon bestsellers in electronics and return JSON that can feed the next step of a pipeline. We also compare the output with the live pages to check that the model didn't hallucinate.

## What's inside

- Decodo MCP returns Markdown for LLMs, JSON for structured pipelines, and screenshots for visual context.
- The server exposes tools for Google, Amazon, Walmart, Target, TikTok Shop, YouTube, Reddit, Bing, ChatGPT and Perplexity.
- Setup needs Claude Desktop, a Decodo account with a free tier, and a basic authentication token from the API playground.
- Claude asks permission before using an MCP tool, and closing the Desktop window is not enough to load a new config.

**In the full article:** The JSON config for Claude Desktop, the full list of Decodo MCP tools, the prompts for both examples, and the screenshots comparing Claude's output with Google and Amazon.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/claude-decodo-mcp-how-to?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
