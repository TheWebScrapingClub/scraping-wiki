---
type: article_summary
title: 'THE LAB #29: Bypass Cloudflare Bot Protection with Scrapy'
slug: the-lab-29-bypass-cloudflare-bot
canonical_url: https://www.scraping.club/p/the-lab-29-bypass-cloudflare-bot
publish_date: '2023-10-12'
visibility: premium
topics:
- cloudflare
- antibot
- browser-automation
- captcha
description: Bypassing Cloudflare Bot Protection with Scrapy and the Scrapy Impersonate package after web unblockers stopped working, and how Cloudflare flags bots.
source_hash: 781b910cdf58c7c1
---

# THE LAB #29: Bypass Cloudflare Bot Protection with Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-10-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-29-bypass-cloudflare-bot?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Cloudflare holds more than 86% of the anti-bot market according to Statista, so on a medium-large project you will meet it. A plain Scrapy spider gets a 429 and stops. I had moved from headful Playwright to web unblockers, because a browser costs more resources and time and the bill ended up close anyway. Then, as always in this cat-and-mouse game, the setup broke: sites protected by Cloudflare and Datadome stopped working through the unblockers.

In this episode of The Lab I explain how I think Cloudflare decides who gets challenged. I don't reverse-engineer its API calls. My view comes from trial and error and the general principles of bot detection. I cover Turnstile and the signals behind it: IP reputation and type, fingerprinting, and JavaScript challenges. Then I move to the Scrapy Impersonate package, which I found while working on the previous post, to get Scrapy past it.

## What's inside

- How to check whether a target uses Cloudflare with the Wappalyzer Chrome extension.
- Why Turnstile relies on detection and not on a task to complete like a proof-of-work Captcha, and what that means for scrapers and for users behind a VPN or proxy.
- Why Playwright on a data center IP needed residential proxies on some sites, and how that changed the cost comparison with the cheapest unblockers.
- A caveat on the method: every website sets its own Cloudflare rules, so a solution that works on one target can fail on another.

**In the full article:** The Scrapy Impersonate spider code and its implementation, kept in The Lab's GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-29-bypass-cloudflare-bot?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
