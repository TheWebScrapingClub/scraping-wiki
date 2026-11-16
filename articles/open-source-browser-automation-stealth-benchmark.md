---
type: article_summary
title: 'THE LAB #111: The OSS browser automation stealth benchmark'
slug: open-source-browser-automation-stealth-benchmark
canonical_url: https://www.scraping.club/p/open-source-browser-automation-stealth-benchmark
publish_date: '2026-07-23'
visibility: premium
topics:
- browser-automation
- anti-detect-browsers
- scraping-infra
- cloudflare
description: A benchmark of fifteen open source Python browser automation tools, scored on the JavaScript fingerprint tells a bot detector checks in headless mode.
source_hash: c80e3c6def564d98
---

# THE LAB #111: The OSS browser automation stealth benchmark

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-07-23 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/open-source-browser-automation-stealth-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Every few months a new "undetectable" browser automation library shows up on GitHub. The README always promises the same things: no navigator.webdriver, patched fingerprints, Cloudflare bypasses. Those claims are easy to make and hard to verify. Choose the wrong tool and your scraper keeps running and pages keep loading, but the data slowly turns into soft-blocked junk that looks fine until you check it.

We took fifteen open source Python tools and scored them the same way: plain Playwright and Selenium as baselines, Playwright patches like patchright, CDP-native drivers like nodriver and zendriver, and rebuilt browsers like camoufox, CloakBrowser and RayoBrowse. Each tool loads one probe page that reads the JavaScript fingerprint surface in headless mode, and we cross-check the score against BrowserScan and deviceandbrowserinfo. Transport, timing and proxy reputation stay out on purpose.

## What's inside

- Why we scoped the test to the JavaScript fingerprint surface only, and why TLS and HTTP/2, request timing and proxy exit don't depend on which Python library you pick.
- The list of tells the probe looks for, from the HeadlessChrome user agent and software WebGL renderers to leftover automation globals and Client Hints that disagree with the OS.
- Why every Chrome-based tool drives the real installed Chrome instead of Playwright's bundled Chromium, and why we ran everything headless.
- How we calibrated our 0 to 100 probe score against an outside referee, and why we keep a screenshot of each verdict on record.

**In the full article:** The probe page, the render adapters that wrap all fifteen tools, the results table and heatmap, the per-tool scores and the GitHub folder with the full harness you can run yourself.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/open-source-browser-automation-stealth-benchmark?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
