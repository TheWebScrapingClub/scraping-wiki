---
type: article_summary
title: 'The Lab #36: Bypassing Cloudflare with anti-detect browsers'
slug: bypassing-cloudflare-gologin-playwrigh
canonical_url: https://www.scraping.club/p/bypassing-cloudflare-gologin-playwrigh
publish_date: '2024-01-11'
visibility: premium
topics:
- cloudflare
- anti-detect-browsers
- browser-fingerprinting
- scraping-infra
description: Using GoLogin anti-detect browser profiles with Playwright to get past Cloudflare Turnstile on indeed.com and harrods.com, one fingerprint layer at a time.
source_hash: 8662db4d29223d46
---

# The Lab #36: Bypassing Cloudflare with anti-detect browsers

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-01-11 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-cloudflare-gologin-playwrigh?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare Bot Protection relies on device fingerprinting to spot bots. You often see it as a scraper that runs fine on your laptop and gets blocked once it is deployed on a data center machine. Before touching the fingerprint, you need to know it is the real cause, because a untrusted server IP produces the same symptom and costs less to fix.

This Lab covers GoLogin only. I meant to compare several anti-detect browsers, but time ran short, so that comparison comes later. We took a baseline Playwright scraper for indeed.com, blocked by Cloudflare Turnstile on an AWS machine even with the same residential IP provider that works locally. We connected it over CDP to GoLogin profiles built with increasing layers of masking, then repeated the test on harrods.com, where the Cloudflare rules are stricter. We started with an unmasked Linux profile and then added noise to Audio Context and Client Rects.

## What's inside

- A two-step check with residential proxies, run locally and in production, to tell an IP reputation block from a device fingerprint block.
- GoLogin profiles can be created from the desktop app or via API, and the desktop app seems to offer more fine-tuning options.
- The same anti-bot gives different results on different sites, because each website owner sets their own rules and red flags.
- What Client Rects and Audio Context fingerprints measure, and why masking them was tested as a separate layer.

**In the full article:** The Playwright and GoLogin code from the GitHub repository for paying subscribers, the profile settings screenshots, and the result of each profile against indeed.com and harrods.com.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-cloudflare-gologin-playwrigh?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
