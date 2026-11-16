---
type: article_summary
title: 'Web Scraping from 0 to hero: Our first scraper with Selenium'
slug: selenium-first-scraper
canonical_url: https://www.scraping.club/p/selenium-first-scraper
publish_date: '2024-03-17'
visibility: free
topics:
- browser-automation
- anti-detect-browsers
- industry-overview
description: Writing a first Selenium scraper in Python on quotes.toscrape.com, with XPath compared to CSS selectors, exception handling and pagination.
source_hash: cc6637cac7ba6b0e
---

# Web Scraping from 0 to hero: Our first scraper with Selenium

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-17 (free to read). **[Read the full article](https://www.scraping.club/p/selenium-first-scraper?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

After introducing Selenium in the last episode, this one gets to the first working scraper. A browser automation tool is only useful once you can point it at a page, pick the right elements and survive when the page does not behave. That is what separates a demo from something you can leave running.

We build the scraper on quotes.toscrape.com, a site made for practice. We set up the environment (Python, the selenium package, a WebDriver for your browser), open the site and select the quotes with XPath. Then we compare XPath and CSS selectors side by side on attributes, text matching, logical operators, parent and sibling navigation, wildcards and combined selectors, noting where CSS stops. We cover the two exceptions you will meet most often, NoSuchElementException and TimeoutException, and how to handle them with explicit waits and try-except blocks. Everything ends in a final scraper that walks through the pages.

## What's inside

- Why find_elements and find_element behave differently: one returns a list to iterate, the other a single item used for navigation.
- Where CSS selectors fall short of XPath: matching on text, logical operators and reaching a parent or previous sibling.
- Four rules for exception handling: catch specific exceptions, log the error, decide a recovery strategy, and set reasonable timeouts.
- How the final scraper decides when to stop paginating and when to give up after repeated timeouts.

**In the full article:** The full code for each step, the XPath and CSS selector examples side by side, the try-except block with WebDriverWait, and the final pagination scraper with its retry logic.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/selenium-first-scraper?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
