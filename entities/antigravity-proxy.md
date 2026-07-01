---
name: antigravity-proxy
type: entity
category: proxy-provider
first_seen: 2026-07-01
last_updated: 2026-07-01
sources:
  - rajibbora1965-WhatsAppCoding.md
---

# antigravity-proxy

## What it is

The `antigravity-proxy` is a local Node.js proxy designed to function as a TLS-terminating server. Its primary role is to intercept network traffic that is bound for Google's generative language servers, facilitating the operation of the WhatsApp Coding framework.

## How it works

This proxy operates using host-level loopback routing, acting as a TLS-terminating server on ports 4000/443. It utilizes a self-signed wildcard certificate to intercept traffic destined for generative language servers.

The proxy performs context sifting and sanitization by automatically stripping repetitive inline system prompts, workspace configurations, and metadata blocks from the traffic. It also reconstructs mock headers, including artificial safety ratings and grounding metadata, for inbound completion streams to ensure smooth processing by the desktop application.

## TWSC experience

Not yet tested by TWSC.

## Related

- [mitmproxy](../entities/mitmproxy.md)
- [nodejs-based-scraper](../entities/nodejs-based-scraper.md)


## Sources

- [https://github.com/rajibbora1965/WhatsAppCoding](https://github.com/rajibbora1965/WhatsAppCoding)
