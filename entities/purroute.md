---
name: purroute
type: entity
category: proxy-provider
first_seen: 2026-06-24
last_updated: 2026-06-24
sources:
  - femboyisp-purroute.md
---

# Purroute

## What it is

Purroute is an advanced proxy server designed to act as an auto-detecting proxy router or gateway. It supports the detection of inbound proxy protocols, such as SOCKS5, SOCKS4/4a, HTTP, and HTTPS-CONNECT, and performs protocol translation between them. It also supports multi-hop proxy chaining and enforces per-user authentication and bandwidth limits.

## How it works

The router detects the inbound proxy protocol from the initial bytes of each connection and translates it to the appropriate upstream protocol. It manages traffic flow through a single proxy or a multi-hop chain, allowing for protocol translation across all inbound-to-upstream combinations.

It supports tag-based exit selection by encoding routing tokens (such as country, city, ISP, or type) into the proxy username, allowing clients to select an exit point from a set of tagged upstreams. Authentication is handled by a pluggable `AuthBackend` which can be configured for inline users or integration with PostgreSQL.

## TWSC experience

Not yet tested by TWSC.

## Related

- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/femboyisp/purroute](https://github.com/femboyisp/purroute)
