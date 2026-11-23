---
name: reverse-socks-go
type: entity
category: tool
first_seen: 2026-11-23
last_updated: 2026-11-23
sources:
  - zenkdom-reverse-socks-go.md
---

## What it is

reverse-socks-go is a high-performance reverse proxy cluster written in Go. It supports SOCKS5 (TCP/UDP), SOCKS4/4a, HTTP, and HTTPS (CONNECT) proxy protocols, as well as Telegram's MTProto Fake-TLS 1.3 protocol. The project is designed for speed and efficiency, utilizing hardware-accelerated AES-NI encryption and zero-allocation buffer pools.

## How it works

The core of reverse-socks-go is its ability to act as a universal listener on a single port, automatically detecting and handling SOCKS5, SOCKS4/4a, and HTTP/HTTPS proxy requests. For Telegram, it provides an MTProto Fake-TLS engine that masquerades as legitimate TLS 1.3 traffic to bypass firewalls and DPI. The system includes an outbound reverse node pool where exit nodes connect back to a control server, enabling them to function behind NAT or CGNAT. It also features a multi-Tor cluster module for running isolated exit nodes with distinct IP addresses.

## TWSC experience

Not yet tested by TWSC.

## Related

- [socks5-proxy](../entities/socks5-proxy.md)
- [socks5-bridge](../entities/socks5-bridge.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/zenkdom/reverse-socks-go](https://github.com/zenkdom/reverse-socks-go)
