---
type: article_summary
title: The latest papers in 2023 about browser fingerprinting
slug: the-latest-papers-about-browser-fingerpinting
canonical_url: https://www.scraping.club/p/the-latest-papers-about-browser-fingerpinting
publish_date: '2024-02-11'
visibility: free
topics:
- browser-fingerprinting
- datadome
- browser-automation
description: A walkthrough of recent browser fingerprinting papers, from Datadome's use of Google's Picasso to WebGPU attacks, and what they mean for web scraping.
source_hash: 724accb8306e4b84
---

# The latest papers in 2023 about browser fingerprinting

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-11 (free to read). **[Read the full article](https://www.scraping.club/p/the-latest-papers-about-browser-fingerpinting?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Datadome recently described how it uses Picasso, Google's canvas fingerprinting tool, in its anti-bot solution. Picasso draws an HTML5 canvas, infers the device and browser settings, and compares them with what the client declares. A mismatch gets the traffic labeled as suspect and blocked. The topic reaches well beyond scraping, and it made me want to see what researchers had published lately.

So I went through the newest browser fingerprinting papers on ArXiv and elsewhere, and I report on three of them. One is a general overview of fingerprinting and the privacy concerns around it. One is adF, which measured passive fingerprinting through ads. One is WebGPU-SPY, on GPU-based techniques, which I tie to the earlier DRAWNAPART paper. For each, I pull out what matters for people running scrapers, including my own experience with Chrome and Brave in Playwright, and where I find the privacy implications worrying.

## What's inside

- Why fingerprinting exists as an alternative to cookies, and why users have fewer ways to opt out of it than of cookies
- What adF's measurements on desktop versus mobile devices suggest for choosing which device to impersonate when scraping
- How Chrome compares with Safari, Firefox and Brave in the details it exposes, and what I saw in my own Playwright scrapers
- Why GPU-based fingerprinting could be a problem for scrapers running on servers, where a GPU is often missing

**In the full article:** The links to each paper, the adF list of browser attributes used for fingerprinting, the WebGPU-SPY and DRAWNAPART details, and my notes on each for scraping projects.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-latest-papers-about-browser-fingerpinting?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
