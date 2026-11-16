---
type: article_summary
title: 'THE LAB #98: Scraping Google Search Results in 2026: Device, Location, and Identity'
slug: scraping-serp-google-search
canonical_url: https://www.scraping.club/p/scraping-serp-google-search
publish_date: '2026-02-19'
visibility: premium
topics:
- anti-detect-browsers
- serp-scraping
- scraping-infra
- browser-automation
description: How location, device type and login state change Google SERPs in 2026, and how we control them with Kameleo, Playwright and proxies against SearchGuard.
source_hash: b27785a785f92517
---

# THE LAB #98: Scraping Google Search Results in 2026: Device, Location, and Identity

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-02-19 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-serp-google-search?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A Google SERP is never the page. It is a version of the page, shaped by location, device type, login state and keyword. A datacenter IP in Virginia with desktop Chrome, logged out, gets one result set. A logged-in mobile session in Milan gets another. Both are correct, neither is complete. Since January 2025 there is also SearchGuard, which sends JavaScript challenges to unrecognized sources and has pushed up costs for SEO tools and anyone scraping Google.

We built a test setup to see how much each variable changes the output and how to control it. It uses Playwright with Kameleo, an anti-detect browser with persistent profiles, running on a Windows EC2 instance in the US and driven remotely from Python. The first test runs the query "weather" from that instance with no proxy, a residential proxy in Italy and a datacenter proxy also claiming to be in Italy. I'm sure you'll be surprised by what we found.

## What's inside

- Why a plain HTTP client like requests or httpx cannot pass SearchGuard, and why a stock automated Chrome or Firefox is not enough either
- Why persistent profiles matter: staying logged into a Google account across sessions without re-authenticating on every run
- How mobile and desktop SERPs differ in structure, not only in layout, and how keywords like "trousers" and "aspirin" change the page layout
- How the Kameleo remote setup works: REST API on port 5050, Chroma and Junglefox profiles, and a local script driving the browser on AWS

**In the full article:** The Python code for the Kameleo setup and the location test, the output Google returned for each of the three proxy configurations, and the exit IP checks.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-serp-google-search?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
