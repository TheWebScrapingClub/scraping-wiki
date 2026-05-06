---
name: Zyte API
type: entity
category: tool
first_seen: 2023-04-06
last_updated: 2026-04-22
sources:
  - hands-on-2-testing-the-new-zyte-api.md
  - web-unblocker-benchmark-march-2024.md
  - web-unblocker-test-kasada.md
  - the-web-unblocker-cost-benchmark.md
---

# Zyte API

## What It Is

Zyte API is a managed web scraping API operated by Zyte (the company that maintains Scrapy). It handles anti-bot bypass, IP rotation, and optionally JavaScript rendering behind a single endpoint. It is classified as a web unblocker. Zyte also operates Scrapy Cloud, a hosted scheduling platform for Scrapy spiders.

## How It Works

Zyte API accepts a target URL and returns page content. Two modes are available:

- **Raw HTTP mode**: Fetches the page without browser rendering. Faster and cheaper per request.
- **Browser rendering mode**: Launches a headless browser, executes JavaScript, and returns the rendered HTML.

Scrapy integration is handled by the `scrapy-zyte-api` package, which acts as a downloader middleware. Per-request pricing adjusts dynamically based on whether rendering is triggered.

## TWSC Experience

Tested in Hands-On #2 (April 2023):

- **Score: 100/100** with browser rendering enabled.
- **Score: 81/100** in raw HTTP mode.

The score gap between rendering modes reflects the limitations of raw HTTP against targets that require JavaScript execution or use JS-based bot challenges. With rendering enabled, Zyte API passed all tested anti-bot targets in the TWSC standard benchmark.

In the March 2024 multi-provider benchmark:
- Passed Cloudflare (Harrods.com).
- Failed Kasada (Canada Goose) in that test.

In the June 2024 Kasada-specific test (101 URLs on canadagoose.com): Zyte failed. This is consistent across both Kasada benchmark tests.

Cost benchmark (2023): Zyte's weighted average pricing across their top 250,000 target sites was approximately $1.974/1,000 requests. At Zalando scale (31GB/30,000 requests), per-GB pricing would have been more favorable. At Zara scale (1.6GB/44,000 requests), per-request pricing was more competitive.

## Known Limitations

- Kasada has been a documented failure point across two separate TWSC benchmarks. This is the clearest known weakness.
- Per-request dynamic pricing makes cost estimation for new targets harder than flat per-GB or per-request pricing.
- Raw HTTP mode scores significantly lower than browser rendering mode, so use cases requiring JS execution need to budget for the higher rendering cost.

## Related

- [web-unblockers](../concepts/web-unblockers.md)
- [Cloudflare](./cloudflare.md)
- [Kasada](./kasada.md)
- [DataDome](./datadome.md)
- [Oxylabs Unblocker](./oxylabs-unblocker.md)
- [Smartproxy Unblocker](./smartproxy-unblocker.md)

## Sources

- [https://substack.thewebscraping.club/p/hands-on-2-testing-the-new-zyte-api](https://substack.thewebscraping.club/p/hands-on-2-testing-the-new-zyte-api)
- [https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024](https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024)
- [https://substack.thewebscraping.club/p/web-unblocker-test-kasada](https://substack.thewebscraping.club/p/web-unblocker-test-kasada)
- [https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark](https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark)
