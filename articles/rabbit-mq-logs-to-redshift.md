---
type: article_summary
title: 'THE LAB #71: Sending Scrapy logs to RabbitMQ'
slug: rabbit-mq-logs-to-redshift
canonical_url: https://www.scraping.club/p/rabbit-mq-logs-to-redshift
publish_date: '2024-12-19'
visibility: premium
topics:
- scraping-infra
description: Modifying our Scrapy logging middleware to publish logs to a RabbitMQ queue with Pika, ahead of batch loading into AWS Redshift.
source_hash: 334793544afbfc49
---

# THE LAB #71: Sending Scrapy logs to RabbitMQ

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-19 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/rabbit-mq-logs-to-redshift?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In the last episode we improved the standard Scrapy logs to print live data and summary statistics. Printing them on screen is not enough when you run hundreds of scrapers, so we want to push them to AWS Redshift. That needs ingestion with high concurrency, no bottleneck on the scrapers from database writes, and batch consumption instead of millions of small inserts. RabbitMQ covers all three.

We modify the middleware so log_metric sends messages to a RabbitMQ queue instead of the console. I go through publishers, exchanges, queues, consumers and listeners, then we install Pika, start RabbitMQ locally with Docker, and create the scrapy_logs queue from the management UI. The consumer that reads the queue and writes to the database is the next piece.

## What's inside

- How acknowledgment (ACK) and requeueing keep delivery reliable when a consumer fails to process a message.
- Why Pika fits lightweight systems like Scrapy spiders, and its support for both synchronous and asynchronous communication.
- The parameters we set on scrapy_logs: message TTL (one hour), queue expiry and maximum queue length.
- The demo runs on a local RabbitMQ install, which can move to a cluster as message volume grows.

**In the full article:** The modified log_metric middleware code, the queue consumer that writes batches to the database, and the 71.RABBITMQ folder of the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/rabbit-mq-logs-to-redshift?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
