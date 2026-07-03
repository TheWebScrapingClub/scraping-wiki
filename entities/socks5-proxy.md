---
name: socks5-proxy
type: entity
category: proxy-provider
first_seen: 2026-07-03
last_updated: 2026-07-03
sources:
  - Koukyosyumei-claude-codes-socks5-proxy-bypass-why-egress-filtering-must-happen-a.md
---

# SOCKS5 proxy

## What it is

A SOCKS5 proxy is used by systems, such as Claude Code’s sandbox, to route outbound traffic and enforce an egress allowlist. This mechanism is responsible for permitting connections to specific domains while blocking all others.

## How it works

The SOCKS5 proxy enforces the egress allowlist by validating the requested hostname using JavaScript, typically employing an `endsWith()`-style string check against allowed suffixes. This application-layer check is intended to determine if a connection is permitted.

The bypass exploits a discrepancy between how JavaScript strings and C strings handle hostnames. While the JavaScript filter sees the full string and approves the connection, the underlying system's `getaddrinfo()` function treats the string as a C string and terminates at an embedded null byte (`\x00`), resolving only a truncated, blocked hostname.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The enforcement mechanism is fragile because it relies on an application-layer name match between two different parsing systems: JavaScript and C. JavaScript strings can contain null bytes, whereas C strings cannot. This disagreement means that the decision made by the application layer (the allowlist check) is not always enforced on the actual connection being made, allowing a blocked destination to bypass the filter.

## Related

* [proxy-server](../entities/proxy-server.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)
* [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://medium.com/@Koukyosyumei/claude-codes-socks5-proxy-bypass-why-egress-filtering-must-happen-at-the-boundary-aaa445019e69](https://medium.com/@Koukyosyumei/claude-codes-socks5-proxy-bypass-why-egress-filtering-must-happen-at-the-boundary-aaa445019e69)
