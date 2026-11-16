---
type: article_summary
title: How to Improve the Performance of Puppeteer Stealth Evasions
slug: improving-performance-puppeteer-scraping
canonical_url: https://www.scraping.club/p/improving-performance-puppeteer-scraping
publish_date: '2024-04-02'
visibility: free
topics:
- browser-automation
- antibot
- browser-fingerprinting
description: How Puppeteer Stealth evasions work, where they stop against anything beyond basic protection, and how to write custom ones for navigator.platform, deviceMemory
source_hash: 9beb77b3324b6cc3
---

# How to Improve the Performance of Puppeteer Stealth Evasions

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-04-02 (free to read). **[Read the full article](https://www.scraping.club/p/improving-performance-puppeteer-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Vanilla Puppeteer leaves obvious tracks. Headless flags and the WebDriver property are enough for an anti-bot to flag it. The Stealth plugin for Puppeteer Extra patches many of them, and it is popular, but in practice it holds up only against basic protection. To push it further, you first need to know what it does behind the scenes.

We compared vanilla Puppeteer and Stealth on CreepJS, looking at headless behavior and the WebDriver property. Then we went through the evasions that matter most: UA override, navigator.webdriver, media codecs, plugins, and WebGL vendor and renderer. Finally, we wrote two custom evasions on top of Stealth. One patches navigator.platform to present a different operating system. The other patches deviceMemory and hardwareConcurrency to change the hardware profile. We checked both against CreepJS in non-headless mode. This is the first part of a series done with ZenRows.

## What's inside

- Which headless and WebDriver signals CreepJS reads, and how we used them to compare vanilla Puppeteer with Stealth
- What each of the five core evasions patches and why anti-bot systems check it
- Why the platform patch can help against systems that target a specific operating system
- Why changing memory and CPU cores per request can reduce tracking by hardware fingerprint

**In the full article:** The CreepJS screenshots for each comparison, the full scripts for the platform and hardware patches, the npm setup, and the preview of the next part on the navigator object and WebDriver.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/improving-performance-puppeteer-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
