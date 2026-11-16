---
type: article_summary
title: 'THE LAB #21 - Bypass anti-bot challenges with AI'
slug: the-lab-21-bypass-anti-bot-challenges
canonical_url: https://www.scraping.club/p/the-lab-21-bypass-anti-bot-challenges
publish_date: '2023-06-22'
visibility: free
topics:
- cloudflare
- datadome
- proxies
description: Testing the Nimble browser's AI against Cloudflare, F5, Datadome, PerimeterX and Kasada on five product URLs each, with rendering and parsing enabled.
source_hash: 734f5ea2c498cac0
---

# THE LAB #21 - Bypass anti-bot challenges with AI

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-06-22 (free to read). **[Read the full article](https://www.scraping.club/p/the-lab-21-bypass-anti-bot-challenges?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anti-bot vendors say they train AI models on billions of daily requests to spot anomalies in fingerprints and behavior. AI can also generate believable fingerprints and mimic human behavior, so it is turning into a fight between models. For anyone scraping e-commerce, the practical question is whether an AI-driven browser can get through the protections you meet most often.

We ran our usual testing methodology on the Nimble browser, a headful automated browser built for scraping. For each of five anti-bot systems (Cloudflare, Datadome, Kasada, F5, PerimeterX) I picked five random product URLs and always asked for rendering. Each response returns the HTML plus a parsed version. Targets were Harrods, Nordstrom, Footlocker Italy, Neiman Marcus and a Kasada-protected site. I ordered the tests by Statista's 2022 market share figures and add my own view on what that report leaves out. This is part of the AI month with Nimble.

## What's inside

- Why I think the Statista market share ranking misses Datadome and PerimeterX, based on what I see in e-commerce projects.
- Bypassing an anti-bot and getting usable data are two separate results, and one target showed the difference.
- For smaller sites the parsed output is usually the product JSON schema, so no scraper is needed.
- Final remarks apply the Pareto rule to judging a young product with room to improve.

**In the full article:** The Python code for the requests, the pass or fail verdict for each anti-bot, the parsed output screenshots and the link to The Lab GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-21-bypass-anti-bot-challenges?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
