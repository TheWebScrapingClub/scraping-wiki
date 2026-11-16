---
type: article_summary
title: HTTP Toolkit, your best friend for network inspection
slug: http-toolkit-network-intercept
canonical_url: https://www.scraping.club/p/http-toolkit-network-intercept
publish_date: '2024-10-27'
visibility: free
topics:
- http-clients
description: 'HTTP Toolkit for network inspection in scraping work: browser and Android app interception, request export, and how it compares to Fiddler Everywhere and Frida.'
source_hash: b9ea4cddc35fc25d
---

# HTTP Toolkit, your best friend for network inspection

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-10-27 (free to read). **[Read the full article](https://www.scraping.club/p/http-toolkit-network-intercept?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

At Re-Analytics we had a few consultancy tasks that needed app network inspection. We don't do it daily, so I had to dig back into it. My earlier setup with Fiddler Everywhere and Frida for certificate unpinning worked, but it meant rooting the device, installing Frida and editing scripts to use the Fiddler certificate. Some Frida codeshare scripts never worked fully for me, and apps with pinned external authentication services stayed unusable.

I recently found HTTP Toolkit, a man-in-the-middle tool for HTTP and HTTPS traffic that handles the certificate installation by itself. We looked at how it works in a browser, including sites that don't let you browse with dev tools open, and on a virtual Android device. For Android we compared the connection options it offers, including the one that still uses Frida, and checked them against a few apps, Google Maps among them. I also cover the request export formats, the rules to mock and modify requests, and why I pay for the basic plan.

## What's inside

- Why it works on sites like bet365.it that don't let you browse with Chrome dev tools open
- Request export in many languages beyond JS, Python and cURL, and which of those exports sit behind the paid plan
- The three Android connection options: non-rooted device over ADB, QR code setup, and rooted device with Frida
- Where it still falls short: Google Maps calls and API endpoints protected by an anti-bot

**In the full article:** Screenshots of the HTTP Toolkit interface, the Android connection options screen, the request export and mock rule examples, and my notes on how each Android option behaved on the apps I tried.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/http-toolkit-network-intercept?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
