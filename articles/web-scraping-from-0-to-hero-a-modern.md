---
type: article_summary
title: 'Web scraping from 0 to hero: a modern tech stack'
slug: web-scraping-from-0-to-hero-a-modern
canonical_url: https://www.scraping.club/p/web-scraping-from-0-to-hero-a-modern
publish_date: '2023-11-19'
visibility: free
topics:
- browser-automation
- proxies
- captcha
- residential-proxies
description: The components of a modern web scraping pipeline for recurring jobs, from scraper code and cloud environments to proxies, storage and data quality checks.
source_hash: 08406bc52011e714
---

# Web scraping from 0 to hero: a modern tech stack

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-19 (free to read). **[Read the full article](https://www.scraping.club/p/web-scraping-from-0-to-hero-a-modern?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A one-off scraper needs nothing beyond the spider and a place to run it. Once you have a freelance career or a company built on web scraping, you need an infrastructure that handles daily operations and a growing crawling base without losing control of costs. What we owe the customer is correct data, on schedule, at a reasonable price. That gives three challenges: data quality, data freshness and costs.

I picture the pipeline as an assembly line, with data moving from the website to the customer and one task done at each station. We go through the stations: building the scrapers, the running environments, the extra tools such as proxies, scraping APIs and CAPTCHA solvers, and the storage and checking of output data. Then I cover the features that keep hundreds of scrapers manageable: centralized scheduling, standard launch processes, and centralized logging of runs and scraper stats. These are the ones that have helped me most in practice.

## What's inside

- When a single generic scraper over Schema.org JSON data can replace one scraper per website, and which conventions help when you do need many.
- Why cloud VMs or containers are preferred over bare metal, and why browser automation changes the sizing of the environment.
- The trade-off between storing raw HTML for a rolling window and storing only parsed output, in storage cost and in the ability to recover from errors.
- Why a crontab per scraper becomes unmanageable at scale, and which Scrapy stats are worth logging to estimate proxy costs.

**In the full article:** The assembly line diagram of the pipeline, the Scrapy stats screenshot, and the full list of the features I rely on to manage scrapers at scale.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-scraping-from-0-to-hero-a-modern?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
