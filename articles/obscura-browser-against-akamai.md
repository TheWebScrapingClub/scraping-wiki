---
type: article_summary
title: 'THE LAB #113: Obscura browser against Akamai'
slug: obscura-browser-against-akamai
canonical_url: https://www.scraping.club/p/obscura-browser-against-akamai
publish_date: '2026-08-20'
visibility: premium
topics:
- akamai
- http-clients
- browser-automation
- anti-detect-browsers
description: A hands-on test of the Rust-built Obscura browser against Akamai Bot Manager on Radisson, minting sessions that curl_cffi reuses to track hotel rates.
source_hash: 843920e38c98f735
---

# THE LAB #113: Obscura browser against Akamai

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-08-20 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/obscura-browser-against-akamai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Obscura is a browser engine written from scratch in Rust, with V8 embedded, no Chromium, no Node.js, and a claimed footprint of about 30 MB of RAM. It did well in the controlled fingerprint probe in THE LAB #111, but a lab score is not a real anti-bot. So we pointed it at Radisson, whose availability API returns every room rate for a hotel and date range and sits behind Akamai Bot Manager. The job: track nightly prices for a Munich hotel around Oktoberfest 2026.

We modeled the target first: TLS tier, Akamai sensor cookies, sec-cpt behavioral challenge. We drove Obscura with Playwright over CDP in its stealth mode to mint the session, and curl_cffi replayed it, the hybrid from THE LAB #100 that used Camoufox. We re-ran the fingerprint bench and the public test suites, and used CloakBrowser and Camoufox as controls to tell a tool problem from a proxy problem.

## What's inside

- Radisson is protected in three tiers, and only some of them need a browser. We map which tier curl_cffi covers alone and which one needs the Akamai sensor to run.
- Which public fingerprint suites Obscura completes and which it stalls on, and why that matters when the target's sensor is a heavy script.
- How the session minting loop works, including what makes a harvested cookie jar valid and why a retry is part of the design.
- What changes when the API is called from inside the browser page instead of replayed externally, and how to read the status code that comes back.

**In the full article:** The session.py code and the Munich rate scanner from the 113.Obscura folder, the full fingerprint scores, the per-suite results, and the proxy comparison across the three browsers.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/obscura-browser-against-akamai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
