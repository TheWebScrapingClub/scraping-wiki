---
name: hybrid-scraping
type: concept
first_seen:
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi
  - https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with
  - https://substack.thewebscraping.club/p/hybrid-scraping-browser-login-http-extraction
---

# Hybrid Scraping

## Definition

An architecture that uses a full browser only for the portions of a session that require anti-bot clearance, then hands off to a lightweight HTTP client for all subsequent data requests. The browser handles authentication and challenge resolution; the HTTP client handles scale.

## How It Works

The session handoff is the core mechanism. After the browser completes its interaction with the anti-bot system, the scraper extracts the session cookies — including HttpOnly cookies that are not directly accessible from JavaScript — and transfers them to an HTTP client. From that point, data requests go through the HTTP client rather than the browser.

Three conditions must hold for the handoff to work. The TLS fingerprint of the HTTP client must be consistent with the browser that established the session — if the browser is Firefox-based, the HTTP client must impersonate Firefox at the TLS layer. All cookies must transfer completely, including HttpOnly cookies that require Playwright or a similar tool with access to the full cookie jar. Request headers must match what the real browser was sending, which means capturing them from an actual browser session rather than constructing them manually.

The browser-to-client pairing determines what TLS impersonation is needed. Using [Camoufox](../entities/camoufox.md) (Firefox-based) means the HTTP client must use `curl_cffi` with `impersonate="firefox135"` or equivalent. Using a Chromium-based browser would require a Chrome impersonation profile. Mixing the two — Firefox session, Chrome TLS — exposes the mismatch to [TLS fingerprinting](./tls-fingerprinting.md).

## Where It Matters

The primary motivation is speed. A browser rendering pages and executing JavaScript is orders of magnitude slower than an HTTP client making API calls. We measured a 27x speed difference between browser-only and hybrid approaches on the same target.

The pattern is most valuable when the target site exposes data through internal APIs that the browser's network tab reveals. Once the scraper has valid session credentials, it can call those APIs directly rather than parsing rendered HTML.

Two risks require explicit handling. Anti-bot session cookies can have short TTLs — [Akamai](../entities/akamai.md) cookies in particular can expire in minutes, requiring periodic browser refreshes. Request rate anomalies are also dangerous: a session that viewed three pages in the browser and then immediately issued 100 API calls per second is a behavioral fingerprint that does not match human usage patterns.

Advanced implementations have to account for cookie-to-TLS-session binding, where the server checks that the same TLS session that received a cookie is the one presenting it. This is not universal, but it exists on some high-security targets.

## What We Tested

We tested this pattern against Net-a-Porter ([Akamai](../entities/akamai.md)-protected). The setup used [Camoufox](../entities/camoufox.md) to perform the login and collect session credentials, then `curl_cffi` to call the wishlist API. Using `httpx` instead of `curl_cffi` for the HTTP client stage caused silent timeouts — the TLS fingerprint mismatch was enough for Akamai to drop the connection without an explicit error response.

## Current State

Hybrid scraping is an established pattern with clear implementation requirements. The main constraint is the TLS consistency requirement, which rules out most default HTTP clients and requires deliberate selection of the HTTP client based on the browser used for clearance. The tooling (`curl_cffi`, Camoufox) is mature enough to make this practical.

## Related

- [tls-fingerprinting](./tls-fingerprinting.md)
- [cookie-session-reuse](./cookie-session-reuse.md)
- [homepage-first-navigation](./homepage-first-navigation.md)
- [Camoufox](../entities/camoufox.md)
- [Akamai](../entities/akamai.md)
