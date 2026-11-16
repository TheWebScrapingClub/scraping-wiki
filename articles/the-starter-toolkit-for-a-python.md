---
type: article_summary
title: The starter toolkit for a python web scraping developer (2022)
slug: the-starter-toolkit-for-a-python
canonical_url: https://www.scraping.club/p/the-starter-toolkit-for-a-python
publish_date: '2022-08-21'
visibility: free
topics:
- browser-automation
- proxies
description: 'The Python tools a web scraping developer needs in 2022: Scrapy, Scrapy Splash, Playwright, Wappalyzer Python and a proxy package for Scrapy.'
source_hash: 6519bb6f0e819f3c
---

# The starter toolkit for a python web scraping developer (2022)

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-08-21 (free to read). **[Read the full article](https://www.scraping.club/p/the-starter-toolkit-for-a-python?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy covers most of a Python scraping job, but not all of it. It reads only static HTML, proxies need managing, some targets need a real browser, and you want to know what a site runs before you write a spider. A starter toolkit should fill these gaps without piling up tools.

I go through the tools we use. First Scrapy and its modular architecture. Then Advanced Scrapy Proxies, a package I wrote and we run daily in production. Then scrapy-splash, which routes requests to a Splash server so JavaScript gets executed. Then Microsoft Playwright with playwright-stealth, for sites protected by anti-bot software. Last is the Python wrapper for Wappalyzer, which identifies the technology stack behind a target. I also ask for suggestions on what is missing from the list.

## What's inside

- What Downloader Middlewares can do to requests and responses, for example filtering duplicated requests before they reach the website.
- How Item Pipelines handle the output of a spider, and why that suits structured data with several columns per row.
- Where the proxy package can read its list from: a public URL, a local file, or a proxy set directly in the options.
- How Playwright compares with Selenium, and what Splash is built on.

**In the full article:** The Scrapy architecture diagram, the request and response workflow between its components, and the links to the documentation and repository of each tool.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-starter-toolkit-for-a-python?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
