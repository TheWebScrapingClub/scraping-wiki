---
type: article_summary
title: 'THE LAB 32: hRequests vs anti-bots: a full benchmark'
slug: the-lab-32-hrequests-vs-anti-bots
canonical_url: https://www.scraping.club/p/the-lab-32-hrequests-vs-anti-bots
publish_date: '2023-11-23'
visibility: premium
topics:
- akamai
- cloudflare
- datadome
- captcha
description: A benchmark of the hRequests Python package against Akamai, Cloudflare, Datadome, PerimeterX and Kasada, run on the usual Hands-On test websites.
source_hash: 1a6ed11470627014
---

# THE LAB 32: hRequests vs anti-bots: a full benchmark

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-23 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-32-hrequests-vs-anti-bots?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

hRequests is a Python package that adds headless browsing and real browser TLS fingerprints to plain HTTP requests. We had already tested it against Akamai. What I wanted to know was whether the same tool holds up against the other anti-bots we meet most often: Cloudflare, Datadome, PerimeterX and Kasada.

We ran it against the usual websites of our Hands-On series, so the baseline stays the same as in the other tests. Akamai with reCAPTCHA on luisaviaroma.com is the recap, Cloudflare on harrods.com is the next target, and the remaining anti-bots follow one by one. I ran everything from my office laptop, with a clean IP and a legit device fingerprint, so a different setup can give different results. A pass on one site also says little about other sites using the same anti-bot.

## What's inside

- Why a result on one website does not carry over to others running the same anti-bot, since these products are highly customizable.
- Whether the approach that worked on Akamai transfers to Cloudflare, and what changes in the session setup when it does not.
- The choice of browser and operating system to mock in hRequests, and the timing problems between page load and parsing.
- How a clean IP and a genuine device fingerprint on an office laptop shape what the benchmark can tell you.

**In the full article:** The full code for each anti-bot test, the browser and OS settings used per target, and the results for Cloudflare, Datadome, PerimeterX and Kasada.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-32-hrequests-vs-anti-bots?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
