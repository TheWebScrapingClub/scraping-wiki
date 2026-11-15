---
type: article_summary
title: Google removed the URLs. Only for the people who resell them.
slug: google-removed-the-urls-serp
canonical_url: https://www.scraping.club/p/google-removed-the-urls-serp
publish_date: '2026-08-30'
visibility: free
topics:
- proxies
- anti-detect-browsers
- http-clients
- serp-scraping
description: Google now wraps result links in google.com/goto tokens for traffic it flags as automated. What it costs SERP scrapers, and what the change signals.
source_hash: 019cd3a121528acc
---

# Google removed the URLs. Only for the people who resell them.

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-08-30 (free to read). **[Read the full article](https://www.scraping.club/p/google-removed-the-urls-serp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Google replaced the real destination URLs in search results with google.com/goto?url= links, and a first reading says every rank tracker now pays 500 to 1,000 requests to resolve a five-page ranking. Our measurements say the cost is not the real issue. The change is not a normal rollout: it looks like Google responding to something, which explains why some people saw it everywhere and others never saw it.

We ran the same query from the same machine and connection, changing only how the browser was started, then repeated it with a stealth browser. We looked inside the goto token, tried HEAD requests, checked whether tokens repeat across sessions, and looked for places where the destination leaks anyway. Then we measured what resolving links costs with plain requests and curl_cffi, at different concurrency levels. Finally, we asked who in the SERP and AI search business is actually exposed, and what it means that a quiet, classifier-driven change like this is possible.

## What's inside

- How we isolated the one variable that decides whether Google serves direct URLs or wrapped ones, and why reported behavior differed between Barry Schwartz and Nozzle.
- What the token is made of at byte level, and why you cannot reverse it into the URL yourself.
- Why HEAD requests look like they work while returning nothing useful, and why a token-to-URL lookup table cannot work.
- Which parts of the AI search and SERP API market are exposed, and which are not, including Claude and ChatGPT.

**In the full article:** The console script for the two-window test, the capture counts, the protobuf field walk, the HEAD and GET results, the token stability numbers, the resolution benchmarks per client and concurrency level, and the sources on Claude and ChatGPT search backends.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/google-removed-the-urls-serp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
