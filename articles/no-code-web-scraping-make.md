---
type: article_summary
title: No-Code Web Scraping with Make.com
slug: no-code-web-scraping-make
canonical_url: https://www.scraping.club/p/no-code-web-scraping-make
publish_date: '2024-06-09'
visibility: free
topics:
- scraping-infra
description: How to build a no-code scraping pipeline in Make.com that reads a sitemap, parses product pages with ChatGPT and uploads a CSV to AWS S3.
source_hash: f0750dc2ec9640a6
---

# No-Code Web Scraping with Make.com

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-09 (free to read). **[Read the full article](https://www.scraping.club/p/no-code-web-scraping-make?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Many marketers, sales people and managers want web data delivered to a tool they already know, and they can't write a scraper. No-code solutions have multiplied to cover that need, helped by the LLM boom. The practical question is how far a non-programmer can get with one of them on a real site, and where it stops making sense.

We built a Make.com scenario that reads the sitemap of Moscot.com, an eyewear brand, and iterates over the product URLs. Each page is downloaded, converted to Markdown and sent to ChatGPT to get structured fields back. An aggregator collects the results, a CSV is created and the file is uploaded to an AWS S3 bucket. I also cover the limits: anti-bot protection, OpenAI rate limits and how Make.com bills.

## What's inside

- Why we feed ChatGPT Markdown converted by a built-in Make.com node instead of raw HTML.
- Which product fields we asked the Transform Text to Structured Data node to extract, and why a sleep node was needed after it.
- How the iterator, the aggregator and the Create CSV file (advanced) node fit together to close the loop.
- Why per-operation billing makes this approach a poor fit for sites with thousands of pages, and how an HTML node with your own selectors can speed it up.

**In the full article:** Screenshots of every node configuration, the sitemap XML sample, the field-by-field extraction setup and the operation count and monthly cost compared with a coded scraper.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/no-code-web-scraping-make?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
