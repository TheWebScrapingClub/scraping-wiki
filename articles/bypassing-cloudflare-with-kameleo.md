---
type: article_summary
title: 'The Lab #37: Bypassing Cloudflare with anti-detect browsers - Part 2'
slug: bypassing-cloudflare-with-kameleo
canonical_url: https://www.scraping.club/p/bypassing-cloudflare-with-kameleo
publish_date: '2024-01-18'
visibility: premium
topics:
- anti-detect-browsers
- browser-automation
- cloudflare
- antibot
description: Testing Kameleo, an anti-detect browser, against Cloudflare Bot Protection with Playwright, after GoLogin worked locally but failed from an AWS datacenter.
source_hash: 37da02bd9201a130
---

# The Lab #37: Bypassing Cloudflare with anti-detect browsers - Part 2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-01-18 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-cloudflare-with-kameleo?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In the previous Lab, GoLogin got our scraper past Cloudflare Bot Protection. The same scraper worked from our local machine but not from a server in an AWS datacenter, even with residential proxies. That is device fingerprinting at work, and it is the reason a good anti-detect browser matters when you move a scraper to production.

Thanks to the Kameleo team, I had the chance to test their anti-detect browser and add it to the toolbelt. We looked at how Kameleo builds profiles from a database of real-device fingerprints, and how that keeps the fingerprint coherent. Then we created a Windows profile and a Mac OS profile, both driven with Playwright over CDP. We ran them on a Windows Server 2022 machine on AWS and checked them against the Sannysoft and BrowserLeaks fingerprint tests. Finally, we pointed a Playwright script at Harrods to see whether Kameleo gets past Cloudflare.

## What's inside

- How Kameleo separates base profiles, taken from real devices, from the virtual profiles you create, and why that limits which options you can change.
- The setup: a Kameleo server on Windows, and the API client on the machine that runs the scraper.
- What changes when a Mac OS profile runs on a Windows Server: user agent, navigator.platform and WebGL renderer.
- Profiles created on the same OS still differ in details like screen size and sound devices, so each one looks like a plausible but different machine.

**In the full article:** The full Playwright and Kameleo code, the Sannysoft and BrowserLeaks screenshots for both profiles, the playwright_kameleo_harrods.py script and the result of the Cloudflare test.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-cloudflare-with-kameleo?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
