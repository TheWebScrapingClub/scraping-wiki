---
type: article_summary
title: What is Scrapy?
slug: what-is-scrapy
canonical_url: https://www.scraping.club/p/what-is-scrapy
publish_date: '2023-02-06'
visibility: free
topics:
- proxies
description: 'An introduction to Scrapy, the open-source Python crawling framework maintained by Zyte: what it does, how you start a project, and how its architecture works.'
source_hash: 11157bb4f4fbeb1a
---

# What is Scrapy?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-06 (free to read). **[Read the full article](https://www.scraping.club/p/what-is-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy is the open-source Python framework for crawling and extracting data from websites, maintained by Zyte. If you scrape professionally you will meet it sooner or later, either as your main tool or as the base other tools are built on. It ships with auto-throttle, support for rotating proxies and user agents, and it is modular enough to extend with extra features.

In this introduction I cover what you need to get started: basic Python, a pip install, and the Scrapy CLI to create a project and write your first spiders. I list the built-in features for requests and responses, link following, cookies and sessions, output formats, logging, duplicate filtering and exception handling. Then I go through Scrapy's architecture, following the data flow controlled by the engine across the spider, scheduler, downloader, middlewares and item pipelines, taking the description from the official documentation. I also point to my first-spider tutorial and a beginner video.

## What's inside

- Which built-in features cover requests, link following, cookies, sessions and duplicate filtering
- The role of each architecture component: engine, scheduler, downloader, spider, middlewares and item pipelines
- How downloader middlewares and spider middlewares sit in the request and response flow
- Pointers to the official tutorial, my first-spider post and a beginner video by John Watson Rooney

**In the full article:** The nine-step data flow as the documentation lists it, the architecture diagram, and the links to the tutorial, the documentation and the video.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/what-is-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
