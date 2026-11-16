---
type: article_summary
title: 'THE LAB #4: Scrapyd - how to manage and schedule a fleet of scrapers'
slug: scrapyd-manage-schedule-scrapers
canonical_url: https://www.scraping.club/p/scrapyd-manage-schedule-scrapers
publish_date: '2022-10-12'
visibility: premium
topics:
- cloudflare
description: How to manage and schedule many Scrapy spiders with Scrapyd, starting from the telnet console that Scrapy already ships with.
source_hash: ade96c1596f708bb
---

# THE LAB #4: Scrapyd - how to manage and schedule a fleet of scrapers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-10-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scrapyd-manage-schedule-scrapers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Web scraping is like eating cherries: one website pulls the other, and soon you have hundreds of scattered scrapers on your servers, scheduled through crontab with no real order. At that point the problem is no longer writing a spider. It is knowing which ones are running, what they collected and how to start or stop them without logging into each machine.

We start from what Scrapy already gives us: the built-in telnet console, which exposes engine status and data collection stats and lets an external tool control a running spider. Then we look at Scrapyd, an application that schedules and monitors Scrapy spiders through a basic web interface and also keeps multiple versions of the same scraper. We begin setting up a basic Scrapyd server, so you can see how a dashboard for a fleet of spiders is built on those native functions instead of custom scripts.

## What's inside

- How the telnet console works, including its default settings and what happens when no password is set
- Which commands read stats from a running spider and which ones pause, resume or stop the engine
- How Scrapyd handles versioning of the same scraper, and the limit on which version can be launched
- Why existing open-source tools make more sense than writing your own scripts to collect stats from each spider

**In the full article:** The settings and commands for the telnet console, the sample stats output and the step-by-step configuration of the Scrapyd server are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapyd-manage-schedule-scrapers?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
