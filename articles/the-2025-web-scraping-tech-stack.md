---
type: article_summary
title: The 2025 web scraping tech stack
slug: the-2025-web-scraping-tech-stack
canonical_url: https://www.scraping.club/p/the-2025-web-scraping-tech-stack
publish_date: '2025-01-12'
visibility: free
topics:
- browser-automation
- captcha
- anti-detect-browsers
- proxies
description: 'A practical map of the 2025 web scraping stack: Scrapy, proxies and unblockers, Playwright with stealth tools, anti-detect browsers and CAPTCHA solvers.'
source_hash: e585c61f00bfc8fe
---

# The 2025 web scraping tech stack

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-12 (free to read). **[Read the full article](https://www.scraping.club/p/the-2025-web-scraping-tech-stack?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Web scraping keeps getting harder. Since we started our consultancy, we have seen the variety of targets and anti-bot defenses firsthand, so I wanted to open the year with a reminder of which tools belong in the toolbelt. In my experience, if you scrape one hundred e-commerce websites, most of them still do not need anything fancy.

I walk through the stack in layers. It starts with browserless frameworks like Scrapy, its extensions and the proxy types you can plug in. Then come commercial scraping APIs and unblockers, with the cost trade-off against building your own. Next is browser automation with Playwright and why detection now makes it insufficient alone. I cover Patchright, Camoufox, GoLogin and Multilogin for stealth and fingerprints, and CAPTCHA solving services such as NopeCHA, 2Captcha and Anti-Captcha. I left "Scraping with AI" out on purpose, because it deserves its own series.

## What's inside

- Where Scrapy still fits: the share of e-commerce sites that need no heavy anti-bot handling, and the extension I use against Akamai.
- How I choose between a commercial API or unblocker and a homemade browser automation setup, weighing budget, speed and infrastructure simplicity.
- Why launch arguments that worked for Playwright in 2023 and early 2024 no longer do, and the role of CDP detection and browser fingerprints.
- Where anti-detect browsers help with logins and session management, and the CAPTCHA providers that cannot be bypassed except by acting like a human.

**In the full article:** Links to each tool and extension, the earlier posts on TLS fingerprinting and CDP detection, and my closing notes on strategy, request costs and legal risk.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-2025-web-scraping-tech-stack?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
