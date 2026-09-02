---
name: pingora
type: entity
category: proxy-provider
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet.md
---

# Pingora

## What it is

Pingora is an in-house HTTP proxy built in Rust by Cloudflare, designed to serve over a trillion requests daily. It was developed to boost performance and enable new features for Cloudflare customers while requiring significantly fewer CPU and memory resources than the previous proxy infrastructure. Pingora powers various Cloudflare features including CDN, Workers fetch, Tunnel, Stream, and R2.

## How it works

Pingora was built to replace the legacy NGINX service due to architectural limitations that hurt performance and efficiency at Cloudflare's scale. The NGINX worker architecture resulted in unbalanced load across CPU cores and poor connection reuse, as the connection pool was per worker.

Pingora addresses these issues by fundamentally addressing the worker/process model to improve load balancing and connection reuse, which speeds up the time-to-first-byte (TTFB) of requests and reduces resource consumption.

## TWSC experience

Not yet tested by TWSC.

## Related

- [rustwright](../entities/rustwright.md)
- [proxy-server](../entities/proxy-server.md)
- [cloudflare](../entities/cloudflare.md)


## Sources

- [https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/)
