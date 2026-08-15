---
name: Web Unblockers
type: concept
first_seen: 2023-04-06
last_updated: '2026-08-15'
sources:
- hands-on-2-testing-the-new-zyte-api.md
- testing-smartproxy-site-unblocker.md
- oxylabs-web-unblocker-test.md
- hands-on-6-testing-the-infatica-web.md
- web-unblocker-benchmark-march-2024.md
- the-web-unblocker-cost-benchmark.md
- web-unblocker-test-kasada.md
- web-unblocker-vs-browser-as-a-service-scraping.md
- sensecollect-com.md
- guestlist-tools.md
- demo.md
- NW-Hiker-Skier-quietsky-privacy-proxy.md
- open-sourcing-our-privacy-proxy-cli.md
---

# Web Unblockers

## Definition

A web unblocker is a managed API that accepts a target URL and returns the page content after transparently handling IP rotation, CAPTCHA solving, browser fingerprinting, and anti-bot bypass on the provider's infrastructure. The caller makes a standard HTTP request; the provider does the work of getting through the target's defenses.

Web unblockers are distinct from raw proxy services and from Browser-as-a-Service (BaaS) platforms. A proxy gives you an IP to route through. An unblocker gives you a response. A BaaS gives you a cloud browser you control directly. The unblocker is the most opaque of the three.

## How It Works

The request flow for most unblockers follows the same pattern: the caller sends the target URL (either as a GET/POST endpoint or formatted as a proxy URL), the unblocker selects an appropriate IP (residential, mobile, or datacenter depending on target difficulty), optionally executes JavaScript in a headless browser to solve challenges, and returns the rendered HTML. Some providers also handle JavaScript rendering via a header flag rather than always.

Pricing models vary. Some providers bill per GB of bandwidth consumed (making rendering-heavy pages expensive). Others bill per request (making large-page targets cheaper but simple API targets expensive). Choosing the wrong model for a given workload can multiply effective cost by 5-10x.

### Unblocker vs. Browser-as-a-Service

The distinction matters operationally. An unblocker is stateless: you send a URL, you get HTML back. You have no control over the browser session, headers, cookies, or navigation sequence. A BaaS gives you a remote browser you can script with Playwright or Puppeteer: you control page flow, can log in, handle pagination, click through flows. The tradeoff is complexity and cost. BaaS platforms require you to write the browser automation logic; unblockers abstract it away.

As of April 2025, the BaaS space includes: Browserbase, Browserless, Browser Use, Hyperbrowser, Lightpanda, and Rebrowser.

## Where It Matters

Web unblockers sit at the top of the Proxy Ladder, where every cheaper option has already failed. They are the last resort before manual data collection or data purchasing. Their primary market is targets with Cloudflare, DataDome, Kasada, PerimeterX, or similar enterprise anti-bot deployed.

The economics of unblockers change the cost calculation relative to raw proxies. At Zalando scale (31GB/30,000 requests), per-request pricing is significantly more expensive than per-GB. At Zara scale (1.6GB/44,000 requests), the per-request model performs better because pages are small. The choice of pricing model matters as much as the choice of provider.

## What We Tested

### March 2024 Multi-Provider Benchmark (5 unblockers, 4 anti-bot targets)

Tested via Scrapy with each unblocker configured as a proxy middleware. Targets: Harrods.com (Cloudflare), Footlocker.it (DataDome), Canada Goose (Kasada), Neiman Marcus (PerimeterX).

Results by anti-bot target:
- **Cloudflare (Harrods)**: All 5 providers passed.
- **DataDome (Footlocker.it)**: Only Zenrows passed, and only partially.
- **Kasada (Canada Goose)**: Bright Data, Oxylabs, and Smartproxy passed. Infatica and Zyte failed.
- **PerimeterX (Neiman Marcus)**: All providers passed.

DataDome emerged as the hardest target for unblockers across testing.

### Kasada-Specific Benchmark (June 2024, 101 URLs on canadagoose.com)

| Provider | Success | Time | Cost |
|---|---|---|---|
| Bright Data | 96/100 | 58 min | $0.303 |
| NetNut | 97/100 | 595s | not disclosed |
| Oxylabs | 96/100 | 10 min | $0.10 |
| Smartproxy | 92/100 | 413s | $0.13 EUR |
| Zenrows | 95/100 | 76 min | $0.70 EUR |
| Infatica | Failed | — | — |
| Zyte | Failed | — | — |

