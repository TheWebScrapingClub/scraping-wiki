---
type: article_summary
title: 'THE LAB #64: JWT Tokens and API scraping'
slug: jwt-tokens-and-api-scraping
canonical_url: https://www.scraping.club/p/jwt-tokens-and-api-scraping
publish_date: '2024-10-17'
visibility: premium
topics:
- api-scraping
description: How JWT tokens work and why they matter when scraping the Tractor Supply Company mobile app API, which the website does not expose.
source_hash: 654ae9f35c9ae09b
---

# THE LAB #64: JWT Tokens and API scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-10-17 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/jwt-tokens-and-api-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Finding a web API under a target is one of the best things that can happen to a scraper. It is less prone to changes than HTML because more actors use it, and it often returns more data than the website shows. Apps are harder. On Tractor Supply Company the website shows no API call for product data, while the mobile app uses endpoints the site never touches, and those calls need an authentication token.

I start with what a JWT token is, using a boarding pass as the analogy, and go through its three parts: header, payload and signature. For scraping, the payload matters most because of the expiry date, which tells you how often to refresh. For Tractor Supply we set up a rooted virtual Android device with the Frida server, unpin the SSL certificate and watch the traffic with Fiddler Everywhere.

## What's inside

- The difference between registered, public and private claims in the payload, with the fields the JWT specification recommends.
- Why the signature, built with a key held by the server, stops a third party from forging the payload, for example to extend the expiry.
- Token lifetime changes from site to site, from a few minutes to several hours, so each target needs its own refresh schedule.
- In the Tractor Supply app the JWT is requested even when no user is logged in, and it then authenticates the other endpoints.

**In the full article:** The scraper code for the Tractor Supply app, split by task in the 64.JWT folder of The Lab GitHub repository, plus the Fiddler capture of the app's first API calls.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/jwt-tokens-and-api-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
