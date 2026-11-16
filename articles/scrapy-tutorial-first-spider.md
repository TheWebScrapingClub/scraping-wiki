---
type: article_summary
title: Create your first python scraper with Scrapy
slug: scrapy-tutorial-first-spider
canonical_url: https://www.scraping.club/p/scrapy-tutorial-first-spider
publish_date: '2022-10-07'
visibility: free
topics:
- legal-ethics
description: A beginner tutorial on building a first Scrapy spider against books.toscrape.com, covering project setup, items, settings, spider start options and XPath extrac
source_hash: 5b85c8ef6708bee6
---

# Create your first python scraper with Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-10-07 (free to read). **[Read the full article](https://www.scraping.club/p/scrapy-tutorial-first-spider?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy is the de-facto standard for web scraping in Python because it already handles the things scraping needs: robots.txt, request throttling, User Agent changes, XPath and CSS selectors, and export to CSV or JSON. If you are new to it, the hard part is knowing which file does what and which settings matter before you write any parsing code.

We built a first scraper against books.toscrape.com, a fake bookstore whose product data sits in plain HTML, so no headless browser is needed. We generated the project, looked at the files it creates, and went through items.py and settings.py in detail: User Agent, robots.txt, fixed throttling versus AutoThrottle, and default request headers. Then we created the spider, compared two ways to start it, and wrote the XPath selectors for the book pages and the pagination. The scraper writes its output to a JSON file. I also say where I keep cleaning and validation logic.

## What's inside

- Two ways to start a spider, start_urls and start_requests, and when the second one gives you more control, for example a different cookie jar per URL.
- Fixed throttling with concurrency and delay compared with AutoThrottle, including the rules the algorithm follows to adjust the delay.
- Why I leave type declarations and validation out of the scraper and push cleaning to pipelines.py or the database.
- Why most fields need XPath based on the row label, and why the run shows 404 errors that can be ignored in this tutorial.

**In the full article:** The full code for items.py, settings.py and the spider, the XPath selectors for each field, the AutoThrottle configuration, the request headers, the crawl command and the GitHub repository link.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapy-tutorial-first-spider?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
