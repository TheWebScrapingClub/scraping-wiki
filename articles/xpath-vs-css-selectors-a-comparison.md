---
type: article_summary
title: 'XPath vs CSS selectors: a comparison'
slug: xpath-vs-css-selectors-a-comparison
canonical_url: https://www.scraping.club/p/xpath-vs-css-selectors-a-comparison
publish_date: '2023-04-02'
visibility: free
topics:
- industry-overview
description: 'A comparison of XPath and CSS selectors for web scraping: how each works, how to pick a good selector, and a side-by-side test on the Hacker News home page.'
source_hash: 17812781a65707b3
---

# XPath vs CSS selectors: a comparison

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-04-02 (free to read). **[Read the full article](https://www.scraping.club/p/xpath-vs-css-selectors-a-comparison?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Choosing a selector is one of the first decisions in any scraper. A selector is an object that, given a query, returns a portion of a web page, and that query is written in either XPath or CSS. The choice shapes how readable your scrapers are and how well they survive changes to the site, especially on larger projects with several people working on them.

We start from the basics: what a selector is, the difference between ID-based and attribute-based selectors, and a few rules for writing a good one. Then we go through how XPath expressions are built and which types of CSS selectors exist. We compare the two syntaxes on the same target, the title of the first story on the Hacker News home page, using the selectors Chrome DevTools gives us. I close with my own preference and with how much the speed argument really matters.

## What's inside

- The three parts of an XPath expression (axis, node tests and predicates) and the role each one plays.
- Five CSS selector types: universal, type, class, ID and attribute.
- Four rules for a good selector, including using only one selector language per project when several people work on it.
- Whether the common claim that CSS is faster should influence your choice, and what separates the two in flexibility.

**In the full article:** The XPath and CSS selectors we copied from the Hacker News page, the syntax comparison table between the two languages, and my full reasoning on which one to adopt.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/xpath-vs-css-selectors-a-comparison?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
