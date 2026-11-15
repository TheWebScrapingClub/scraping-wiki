---
type: article_summary
title: 'THE LAB #72: Advanced logging in Playwright'
slug: advanced-logging-in-playwright
canonical_url: https://www.scraping.club/p/advanced-logging-in-playwright
publish_date: '2025-01-10'
visibility: premium
topics:
- browser-automation
- proxies
description: 'Logging for Playwright scrapers: tracking CPU, memory and request stats with event listeners, and sending S3 snapshots of selector failures to RabbitMQ.'
source_hash: ef0c591d234f5140
---

# THE LAB #72: Advanced logging in Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-10 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/advanced-logging-in-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy makes logging easy. A request either ends correctly or gets refused by an anti-bot, and Scrapy already records bandwidth and response codes, so I only had to push them into RabbitMQ. Playwright is a different job. We run a real browser driven by our code, it eats CPU and memory, and plenty can break: a cookie banner hiding the selector, an A/B test, a page not fully loaded. Playwright also has no stats collector, so we have to build our own.

We pick the metrics worth watching: CPU and memory of the running environment, request count, bandwidth and status codes, and selector failures. We build the stats collector on Playwright event listeners, and for failures we send snapshots to Amazon S3 for debugging. Everything goes to RabbitMQ with the same data structure as in our earlier Scrapy logging post.

## What's inside

- Why sizing the virtual machine for a browser-based scraper is a trade-off between performance and cost
- How pages and contexts that are never closed leave garbage in memory until the machine stops working on long runs
- How request count and bandwidth help estimate the cost of per-request and pay-per-GB proxy plans
- What an event listener is in Playwright and which events it can observe, such as requests, navigations, console logs and network failures

**In the full article:** Python code for the Playwright logger, the event listener setup, the S3 snapshot upload, the RabbitMQ message format and the table of commonly used Playwright events.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/advanced-logging-in-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
