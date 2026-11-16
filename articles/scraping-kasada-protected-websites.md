---
type: article_summary
title: Scraping Kasada protected websites
slug: scraping-kasada-protected-websites
canonical_url: https://www.scraping.club/p/scraping-kasada-protected-websites
publish_date: '2023-03-12'
visibility: free
topics:
- browser-automation
- serp-scraping
description: 'How Kasada''s zero-trust anti-bot works and which free and commercial tools get past it: Playwright, Undetected Chromedriver, GoLogin and Bright Data Web Unblock'
source_hash: c3afcb428af32ce0
---

# Scraping Kasada protected websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-03-12 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-kasada-protected-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada is one of the newest anti-bot vendors and works differently from most. You can't spot it with Wappalyzer, it shows no captcha, and the very first request to the site returns a 429 until the challenge is solved. Kasada calls this zero-trust: every request is guilty until proven innocent. Its obfuscated code is polymorphic and changes often, so reverse engineering the JS challenges is time-consuming and breaks quickly.

So we went for the second route: make the scraper indistinguishable from a human. After a chat with Dimitar Krastev of Crawlio, I revisited a Playwright with Chrome setup that had failed in our Anti-Detect Anti-Bot matrix and reviewed its launch parameters. We also covered Playwright with Firefox and Undetected Chromedriver on the free side. On the commercial side we looked at Playwright attached to GoLogin and the Bright Data Web Unblocker, the only option here that doesn't need a headful browser.

## What's inside

- How to recognize a Kasada site: the network tab behavior and the 429 on the first request, since Wappalyzer won't tell you.
- Why reverse engineering and deobfuscation is a weak strategy against Kasada's polymorphic code, which Kasada says it changes continuously.
- Which Chrome launch settings I changed in Playwright after Dimitar's post, and why one of them was hard to get right.
- Where the Web Unblocker differs from the other options: it plugs into Scrapy or any other tool as a proxy API, with no headful browser.

**In the full article:** The Playwright Chrome parameters before and after the change, the Firefox, Undetected Chromedriver and GoLogin configurations, and the link to the GitHub repository with all the code.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-kasada-protected-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
