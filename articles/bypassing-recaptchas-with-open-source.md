---
type: article_summary
title: Bypassing reCAPTCHAs With Open Source and Commercial Tools - Part 2
slug: bypassing-recaptchas-with-open-source
canonical_url: https://www.scraping.club/p/bypassing-recaptchas-with-open-source
publish_date: '2025-08-03'
visibility: free
topics:
- captcha
- browser-automation
- anti-detect-browsers
- proxies
description: 'Part 2 of our reCAPTCHA v3 tests: six more open source and commercial tools, including NextCaptcha and CapSolver, run against a real DNS history form.'
source_hash: 5883517b8c38ec1a
---

# Bypassing reCAPTCHAs With Open Source and Commercial Tools - Part 2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-03 (free to read). **[Read the full article](https://www.scraping.club/p/bypassing-recaptchas-with-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

reCAPTCHA v3 is the latest and most challenging version, and a solver that works on one site can fail on the next. In part 1 we covered the history and a first round of tools. Here we continue on the same target, the DNS history form on completedns.com, where a reCAPTCHA token travels in an AJAX call. We count a bypass only if the form returns the real response and not the error info box.

We tested six more tools, free and commercial, including NextCaptcha and CapSolver. For each one we looked at how you get a token, whether replaying the protected request with that token is enough, and what changes when you work through a browser instead. We also tried TLS fingerprint spoofing with hrequests and curl_cffi on top of the token. The snippets are quick test code with hard waits and hardcoded keys, not production scripts.

## What's inside

- How to find the reCAPTCHA site key and the page action by watching the Network tab in DevTools.
- NextCaptcha has thin documentation, so we describe the WebsiteInfo CAPTURE extension workflow and why it clashes with the main NextCaptcha solver extension.
- CapSolver returns the User-Agent used to get the token, and we explain why reusing it in later requests matters.
- A 200 response from the protected endpoint does not mean the bypass worked, so we check the returned HTML each time.

**In the full article:** The full Python code for each tool, the result of every test on the target form, the Playwright setup with the CapSolver extension, and the remaining tools.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-recaptchas-with-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
