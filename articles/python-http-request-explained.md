---
type: article_summary
title: HTTP requests in Python explained
slug: python-http-request-explained
canonical_url: https://www.scraping.club/p/python-http-request-explained
publish_date: '2022-12-04'
visibility: free
topics:
- browser-automation
- antibot
description: A short primer on HTTP requests, then a comparison of the headers sent by Python Requests, Scrapy and Playwright with Firefox, Chromium and Chrome.
source_hash: 058192867e228f23
---

# HTTP requests in Python explained

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-12-04 (free to read). **[Read the full article](https://www.scraping.club/p/python-http-request-explained?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anti-bot systems no longer rely on generic user agent rules. Keeping request headers in order and coherent with a standard browser installation is the first thing a scraper has to get right. A properly set request rarely fools an anti-bot on its own, but it is a must-have.

We start with a quick refresher on the four parts of a request: method, URL, headers and body. Then we look at what a server actually receives. Using webhook.site as the target, we sent requests from Python Requests, plain Scrapy, Scrapy with custom headers, and Playwright with bundled Firefox, bundled Chromium, Chromium plus the stealth plugin, and a standard Chrome installation. For each one we compared the number of headers, their order and the user agent. We also cover Client Hints and the split between low and high entropy hints.

## What's inside

- Why headers are the part of a request that matters most for scraping, including their role in API authentication and in the pass anti-bot software hands to the server
- How Scrapy's default settings show up in the headers, including the referer left by the previous page visited
- Why the playwright stealth plugin works on browser attributes such as window.navigator and not on request headers
- What the sec-ch-ua header is, and how low entropy hints differ from high entropy ones

**In the full article:** The screenshots of the headers captured for each tool, the test script on GitHub, and the side-by-side differences in header count and order.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/python-http-request-explained?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
