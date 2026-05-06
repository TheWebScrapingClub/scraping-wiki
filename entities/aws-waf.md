---
name: AWS WAF
type: entity
category: anti-bot
first_seen: 2024-06-06
last_updated: 2026-04-22
sources:
  - bypassing-aws-waf-scraping.md
---

## What it is

AWS WAF (Web Application Firewall) is Amazon Web Services' managed WAF product. It protects web applications by filtering and monitoring HTTP traffic based on predefined security rules. Unlike purpose-built anti-bot systems like Datadome or Kasada, AWS WAF is a general-purpose web security layer that also includes bot detection capabilities. It is not detectable by Wappalyzer.

## How it works

AWS WAF issues a JavaScript challenge to browsers on session start. If the browser environment satisfies the challenge, a session cookie named `aws-waf-token` is issued. This token is then required in subsequent API calls.

The mechanism is a lightweight version of what dedicated anti-bots do: a background validation of the browser environment on first visit, followed by a cookie that certifies passage. Unlike continuous behavioral scoring systems, AWS WAF's challenge appears to be a one-time gate per session, with re-validation occurring only when the token expires.

The `aws-waf-token` cookie format is a structured string that is not user-interpretable. The challenge payload sent to AWS servers on validation is obfuscated and would require reverse engineering to replicate without a browser. Token lifetime varies by site configuration. On Traveloka.com (the tested target), the `aws-waf-token` was valid for four days.

## How to identify it

The `aws-waf-token` cookie name is self-identifying. Inspect session cookies after loading the first page of a protected site. The cookie is typically set on the home page before any navigation occurs.

## TWSC experience

**Traveloka.com (2024)**: Flight fare aggregator for the APAC market. AWS WAF protects the search endpoints. Plain Scrapy retrieves the homepage HTML but does not receive any session cookies suitable for API calls, because the JavaScript challenge runs client-side. The approach that worked: use Playwright (Firefox, headless=False) to load the homepage and the search results page, capture the resulting cookies including `aws-waf-token`, then inject those cookies into Scrapy POST requests to the flight search API. The `aws-waf-token` remained valid for four days in testing, enabling a hybrid pattern: one browser session generates the token, and thousands of Scrapy API calls reuse it until expiration. Covered in [bypassing-aws-waf-scraping](https://substack.thewebscraping.club/p/bypassing-aws-waf-scraping).

The hybrid Playwright-plus-Scrapy approach uses `scrapy-playwright` to handle the browser session and extract cookies, which are then passed into standard Scrapy requests for the actual data collection.

## Known limitations

The reverse engineering path (understanding and replicating the JavaScript challenge payload) is described as time-consuming and short-lived given the obfuscation. The cookie factory pattern (browser session for token, HTTP client for data) is the more durable approach.

Token validity depends on site configuration. The four-day window observed on Traveloka is not guaranteed on other deployments.

Unlike dedicated anti-bot systems, AWS WAF does not perform continuous behavioral scoring. Once the token is obtained, subsequent API requests are evaluated mainly on IP reputation and rate limits, not per-request fingerprinting. This makes it comparatively easier to work around once the token is in hand.

## Related

- [Hybrid Scraping](../concepts/hybrid-scraping.md)
- [Cookie and Session Reuse](../concepts/cookie-session-reuse.md)
- [Cloudflare](cloudflare.md)
- [Playwright](playwright.md)

## Sources

- [https://substack.thewebscraping.club/p/bypassing-aws-waf-scraping](https://substack.thewebscraping.club/p/bypassing-aws-waf-scraping)
