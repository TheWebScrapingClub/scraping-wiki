---
name: curl-cffi
type: entity
category: library
first_seen: 2023-10-08
last_updated: 2026-04-22
---

# curl-cffi

## What it is

curl-cffi is a Python binding for curl-impersonate. Rather than using Python's standard SSL stack, it links against BoringSSL, which is the SSL library Chrome uses. This means the TLS handshake it produces is structurally identical to what a real Chrome or Firefox browser sends.

## How it works

Standard Python HTTP libraries (requests, httpx in default configuration) produce TLS Client Hello messages with a specific JA3 fingerprint that anti-bot systems recognize as non-browser traffic. curl-cffi bypasses this by replicating the exact TLS fingerprint of supported browsers, including JA3 hash composition and HTTP/2 frame ordering.

The `impersonate` parameter selects which browser profile to use. Profiles cover Chrome and Firefox versions. At time of use we specified `impersonate="firefox135"`.

Because curl-cffi handles only HTTP, it is most powerful in a hybrid pattern: a browser tool handles the session establishment and any JavaScript-gated authentication, then curl-cffi takes over for the bulk of requests using the cookies and tokens the browser obtained. This captures the stealth benefit of browser-based auth while avoiding the performance cost of rendering pages through a full browser for data extraction.

## TWSC experience

We used curl-cffi as the HTTP client in a hybrid scraping setup targeting [Akamai](akamai.md) on Net-a-Porter. [Camoufox](camoufox.md) handled the initial authentication flow and cookie acquisition. curl-cffi then carried out product data requests using those cookies with `impersonate="firefox135"`.

httpx was tested first in the same role and failed silently. No exception was raised; requests timed out. Inspection confirmed the failure was due to TLS fingerprint mismatch at the Akamai layer. Switching to curl-cffi resolved it.

The speed differential on the same target was approximately 27x in favor of curl-cffi over the browser.

**scrapy-impersonate** is a Scrapy plugin that wraps curl-cffi/curl_impersonate and brings its TLS fingerprinting capabilities directly into Scrapy spiders. Usage requires adding download handler settings and passing `meta={'impersonate': 'chrome110'}` in requests. This tool produced 100% success on Harrods.com (Cloudflare) from both local and datacenter environments (with residential proxy on datacenter). It was also used to bypass Akamai on Gucci.com in approximately 90% of first-try attempts. A known issue: network errors when combined with proxies are sometimes not handled correctly, causing the spider to halt rather than retry.

**hrequests** is a separate Python package that wraps a Go-based TLS library (tls-client by bogdanfinn) and provides similar TLS impersonation for Python. It outputs Akamai-specific HTTP/2 fingerprint strings (`akamai_hash`, `akamai_text`) in addition to JA3, which is useful for debugging Akamai classification.

## HTTP/3 Support

curl-cffi supports HTTP/3 via the `http_version` parameter. Setting `http_version="v3"` (or using the `CurlHttpVersion` enum) routes requests over QUIC. As of late 2025, WAF fingerprinting for HTTP/3 traffic is not widely deployed, meaning HTTP/3 requests may face lighter scrutiny on targets that support the protocol.

One important caveat: enabling Chrome impersonation in curl-cffi defaults back to HTTP/2, since real Chrome itself uses HTTP/2 by default. An explicit `http_version="v3"` is required to override this.

```python
from curl_cffi import requests
from curl_cffi.const import CurlHttpVersion

response = requests.get("https://target.com", http_version="v3")
```

In the Polymarket API benchmark (2026), HTTP/1.1 with a pre-warmed connection pool (50 connections via aiohttp) outperformed HTTP/2 multiplexing by 5-7x for concurrent requests. The reason is that all HTTP/2 streams share one TCP connection and one congestion window, which becomes a bottleneck under high concurrency. Multiple HTTP/1.1 connections each get independent TCP flow control. This does not mean HTTP/2 is always worse — for sequential requests it is slightly faster because it avoids head-of-line blocking — but for high-throughput polling, pooled HTTP/1.1 wins.

## HTTP Caching with ETags

curl-cffi is the correct client for implementing HTTP conditional requests on Cloudflare-protected Shopify stores. The `If-None-Match` header pattern (send stored ETag → receive 304 if unchanged, save bandwidth) fails when using Scrapy's default `RFC2616Policy` because Scrapy's Twisted HTTP client presents a Python/OpenSSL TLS fingerprint, which causes Cloudflare to generate different ETags per request. curl-cffi with Chrome impersonation resolves this by presenting a browser-accurate TLS fingerprint, making ETags consistent across requests.

## Known limitations

- Only handles HTTP. Any JavaScript execution or browser fingerprinting challenge requires a browser tool for that step.
- The impersonation profiles cover specific browser versions. If a target checks for a very recent browser TLS profile that has not yet been added to curl-cffi, the impersonation may fall short.
- HTTP/2 support requires that the HTTP client is configured correctly. requests does not support HTTP/2, which is why httpx was the initial candidate and why the distinction matters in practice.

## Related

- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [camoufox](camoufox.md)
- [ja3proxy](ja3proxy.md)
- [Akamai](../concepts/akamai.md)
- [scrapling](scrapling.md)

## Sources

- [https://substack.thewebscraping.club/p/three-web-scraping-tools-just-discovered](https://substack.thewebscraping.club/p/three-web-scraping-tools-just-discovered)
- [https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi](https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/bypass-akamai-bot-protection](https://substack.thewebscraping.club/p/bypass-akamai-bot-protection)
- [https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot](https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot)
- [https://substack.thewebscraping.club/p/bypassing-akamai-for-free](https://substack.thewebscraping.club/p/bypassing-akamai-for-free)
- [https://substack.thewebscraping.club/p/hrequests-bypass-akamai-with-python](https://substack.thewebscraping.club/p/hrequests-bypass-akamai-with-python)
- [https://substack.thewebscraping.club/p/faster-web-scraping-with-http3](https://substack.thewebscraping.club/p/faster-web-scraping-with-http3)
- [https://substack.thewebscraping.club/p/http-caching-scraping](https://substack.thewebscraping.club/p/http-caching-scraping)
- [https://substack.thewebscraping.club/p/how-to-get-data-from-polymarket-fast](https://substack.thewebscraping.club/p/how-to-get-data-from-polymarket-fast)
