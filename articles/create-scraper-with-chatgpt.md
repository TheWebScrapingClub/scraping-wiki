---
type: article_summary
title: How to create a web scraper with ChatGPT
slug: create-scraper-with-chatgpt
canonical_url: https://www.scraping.club/p/create-scraper-with-chatgpt
publish_date: '2023-05-14'
visibility: free
topics:
- browser-automation
description: Building a scraper for Valentino.com bag pages with Scrapeghost, a Python package that sends HTML and a data schema to ChatGPT, and what it cost in time and mon
source_hash: 563304cfdbf88fa9
---

# How to create a web scraper with ChatGPT

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-05-14 (free to read). **[Read the full article](https://www.scraping.club/p/create-scraper-with-chatgpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Writing a scraper means finding a selector for every field, and that gets tedious on large catalogs. Scrapeghost promises a shortcut: it makes the Python request, sends the HTML to ChatGPT together with a data dictionary, and gets the fields back. The catch is the prompt size limit and the API cost. I was curious enough to try it on a real target anyway.

We built a scraper for the bag listing on Valentino.com in two steps: first collect the product URLs from the list page, then pull the details from each product page. The first step was easy. The second took a long trial and error phase, because the full page hits the token limit and we had to split it into sections. We used XPath preprocessors, the split option and custom instructions in the prompt. Then we compared the output with what the site shows and weighed the time saved against speed and cost.

## What's inside

- How Scrapeghost works: pip install, an OpenAI key, a schema, and the option to pass HTML you already fetched with Scrapy or Playwright.
- How the 4000 byte prompt limit shapes the scraper: XPath or CSS preprocessors and automatic splitting of long pages.
- Why the output for some fields was inconsistent between products, and what we changed in the prompt to stabilize it.
- Whether writing the scraper this way saved time, and why speed and API cost make it a poor fit for large production projects.

**In the full article:** The full Python code for both scrapers, the XPath selectors for each product page section, the sample output rows and my final verdict on where this approach makes sense.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/create-scraper-with-chatgpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
