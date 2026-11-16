---
type: article_summary
title: 'THE LAB #15: Deep diving into Apify world'
slug: the-lab-15-deep-diving-into-apify
canonical_url: https://www.scraping.club/p/the-lab-15-deep-diving-into-apify
publish_date: '2023-03-30'
visibility: free
topics:
- cloudflare
- datadome
- human-behavior-emulation
- antibot
description: 'A first hands-on look at Apify: wrapping a Scrapy spider in an Actor with the Python SDK and CLI, deploying it, monitoring runs, and selling it in the Store.'
source_hash: 1424973db8e6bb24
---

# THE LAB #15: Deep diving into Apify world

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-03-30 (free to read). **[Read the full article](https://www.scraping.club/p/the-lab-15-deep-diving-into-apify?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Apify just released its Python SDK, and I had never used the platform. Apify is a scraping platform built around Actors, serverless cloud programs that run your scraper. It also maintains Crawlee, its open-source NodeJs library, and it lets you publish scrapers in a store. If you already use Apify, this adds little. If you come from plain Scrapy like me, it is a quick way to see what the ecosystem offers.

We started from the Apify CLI and its Scrapy template, then adapted a spider to collect product names, prices and URLs from two categories on the Lululemon website. We looked at which template files matter and how the Actor handles output. Then we used the Python SDK to change how results are stored. After that we deployed to the cloud, checked the dashboard for runs, logs, scheduling and integrations, and looked at publishing on the Apify store. I close with what worked for me and where I have doubts.

## What's inside

- Which files in the Apify Scrapy template are still useful, which one becomes redundant, and where execution starts.
- How the SDK changes the output: one CSV dataset instead of a pile of single JSON files, plus other features such as proxy management, webhooks and Actors talking to each other.
- How a scraper gets from the local machine to the Apify cloud, and what the dashboard shows, including the cost per execution.
- My mixed feelings: the cost of large-scale projects and the code overhead needed to turn a working scraper into an Actor.

**In the full article:** The main.py and pipeline code for the Lululemon Actor, the CLI commands for setup and deployment, and the dashboard screenshots with my full list of pros and cons.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-15-deep-diving-into-apify?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
