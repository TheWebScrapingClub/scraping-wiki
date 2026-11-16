---
type: article_summary
title: 'THE LAB #19: How to mask the device fingerprint'
slug: how-to-mask-device-fingerprint
canonical_url: https://www.scraping.club/p/how-to-mask-device-fingerprint
publish_date: '2023-05-25'
visibility: premium
topics:
- cloudflare
- browser-fingerprinting
- browser-automation
description: Why a headful Playwright session can pass Cloudflare on Harrods from a local machine but not from a datacenter VM, and which browsers we tried to mask the finge
source_hash: 2bb26259a0af14b1
---

# THE LAB #19: How to mask the device fingerprint

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-05-25 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-mask-device-fingerprint?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Against modern anti-bot software we mostly need a headful browser, because it looks more human. The catch is that it also exposes a lot of data from the environment where the scraper runs, and sometimes that works against us. Harrods is a good example, with Cloudflare set at its highest level of paranoia. A Playwright script with Chrome and some human-like flags does not behave the same from a local machine and from a virtual machine in a datacenter.

We tested the IP angle with a residential proxy, then went through browsers: Chrome, Firefox, which is my usual advice with Playwright, and Brave, which spoofs some fingerprints. I also ran into odd incognito behavior with Brave under Playwright and ask for a workaround in the comments. Last, I cover anti-detect browsers, a class built to spoof the fingerprints they send.

## What's inside

- What the residential proxy test tells us about where Cloudflare is actually looking.
- Why Firefox is my default with Playwright: it leaks fewer pieces of information than Chrome.
- What the deviceinfo.me test shows about Brave's fingerprint spoofing, and the open Brave GitHub issue where new_page() opens a window outside the incognito context.
- Where anti-detect browsers fit as a separate class of tool, built to spoof the fingerprint they send.

**In the full article:** The test scripts for Chrome, Firefox and Brave from The Lab repository, the Playwright launch configuration, the result on Harrods for each browser and the anti-detect browser solution.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-mask-device-fingerprint?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
