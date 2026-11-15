---
type: article_summary
title: 'THE LAB #104: Bypassing AWS WAF on IMDB with Scrapling '
slug: bypassing-aws-waf-with-scrapling
canonical_url: https://www.scraping.club/p/bypassing-aws-waf-with-scrapling
publish_date: '2026-05-15'
visibility: premium
topics:
- scraping-infra
- http-clients
- cloudflare
- datadome
description: Testing whether curl_cffi, httpx-curl-cffi and rnet can get past AWS WAF on IMDB without a browser, and what Scrapling's browser step adds.
source_hash: daa07d7d2a62a667
---

# THE LAB #104: Bypassing AWS WAF on IMDB with Scrapling 

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-05-15 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-aws-waf-with-scrapling?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

AWS WAF is the protection we meet most often on Amazon's public properties, and it also sits in front of many third-party sites built on AWS. We covered it two years ago in The Lab #53, but that target also ran DataDome, so the analysis had to account for two systems at once. This time we wanted AWS WAF alone.

IMDB fits: an Amazon subsidiary, a standard AWS WAF deployment, and no other anti-bot according to Wappalyzer. We tested three Python HTTP clients with strong TLS impersonation, curl_cffi, httpx-curl-cffi and rnet, against the home page and a title page, with a plain httpx client as control. Then we looked at Scrapling's StealthyFetcher as the browser step. The question is whether a convincing TLS fingerprint and headers are enough, or whether we need JavaScript rendering. If we do, we want the smallest browser step, so the rest of the work can run on a cheap HTTP client.

## What's inside

- How the AWS WAF challenge works: the 202 response, the token script on token.awswaf.com, and the aws-waf-token cookie that unlocks the real page.
- Why a token-based gate behaves differently from systems that score every request, and what still applies afterward (IP reputation and rate limits).
- What each tool brings: curl_cffi's curl-impersonate profiles, httpx-curl-cffi's httpx programming model, rnet's own Rust impersonation stack.
- The test design: two URLs, redirects off, full capture of status, headers, cookies and body, and pinned library versions on Python 3.11.

**In the full article:** The test results for each client, the Scrapling configuration, the probe scripts and the saved responses are in the full article and in the private GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-aws-waf-with-scrapling?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