Oxylabs was cheapest at $0.10 for 101 URLs. Zenrows was most expensive at $0.70 for the same job. Infatica and Zyte could not bypass Kasada in this test.

### Individual Provider Scores (TWSC Hands-On Series)

Scores reflect overall performance across TWSC's standard anti-bot test set.

**Zyte API (2023)**: 100/100 with browser rendering enabled. 81/100 in raw HTTP mode. Per-request dynamic pricing. Scrapy integration via scrapy-zyte-api package. The pricing model adjusts cost based on whether rendering is required.

**Oxylabs Web Unblocker (2023)**: 96/100. Passed all tested anti-bots. Starting at $15/GB. JavaScript rendering triggered via `X-Oxylabs-Render` header. Best dashboard among tested providers, with per-domain traffic breakdown. Cheapest on the June 2024 Kasada test at $0.10/101 URLs.

**Smartproxy Site Unblocker (2023)**: 80/100. 100% success on Cloudflare, DataDome, PerimeterX. Mixed on F5. 0% on Kasada. Price at time of test: $12/GB. Kasada failure is consistent with the broader pattern.

**Infatica (2023)**: 80/100. Passes 4/5 anti-bots with JS rendering. Kasada fails. Distinctive pricing at $1/1,000 requests vs. Bright Data's $3/1,000 at the time. API model differs from peers: POST endpoint where the target URL goes in the request payload, not as a proxy URL.

### Cost Benchmark (2023, Zalando and Zara)

Zalando: 31GB across 30,000 requests. At Zyte's pricing structure, the weighted average across their top 250,000 target sites was approximately $1.974/1,000 requests. Per-GB pricing advantages per-request at this page size.

Zara: 1.6GB across 44,000 requests. Per-request models are more competitive here because pages are small relative to request count.

## Current State

As of April 2025, thirteen unblocker providers have been identified in the TWSC corpus. Pricing ranges from NetNut at $4.80/GB to Bright Data at $1.05/1,000 URLs at the per-request end. No single provider dominates across all anti-bot targets. DataDome remains the hardest target for unblockers. Kasada is hard but solvable by the leading providers (Bright Data, Oxylabs, NetNut, Smartproxy). Cloudflare and PerimeterX are passed by most providers.

The gap between unblockers and Browser-as-a-Service is closing as BaaS platforms add managed navigation features and unblockers add stateful session support.

## Related

- [proxy-fundamentals](./proxy-fundamentals.md)
- [Cloudflare](../entities/cloudflare.md)
- [DataDome](../entities/datadome.md)
- [Kasada](../entities/kasada.md)
- [PerimeterX](../entities/perimeterx.md)
- [Zyte API](../entities/zyte-api.md)
- [Oxylabs Unblocker](../entities/oxylabs-unblocker.md)
- [Smartproxy Unblocker](../entities/smartproxy-unblocker.md)
- [scraping-infrastructure](./scraping-infrastructure.md)

## Sources

- [https://substack.thewebscraping.club/p/hands-on-2-testing-the-new-zyte-api](https://substack.thewebscraping.club/p/hands-on-2-testing-the-new-zyte-api)
- [https://substack.thewebscraping.club/p/testing-smartproxy-site-unblocker](https://substack.thewebscraping.club/p/testing-smartproxy-site-unblocker)
- [https://substack.thewebscraping.club/p/oxylabs-web-unblocker-test](https://substack.thewebscraping.club/p/oxylabs-web-unblocker-test)
- [https://substack.thewebscraping.club/p/hands-on-6-testing-the-infatica-web](https://substack.thewebscraping.club/p/hands-on-6-testing-the-infatica-web)
- [https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024](https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024)
- [https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark](https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark)
- [https://substack.thewebscraping.club/p/web-unblocker-test-kasada](https://substack.thewebscraping.club/p/web-unblocker-test-kasada)
- [https://substack.thewebscraping.club/p/web-unblocker-vs-browser-as-a-service-scraping](https://substack.thewebscraping.club/p/web-unblocker-vs-browser-as-a-service-scraping)
