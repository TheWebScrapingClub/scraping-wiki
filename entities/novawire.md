---
name: novawire
type: entity
category: proxy-provider
first_seen: 2026-10-29
last_updated: 2026-10-29
sources:
  - novawire-dev.md
---

# NovaWire

## What it is

NovaWire is a fast, native debugging proxy designed to intercept, read, rewrite, and replay HTTP/HTTPS traffic. It functions as a single window tool that allows users to inspect network exchanges, modify traffic in real-time, and generate documentation from captured data.

## How it works

The engine is a Rust MITM proxy that captures raw socket bytes, handling protocols such as HTTP/1.1, HTTP/2, WebSocket frames, and SSE events. It decrypts HTTPS and HTTP/2 traffic using a root CA to make exchanges readable.

NovaWire allows users to read various body types, including JSON, XML, HTML, rendered pages, images, and compressed bodies, decoding them for inspection. It also attributes proxied requests to the executable and PID behind them, providing context for the traffic.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The proxy utilizes a bounded 32-512 MiB body store, and truncation is flagged when this limit is reached.

## Related

* [mitmproxy](../entities/mitmproxy.md)
* [curl](../entities/curl.md)


## Sources

- [https://novawire.dev](https://novawire.dev)
