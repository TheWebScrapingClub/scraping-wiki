---
type: article_summary
title: 'THE LAB #30: How to bypass Akamai protected website when nothing else works'
slug: the-lab-30-how-to-bypass-akamai-protected
canonical_url: https://www.scraping.club/p/the-lab-30-how-to-bypass-akamai-protected
publish_date: '2023-10-27'
visibility: premium
topics:
- akamai
- browser-automation
- http-clients
- captcha
description: Debugging a Scrapy spider on a fashion retailer behind Akamai and reCAPTCHA that started blocking at the first request, without commercial tools.
source_hash: 966ff721e17c13fa
---

# THE LAB #30: How to bypass Akamai protected website when nothing else works

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-10-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-30-how-to-bypass-akamai-protected?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A well-known fashion retailer with around 40k items sits behind Akamai. Until a few weeks ago, our Scrapy spider, split into concurrent runs per product category, collected the whole catalog before getting blocked. Then the scrapers started failing at the first request. Other people in our Discord server reported the same thing, so I think Akamai pushed an update.

We start from what is protecting the site, using the Wappalyzer extension, which shows reCAPTCHA together with Akamai. Then I go through the debugging order I usually follow, discarding the easy causes first: the IP and the datacenter, whether a headful browser is needed, scrapy_impersonate and its JA3 TLS masking, and which cookies the requests really need. The cookie question leaves us stuck, because we cannot load a single page to get them. Playwright does not help either, and that leads to the mobile app of the retailer as the next angle.

## What's inside

- How to tell an IP problem from a scraper problem by running the same spider on a laptop instead of a cloud VM.
- A quick test of whether you need a headful browser: copy the browser request as cURL from developer tools and check the HTML.
- Why I normally prefer cookies generated at runtime, and why this case turned out to be the opposite.
- Why Playwright could not generate the Akamai cookies, and why the mobile app is the next route.

**In the full article:** The cURL tests, the cookie findings, the final no-cost solution and the way we scrape the mobile app are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-30-how-to-bypass-akamai-protected?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
