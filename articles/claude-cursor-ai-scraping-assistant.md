---
type: article_summary
title: Build your web scraping assistant with Claude and Cursor
slug: claude-cursor-ai-scraping-assistant
canonical_url: https://www.scraping.club/p/claude-cursor-ai-scraping-assistant
publish_date: '2025-04-13'
visibility: free
topics:
- antibot
- akamai
- datadome
- browser-automation
description: A Scrapy coding assistant built with Cursor, Claude 3.7 Sonnet, a custom MCP server and Cursor rules, to automate repetitive e-commerce scraper creation.
source_hash: 52dc8e03f24315b2
---

# Build your web scraping assistant with Claude and Cursor

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-04-13 (free to read). **[Read the full article](https://www.scraping.club/p/claude-cursor-ai-scraping-assistant?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

At Re Analytics we set up hundreds of e-commerce scrapers that shared the same three or four data structures. Then came the maintenance: new selectors, proxy changes, scraper settings, sometimes a move from Scrapy to Playwright. Most of it is not rocket science, but keeping proxy bills and headcount low means removing friction from onboarding and upkeep.

I started building a web scraping assistant on Cursor as the IDE, with Claude 3.7 Sonnet as the model, a custom MCP server and Cursor rules. We explain what MCP servers and Cursor rules are and why Claude replaced GPT-4o for me. Then we apply them to the boring part of the job, creating Scrapy spiders. The goal is that a prompt like "Create a PLP E-commerce scraper for website X" produces a working spider with a predefined output structure. Choosing the scraping approach, such as internal APIs or the mobile app, stays with me. The whole project is open source.

## What's inside

- How PLP and PDP e-commerce scrapers differ, and why those are the only two types encoded in the rules so far.
- The workflow we want the assistant to follow, from project creation to a first run, including a check on cookies for anti-bot protection.
- Why a codebase of standardized scrapers makes Cursor's autocomplete predict the next line the way I would write it.
- The caveat that this is a supervised collaboration, not set and forget, and why simple, clear rules keep the LLM from going off the rails.

**In the full article:** The screenshot of the assistant at work, the link to the open-source repository with the rules and MCP server, and my conclusions on how to keep prompting under control.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/claude-cursor-ai-scraping-assistant?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
