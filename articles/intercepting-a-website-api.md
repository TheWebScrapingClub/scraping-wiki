---
type: article_summary
title: 'THE LAB #112: Intercepting a Website''s Internal API Calls'
slug: intercepting-a-website-api
canonical_url: https://www.scraping.club/p/intercepting-a-website-api
publish_date: '2026-07-31'
visibility: premium
topics:
- akamai
- browser-automation
- anti-detect-browsers
- proxies
description: How to find and intercept a site's internal JSON API with a Playwright and Camoufox script, using Harrods behind Akamai Bot Manager as the target.
source_hash: 98aced7f23c66982
---

# THE LAB #112: Intercepting a Website's Internal API Calls

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-07-31 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/intercepting-a-website-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Sites with changing data, like product catalogs and prices, rarely put it in the HTML. The frontend fetches JSON from an internal API, and that endpoint survives a redesign better than your selectors do. The hard part is finding the right request and reaching it past anti-bot protection. Harrods adds a twist: the category page is server side rendered, so the first load shows no product API call at all.

We start by hand in the DevTools Network tab, then automate the search with a Python script that listens to browser responses and keeps the JSON ones. We map the Harrods stack: Nuxt, SCAYLE, Algolia behind a first-party proxy, Global-e and Akamai Bot Manager. We run a plain Playwright control against Camoufox, use a homepage warm-up, and trigger client-side pagination. Then we read the response and the request body the frontend sends.

## What's inside

- Why the data call only fires when the page needs products it doesn't have, and which interactions to try: paginate, filter, sort, scroll.
- How the interceptor cuts noise: a content type filter, a blocklist of analytics and consent hosts, and deduplication by method and path.
- Why a deep URL needs a homepage warm-up for Akamai cookies, and why a DOM-triggered click replaces Playwright's normal click on the pagination control.
- What the Algolia proxy changes: the request carries no Algolia application ID or API key, and what that means for replaying it.

**In the full article:** The full intercept.py handler and click code, the exact commands for the control and Camoufox runs, the list of captured endpoints, the decoded request parameters and the replay section that pages through the catalog.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/intercepting-a-website-api?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
