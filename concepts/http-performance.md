---
name: HTTP Performance in Scraping
type: concept
first_seen: 2022-11-08
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/faster-web-scraping-with-http3
  - https://substack.thewebscraping.club/p/http-caching-scraping
  - https://substack.thewebscraping.club/p/python-async-for-faster-scraping
  - https://substack.thewebscraping.club/p/scraping-high-frequency-python
  - https://substack.thewebscraping.club/p/rate-limit-scraping-exponential-backoff
  - https://substack.thewebscraping.club/p/change-ciphers-scrapy
  - https://substack.thewebscraping.club/p/how-to-get-data-from-polymarket-fast
  - https://substack.thewebscraping.club/p/how-fast-can-you-call-polymarket-apis
  - https://substack.thewebscraping.club/p/scraping-real-time-data-bitstamp
  - https://singh-sanjay.com/2026/03/09/concurrent-requests-reverse-proxy.html
---

# HTTP Performance in Scraping

## Definition

HTTP performance optimization for scraping covers the set of techniques that reduce execution time, bandwidth cost, and infrastructure requirements without changing the data extracted. The main levers are concurrency, protocol selection, caching, and retry behavior.

## How It Works

### Asynchronous Requests

Scraping is I/O-bound. The bottleneck is waiting for network responses, not CPU computation. Synchronous scrapers process one request at a time. Async scrapers initiate multiple requests concurrently and handle responses as they arrive.

Measured comparison on 10 pages (quotes.toscrape.com): synchronous took 3.11 seconds, async via `aiohttp` + `asyncio.gather()` took 0.56 seconds. For 10 pages, the async architecture was 6x faster.

The key Python async tools:
- `asyncio`: Standard library event loop. Core engine for async operations.
- `aiohttp`: Async HTTP client built on asyncio. `ClientSession` reuses connections across requests, avoiding the TCP/TLS handshake overhead per request.
- Scrapy: Built on Twisted (event-driven networking). Handles concurrency automatically without explicit async code. `CONCURRENT_REQUESTS`, `CONCURRENT_REQUESTS_PER_DOMAIN`, and `DOWNLOAD_DELAY` control the rate. `AutoThrottle` adjusts delay dynamically based on server response latency.

### HTTP Caching (Conditional Requests)

A bandwidth optimization native to the HTTP protocol. When a server response includes an `ETag` header, the client stores that value. On the next request to the same URL, the client sends `If-None-Match: <stored_etag>`. If the content has not changed, the server responds with `304 Not Modified` and an empty body. The client consumes near-zero bandwidth for unchanged pages.

Measured on Shopify product JSON endpoints:
- ETag format from Shopify: `"page_cache:11044168:ProductDetailsController:de822deb7906aa6f9932541f4fe3dae9"`
- Pass 1 (no cache): 31,878 bytes downloaded for 4 products
- Pass 2 (conditional): 0 bytes downloaded (100% cache hit rate)

Concrete cost model at scale: 10,000 products, hourly polling, 30 days, 95% unchanged rate, 8KB average response:
- Without conditional requests: 54.9 GB/month
- With conditional requests: 2.7 GB/month
- Saving: 52.2 GB (~95%), approximately $261/month at $5/GB proxy rates

Shopify stores with the native page cache enabled (Allbirds, Kylie Cosmetics, Brooklinen) support conditional requests. Stores with heavy customization or CDN bypass layers (Gymshark, Fashion Nova) do not.

Important constraint: Scrapy's `RFC2616Policy` sends the correct `If-None-Match` headers but fails to receive 304 responses on Cloudflare-protected Shopify stores because Scrapy uses Twisted's HTTP client, which presents a standard Python TLS fingerprint. Cloudflare distinguishes it from a real browser and generates different ETags per request. Using `curl_cffi` with Chrome impersonation resolves this.

### HTTP/3

HTTP/3 runs over QUIC (UDP-based) instead of TCP. Key differences for scraping:
- 0-RTT connection resumption: reduced latency on repeated connections to the same server
- No head-of-line blocking: packet loss on one request does not block others
- Connection migration: sessions survive IP changes (useful with rotating proxies)
- Built-in TLS 1.3: no separate TLS handshake step

Adoption as of November 2025: 35.9% of websites support HTTP/3. 92.75% of browsers can use it.

