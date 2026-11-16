---
type: article_summary
title: 'The LAB #116: Warming an Imperva reese84 cookie, and replaying it without a browser'
slug: the-lab-116-warming-an-imperva-reese84
canonical_url: https://www.scraping.club/p/the-lab-116-warming-an-imperva-reese84
publish_date: '2026-09-24'
visibility: premium
topics:
- http-clients
- captcha
- residential-proxies
- datadome
description: 'A case study on Imperva''s reese84 on smythstoys.com: warming a cookie with a browser and a CAPTCHA solver, then replaying it over plain HTTP without a browser.'
source_hash: de06006bc627ea00
---

# The LAB #116: Warming an Imperva reese84 cookie, and replaying it without a browser

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-09-24 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-116-warming-an-imperva-reese84?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Imperva is an anti-bot I have rarely covered. Smythstoys.com, the Irish site of Smyths Toys, is my target. The product pages are server-rendered HTML, and the one internal endpoint that returns stock is protected too. Someone on r/webscraping proposed one hot cookie per proxy, forged in a browser and replayed over cheap datacenter IPs. I wanted to check whether that works, how long the cookie lasts and when it breaks.

I worked two ways at once. My bypass warms a session with Scrapling, solves the GeeTest CAPTCHA with CapSolver and replays the cookie jar with curl_cffi, no browser. In parallel I ran Manus on the same site, with an instrumented headless Chromium, to read the sensor, token and renewal protocol from the inside. I varied IPs, TLS fingerprints and User-Agents on the replay.

## What's inside

- The protection has five pieces: the edge WAF interstitial, the short-lived ___utmvc cookie, the reese84 sensor, the token exchange and the GeeTest fallback.
- Manus did not vary IP, User-Agent or TLS fingerprint and did not solve a CAPTCHA, so those tests are mine. Where I quote a Manus figure, I say so.
- The warming step depends on a GeeTest challenge inside the interstitial frame, so solver reliability and retries are part of the setup.
- We also look at what the reese84 token is tied to, and what that means for replaying a warmed jar from another client.

**In the full article:** The warming and replay scripts, the request logs, the replay tables per IP and HTTP client, the Manus findings on sensor, token and renewal, and the cookie lifetime figures.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-116-warming-an-imperva-reese84?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
