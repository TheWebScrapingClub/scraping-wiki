---
type: article_summary
title: Building a custom GPT using Firecrawl
slug: building-a-custom-web-scraping-gpt
canonical_url: https://www.scraping.club/p/building-a-custom-web-scraping-gpt
publish_date: '2024-10-06'
visibility: free
topics:
- http-clients
- legal-ethics
description: How Pierluigi built a custom GPT on web scraping knowledge, using Firecrawl to turn his newsletter articles into markdown files for the ChatGPT knowledge base.
source_hash: c763cb3e36196f4a
---

# Building a custom GPT using Firecrawl

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-10-06 (free to read). **[Read the full article](https://www.scraping.club/p/building-a-custom-web-scraping-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

The standard ChatGPT model, even o1-preview, gives shallow answers on web scraping, when it answers at all. I suspect part of this comes from the limits OpenAI puts on suggesting techniques that touch copyright or terms of service, which would be ironic given how the company collects its own data. So I wanted to put my own scraping knowledge on top of a ChatGPT base model and build a custom GPT.

I built it in the ChatGPT web interface and used the newsletter's free articles as the knowledge base. Forums disagree on the best upload format, PDF or Markdown, so I tested the question on my own content. I scraped the articles into markdown with the Firecrawl API on the free plan and called it with cURL, because the Python package gave me errors. We ran two tests: one on a single article the base model knew nothing about, and one on the latest 20 free articles merged into a single file, given the 20-file upload limit.

## What's inside

- Why the Python package for Firecrawl was dropped in favor of cURL, and what that cost in speed.
- How leftover Substack headers and newsletter names in the scraped markdown affected the GPT.
- The 20-file upload limit on custom GPTs and the workaround of appending articles into one file.
- Where the GPT answered well from my articles and where marketing material from the web overrode my benchmarks.

**In the full article:** The cURL call used with Firecrawl, the screenshots of the GPT's answers in both tests, the details of the Configure tab setup, and the link to the published Web Scraping Club GPT.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-a-custom-web-scraping-gpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
