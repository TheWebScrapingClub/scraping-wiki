---
type: article_summary
title: 'The Lab #46: Fingerprint injection in Playwright'
slug: fingerprint-injection-playwright
canonical_url: https://www.scraping.club/p/fingerprint-injection-playwright
publish_date: '2024-03-28'
visibility: premium
topics:
- anti-detect-browsers
- browser-automation
- cloudflare
- browser-fingerprinting
description: Testing Browserforge fingerprint injection with Playwright against Cloudflare, Datadome and PerimeterX, and comparing it with a Kameleo anti-detect profile.
source_hash: c418676b2d3148ae
---

# The Lab #46: Fingerprint injection in Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-28 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/fingerprint-injection-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Browser fingerprinting is the one challenge I usually hand to commercial tools, like unblockers or anti-detect browsers. A scraper running from a datacenter leaks plenty of signals: a WebRTC address, a timezone that doesn't match the IP, a software renderer typical of servers without a GPU. Proxies alone don't fix any of that. I wanted to know how much of the job an open source Python tool can do before paying for a commercial one.

We tested Browserforge, a Python reimplementation of Apify's fingerprint suite, together with Playwright. From an AWS server in Berlin, with residential proxies, we loaded a BrowserScan check and then pages on Harrods (Cloudflare), Footlocker (Datadome) and StockX (PerimeterX). We ran several configurations, from default Chromium to injected fingerprints in different browsers, and compared them with a Kameleo profile.

## What's inside

- Why I follow a Buy AND Make approach to anti-bot challenges, and why I leave browser fingerprinting to commercial tools when a site relies on it heavily.
- What happens when the browser engine and the injected fingerprint don't match, for example Chromium carrying a Firefox on Windows fingerprint.
- How the system timezone and the proxy country have to line up with the fingerprint, and what we changed on the Berlin server.
- Where Browserforge falls short of an anti-detect browser: the browser version can't be chosen, and WebRTC can't be switched off programmatically in traditional browsers.

**In the full article:** Code for every run from The Lab repository (folder 46), the BrowserScan screenshots for each configuration, the Kameleo comparison and the results against Cloudflare, Datadome and PerimeterX.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/fingerprint-injection-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
