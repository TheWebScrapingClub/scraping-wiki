---
type: article_summary
title: 'Indexing data in the web: Robots file and Sitemaps'
slug: indexing-data-in-the-web-robots-file
canonical_url: https://www.scraping.club/p/indexing-data-in-the-web-robots-file
publish_date: '2023-08-13'
visibility: free
topics:
- legal-ethics
description: History of robots.txt and XML sitemaps, whether ignoring robots.txt is legal when scraping, and when a sitemap is a good entry point for a scraping project.
source_hash: 0b505892e7e6937d
---

# Indexing data in the web: Robots file and Sitemaps

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-13 (free to read). **[Read the full article](https://www.scraping.club/p/indexing-data-in-the-web-robots-file?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A post by Gergely Orosz about banning the GPTbot user agent from his blog made me curious about the basics we all use and rarely question. Who invented the robots file, and when? Is it legal to ignore it when scraping? And how do XML sitemaps fit in? These files shape what search engines crawl and index, and they shape what we find when we start a scraping project.

I did the research and found something I didn't expect, mostly about where robots.txt comes from. I cover its origin, what the file does, and why websites hide some sections from crawlers. I look at whether bots actually follow it, including the Internet Archive's position, the legal side, and how Scrapy handles it by default. Then I compare it with XML sitemaps, who introduced them, and when they work as a starting point for scraping a site.

## What's inside

- Who proposed the robots.txt standard, in which context, and why it is still not an official standard
- Why a robots file is a set of suggestions that nothing forces a scraper to follow
- How the Internet Archive and security researchers use robots.txt in ways that differ from search engines
- Which scraping cases make a sitemap a good entry point, and what you lose by skipping the site's own structure

**In the full article:** The dates and sources on the history of robots.txt and sitemaps, the sample robots file, the Scrapy settings that control robots.txt behavior, and my closing thoughts on what surprised me.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/indexing-data-in-the-web-robots-file?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
