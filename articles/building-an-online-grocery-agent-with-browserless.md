---
type: article_summary
title: Building an online grocery agent with Browserless
slug: building-an-online-grocery-agent-with-browserless
canonical_url: https://www.scraping.club/p/building-an-online-grocery-agent-with-browserless
publish_date: '2026-10-06'
visibility: free
topics:
- captcha
- browser-as-a-service
- browser-automation
- cloudflare
description: Building an AI agent on Browserless that logs in to two Italian grocery sites, saves the session as a profile and adds an item to the cart.
source_hash: 3358b2ed8a261de3
---

# Building an online grocery agent with Browserless

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-10-06 (free to read). **[Read the full article](https://www.scraping.club/p/building-an-online-grocery-agent-with-browserless?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A local browser comes with logins, saved sessions, a clean residential IP and real hardware. An agent running on a Linux VM in a data center has none of that, and its IP raises red flags from the first request. For an agent that has to act as a logged-in user, that gap is where things break.

For this Tool of the Week we used Browserless to build an agent that logs in to an Italian grocery site and adds a product to the cart. We worked with Playwright over CDP, the stealth route, the built-in Italian residential proxy and the native CAPTCHA solver. We tried two targets: Esselunga, behind F5 BIG-IP, and Tigros, behind Cloudflare with reCAPTCHA Enterprise. Then we tested Authenticated Profiles and the Session API, to see whether a new browser could skip the login. We also looked at how Browserless bills units.

## What's inside

- How the stealth and plain Chromium endpoints compared on the first Esselunga request, and which anti-bot signal showed up.
- What happened with the second factor on Esselunga, and why our hypothesis about the Linux identity could not be proven.
- Why we used reCAPTCHA Enterprise's invisible, score-based version on Tigros and how the native solver behaved against the page's own token.
- Profile versus persisted session: a copy by value against a browser identity that keeps changing on disk, and what changes when the exit IP changes.

**In the full article:** The Python and Playwright code, the connection parameters, the CAPTCHA solve results per run, the profile and Session API calls, the unit costs and the cart test on Tigros.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-an-online-grocery-agent-with-browserless?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
