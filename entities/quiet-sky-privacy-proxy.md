---
name: quiet-sky-privacy-proxy
type: entity
category: proxy-provider
first_seen: 2026-07-07
last_updated: 2026-07-07
sources:
  - NW-Hiker-Skier-quietsky-privacy-proxy.md
---

# Quiet Sky Privacy Proxy

## What it is

The Quiet Sky Privacy Proxy is a Cloudflare Worker designed to serve as a privacy core for the Quiet Sky weather proxy. Its primary function is to strip client identity, including the IP address, device headers, cookies, and other identifying information, before any request is forwarded to external weather providers.

## How it works

This Worker sits between the Android application and weather providers, ensuring that providers never receive the client's identity. It enforces two mechanical invariants: first, that identity is unreachable outside the gate, and second, that every authenticated upstream request is built from scratch, meaning no code path copies inbound headers to the request sent to the provider.

The proxy strips identity information such as the IP, device headers, cookies, user-agent, and tokens. It does not hide location data; instead, it forwards the client-selected coordinate precision unchanged, allowing the weather provider to receive the coordinates necessary to answer the query accurately.

## TWSC experience

Not yet tested by TWSC.

## Related

* [Cloudflare](/entities/cloudflare.md)
* [proxy-server](/entities/proxy-server.md)
* [bot-detection-system](/entities/bot-detection-system.md)


## Sources

- [https://github.com/NW-Hiker-Skier/quietsky-privacy-proxy](https://github.com/NW-Hiker-Skier/quietsky-privacy-proxy)
