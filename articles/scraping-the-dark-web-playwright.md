---
type: article_summary
title: Scraping the dark web with Playwright and Brave
slug: scraping-the-dark-web-playwright
canonical_url: https://www.scraping.club/p/scraping-the-dark-web-playwright
publish_date: '2024-03-07'
visibility: premium
topics:
- browser-automation
- anti-detect-browsers
- industry-overview
description: Scraping onion websites on the TOR network with Playwright and Brave, plus a primer on the deep web, onion routing and how to find .onion URLs.
source_hash: 94ade58c45bf4273
---

# Scraping the dark web with Playwright and Brave

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-07 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-the-dark-web-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most scraping targets are public pages that search engines index. The deep web, which they don't index, is estimated at 400-500 times bigger. The dark web is a small slice of it, put at 0.01-5% of the standard internet, and you reach it only through TOR, which hides both client and server. That makes onion sites a different kind of target from anything you scrape on the open web.

I start with the groundwork: what TOR is, how onion routing sends traffic through volunteer relays, and what an onion URL looks like. Then I cover where to find onion links, from dark web search engines and directories to forums and sites that link to each other. After that we move to the scraper for a TOR website, built with Playwright and the Brave browser.

## What's inside

- Where TOR comes from: developed in the mid-1990s by US Naval Research Laboratory employees, then released to the public domain.
- How layered encryption works across a path of at least three relays, and why no single relay sees both the origin IP and the destination.
- The costs of TOR to plan around: slower speeds, authorities trying to compromise its anonymity, and exit node exposure, which HTTPS helps mitigate.
- The discovery tools we name: Ahmia.fi, DuckDuckGo's onion version, Candle, The Hidden Wiki and OnionDir.

**In the full article:** The Playwright and Brave scraper code for a TOR website, published in The Web Scraping Club GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-the-dark-web-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
