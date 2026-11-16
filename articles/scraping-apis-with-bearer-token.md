---
type: article_summary
title: Scraping APIs with Bearer Token
slug: scraping-apis-with-bearer-token
canonical_url: https://www.scraping.club/p/scraping-apis-with-bearer-token
publish_date: '2024-05-17'
visibility: premium
topics:
- antibot
- proxies
description: Scraping an internal API that requires a Bearer token, shown on the Loewe e-commerce site with Scrapy, and how it differs from Castle tokens.
source_hash: 80f4a57e559750eb
---

# Scraping APIs with Bearer Token

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-05-17 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-apis-with-bearer-token?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

When I start a scraping project, I check whether the site has an internal API. If it does, that's the preferred route: less data on both sides, lower cost if proxies are billed per GB, and fewer breakages than with HTML. The trouble starts when the endpoint answers Unauthorized because it wants a Bearer token in the Authorization header. Loading the URL in the browser is not enough.

We first separate Bearer tokens from Castle anti-bot tokens, which are generated from browser data and can't be replicated by watching the site. Then we work on a real target, the Loewe e-commerce site. In the network tab we trace how the site gets its token: which call issues it, what parameters it needs and where the value feeding that call comes from. From there we build a Scrapy spider that goes from the home page to the product list API.

## What's inside

- Why Castle's x-castle-request-token can't be handled like a Bearer token, and when reverse-engineering it is overkill.
- The three steps to look for in the network tab: token request, token parsing, final API call.
- How to find the call that issues the token by searching for the token string in the network tab.
- How the token refresh and the first token request relate, and why that helps when the scraper enters the site.

**In the full article:** The Scrapy spider code, the token request parameters, the cookie handling and the sequence of calls from home page to product list API.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-apis-with-bearer-token?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
