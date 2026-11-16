---
type: article_summary
title: Browser fingerprinting and web scraping
slug: scraper-fingerprints-and-proxies
canonical_url: https://www.scraping.club/p/scraper-fingerprints-and-proxies
publish_date: '2023-07-09'
visibility: free
topics:
- cloudflare
- browser-fingerprinting
- browser-automation
- anti-detect-browsers
description: How browser fingerprinting works, why anti-bot systems rely on it to tell scrapers from humans, and the main ways scrapers can alter their fingerprint.
source_hash: bcc23af6b70ff597
---

# Browser fingerprinting and web scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-07-09 (free to read). **[Read the full article](https://www.scraping.club/p/scraper-fingerprints-and-proxies?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anti-bot software uses fingerprinting to read the hardware and software setup behind a request and compare it with a list of human-like configurations. Scrapers built with Scrapy or similar tools already fail the first challenges. Against more advanced bots, a plausible fingerprint is what lets a scraper keep going.

I cover why fingerprinting matters for scraping and why it raises privacy concerns similar to the ones cookies raised. Fingerprints are built to track devices and generate a unique id, whatever the IP. I then show a Cloudflare example on harrods.com, comparing a browser on a personal computer with one on a cloud virtual machine, and what a Smartproxy residential proxy changed in that setup. The last part lists the families of solutions for altering a fingerprint: scraping APIs, anti-detect browsers and AI-powered browsers. I also link a few resources for going deeper, including CreepJS and FingerprintJS.

## What's inside

- Why IP data has little weight in a fingerprint, and how that differs from how anti-bot systems combine IP and browser signals
- The Battery API study, used to show how fine-grained a fingerprint can get
- What the harrods.com test on a cloud virtual machine says about the weight of IP-related data versus the hardware environment
- Three ways to alter a fingerprint: scraping APIs, anti-detect browsers and AI-powered browsers

**In the full article:** The screenshots of the Cloudflare challenge on harrods.com, the links to the CreepJS and FingerprintJS repositories and the research papers, and the references to the tools for altering fingerprints.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraper-fingerprints-and-proxies?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
