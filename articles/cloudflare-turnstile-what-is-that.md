---
type: article_summary
title: 'Cloudflare Turnstile: what is that and how it works?'
slug: cloudflare-turnstile-what-is-that
canonical_url: https://www.scraping.club/p/cloudflare-turnstile-what-is-that
publish_date: '2023-08-20'
visibility: free
topics:
- cloudflare
- captcha
- antibot
description: 'Cloudflare Turnstile, the "No Captcha" challenge launched in September 2022: how its background checks work, what it looks like on sites, and how it compares to'
source_hash: 8bd246bcba165dd3
---

# Cloudflare Turnstile: what is that and how it works?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-20 (free to read). **[Read the full article](https://www.scraping.club/p/cloudflare-turnstile-what-is-that?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In September 2022 Cloudflare launched Turnstile, a "No Captcha" Captcha. It is a JavaScript challenge that separates human traffic from bots without asking the user to pick traffic lights or vans. For anyone scraping Cloudflare-protected sites, it is one more check between your scraper and the page, and it is free for site owners to install, so we will meet it more and more.

I go through how Turnstile decides who is human: a set of small non-interactive challenges that collect signals about the browser environment. I describe the three installation modes a site can choose, from a box that appears only when Cloudflare is in doubt to a fully invisible check, and show Harrods.com as a real example. I also built a Cloudflare Turnstile Tester on The Web Scraping Club website, so you can load it with your scraper and see if it passes safely. Last, I compare Turnstile with reCAPTCHA v3 and hCaptcha.

## What's inside

- Why Cloudflare positions Turnstile against Google's reCAPTCHA, and the data trade-off I suspect sits behind a free product.
- The kinds of background challenges Turnstile mixes, including proof-of-work, proof-of-space and probing of web APIs.
- What a scraper sees on Harrods.com before it is redirected to the home page, compared with a normal visitor.
- How reCAPTCHA v3, hCaptcha and Turnstile differ, and why proof-of-work still matters against DDoS.

**In the full article:** The screenshots of the three Turnstile installation modes and of the Harrods.com waiting page, the link to the Turnstile Tester, and the pointer to our Cloudflare bypass archive.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/cloudflare-turnstile-what-is-that?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
