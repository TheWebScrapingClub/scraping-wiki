---
type: article_summary
title: 'THE LAB #70: Advanced logging in Scrapy'
slug: advanced-logging-scrapy
canonical_url: https://www.scraping.club/p/advanced-logging-scrapy
publish_date: '2024-12-12'
visibility: premium
topics:
- proxies
- proxy-industry
description: Why distributed Scrapy operations need centralized logging, which live and summary metrics to track, and why RabbitMQ fits better than Kafka or direct writes.
source_hash: 84509123b28f3b9d
---

# THE LAB #70: Advanced logging in Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/advanced-logging-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Watching a single scraper's runtime logs on a Grafana dashboard is nice, but it does little for an operations team running hundreds of scrapers across several machines. A local Prometheus per machine does not scale there. With that many spiders you can easily reach millions of log rows per day, and logging must not slow the scrapers down.

This is the first post of a small masterclass on logging for distributed scraping. We start from what is worth tracking and split it into live metrics and summary metrics, and tie both to monitoring, debugging and cost control. Then we choose the architecture: a message queue that decouples log production from storage. We compare it with direct database writes, API-based logging and Kafka, and explain why we picked RabbitMQ. Finally, we start building a Scrapy middleware that extracts the data, printing JSON messages to screen for now. In the next post they go to RabbitMQ.

## What's inside

- Live metrics (status codes, proxy endpoint, execution IP) support dynamic proxy rotation and early fixes, while summary metrics (requests, failures, bytes transferred) support cost estimates.
- The cost questions logging should answer: which website costs the most to scrape, and whether a site stays affordable if it needs an unblocker.
- How a message queue works: producers, consumers, acknowledgments, retries and delivery guarantees, plus the use cases where it fits best.
- Why direct database writes and API-based logging struggle at this volume, and why Kafka is more infrastructure than this use case needs.

**In the full article:** The Scrapy middleware code from the 70.LOGGING folder of the GitHub repository, the architecture diagram and the JSON message structure we designed for the logs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/advanced-logging-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
