---
type: article_summary
title: The Impact of Chrome's New CPU Performance API on Web Scraping Detection
slug: the-impact-of-chromes-new-cpu-performance-api
canonical_url: https://www.scraping.club/p/the-impact-of-chromes-new-cpu-performance-api
publish_date: '2026-09-06'
visibility: free
topics:
- antibot
- anti-detect-browsers
- scraping-infra
- browser-fingerprinting
description: Chrome 152 adds navigator.cpuPerformance, a CPU performance tier value. What it exposes, how it compares to other hardware signals, and what it means for scrape
source_hash: 585d0b146e768c84
---

# The Impact of Chrome's New CPU Performance API on Web Scraping Detection

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-09-06 (free to read). **[Read the full article](https://www.scraping.club/p/the-impact-of-chromes-new-cpu-performance-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Chrome 152 ships the CPU Performance API. Through navigator.cpuPerformance, a site can read a small integer that places the device in a performance tier, without seeing the processor model, clock speed or core count. It was built so web apps can adapt to the hardware, but it is also a new hardware signal that anti-bot systems can read. So I wanted to know whether it is a real problem for scraping or just another piece of the fingerprinting puzzle.

I cover how the API works and why Chrome introduced it. Then I compare it with the hardware signals already available: WorkerNavigator and hardwareConcurrency, the Device Memory API, WebGPU and the Summarizer API. After that I look at how a scraper can spoof the property, at two different levels, and which stealth browser tools already handle it. The last part is about what anti-bot systems really check, which is whether all the hardware signals tell the same story.

## What's inside

- What the tier values mean, including the special value for a device Chrome can't classify, and why the tier is static and not tied to current load.
- How the API relates to the Compute Pressure API: one tells you how powerful the device is, the other how busy the CPU is right now.
- Why spoofing at the JavaScript level and patching Chromium itself differ in how detectable they are, and why most scraping teams can't maintain a custom build.
- Whether switching to Firefox avoids the signal, plus the Chrome version and privacy questions in the FAQ.

**In the full article:** The code snippets for each API, the DevTools screenshots of their output, the list of stealth browser tools by category and the FAQ on Chrome versions, privacy and Firefox.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-impact-of-chromes-new-cpu-performance-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
