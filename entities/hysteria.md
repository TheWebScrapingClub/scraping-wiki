---
name: hysteria
type: entity
category: proxy-provider
first_seen: 2026-05-14
last_updated: 2026-05-14
sources:
  - apernet-hysteria.md
---

# Hysteria

## What it is

Hysteria is a powerful, lightning fast, and censorship-resistant proxy. It is designed to operate efficiently over unreliable networks while maintaining resistance against detection and blocking by censors.

## How it works

Hysteria is powered by a customized QUIC protocol, which allows it to deliver unparalleled performance over lossy networks. This protocol enables the proxy to masquerade as standard HTTP/3 traffic, making it difficult for censors to detect and block.

It offers a wide range of modes, including SOCKS5, HTTP Proxy, TCP/UDP Forwarding, Linux TProxy, and TUN support. It also features built-in support for custom authentication, traffic statistics, and access control for easy integration into infrastructure.

## TWSC experience

Not yet tested by TWSC.

## Related

- [proxy-server](../entities/proxy-server.md)
- [roxy](../entities/roxy.md)


## Sources

- [https://github.com/apernet/hysteria](https://github.com/apernet/hysteria)