HTTP/3 fingerprinting is not yet widely deployed by WAFs, making HTTP/3 requests potentially less scrutinized than HTTP/2 or HTTP/1.1. The `curl_cffi` documentation notes: "for a lot of sites, there is less or even none detection when using http/3."

Python usage with `curl_cffi`:
```python
from curl_cffi import requests
from curl_cffi.const import CurlHttpVersion

response = requests.get("https://wordpress.org", http_version="v3")
```

Note: enabling Chrome impersonation in `curl_cffi` defaults back to HTTP/2, as Chrome itself defaults to HTTP/2. Explicit `http_version="v3"` overrides this.

### TLS Cipher Customization in Scrapy

Scrapy's default TLS cipher list is identifiable as Python/OpenSSL. The `DOWNLOADER_CLIENT_TLS_CIPHERS='HIGH'` setting changes the cipher list, which alters the JA3 fingerprint enough to avoid some blocklists. This was an early (2022) workaround before tools like `curl_cffi` existed. It is less reliable than full TLS impersonation but does not require additional dependencies.

### HTTP/1.1 vs HTTP/2 Under High Concurrency

Protocol theory suggests HTTP/2 multiplexing should outperform HTTP/1.1 for concurrent requests. The Polymarket API benchmark (2026) contradicts this for server-to-server high-frequency polling. Testing 50 concurrent workers against Polymarket's `/midpoint` endpoint from AWS eu-west-2 produced:

- aiohttp with 50 HTTP/1.1 connections (pre-warmed): **3,012 rps**
- httpx with HTTP/2 multiplexing: **451 rps**

The 6.7x difference is explained by TCP-level mechanics. All HTTP/2 streams share one TCP connection, one congestion window, and one TLS encryption pipeline. Under 50 concurrent requests, this single connection becomes the bottleneck. With 50 independent HTTP/1.1 connections, the OS distributes I/O across 50 TCP flows with independent buffering and flow control.

HTTP/2 is slightly better for sequential requests because it eliminates head-of-line blocking at the HTTP layer. For concurrent high-throughput polling from a co-located server, pooled HTTP/1.1 connections win.

### Connection Pre-warming

Cold connections inflate tail latency. A pool of 50 concurrent connections, all starting cold, must each complete a TCP handshake and TLS exchange before the first real request. In the Polymarket benchmark, Python's p99 latency from eu-west-2 was 111ms without pre-warming and 32ms after pre-warming. The fix is to open all connections and send one throwaway request before the timer starts. In production, pre-warming should happen at startup.

### Server Co-location

Network round-trip dominates API polling performance more than any code-level optimization. In the Polymarket benchmark, the same Python aiohttp code achieved 493 rps from AWS us-east-1 (Virginia) and 3,012 rps from AWS eu-west-2 (London) — a 6x difference. The Polymarket origin server is in or near London; Cloudflare's `cf-ray` header confirmed which PoP handled each request, and the London PoP showed 27ms first-byte latency vs 113ms from Virginia.

A commercial VPS marketed as "optimized for Polymarket" was located in Dublin and routed through the DUB PoP. Its performance was indistinguishable from the Virginia data center. A standard t3.micro in eu-west-2 at $7.50/month outperformed it by 4x.

The priority ranking for API performance optimization, from highest to lowest impact: location > connection strategy > I/O architecture > language.

### Reverse Proxy Concurrency Models (ATS, HAProxy, Envoy)

For scrapers that operate their own reverse proxy layer (scraping fleets, proxy aggregators, middleware), or when analyzing how anti-bot infrastructure behaves under load, understanding the concurrency model of the proxy component is relevant. A 2026-03 technical analysis compared Apache Traffic Server, HAProxy, and Envoy at high connection counts.

The core constraint is the thin layer: a reverse proxy holds thousands of simultaneous connections (active, keepalive, idle WebSocket streams), so per-connection memory overhead multiplies directly. At 10,000 concurrent connections: 1 KB/connection = 10 MB total; 10 KB/connection = 100 MB; 100 KB = 1 GB. Thread-per-connection (Apache HTTPd prefork) fails here: a Linux thread default stack is 8 MB, so 10,000 connections requires 80 GB of stack space before any work is done. The solution is event loops: one thread manages thousands of file descriptors via epoll (Linux) or kqueue (macOS/BSD), waking up only when a socket becomes readable or writable.

