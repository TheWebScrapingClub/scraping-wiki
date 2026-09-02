---
name: tls-fingerprinting
type: concept
first_seen: 2017-01-01
last_updated: '2026-09-02'
sources:
- bypass-akamai-bot-protection.md
- https://konstantinlebedev.com/bypassing-automated-traffic-detection/
- the-lab-33-fingerprinting-at-different.md
- the-stealth-stack-web-scraping.md
- hybrid-scraping-camoufox-curl-cffi.md
- change-ciphers-scrapy.md
- faster-web-scraping-with-http3.md
- http-caching-scraping.md
- antibot-microlink-io.md
- dbi-analyze-open-bullet2-request-mode.md
- itsVentie-Latch.md
- ytkoka-impersonate-proxy.md
---

# TLS Fingerprinting

## Definition

A detection technique that identifies the client making an HTTPS request by analyzing the structure of its TLS ClientHello message, before any application-layer data is exchanged. The most common implementation is JA3, which produces an MD5 hash from five fields in the handshake: TLS version, cipher suite IDs, extension IDs, elliptic curve IDs, and elliptic curve format IDs. JA4 is the more recent successor scheme, more granular and harder to evade, but built on the same principle of hashing handshake fields the client never chooses from code.

## How It Works

Every TLS implementation makes slightly different choices about which cipher suites to advertise, in what order, and which extensions to include. Python's `requests` library uses OpenSSL. Chrome uses BoringSSL. These produce different ClientHello structures, and therefore different JA3 hashes — even when both are connecting to the same server over the same network.

The detection happens at the TCP handshake level. By the time the HTTP request with its User-Agent header arrives, the server has already collected the TLS fingerprint. A script that sends `User-Agent: Mozilla/5.0 Chrome/124...` but generates a Python/OpenSSL JA3 is flagged on the first byte of the handshake.

GREASE (Generate Random Extensions And Sustain Extensibility) is a mechanism Chrome uses to insert randomized dummy cipher entries, preventing ossification of the TLS ecosystem. Ironically, the presence and pattern of GREASE values is itself a fingerprint — real Chrome uses GREASE consistently, while most HTTP clients do not.

HTTP/2 fingerprinting (sometimes called JA3 for HTTP/2) extends the same concept to the application layer: the ordering of HTTP/2 frames, window update values, priority headers, and settings frames vary by client and can identify the underlying library even after TLS is established.

## Where It Matters

[Akamai](../entities/akamai.md) relies heavily on TLS fingerprinting and treats it as a primary signal. [Cloudflare](../entities/cloudflare.md) uses it as a first-layer check before any JavaScript challenge is issued. A mismatched JA3 can result in silent connection drops, empty responses, or immediate CAPTCHA challenges — often with no visible error to diagnose. With [Cloudflare](../entities/cloudflare.md) specifically, a TLS-layer rejection usually returns Cloudflare's own error page (a Ray ID and a 403) rather than a response from the origin. That error page is itself the tell: the request was answered at the edge and never reached the application.

The practical consequence for scrapers is that switching to a "stealth" browser profile while still using `requests` or `httpx` underneath achieves nothing. The TLS handshake exposes the real client regardless of what headers are set.

## What We Tested

We used three tools to inspect TLS fingerprints from different client configurations: Scrapfly's TLS inspection endpoint (tls.scrapfly.io), the Browserleaks TLS API, and the Incolumitas TCP fingerprinting API. Each returns the raw JA3 hash and decoded fields, making it straightforward to compare what a scraper sends against what a real browser sends. A fourth public endpoint, tls.peet.ws, returns parsed JA3 and JA4 values from the connection and is handy for a quick command-line versus browser comparison; it features in Konstantin Lebedev's 2026 TLS-detection primer.

The standard defense is to replace the TLS stack entirely. `curl_cffi` bundles BoringSSL and allows impersonating specific Chrome or Firefox builds at the TLS layer. JA3Proxy routes traffic through a uTLS proxy that rewrites the handshake. `scrapy-impersonate` applies the same approach within the Scrapy pipeline. Each of these produces a JA3 that matches the target browser rather than the underlying Python runtime. For command-line use, [coorl](../entities/coorl.md) takes the same approach in a standalone curl-compatible client that handshakes like Chrome.

An earlier (2022) workaround for Scrapy specifically was changing `DOWNLOADER_CLIENT_TLS_CIPHERS` in settings. The default Scrapy cipher list is long, includes DHE suites that Chrome never uses, and is in a different order than Chrome. Setting this to `'HIGH'` changes the cipher composition enough to avoid some blocklists. Observed cipher count difference: default Scrapy sends ~30 ciphers, Chrome sends ~16. This approach is less reliable than full TLS impersonation but requires no additional dependencies.

## Current State

TLS fingerprinting is now a baseline check on any serious anti-bot deployment. It is no longer an advanced technique — it is table stakes. Scripts that rely on `requests` or `httpx` with default settings will be fingerprinted immediately on [Akamai](../entities/akamai.md) and [Cloudflare](../entities/cloudflare.md) protected targets.

The arms race has moved to HTTP/2 frame fingerprinting and TLS session-level binding, where the server checks whether the same client that performed the TLS handshake is the one sending subsequent requests.

HTTP/3 fingerprinting is an emerging frontier. WAFs have not yet widely deployed HTTP/3 fingerprint analysis. As of late 2025, using HTTP/3 (via `curl_cffi` with `http_version="v3"`) reduces or eliminates detection on some targets. This is expected to close as adoption increases.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [hybrid-scraping](./hybrid-scraping.md)
- [Akamai](../entities/akamai.md)
- [Cloudflare](../entities/cloudflare.md)
- [Camoufox](../entities/camoufox.md)
- [coorl](../entities/coorl.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-akamai-bot-protection](https://substack.thewebscraping.club/p/bypass-akamai-bot-protection)
- [https://konstantinlebedev.com/bypassing-automated-traffic-detection/](https://konstantinlebedev.com/bypassing-automated-traffic-detection/)
- [https://substack.thewebscraping.club/p/the-lab-33-fingerprinting-at-different](https://substack.thewebscraping.club/p/the-lab-33-fingerprinting-at-different)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi](https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi)
- [https://substack.thewebscraping.club/p/change-ciphers-scrapy](https://substack.thewebscraping.club/p/change-ciphers-scrapy)
- [https://substack.thewebscraping.club/p/faster-web-scraping-with-http3](https://substack.thewebscraping.club/p/faster-web-scraping-with-http3)
- [https://substack.thewebscraping.club/p/http-caching-scraping](https://substack.thewebscraping.club/p/http-caching-scraping)
