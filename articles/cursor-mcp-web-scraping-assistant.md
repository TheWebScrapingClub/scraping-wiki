---
type: article_summary
title: Use Cursor as web scraping assistant with MCP servers
slug: cursor-mcp-web-scraping-assistant
canonical_url: https://www.scraping.club/p/cursor-mcp-web-scraping-assistant
publish_date: '2025-03-21'
visibility: premium
topics:
- anti-detect-browsers
- browser-as-a-service
- antibot
description: Building a local MCP server with the Python SDK and Camoufox so Cursor can fetch a page, write XPath selectors and generate a working Camoufox scraper.
source_hash: 160c5e586545124d
---

# Use Cursor as web scraping assistant with MCP servers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-03-21 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/cursor-mcp-web-scraping-assistant?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In past Lab episodes we used Firecrawl to scrape this newsletter, Pinecone to store the markdown and the OpenAI API to add context to the prompt. The limit was the context window: it is small, so the answers were not always good. RAG with a vector DB now feels old school, and the new buzzword is Model Context Protocol (MCP), so I ran a small experiment to see what it can do for web scraping.

We built a local MCP server with the official Python SDK and used Camoufox to fetch the HTML. The server has three tools: one saves the page, one writes XPath selectors for a PLP or PDP template, and one writes a Camoufox spider from a template. We plugged it into Cursor and ran it on a Gucci listing page with Claude 3.7 Sonnet.

## What's inside

- How MCP splits into clients, servers, resources (like GET endpoints) and tools (like POST endpoints), and why OpenAI's missing support is a bad sign for adoption.
- Why each step saves its output to a file instead of passing it through the context window, and why running locally means no proxy.
- Why the spider template is needed: without it, the generated code is usually a hallucination.
- Prebuilt alternatives (BrowserBase and Hyperbrowser MCP servers), plus two caveats on reliability: consistency between runs and the shape of the output data.

**In the full article:** Code for xpath_server.py and the three tools, the Cursor setup steps, the exact prompt, screenshots of the Gucci run and the 79.MCP repository folder.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/cursor-mcp-web-scraping-assistant?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
