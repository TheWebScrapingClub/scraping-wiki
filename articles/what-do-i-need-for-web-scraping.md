---
type: article_summary
title: What do I need for web scraping?
slug: what-do-i-need-for-web-scraping
canonical_url: https://www.scraping.club/p/what-do-i-need-for-web-scraping
publish_date: '2023-02-24'
visibility: free
topics:
- browser-automation
- cloudflare
- anti-detect-browsers
- proxies
description: 'A starter toolset for a first scraper: site analysis tools, Python frameworks, and where to run it, including proxies and the anti-bot checks that shape the cho'
source_hash: a28fd4449fdebc4d
---

# What do I need for web scraping?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-24 (free to read). **[Read the full article](https://www.scraping.club/p/what-do-i-need-for-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Before writing a scraper, you need to know what you are scraping. The first job is analyzing the target website to find its technology stack and, above all, whether an anti-bot is in place and how hard it is to approach. That analysis decides which tools make sense, and a wrong guess here costs time later.

This is the third piece of the Web Scraping 101 Wiki, after what web scraping is and its legal side. We go through the basic toolset in three groups. First, tools for website analysis, Wappalyzer and Lambdatest. Second, the Python tools and frameworks: Scrapy, Splash, Selenium, Undetected-Chromedriver and Playwright, each with the kind of target it fits. Third, the running environment, where IP restrictions and per-IP request limits can push you to choose a specific proxy provider. Each tool links to a dedicated page for more detail.

## What's inside

- Wappalyzer works as a browser extension or through an API, and can detect most anti-bot solutions on a site.
- Lambdatest helps find which operating system and browser combinations a protected site tolerates, since some Cloudflare setups treat server operating systems as suspicious.
- The tools are matched to the target: Scrapy for sites without particular countermeasures, Splash when JavaScript rendering is also needed, and Selenium, Undetected-Chromedriver or Playwright when you have to act like a human using a browser.
- Proxies are classified by IP origin, datacenter or residential, and by the level of anonymity they give the client.

**In the full article:** The links to the dedicated pages on Scrapy, Splash, Selenium, Playwright and proxies, and the embedded video on starting web scraping in Python.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/what-do-i-need-for-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
