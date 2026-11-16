---
type: article_summary
title: Behind the scenes of anti-detect browsers
slug: kameleo-anti-detect-browser
canonical_url: https://www.scraping.club/p/kameleo-anti-detect-browser
publish_date: '2024-03-05'
visibility: free
topics:
- anti-detect-browsers
- browser-automation
- antibot
- cloudflare
description: What an anti-detect browser is, how it keeps a consistent device fingerprint, and why Playwright and Puppeteer Stealth fall short, with Kameleo's CEO.
source_hash: 7c70f6754dc9ee6a
---

# Behind the scenes of anti-detect browsers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-05 (free to read). **[Read the full article](https://www.scraping.club/p/kameleo-anti-detect-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Rotating IPs or using a privacy browser does not hide who you are. Websites read a device fingerprint: operating system, location, plugins and other values. If those values change between sessions or contradict each other, anti-bot systems notice. That matters for scraping sites behind Cloudflare, and for anyone running many accounts that must look like different real users.

I asked Tamas, CEO of Kameleo, to explain what an anti-detect browser does under the hood. We cover how these tools conceal and keep a fingerprint stable across sessions, and why Playwright, built for testing, and add-ons like Puppeteer Stealth struggle against major anti-bot systems. We then go through what a vendor has to maintain: custom-built browsers, constant updates, cloud-reusable profiles, support, and a local API for Selenium, Puppeteer and Playwright. We also look at the planned scraping-only package, where you pay mostly for the browser and skip profile reuse and the GUI.

## What's inside

- Why a consistent fingerprint is more than a mask: the values have to hold up under deeper inspection, which regular tools do not manage.
- What "built-in browser" means: the vendor modifies the native C++ code and ships its own builds, such as Junglefox and Chroma in Kameleo.
- Why maintenance never ends: Chrome updates every 4 weeks and the vendor has to track new fingerprinting research.
- Which scraping jobs need profile reuse, like marketplaces with logins and browser history, and which can do without it.

**In the full article:** Details of the planned scraping-only package, the platform availability notes, and the full list of vendor responsibilities Tamas describes.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/kameleo-anti-detect-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
