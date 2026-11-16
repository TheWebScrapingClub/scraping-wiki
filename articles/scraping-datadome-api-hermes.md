---
type: article_summary
title: 'THE LAB #2: scraping data from a website with Datadome and xsrf tokens'
slug: scraping-datadome-api-hermes
canonical_url: https://www.scraping.club/p/scraping-datadome-api-hermes
publish_date: '2022-09-15'
visibility: premium
topics:
- datadome
- antibot
description: How we scraped Hermes.com, protected by Datadome and XSRF tokens, starting from a plain Scrapy spider and moving to a mobile-based approach.
source_hash: 758f35d958bf9ac0
---

# THE LAB #2: scraping data from a website with Datadome and xsrf tokens

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-09-15 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-datadome-api-hermes?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Datadome is one of the key players in anti-bot software and runs on sites like FootLocker, Rakuten and Reddit. Sooner or later you will meet it, and a scraper that worked yesterday can stop working today. I had to update one that no longer got past it, so I wrote down the process.

The target is Hermes.com. The product details we need come from an internal API that the site calls while you browse each category. We started with a standard Scrapy spider and adjusted DEFAULT_REQUEST_HEADERS to see if it could get in. Datadome reacted quickly: the spider was redirected and locked out, while the browser, with the same redirect, landed on the home page. We then changed path. Hermes has no official app, so I reused the procedure from the first post of THE LAB to see how the website behaves when accessed from mobile.

## What's inside

- Why the internal API called from the category pages is the data source, and how we spotted it in the browser's network tab.
- How the plain Scrapy spider is treated by Datadome compared with a real browser hitting the same redirect.
- How the mobile-access method from the first post of THE LAB is applied to a site that has no official app.
- The role of the XSRF tokens in the requests to the Hermes API.

**In the full article:** The Scrapy spider code, the request headers, the mobile traffic analysis, the handling of the XSRF token and the working scraper for Hermes.com.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-datadome-api-hermes?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
