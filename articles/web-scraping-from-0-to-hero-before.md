---
type: article_summary
title: 'Web scraping from 0 to hero: before start scraping'
slug: web-scraping-from-0-to-hero-before
canonical_url: https://www.scraping.club/p/web-scraping-from-0-to-hero-before
publish_date: '2023-11-05'
visibility: free
topics:
- cloudflare
- browser-automation
- legal-ethics
- antibot
description: 'Preliminary checks before writing a scraper: output data model, APIs, JSON in the HTML, JS rendering, anti-bot detection, robots.txt and sitemap.'
source_hash: 00968ccb8cd8809a
---

# Web scraping from 0 to hero: before start scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-05 (free to read). **[Read the full article](https://www.scraping.club/p/web-scraping-from-0-to-hero-before?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most scrapers that need rework were started too early. Web scraping is no longer plain vanilla: anti-bots are everywhere, there are hundreds of tools, and picking the wrong one costs time and money. So before writing any code, and assuming we are allowed to scrape the site, a short round of checks pays off.

This is the second lesson of the WSF0TH course. I go through the checks in the order I run them. First we define the output data model and locate each field on the site. Then we look for the cleanest source: an API behind the website, an API used by a mobile app, or JSON embedded in the HTML. If none of those exist, we decide between plain HTML and JavaScript rendering, which drives the choice of tool. Then we look at the site's architecture: which anti-bot it runs, what robots.txt says, and whether the sitemap can do the crawling for us.

## What's inside

- Why the output data model comes first, and what rework looks like when a field turns out to sit on another page.
- The advantages of APIs over HTML parsing, including data the website never shows, such as inventory levels.
- How the HTML versus JavaScript-rendered question maps to Scrapy or to browser automation like Selenium, Playwright or Puppeteer, and what it means for operating costs.
- Which free extension we use to spot anti-bots, and why a quick look at robots.txt can occasionally give a quick win.

**In the full article:** The screenshots of the network tab and of the Wappalyzer reports for Cloudflare and Kasada, the links to the earlier Fiddler and Charles Proxy lessons on app APIs, and the full reasoning behind each check.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/web-scraping-from-0-to-hero-before?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
