---
type: article_summary
title: 'THE LAB #96: Scraping Nike.com with 5 open source tools'
slug: scraping-nike-with-open-source
canonical_url: https://www.scraping.club/p/scraping-nike-with-open-source
publish_date: '2026-01-29'
visibility: premium
topics:
- anti-detect-browsers
- browser-automation
- http-clients
- akamai
description: A test of five open-source scraping tools (Pydoll, Camoufox, Scrapling, Rnet, Undetected-httpx) on 1000 Nike.com product URLs, with the site's anti-bot setup.
source_hash: 833fb517ef39fb5c
---

# THE LAB #96: Scraping Nike.com with 5 open source tools

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-01-29 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-nike-with-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Nike.com is one of the most scraped e-commerce targets, from competitor price tracking to the sneaker resale market, and it sits behind anti-bot protection. The common assumption is that a site like this needs browser automation. We wanted to check it against real numbers instead of habit.

We first mapped what Nike serves. Akamai Bot Manager covers the public catalog, Kasada covers authenticated flows, and we stayed on public catalog data only. Then we ran five open-source tools on the same 1000 product URLs taken from the Austrian EN sitemap: Pydoll, Camoufox, Scrapling, Rnet and Undetected-httpx. Two are browser tools, the others are HTTP clients with fingerprint emulation. All of them used identical parsing, so the differences come from fetching alone. We measured success rate, speed and reliability, and ran the requests with no delays as a worst case.

## What's inside

- How TLS and HTTP/2 fingerprinting (header order, pseudo-headers, SETTINGS frames) apply to Nike's catalog, and why plain Python requests fails at the first step.
- Why the product pages being server-side rendered matters: the data is in the first response, so JavaScript execution is not needed.
- We scraped from a residential IP, so IP reputation was not a variable, and we saw no JavaScript challenges on product pages.
- Why we parsed with stable data-testid selectors instead of class names, and how each tool was configured and paced.

**In the full article:** The test results per tool, the speed and success-rate comparison, the full scraping code in the private GitHub repository and the conclusions on browser automation versus HTTP clients.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-nike-with-open-source?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
