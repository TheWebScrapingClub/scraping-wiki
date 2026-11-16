---
type: article_summary
title: XPATH and CSS Selectors in Web Scraping
slug: xpath-css-selectors-web-scraping
canonical_url: https://www.scraping.club/p/xpath-css-selectors-web-scraping
publish_date: '2024-04-28'
visibility: free
topics:
- captcha
- browser-automation
description: Ten side-by-side examples of XPATH and CSS selectors in Scrapy spiders, from basic paragraph selection to text matching and sibling navigation.
source_hash: 14cfff75405ac198
---

# XPATH and CSS Selectors in Web Scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-04-28 (free to read). **[Read the full article](https://www.scraping.club/p/xpath-css-selectors-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Selectors are the part of a scraper that picks the interesting pieces out of the HTML, and they matter whatever tool you use, Scrapy or Playwright. The two common options are XPATH and CSS selectors. We had already compared them in theory in an earlier post. In this episode of the "Web Scraping from 0 to Hero" course, the goal is to see how they differ when you actually write the spider.

We took ten small HTML snippets and wrote the same extraction twice in Scrapy, once with CSS and once with XPATH. The cases go from simple ones, like paragraphs inside a div or elements with a given class, to attribute values, nested text, last and first children, siblings after a heading, and elements matched on several attributes. One case is selection by text content, where the two approaches are not equivalent. We close with my view on when CSS is enough and when XPATH is the better choice for complex pages.

## What's inside

- Each example pairs one HTML snippet with a CSS selector and an XPATH written for Scrapy's response object.
- One example covers selecting by text content, where the two languages are not on equal footing.
- Sibling relationships and attribute extraction are shown in both syntaxes, so you can compare how each reads.
- The final remarks say which kind of target suits CSS and which suits XPATH, including moving up and sideways in the document.

**In the full article:** The ten HTML snippets with the CSS and XPATH code for each, plus the closing comparison of when to pick one over the other.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/xpath-css-selectors-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
