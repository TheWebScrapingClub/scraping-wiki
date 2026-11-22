---
name: torgrid
type: entity
category: tool
first_seen: 2026-11-22
last_updated: 2026-11-22
sources:
  - localhost-server-TorGrid.md
---

# TorGrid

## What it is

TorGrid is a self-healing, rotating proxy pool that provides access to a large number of Tor exit IP addresses. It functions as a SOCKS5/HTTP proxy and can also be used as a split-tunnel Android VPN. It is available for Android, Windows, and Linux operating systems, aiming for a zero-configuration setup.

## How it works

TorGrid establishes connections to a large number of unique Tor exit nodes in parallel. These connections are managed through isolated "daemon circuits." The tool provides a local gateway, accessible via SOCKS5 on port 10000 and HTTP/HTTPS on port 8080, through which all traffic is routed. It automatically rotates the exit IP for browser reloads and scraper requests, while simultaneously managing and healing dead circuits in the background without interrupting active connections.

The system supports different grid sizes, ranging from 100 to 1,100 unique exit IPs. It includes built-in support for `obfs4` bridges to circumvent censorship and offers options for whole-phone VPN or per-app split-tunneling on Android. For public Wi-Fi security, it defaults to blocking external access to the proxy, but can be configured to allow access over a local network.

## TWSC experience

Not yet tested by TWSC.
## Related

The source mentions Tor and proxy functionality, which are conceptually related to [proxy-fundamentals](../concepts/proxy-fundamentals.md) and [socks5-proxy](../entities/socks5-proxy.md). It also mentions Android VPN capabilities, which relates to [mobile-app-scraping](../concepts/mobile-app-scraping.md).


## Sources

- [https://github.com/localhost-server/TorGrid](https://github.com/localhost-server/TorGrid)
