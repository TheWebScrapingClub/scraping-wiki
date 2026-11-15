---
type: article_summary
title: 'THE LAB #95: Bypassing Cloudflare in 2026'
slug: bypassing-cloudflare-in-2026
canonical_url: https://www.scraping.club/p/bypassing-cloudflare-in-2026
publish_date: '2026-01-22'
visibility: premium
topics:
- cloudflare
- anti-detect-browsers
- browser-automation
- tls-fingerprinting
description: Test of Camoufox, Pydoll and undetected-chromedriver against two Cloudflare-protected sites, Harrods.com and Indeed.com, aimed at the JavaScript detection and c
source_hash: 0b2b880404f6ffa8
---

# THE LAB #95: Bypassing Cloudflare in 2026

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-01-22 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-cloudflare-in-2026?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare is the most common anti-bot measure on the market, and it keeps changing. What worked in 2025 may fail in 2026. Picking the wrong tool or the wrong technique costs development time and blocked pipelines, so operations get more expensive. There is no silver bullet.

We tested three open-source browser automation tools: Camoufox, Pydoll and undetected-chromedriver. The targets were two production sites with active Cloudflare protection, Harrods.com and Indeed.com. We split Cloudflare into five detection layers and focused on JavaScript detections and the JavaScript challenge, with clean residential IPs assumed. Indeed returns 403 even on the sitemap, so we had to build URLs differently from Harrods. To judge a load we check for site-specific page elements instead of generic "just a moment" strings, which gave us false positives. We then set up each tool and began with Camoufox on Indeed, where Turnstile showed specific behavior.

## What's inside

- How we model Cloudflare in five layers: TLS and network fingerprinting, JavaScript detections, the JavaScript challenge, behavioral analysis and ML bot scoring.
- Why string matching on Cloudflare block pages produces false positives, and which page elements we check instead on each site.
- How we collected URLs when Indeed blocked the sitemap but Harrods exposed it.
- Pydoll's documentation did not match the installed version, so we had to find the working API by testing.

**In the full article:** The full code for the test framework and the three scrapers, the per-tool results on Harrods and Indeed, and the Turnstile behavior we observed on Indeed with Camoufox.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-cloudflare-in-2026?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
