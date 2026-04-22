---
name: scrapling
type: entity
category: library
first_seen: 2024-01-01
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/scrapling-hands-on-guide
  - https://substack.thewebscraping.club/p/nike-scraping-benchmark
---

# Scrapling

## What it is

Scrapling is a Python scraping library by D4Vinci (Karim Shoair). Version 0.3 was a complete rewrite of the earlier versions, significantly changing the architecture and expanding the fetcher options. It handles both the data fetching and the parsing phases, with a clean separation between the two.

## How it works

Scrapling organizes work into two phases: fetch, then parse. Three fetcher classes cover different access requirements:

**Fetcher** handles static HTTP requests with TLS impersonation. It is the fast path for targets that do not require JavaScript execution.

**DynamicFetcher** uses [Playwright](playwright.md) with Patchright stealth applied. It is the browser-based fetcher for targets that require JavaScript rendering.

**StealthyFetcher** uses a modified version of [Camoufox](camoufox.md) internals. This is distinct from importing and using the Camoufox library directly: Scrapling maintains its own modified build. StealthyFetcher can bypass [Cloudflare](cloudflare.md) Turnstile even in headless mode.

Session classes support tab pooling for concurrent fetching. The parsing layer includes adaptive scraping through similarity scoring, which tracks element relationships rather than fixed selectors. When a site redesign moves elements around, the similarity model can still locate the correct node without a selector update.

Performance numbers from the Scrapling benchmark: up to 1735x faster than BeautifulSoup on equivalent parsing tasks. JSON serialization runs approximately 10x faster than comparable Python parsing libraries.

## TWSC experience

We covered Scrapling in a hands-on guide that tested all three fetchers against real targets. StealthyFetcher's ability to clear Cloudflare Turnstile in headless mode is notable, since most browser tools require headed mode or virtual display workarounds to pass Turnstile. The adaptive scraping feature is practically useful for long-running scrapers on sites that redesign frequently, as it reduces maintenance overhead for selector updates.

**Nike.com benchmark (2026):** In a five-tool benchmark on 1,000 Nike product URLs (Austria EN locale, Akamai-protected), `Fetcher.get()` with `impersonate='chrome'` and `stealthy_headers=True` achieved 100% success at approximately 1.96 requests per second. This used the simple Fetcher class, not StealthyFetcher. Nike's product pages are server-side rendered and protected by Akamai TLS fingerprinting only (no JS challenges), making full browser automation unnecessary. The `Fetcher` class provided sufficient fingerprint fidelity. This confirmed the tiered fetcher design: use `Fetcher` when TLS impersonation is sufficient, escalate to `StealthyFetcher` or `DynamicFetcher` only when JavaScript challenges require it.

## Known limitations

- StealthyFetcher uses an internal Camoufox build, not the publicly updated Camoufox release. Any divergence between the two in response to new anti-bot techniques requires a Scrapling update, not a Camoufox update.
- The library is younger than [Playwright](playwright.md) or Selenium-based tools. Edge cases in the adaptive scraping logic may appear on unusual page structures.

## Related

- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [Cloudflare](cloudflare.md)
- [camoufox](camoufox.md)
- [playwright](playwright.md)
- [curl-cffi](curl-cffi.md)
