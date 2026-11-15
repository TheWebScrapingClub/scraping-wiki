---
type: article_summary
title: How to by-pass Kasada bot mitigation?
slug: how-to-by-pass-kasada-bot-mitigation
canonical_url: https://www.scraping.club/p/how-to-by-pass-kasada-bot-mitigation
publish_date: '2023-03-13'
visibility: free
topics:
- browser-automation
- cloudflare
description: 'Four ways to get past Kasada bot mitigation: Playwright with Chrome or Firefox, Playwright on GoLogin, and Bright Data Web Unblocker, free and paid.'
source_hash: 8e2fece23c0d6094
---

# How to by-pass Kasada bot mitigation?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-03-13 (free to read). **[Read the full article](https://www.scraping.club/p/how-to-by-pass-kasada-bot-mitigation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada was a real problem for our scraping work until 2022. Since then, better tooling and more study on my side have given us several ways around it. The question now is which ones are worth setting up, and which of them need a headful browser.

We split the options into free and commercial. On the free side, I went back to Playwright with Chrome, which had failed in our Anti-Detect Anti-Bot matrix with a setup that had been reliable for a long time. A post on the Crawlio page by Dimitar pushed me to retry it, so I reviewed the Chrome parameters in my test scraper. We also looked at Playwright with Firefox. On the commercial side, we attached Playwright to a GoLogin browser instance, then looked at Bright Data Web Unblocker, a proxy API that works with Scrapy or any other tool. I close with a note on ethics and on the cost of this cat and mouse game.

## What's inside

- Why the old Playwright and Chrome setup failed on Kasada and which parts of the configuration changed on the retry.
- How to get rid of the "Chrome is controlled by an automated test service" infobar in Playwright, which I had struggled with.
- How a Playwright script attaches to an already open GoLogin instance and its profiles.
- Why Bright Data Web Unblocker is the only option here that does not need a headful browser, and how it fits into a Scrapy project.

**In the full article:** The old and new Playwright Chrome configurations, the Firefox and GoLogin setups, the Crawlio post screenshot and the results of each run against the target website.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-by-pass-kasada-bot-mitigation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
