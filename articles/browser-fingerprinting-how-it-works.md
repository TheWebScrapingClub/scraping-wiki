---
type: article_summary
title: Browser Fingerprinting 101 - What it is and how it works
slug: browser-fingerprinting-how-it-works
canonical_url: https://www.scraping.club/p/browser-fingerprinting-how-it-works
publish_date: '2025-03-02'
visibility: free
topics:
- browser-automation
- browser-fingerprinting
- anti-detect-browsers
- antibot
description: 'Browser fingerprinting explained for scrapers: canvas, WebGL, audio, font and DOM signals, how anti-bot systems use them, and ways to change your fingerprint.'
source_hash: 9dda5413250d9d76
---

# Browser Fingerprinting 101 - What it is and how it works

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-03-02 (free to read). **[Read the full article](https://www.scraping.club/p/browser-fingerprinting-how-it-works?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

You build a headful scraper and it runs fine on your machine. You deploy it on a VM or a server with the same configuration and the same residential proxy, and it gets blocked. The only thing that changed is the hardware, and that points to one cause: the target site is flagging your browser fingerprint. Browserless scrapers don't have this problem, browser-based ones do.

I go through what a browser fingerprint is and how sites collect it. It is stateless, so clearing cookies doesn't help, and I cite the EFF Panopticlick study and a 2024 paper on demographics. Then I cover the main techniques: canvas, WebGL, AudioContext, fonts, DOM properties and device-level signals. I also look at how anti-bot systems use them to spot headless Chrome and automation. Last, I list the ways to change a fingerprint: real headed browsers, open-source tools like Camoufox and Nodriver, anti-detect browsers and browsers as a service.

## What's inside

- Why a zero count of audio and video devices on a server is a red flag we met in real scraping work.
- How anti-bot systems check consistency, for example whether the User-Agent matches what canvas and WebGL report, with SwiftShader as a giveaway.
- Why Selenium Stealth, puppeteer-extra and Playwright stealth are no longer a good choice, and the weakness of open-source tools in general.
- The limits of anti-detect browsers, mainly parallelism, and where browsers-as-a-service fit in.

**In the full article:** The Playwright argument for removing the automation flag, the named anti-detect browsers and browser-as-a-service vendors, and the links to the studies and tools mentioned.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/browser-fingerprinting-how-it-works?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