**Apache Traffic Server (ATS):** Pool of event threads, one per CPU core (`proxy.config.exec.thread.limit`). Each connection is owned by one ET_NET thread for its lifetime. Processing model is the continuation system — callback chains scheduled on the event thread. A blocking call in any plugin stalls all connections on that thread. Strong for CDN-scale HTTP caching; weak for general-purpose reverse proxy use.

**HAProxy:** Originally single-process, single-thread event loop. Multi-threading added in version 1.8 via `nbthread`. Uses `SO_REUSEPORT` to distribute new connections across threads without a shared accept mutex. Per-object spinlocks protect shared state (stick-tables, counters, health info). Per-connection overhead historically in the low hundreds of bytes. Strong for L4/L7 load balancing with predictable latency and static configuration; hot reload via process replacement (`haproxy -sf`).

**Envoy:** Thread-per-core with complete worker isolation — worker threads share nothing by design. Listener thread dispatches connections to workers via consistent hash. Each worker holds its own config snapshot (delivered via xDS protocol), its own upstream connection pool, and its own filter chain execution. No inter-worker coordination required for request processing. Filter chains (JWT validation, header rewriting, rate limiting, gRPC transcoding) are composable and thread-local, requiring no locks. Higher memory footprint than HAProxy due to per-worker state duplication. Strong for programmatically-driven routing, service mesh sidecars, and complex L7 processing.

**Graceful restart** is a shared pattern: all three allow the new process to take over listening sockets while the old process drains in-flight connections. **Circuit breaking** prevents backend failure from cascading into proxy resource exhaustion (Envoy: per-cluster thresholds on pending/active/retry counts; HAProxy: `maxconn` per server with health-check-driven state transitions).

Source: [https://singh-sanjay.com/2026/03/09/concurrent-requests-reverse-proxy.html](https://singh-sanjay.com/2026/03/09/concurrent-requests-reverse-proxy.html) (2026-03-09)

## Rate Limiting and Exponential Backoff

Rate limiting is the primary server-side defense against excessive request rates. The server tracks requests per IP (or per token/session) within a time window. When the threshold is exceeded, the server returns:
- `429 Too Many Requests` (most common)
- `403 Forbidden` (some implementations)
- `503 Service Unavailable` (rarer)

Two primary countermeasures:
1. **Proxy rotation**: Distributes load across many IPs. Each IP appears below the rate limit threshold.
2. **Exponential backoff**: Increases wait time between retries geometrically after each failure.

Exponential backoff formula: `delay = jitter + base * (2 ** retries)`

Binary exponential backoff with `base=1`: delay sequence is 2s, 4s, 8s, 16s...

Python implementation with `urllib3`:
```python
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    backoff_jitter=0.3
)
```

Some websites apply rate limits per URL, not per IP (observed on Royal Mail tracking). In these cases, proxy rotation does not help. The `Retry-After` response header, when present, provides the exact wait time.

## What We Tested

- **Async vs sync**: 6x speedup on 10 pages with `aiohttp`. Extrapolated to thousands of pages, this difference is material for real-time data needs.
- **HTTP caching on Shopify**: 100% bandwidth reduction on unchanged products. Conditional requests work reliably with `curl_cffi` (Chrome impersonation) but fail with Scrapy's `RFC2616Policy` on Cloudflare-protected targets.
- **HTTP/3**: Confirmed working via `curl_cffi` on WordPress.org. No fingerprint resistance testing performed yet.
- **Scrapy cipher changes**: Changing `DOWNLOADER_CLIENT_TLS_CIPHERS` to `HIGH` alters JA3. Less reliable than `curl_cffi` impersonation. Only practical for targets that rely on blocklisting known Scrapy JA3 hashes.

## Current State (as of 2026-04)

Async scraping is the baseline for any production pipeline. HTTP caching is an underused optimization that applies directly to recurring scraping on platforms like Shopify. HTTP/3 is worth testing on targets that support it, particularly because WAF fingerprinting for HTTP/3 lags behind HTTP/2. Exponential backoff is table stakes for any resilient scraper.

## Related

- [tls-fingerprinting](./tls-fingerprinting.md)
- [proxy-fundamentals](./proxy-fundamentals.md)
- [api-scraping](./api-scraping.md)
- [curl-cffi](../entities/curl-cffi.md)
