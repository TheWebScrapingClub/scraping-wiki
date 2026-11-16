---
type: article_summary
title: Dealing with Rate Limiting Using Exponential Backoff
slug: rate-limit-scraping-exponential-backoff
canonical_url: https://www.scraping.club/p/rate-limit-scraping-exponential-backoff
publish_date: '2025-06-08'
visibility: free
topics:
- human-behavior-emulation
- http-clients
- proxies
- legal-ethics
description: How exponential backoff handles rate limiting in web scraping, compared with fixed and linear waits, with Python Requests and Axios implementations.
source_hash: aa4c3758a270e7d3
---

# Dealing with Rate Limiting Using Exponential Backoff

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-06-08 (free to read). **[Read the full article](https://www.scraping.club/p/rate-limit-scraping-exponential-backoff?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Your scraper sends too many requests, the rate limiter kicks in, and you start getting 429 errors, sometimes 403 or even 503. Proxies are the usual answer at scale. But you may not want them, or your project may not allow them. In that case the only option is to wait for the time window to reset, and how you wait decides whether you get through or get blocked for good.

I compare three waiting strategies: fixed, linear and exponential. I explain why exponential backoff is the one most scrapers should pick, and how the delay formula works, including jitter and the binary variant. Then I show how to set it up in the two HTTP clients most used for scraping. In Python we use urllib3's Retry with Requests. In JavaScript we use axios-retry with Axios. We run both against an endpoint that always returns 429 and look at the retry logs. I close with best practices and a case where IP rotation does not help.

## What's inside

- How a retry storm happens when many clients retry at the same moment, and what jitter does about it
- Why Requests and Axios need an extra library for retries, and which default behaviors can catch you out, such as idempotent methods only and timeouts across retries
- Checking Retry-After and RateLimit headers, and why most web servers do not send them while API backends sometimes do
- The Royal Mail tracking page as an example of a limit tied to the URL rather than the IP, so rotating proxies does nothing

**In the full article:** The Python and JavaScript code for both clients, the delay formulas, the retry log output, the simulation of binary backoff with jitter, and the full list of best practices.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/rate-limit-scraping-exponential-backoff?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
