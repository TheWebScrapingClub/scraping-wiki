---
type: article_summary
title: 'THE LAB #69: Building a dashboard for your scrapers with Grafana'
slug: scrapy-grafana-prometheus-tutorial
canonical_url: https://www.scraping.club/p/scrapy-grafana-prometheus-tutorial
publish_date: '2024-12-05'
visibility: premium
topics:
- antibot
description: Why logging matters in large scraping projects, and how to set up Grafana with Prometheus as the data source to monitor a fleet of scrapers.
source_hash: 91befa53949c046a
---

# THE LAB #69: Building a dashboard for your scrapers with Grafana

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-05 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scrapy-grafana-prometheus-tutorial?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Once the scrapers are scheduled on Airflow and the data lands in S3, the next question is what those scrapers are doing while they run. On larger projects, request counts, error rates and response times are the only way to tell that a scraper stopped midway because of an error or an antibot. Logs also protect data quality, since incomplete or inconsistent data has to be caught before it reaches the end user. That matters most in e-commerce, finance and market research, where up-to-date information drives decisions.

I picked Grafana for the dashboards and Prometheus as the data source, because it is open source, built for real-time metrics and fits Grafana well. We set up both on a Mac, check that each one responds locally, and then connect Prometheus to Grafana from the web interface. That gives us the base for a scraper monitoring dashboard.

## What's inside

- Grafana started as a system monitoring tool, and it also works with Elasticsearch, InfluxDB and MySQL as data sources.
- Its alerting system can send notifications by email or messaging platforms, so you react before the end user notices missing data.
- Acting on errors spotted in the logs is what makes the web data pipeline more resilient, not only easier to debug.
- The setup follows the same pattern for Grafana and Prometheus: install, start as a service, open the local UI.

**In the full article:** The installation commands, the screenshots of each setup step, the data source configuration in Grafana and the access to the script in the 69.GRAFANA folder of The Lab repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapy-grafana-prometheus-tutorial?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
