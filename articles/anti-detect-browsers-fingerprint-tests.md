---
type: article_summary
title: The Anti-Detect Browser Royal Rumble - Fingerprint tests
slug: anti-detect-browsers-fingerprint-tests
canonical_url: https://www.scraping.club/p/anti-detect-browsers-fingerprint-tests
publish_date: '2024-04-23'
visibility: free
topics:
- anti-detect-browsers
- browser-fingerprinting
- browser-automation
- proxies
description: Fingerprint test of seven anti-detect browsers on CreepJS and BrowserScan, scored out of 260 against a real Chrome on Mac baseline.
source_hash: 3421819a07fa2c24
---

# The Anti-Detect Browser Royal Rumble - Fingerprint tests

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-04-23 (free to read). **[Read the full article](https://www.scraping.club/p/anti-detect-browsers-fingerprint-tests?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anti-detect browsers build believable fingerprints so one machine can pass as many different profiles. As anti-bot vendors lean more on device and browser fingerprinting, they are becoming a commercial alternative to homemade or OSS options like Undetected Chromedriver and undetected-playwright. Before putting one in a scraping stack, you want to know how coherent the fingerprint it produces really is.

This is the first episode of the Anti-detect Browsers Benchmark. We tested GoLogin, Incogniton, Kameleo, MoreLogin, NSTBrowser, Octo Browser and Undetectable.io. Every client ran on a Windows Server VM on AWS, with a profile mimicking Chrome on a Mac desktop, residential proxies in eu-central-1, WebRTC disabled and noise on Canvas and WebGL. We scored each one from 0 to 260 on CreepJS, BrowserScan, browser and OS detection, and WebRTC leaks, and compared them with my own Mac as the baseline. I ran the tests without help from the vendors.

## What's inside

- The 260-point formula: CreepJS trust score and BrowserScan authenticity up to 100 each, plus 20 points each for browser, OS and WebRTC checks.
- Why a profile that adds noise to Canvas and WebGL can lose points, and what the tools flag as lies or inconsistent fingerprints.
- Leaks beyond WebRTC that showed up in some profiles, such as a real IP exposure and a DNS leak through the local operator while using a proxy.
- Why a low CreepJS score does not rule out a browser for scraping, since it is an educational OSS project and real browsers can score low too.

**In the full article:** The per-browser scores, the final ranking table against the baseline, the screenshots of each CreepJS and BrowserScan run, and the notes on what each tool flagged in the fingerprint.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/anti-detect-browsers-fingerprint-tests?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
