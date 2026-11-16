---
type: article_summary
title: Making Playwright scrapers undetected with open source solutions
slug: playwright-scrapers-undetected
canonical_url: https://www.scraping.club/p/playwright-scrapers-undetected
publish_date: '2024-12-01'
visibility: free
topics:
- browser-automation
- anti-detect-browsers
- human-behavior-emulation
- datadome
description: 'Open source tools to make Playwright scrapers harder to detect: mouse movement libraries, Browserforge, Camoufox and the patched client Patchwright.'
source_hash: e5ed26e0057a7d5d
---

# Making Playwright scrapers undetected with open source solutions

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-01 (free to read). **[Read the full article](https://www.scraping.club/p/playwright-scrapers-undetected?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A few arguments in Playwright's instance remove the most common red flags of browser automation, but anti-bot vendors know those tricks. They analyze the browser fingerprint, the mouse movements and other configuration details that point to a bot. Demand for web data keeps growing, so commercial unblockers and super APIs multiply, and the open source community is just as active.

I list the open source libraries we can plug into Playwright to cover these detection layers. For mouse movements, we have python-ghost-cursor and Oxymouse, which we rarely need unless the target is protected by Datadome. For fingerprint spoofing, I describe what anti-detect browsers like Kameleo, NSTbrowser and GoLogin do, then point to Browserforge and Camoufox as open source alternatives. For a ready-made fix, there is Patchwright, a patched Playwright client. Some of these tools we already covered, others will follow in the coming weeks.

## What's inside

- Which fingerprint signals anti-bots check: WebGL renderer, audio and video devices, and timezone consistency with the IP.
- How anti-detect browsers build a plausible consumer-device identity instead of a server one, and why they are mostly commercial.
- How Browserforge ended up inside Camoufox, which also adds human-like mouse movement and patches for well-known anti-bot challenges.
- What Patchwright changes in Playwright by default, including the CDP leak used to detect automation.

**In the full article:** Repository links for each tool, references to our earlier Lab articles on mouse movements, Oxymouse and Camoufox with Datadome, and the full list of fixes Patchwright applies.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/playwright-scrapers-undetected?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
