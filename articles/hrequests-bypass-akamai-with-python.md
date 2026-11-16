---
type: article_summary
title: 'hRequests: bypass Akamai with Python requests'
slug: hrequests-bypass-akamai-with-python
canonical_url: https://www.scraping.club/p/hrequests-bypass-akamai-with-python
publish_date: '2023-11-12'
visibility: free
topics:
- akamai
- captcha
- browser-automation
- cloudflare
description: hrequests is a Python package that adds TLS spoofing and browser automation to requests. We tested it on an Akamai-protected site, luisaviaroma.com.
source_hash: cf23154cdb08a665
---

# hRequests: bypass Akamai with Python requests

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-12 (free to read). **[Read the full article](https://www.scraping.club/p/hrequests-bypass-akamai-with-python?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Akamai protects plenty of sites, and my last attempt on one of them left me unhappy. Scrapy Impersonate didn't work, the mobile app's calls were protected, and I ended up forcing a working Akamai cookie into the spider. When that cookie dies, the spider breaks and I have to replace it by hand. That's not a solution I'd want to run in production.

I came across hrequests through a LinkedIn post and decided to test it. It's a Python package with an HTTP backend written in Go, TLS fingerprint spoofing based on tls-client, and headers coherent with the chosen browser. It also has a browser automation side, with a mock_human option based on botright. We checked the fingerprint it sends against tls.browserleaks.com. Then we put it inside a Scrapy project against the same Akamai-protected target, luisaviaroma.com, which also adds a reCAPTCHA. The question was whether hrequests could replace the fixed cookie.

## What's inside

- How the TLS spoofing in hrequests compares with Scrapy Impersonate, and which Go library it builds on.
- Why I find the browser automation part too basic for complex projects, and where it still fits.
- How a single spider uses a headful browser and plain requests in the same session.
- What happens when the reCAPTCHA shows up again during pagination, and where the full code is published.

**In the full article:** The fingerprint output from browserleaks, the Scrapy spider code, the session and pagination logic, the reCAPTCHA handling and the GitHub repository link are all in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/hrequests-bypass-akamai-with-python?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
