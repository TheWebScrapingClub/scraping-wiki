---
type: article_summary
title: Testing the new Botasaurus 4
slug: testing-the-new-botasaurus-4
canonical_url: https://www.scraping.club/p/testing-the-new-botasaurus-4
publish_date: '2024-06-30'
visibility: free
topics:
- browser-automation
- cloudflare
- datadome
- captcha
description: Botasaurus 4 tested against Cloudflare, Datadome and Kasada, locally and on a server with residential proxies, plus a check of the browser fingerprint.
source_hash: 8a4febb79bdaf6fb
---

# Testing the new Botasaurus 4

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-30 (free to read). **[Read the full article](https://www.scraping.club/p/testing-the-new-botasaurus-4?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Botasaurus is an open-source framework for scraping and browser automation. I wrote about it two years ago, and the developers recently told me about version 4. Its pitch is stealth, so I wanted to see whether it gets past the main anti-bot solutions, and whether that holds outside a developer's own machine.

We built a small scraper on the @browser decorator, which opens a Playwright session. We pointed it at Harrods.com behind Cloudflare, footlocker.it behind Datadome and canadagoose.com behind Kasada. Each run loads the homepage, moves to a product list page, scrolls and parses the HTML with soupify. We ran it locally first, then on a server with residential proxies, and checked the machine with Antoine Vastel's fingerprint viewer. I also sum up the framework's main features.

## What's inside

- How the framework is organized: the @browser, @request and @task decorators, the debugging utilities and scaling with Kubernetes.
- How the scraper walks from the homepage to a product list page, scrolls to load all the items and extracts product names with CSS selectors.
- Why we compared a run on a consumer-grade device with a run on a server, and what the fingerprint viewer is used to check.
- A mention of the built-in option to create a UX for your scrapers, useful when you share them with non-technical people.

**In the full article:** Scraper code for the Cloudflare and Datadome tests, the screenshots and results for each anti-bot in both environments, the fingerprint viewer output and the link to the Botasaurus4 folder on our GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/testing-the-new-botasaurus-4?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
