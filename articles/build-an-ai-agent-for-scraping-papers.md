---
type: article_summary
title: Build an AI Agent for Scraping and Analyzing Research Papers
slug: build-an-ai-agent-for-scraping-papers
canonical_url: https://www.scraping.club/p/build-an-ai-agent-for-scraping-papers
publish_date: '2025-12-14'
visibility: free
topics:
- proxies
- residential-proxies
description: How to build a LlamaIndex ReAct agent with Gemini and a custom PDF tool that downloads research papers and writes a structured Markdown report.
source_hash: d0c3e1d494cb25d9
---

# Build an AI Agent for Scraping and Analyzing Research Papers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-12-14 (free to read). **[Read the full article](https://www.scraping.club/p/build-an-ai-agent-for-scraping-papers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Downloading a research paper is the easy part, since most academic sites hand out the PDF for free. The real work is getting clear knowledge out of a long, jargon-heavy document, and doing it fast enough to keep up with what gets published in tech. Reading every paper end to end does not fit in the day.

We built an AI agent for that job. You give it a paper URL, it fetches the PDF from arXiv or any other online source, converts it into a format an LLM handles well, and writes a structured Markdown report. We used LlamaIndex with a ReAct agent, Gemini as the model, and a custom tool built on requests and MarkItDown. I walk through the setup, the tool, the system prompt, the CLI entry point, and a run on a real arXiv paper.

## What's inside

- Why a ReAct agent fits tool-based tasks like this one, and how its Thought, Action and Observation loop works.
- Why we convert the PDF with MarkItDown instead of passing it straight to an LLM, in terms of speed and cost.
- How a Pydantic output model makes the agent return a report we can export to a file.
- Which Gemini model we picked, why it costs nothing for this use case, and when a stronger one makes sense.

**In the full article:** Code for agent.py, the system prompt, the custom tool definition, the project and .env setup, and the screenshots of a run on a real arXiv paper.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/build-an-ai-agent-for-scraping-papers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
