---
type: article_summary
title: Scraping Cloudflare Protected Websites (early 2023 version)
slug: scraping-cloudflare-websites-2023-q1-update
canonical_url: https://www.scraping.club/p/scraping-cloudflare-websites-2023-q1-update
publish_date: '2023-03-16'
visibility: premium
topics:
- cloudflare
- browser-automation
- scraping-infra
- antibot
description: An early 2023 update on scraping Cloudflare-protected sites, tested on Harrods at its highest anti-bot level, from a local machine and from an AWS VM.
source_hash: 84fd0f09d44433bd
---

# Scraping Cloudflare Protected Websites (early 2023 version)

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-03-16 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-cloudflare-websites-2023-q1-update?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare rules are customized per site, so a scraper that works on one website can fail on another. For this update of my old Cloudflare post I picked Harrods, which recently moved its anti-bot settings to the highest level. On an AWS VM you can't even browse it. That matters if your goal, like mine, is to run a large number of scrapers in an automatic and cheap way.

We kept the format of the Kasada post, with one change: every tool runs twice, on a local environment and on a remote VM on AWS. The free side covers Playwright with Chrome, Playwright with Firefox, Undetected Chromedriver and Pyppeteer. I also tried GCP and proxies from both clouds. Then we move to commercial solutions, starting with Playwright and GoLogin. I also give a short primer on how Cloudflare and its Bot Management work.

## What's inside

- The four Bot Management features worth knowing: advanced bot detection, customizable rules, real-time analytics and integration with WAF and rate limiting.
- Why per-site rule customization makes a single test target a weak benchmark, and why I chose one of the toughest.
- Why home computers are not an option for large-scale projects, and how that ties to my earlier post on the rising cost of web scraping.
- How the commercial section builds on the same Playwright setup used in the Kasada post.

**In the full article:** Code screenshots for each tool, the local versus AWS result of every test, and the commercial solutions section starting with the GoLogin test.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-cloudflare-websites-2023-q1-update?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
