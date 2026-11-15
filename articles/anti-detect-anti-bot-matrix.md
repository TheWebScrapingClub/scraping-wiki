---
type: article_summary
title: 'THE LAB #11: The Anti-Detect Anti-Bot matrix'
slug: anti-detect-anti-bot-matrix
canonical_url: https://www.scraping.club/p/anti-detect-anti-bot-matrix
publish_date: '2023-02-02'
visibility: premium
topics:
- browser-automation
- captcha
- cloudflare
- datadome
description: A page-load test of Undetected Chromedriver, Playwright and Pyppeteer with stealth against Cloudflare, PerimeterX, Datadome, Kasada and F5, one site each.
source_hash: f45f1c01c4cc210e
---

# THE LAB #11: The Anti-Detect Anti-Bot matrix

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-02 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/anti-detect-anti-bot-matrix?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scraping keeps getting more complex. Anti-bot software asks for more computing and memory, and the infrastructure gets harder to manage too. There is no silver bullet, so a modern scraper needs a full array of tools, each suited to a different case. The practical question is which one to reach for first when you meet a given anti-bot.

In this episode of The Lab I compare the headful browser tools I use daily as a Python developer: Undetected Chromedriver, Playwright in different sauces, and Pyppeteer with its stealth module. I explain why Selenium, Puppeteer and Cheerio are not in the test. We ran a generic page load on five websites, one each for Cloudflare, PerimeterX, Datadome, Kasada and F5, and put the outcomes in a matrix. One page per site is not an exhaustive test, so I also say what it can and cannot tell you.

## What's inside

- Why Selenium is left out: standard webdrivers were not built for scraping and are easy to detect, and Puppeteer and Cheerio are outside a Python toolset.
- How Playwright can be extended with other clients, such as Chrome instead of the bundled Chromium or an anti-detect browser like GoLogin.
- How each anti-bot works, from Cloudflare's signature and machine learning detection to Kasada's 429 challenge and its zero-trust policy.
- Why a single page load is only a starting point: it cannot show how a full spider behaves, and login pages often have stricter rules than the home page.

**In the full article:** The Anti Detect Anti Bot Matrix with the result for each tool against each anti-bot, plus my comments on the results and the choice of tool.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/anti-detect-anti-bot-matrix?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
