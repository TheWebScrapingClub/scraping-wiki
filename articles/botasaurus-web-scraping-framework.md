---
type: article_summary
title: 'Botasaurus: an anti-ban web scraping framework'
slug: botasaurus-web-scraping-framework
canonical_url: https://www.scraping.club/p/botasaurus-web-scraping-framework
publish_date: '2024-03-10'
visibility: free
topics:
- datadome
- anti-detect-browsers
- cloudflare
- browser-automation
description: Hands-on test of Botasaurus, a Python anti-ban scraping framework, against Cloudflare, Datadome and Kasada, on a laptop and on a server.
source_hash: 97733a7bc0540777
---

# Botasaurus: an anti-ban web scraping framework

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-10 (free to read). **[Read the full article](https://www.scraping.club/p/botasaurus-web-scraping-framework?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Botasaurus claims on GitHub to be the stealthiest framework in both the Python and JavaScript worlds, ahead of undetected-chromedriver and puppeteer-stealth. I wanted to see that claim against real anti-bot systems. For anyone scraping protected sites, a stealth tool is only worth something if it holds on real targets and in the place where you actually run it, not only in a demo.

We built a first scraper with the @browser and @request decorators, then pointed it at Cloudflare on Harrods, Datadome on Footlocker.it and Kasada on Canada Goose. Along the way we looked at the stealth options in the documentation, such as user agent and window size, and at how the framework treats browser fingerprinting. Then we moved the scrapers from a laptop to an AWS instance with a residential proxy and checked what changed.

## What's inside

- How the AntiDetectDriver (Selenium) and AntiDetectRequests (stealth requests) modes differ, and what the requests mode saves compared with a Playwright setup.
- Why I was skeptical about a requests-based approach against Datadome, which collects events from the browser session.
- What the documentation says, and does not say, about browser fingerprinting, and why that matters for the choice of environment.
- A feature that installs Chrome extensions on the fly, plus a note on pairing the browser with a CAPTCHA-solving extension.

**In the full article:** Code for the Cloudflare, Datadome and Kasada scrapers, the result of each test on laptop and on AWS, the stealth driver settings, and my verdict on what size of project suits Botasaurus.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/botasaurus-web-scraping-framework?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
