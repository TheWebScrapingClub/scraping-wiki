---
type: article_summary
title: Are CAPTCHAs still a thing?
slug: are-captchas-still-a-thing
canonical_url: https://www.scraping.club/p/are-captchas-still-a-thing
publish_date: '2023-08-27'
visibility: free
topics:
- captcha
- cloudflare
- scraping-infra
- datadome
description: A look at CAPTCHA history from text to reCAPTCHA v3, how far AI solvers have come, and a test of Nopecha's extension and Python package.
source_hash: 5f4c32b6d754bd8b
---

# Are CAPTCHAs still a thing?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-27 (free to read). **[Read the full article](https://www.scraping.club/p/are-captchas-still-a-thing?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A recent paper claims AI bots now solve CAPTCHAs with accuracy up to 15% higher than humans. That caught my eye, because almost half of web traffic is bots and CAPTCHAs were built to tell them apart from people. If the test no longer works, it changes how we think about scraping targets that still rely on it. Many do: BuiltWith shows a good share of the top million sites still use one.

I first go through the history, from the 2000 text CAPTCHAs to reCAPTCHA v1, v2 and v3, plus the alternatives that came later. Then I look at why CAPTCHAs matter less for scraping today, with dedicated anti-bot vendors and human click-farms in the picture. For the practical part, I picked the cheapest AI solver I found, Nopecha, and tested its browser extension with Playwright and its Python package inside a Scrapy project, both against reCAPTCHA.

## What's inside

- Why the first text CAPTCHAs wasted human work, and how reCAPTCHA v1 reused it for book digitization at Google Books.
- How reCAPTCHA v2 and v3 moved from reading text to behavioral models and device fingerprints.
- Why I have never used human click-farm services: working conditions, and solving times that don't fit scraping.
- Where my tests hit limits: one case I could not get working, and a loop in the extension on one type of challenge.

**In the full article:** The Scrapy spider and Playwright setup for Nopecha, the link to the free GitHub repository, the plan pricing, the test notes per reCAPTCHA version, and the list of CAPTCHAs Nopecha supports.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/are-captchas-still-a-thing?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
