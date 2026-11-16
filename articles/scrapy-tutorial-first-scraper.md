---
type: article_summary
title: How to write your first scraper with Scrapy
slug: scrapy-tutorial-first-scraper
canonical_url: https://www.scraping.club/p/scrapy-tutorial-first-scraper
publish_date: '2023-02-06'
visibility: free
topics:
- industry-overview
description: A beginner tutorial on building a first web scraper with Scrapy, from installation to a working spider that saves its output to a file.
source_hash: eaac36eebd097116
---

# How to write your first scraper with Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-06 (free to read). **[Read the full article](https://www.scraping.club/p/scrapy-tutorial-first-scraper?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scrapy is one of the most popular open-source frameworks for building web scrapers, and it is usually the first one people reach for when they move past a few lines of requests and BeautifulSoup. Getting started is simple, but newcomers still need to know how the pieces fit together: project, spider, selectors, output.

We walk through a first scraper from scratch. We start with a Python setup and the installation of Scrapy, then create a project and generate a spider with the Scrapy command line. We define what the spider extracts using a CSS selector, run it from the terminal, and save the results to a file instead of just printing them. The example is deliberately minimal, so you can see the whole workflow once before adding real parsing logic, link following or anti-bot handling.

## What's inside

- What a spider is in Scrapy and how it differs from the project that contains it
- How the genspider command creates the starting file, and what we replace in it
- How CSS selectors are used in the parse method to pull data from the response
- Where the output goes by default and how to export it to a file

**In the full article:** Step-by-step commands, the full spider code with the selector example, and the run and export instructions for each stage of the tutorial.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scrapy-tutorial-first-scraper?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
