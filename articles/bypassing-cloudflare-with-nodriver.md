---
type: article_summary
title: 'THE LAB #62: Bypassing Cloudflare with Nodriver'
slug: bypassing-cloudflare-with-nodriver
canonical_url: https://www.scraping.club/p/bypassing-cloudflare-with-nodriver
publish_date: '2024-09-26'
visibility: premium
topics:
- browser-automation
- cloudflare
- antibot
- proxies
description: 'Testing nodriver against Cloudflare on Harrods: how it compares with Playwright on CDP detection, and what it lacks for datacenter scraping.'
source_hash: a01606d360164b54
---

# THE LAB #62: Bypassing Cloudflare with Nodriver

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-09-26 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-cloudflare-with-nodriver?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Nodriver is an open-source tool that drives Chromium without a webdriver. The pitch is speed and a smaller detection surface. The questions that matter in practice are whether that is enough against Cloudflare, and where the tool stops being useful. It does not forge fingerprints, it struggles with authenticated proxies, and it has no human behavior simulation.

We ran a standard Playwright scraper on Chrome with a persistent context through the bot detection tests on deviceandbrowserinfo.com, then ran nodriver through the same tests. After that I wrote a minimal nodriver scraper for Harrods, which is protected by Cloudflare, and ran it from an AWS instance and from my laptop. Then we looked at how to pull the product JSON from a category page. I compared the results with Playwright plus BrowserForge and with anti-detect browsers, and I give my verdict on where nodriver fits.

## What's inside

- Which feature gaps matter: no fingerprint forging, no authenticated proxy support because of Chromium limits, no human behavior packages like ghost-cursor.
- Why adding a proxy would not have helped the nodriver scraper on a server, since the device fingerprint still exposes the underlying hardware.
- Whether Playwright running locally gets into Harrods too, and why the CDP check is probably not what Cloudflare relies on there.
- How the product data is extracted from the category page once the block is cleared.

**In the full article:** The scripts for the Playwright and nodriver tests and the Harrods scraper, the screenshots of each run from AWS and from the laptop, and the product JSON extraction code.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-cloudflare-with-nodriver?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
