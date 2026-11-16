---
type: article_summary
title: 'THE LAB #65: Scraping Datadome protected websites with Camoufox'
slug: scraping-datadome-camoufox
canonical_url: https://www.scraping.club/p/scraping-datadome-camoufox
publish_date: '2024-10-24'
visibility: premium
topics:
- anti-detect-browsers
- browser-automation
- datadome
- antibot
description: Camoufox, an open-source Firefox-based browser with fingerprint spoofing and human-like mouse movement, tested on Datadome-protected Hermes.com.
source_hash: df782f91a895d19e
---

# THE LAB #65: Scraping Datadome protected websites with Camoufox

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-10-24 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-datadome-camoufox?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

When a website runs Datadome, the browser we scrape with has to do four things: spoof and rotate fingerprints, move the mouse like a person, run headless or remotely, and survive CDP detection tests. Traditional anti-detect browsers cover fingerprints and headless mode, but rarely ship a human-like mouse movement library. Hermes.com is heavily protected, so it is a fair test.

We tested Camoufox, the open-source package maintained by Daijiro, who also wrote hRequests and BrowserForge. We compared the fingerprint BrowserScan reads on my Mac Studio with the one Camoufox produces, and ran CreepJS to check the stealth patches. I also asked Daijiro how Camoufox hides Playwright from the page and what Juggler does. Then we built a Python scraper with humanize, proxy, headless and GeoIP options and pointed it at Hermes. Camoufox is still a work in progress, so I would not put it in production yet.

## What's inside

- Daijiro's own explanation of why Playwright's injected JavaScript stays invisible to the page: those actions run in an isolated scope outside it.
- Camoufox embeds BrowserForge for fingerprint forging, a project that will soon be deprecated, and I link our earlier Lab on fingerprint injection in Playwright.
- The virtual value of the headless option, which runs the browser on Linux through xvfb when standard headless mode gets detected.
- What the GeoIP option aligns with the proxy IP: browser timezone and WebRTC IP, so no source IP leaks.

**In the full article:** The Hermes scraper code, the test results on Hermes, the full Camoufox and proxy configuration, and the BrowserScan and CreepJS screenshots with the numbers behind them.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-datadome-camoufox?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
