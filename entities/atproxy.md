---
name: atproxy
type: entity
category: proxy-provider
first_seen: 2026-05-29
last_updated: 2026-05-29
sources:
  - lc-at-atproxy.md
---

# atproxy

## What it is

atproxy is a program written in Rust designed to transparently proxy TCP traffic originating from an Android application. It functions by redirecting the app's TCP traffic through an upstream HTTP proxy server.

## How it works

The tool uses `iptables NAT REDIRECT` to route traffic from a specific Android User ID (UID) through an upstream HTTP proxy, such as Burp Suite. This setup allows traffic from a targeted Android app to be transparently routed to an external HTTP proxy server before reaching its original destination.

## TWSC experience

Not yet tested by TWSC.

## Related

- [transparenttorproxy](../entities/transparenttorproxy.md)
- [proxy-server](../entities/proxy-server.md)
- [mobile-app scraping](../concepts/mobile-app-scraping.md)


## Sources

- [https://github.com/lc-at/atproxy](https://github.com/lc-at/atproxy)
