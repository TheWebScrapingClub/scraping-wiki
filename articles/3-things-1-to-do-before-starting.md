---
type: article_summary
title: 3 THINGS + 1 TO DO BEFORE STARTING CODING YOUR SCRAPER
slug: 3-things-1-to-do-before-starting
canonical_url: https://www.scraping.club/p/3-things-1-to-do-before-starting
publish_date: '2022-08-02'
visibility: free
topics:
- browser-automation
description: 'A pre-coding checklist for scraper projects: identify the target''s tech stack and anti-bot, look for APIs and JSON in the HTML, then check legal ground.'
source_hash: f3827d805c12f969
---

# 3 THINGS + 1 TO DO BEFORE STARTING CODING YOUR SCRAPER

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-08-02 (free to read). **[Read the full article](https://www.scraping.club/p/3-things-1-to-do-before-starting?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Before writing any scraper code, a short analysis of the target website can save a lot of time. The questions are simple. Which technology stack and which anti-bot solution does the site run? Is there a cleaner source of data than the rendered page? And are we allowed to scrape it at all?

I go through the checks I run on a new target. First I identify the stack and the known anti-bot software, using a browser extension and cross-checking it with a Discord bot built by the Puppeteer team. Then I look for the API behind the site, using the browser's developer tools and the network tab, on an e-commerce catalog as the example. If the API calls can't be replicated, I look for JSON embedded in the HTML. I compare each option on reliability, resistance to site changes and efficiency. The last step is the legal one: privacy and copyright, which I consider the most important.

## What's inside

- Two tools for the same job, Wappalyzer and the Discord bot, and which one I trust when their results diverge.
- The pagination trick for spotting an API: move from page one to page two of a catalog and watch the network tab.
- Why an API found in the network tab is not a guarantee, since it can sit behind anti-bot protection too.
- The trade-off of JSON inside the HTML: it holds up against site changes, but you load the whole page.

**In the full article:** Screenshots of the Wappalyzer and Discord bot output, the network tab example with the JSON response for page 2 of a catalog, and the embedded pagination JSON in the HTML.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/3-things-1-to-do-before-starting?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
