---
type: article_summary
title: Scrapoxy, the super proxy aggregator, how it works?
slug: scrapoxy-proxy-aggregator
canonical_url: https://www.scraping.club/p/scrapoxy-proxy-aggregator
publish_date: '2024-02-15'
visibility: premium
topics:
- proxies
- scraping-infra
- proxy-industry
- residential-proxies
description: Scrapoxy is an open-source proxy aggregator that manages providers and cloud IPs in one pool. We set it up with Scrapy and look at a cost-aware architecture.
source_hash: be36229219da4c99
---

# Scrapoxy, the super proxy aggregator, how it works?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-15 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scrapoxy-proxy-aggregator?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Any web scraping project past a minimum scale needs one or more proxy providers. Managing one by hand is fine. With two or three, each with different proxy types, you start jumping between dashboards to check usage, success rates and geographies, and that overhead eats your team's time.

We look at Scrapoxy, the open-source tool built by Fabien Vauchelles, which works like a super proxy aggregator. We cover how it connects proxy providers and cloud services such as AWS, GCP and Azure into a single IP pool. We also cover how it rotates IPs, handles bans and scales datacenter proxies up and down. Then we walk through the installation, projects, credentials and connectors, and plug it into a Scrapy spider running against a Docker install on my laptop. The Proxies tab showed two things worth noticing. We close with an architecture that keeps proxy costs under control.

## What's inside

- How connectors are configured per provider: number of proxies, time-outs, and auto-scaling and down-sizing rules
- What Scrapoxy does for cloud providers like AWS or Azure, including the VM image and permissions, compared with proxy providers where you only set credentials
- Which Scrapy settings and middlewares are involved, and why we made Scrapy wait before starting the crawl
- Why one Scrapoxy installation with three projects, one each for datacenter, residential and mobile proxies, can replace spinning up a VM cluster per scraper run

**In the full article:** The Scrapy settings and middleware configuration, the screenshots of the Scrapoxy marketplace, connectors and Proxies tab, the two findings from our test run, and the full three-project architecture.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapoxy-proxy-aggregator?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
