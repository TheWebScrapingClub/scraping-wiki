---
type: article_summary
title: 'The Scriptwall: Why Google is hiding its SERP content behind Javascript'
slug: google-hiding-serp-results-javascripts
canonical_url: https://www.scraping.club/p/google-hiding-serp-results-javascripts
publish_date: '2025-01-19'
visibility: free
topics:
- serp-scraping
- industry-overview
- browser-automation
- nlp-ml
description: Google has required JavaScript for search results since January 15. Who wins and loses from the Scriptwall, from SERP data vendors to AI companies.
source_hash: 119b6c9a0f89c502
---

# The Scriptwall: Why Google is hiding its SERP content behind Javascript

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-19 (free to read). **[Read the full article](https://www.scraping.club/p/google-hiding-serp-results-javascripts?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Since January 15, Google requires JavaScript to show search results. Disable JS in your browser and the SERP won't load. Google told TechCrunch that fewer than 0.1% of searches come from users with JS off, and that the change protects its services from bots and abuse. Requiring JS is nothing new on the web, but when Google does it, the whole scraping industry has to look at its costs.

I go through who wins and who loses: Google, AWS, GCP and Azure on one side, SEO tools, SERP data providers and their end users on the other. My reading is that the Scriptwall protects Google's ranking system from AI companies more than it stops scraping. Then I use Stackoverflow to show how LLMs eat into the traffic of the sites they scrape, and what those sites may do in response.

## What's inside

- Why the 0.1% figure leaves open whether bot traffic is already excluded, and why I suspect bots are a much bigger share of Google's traffic.
- What changes for scrapers in practice: the move from browserless frameworks like Scrapy to browser automation like Playwright, and how the extra compute reaches cloud bills.
- Why ChatGPT wrappers, LinkedIn scrapers and similar businesses should read this as a warning about depending on a third-party data source without a backup plan.
- How AI companies ignoring robots.txt pushes websites toward walled gardens, and why LLMs risk losing fresh training data if their sources shut down.

**In the full article:** Screenshots of the Google results page with JavaScript disabled, the Similarweb traffic chart for Stackoverflow, and the full winners and losers breakdown with my reasoning on AI companies and walled gardens.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/google-hiding-serp-results-javascripts?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
