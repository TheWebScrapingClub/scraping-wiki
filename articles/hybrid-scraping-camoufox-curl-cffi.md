---
type: article_summary
title: 'THE LAB #100: Hybrid Scraping - One Browser Login, Thousands of HTTP Requests'
slug: hybrid-scraping-camoufox-curl-cffi
canonical_url: https://www.scraping.club/p/hybrid-scraping-camoufox-curl-cffi
publish_date: '2026-03-19'
visibility: premium
topics:
- http-clients
- anti-detect-browsers
- akamai
- browser-automation
description: 'A hybrid scraping pattern on Net-a-Porter: log in once with Camoufox, then replay the session through curl_cffi for fast, low-resource authenticated API calls b'
source_hash: d9ca3e348accd4e3
---

# THE LAB #100: Hybrid Scraping - One Browser Login, Thousands of HTTP Requests

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-03-19 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/hybrid-scraping-camoufox-curl-cffi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Browsers are the default answer when a target runs Akamai, Cloudflare or Datadome. They work, but each page costs hundreds of megabytes of RAM and seconds of runtime. At ten pages that is irrelevant. At ten thousand, the browser is the bottleneck, and the gap with an HTTP client can decide whether a pipeline fits on one machine or needs a cluster.

Many sites need a real browser only at the gate: the login, the challenge, the session setup. After that, it is plain API calls. We tested this hybrid pattern on Net-a-Porter, protected by Akamai Bot Manager, with an authenticated wishlist exposed through internal JSON APIs. Camoufox does the login and nothing else. curl_cffi takes over the session and handles the requests. The handoff is not just copying cookies, because Akamai also checks that the client using them looks like the one that earned them. We walk through the attempts, including the ones that did not work.

## What's inside

- Why Camoufox and curl_cffi are paired: Firefox on one side, Firefox TLS impersonation on the other.
- How TLS fingerprint continuity between the browser and the HTTP client affects whether the server accepts the session.
- The three layers of the Net-a-Porter setup: Akamai cookies, the login API with its token, and the authenticated wishlist endpoints.
- The investigation path of failed and successful handoff attempts, and what each one taught us about session transfer.

**In the full article:** The code in the paying-users GitHub repository, the request details for the login and wishlist APIs, and the results of each handoff attempt.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/hybrid-scraping-camoufox-curl-cffi?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
