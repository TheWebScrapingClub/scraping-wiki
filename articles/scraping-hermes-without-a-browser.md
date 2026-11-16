---
type: article_summary
title: 'Scraping Hermès Without a Browser: Hitting the JSON API Behind DataDome'
slug: scraping-hermes-without-a-browser
canonical_url: https://www.scraping.club/p/scraping-hermes-without-a-browser
publish_date: '2026-08-25'
visibility: free
topics:
- datadome
- antibot
- tls-fingerprinting
- proxies
description: A request-based scraper for hermes.com that skips the browser, gets past DataDome and reads the bck.hermes.com JSON API directly.
source_hash: 029243b90b2c0aba
---

# Scraping Hermès Without a Browser: Hitting the JSON API Behind DataDome

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-08-25 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-hermes-without-a-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

hermes.com sits behind DataDome, and a headless browser there pulls the whole product page every time: HTML, scripts, fonts, images, every XHR, all through residential proxies. The catch is that the page is only a wrapper. The frontend gets its product data from a JSON API on bck.hermes.com. Coming from sneakerbotting, we know that a request-based bot lives or dies on three signals: TLS fingerprint, header order and a valid antibot token.

We built a Go scraper around bogdanfinn/tls-client and fhttp, with the Hyper Solutions API minting the DataDome sensor data. It warms a session once, then calls the API directly and reuses the session. We found the catalog through the category tree, ran the whole US catalog on 8 concurrent sessions, and measured bandwidth and sensor calls per product. Then we priced it against buying a ready-made dataset, and projected it across markets.

## What's inside

- Why header order has to match a real browser capture per host: the API calls and the DataDome captcha-delivery endpoints use different HTTP versions and header casing.
- How the session is warmed: the DataDome challenge types handled, the tag posts, and the call that mints the XSRF token the API expects.
- Why the category tree beats the sitemap for discovery, and how far the sitemap overstates the real catalog.
- Which part of the cost is metered, and where buying the dataset still makes sense.

**In the full article:** The Go header block with explicit ordering, the session bootstrap diagram, the measured run metrics for the US catalog, per-market catalog sizes, the build versus buy cost figures and the repo commands.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-hermes-without-a-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
