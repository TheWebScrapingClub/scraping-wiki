---
type: article_summary
title: 'THE LAB #87: Bypassing ReCAPTCHAs with open source and commercial tools'
slug: bypassing-recaptcha-v3
canonical_url: https://www.scraping.club/p/bypassing-recaptcha-v3
publish_date: '2025-06-20'
visibility: premium
topics:
- captcha
- cloudflare
- browser-fingerprinting
- akamai
description: How ReCAPTCHA v1, v2 and v3 work, how hCaptcha, Turnstile, Friendly Captcha and Geetest compare, and a test of open-source and commercial bypass tools.
source_hash: 76942955219d2f35
---

# THE LAB #87: Bypassing ReCAPTCHAs with open source and commercial tools

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-06-20 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-recaptcha-v3?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

More and more people in the TWSC Discord server and on Reddit are struggling with ReCAPTCHA, especially V3. Google held around 98% of the CAPTCHA market as of 2022, so sooner or later a scraper runs into it. The three versions are very different targets, and it pays to know how each one decides who is human before choosing a tool.

I start with the history, from v1's book-digitizing word pairs to v2's checkbox and v3's invisible risk score, and then explain how each version works technically. After that I cover the alternatives: hCaptcha, Cloudflare Turnstile, Friendly Captcha, Geetest and the bot management vendors. Finally, we test open-source packages and commercial solutions against a real-world use case.

## What's inside

- How v3 turns telemetry into a score from 0.0 to 1.0, what site owners do with a threshold, and why Google suggests embedding it on every page.
- What ReCAPTCHA Enterprise adds on top of v3, including the fallback to a v2 challenge when the invisible score is not confident.
- Why Cloudflare dropped Google in 2020, and how Turnstile now relies on rotating background challenges and Private Access Tokens developed with Apple.
- Different ways to avoid a human puzzle: proof-of-work in Friendly Captcha, sliders in Geetest, and silent fingerprinting in bot management products.

**In the full article:** The real-world use case, the open-source packages and commercial solutions we tested with their results, and the scripts in the 87.RECAPTCHA folder of the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-recaptcha-v3?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
