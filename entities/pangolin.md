---
name: pangolin
type: entity
category: proxy-provider
first_seen: 2026-05-29
last_updated: 2026-05-29
sources:
  - news-building-a-peer-to-edge-peer-reverse-proxy.md
---

# Pangolin

## What it is

Pangolin is a peer-to-peer alternative to Cloudflare Tunnels that utilizes a client-to-site VPN combined with an edge reverse proxy to provide cloaked HTTPS traffic. This architecture is designed to solve the tradeoffs associated with traditional reverse proxies, specifically addressing issues related to SSL termination and public exposure.

## How it works

Pangolin flips the traditional architecture by combining peer-to-peer networking with an edge reverse proxy. Instead of relying on public DNS and a cloud server to terminate connections, the client connects to a virtual private network (VPN) and resolves DNS entirely over the tunnels. The HTTPS traffic travels over a blind transport layer and decrypts all the way down at the local network edge, resulting in a service that is fully functional with valid SSL yet cloaked and untraceable from the public internet.

To achieve this, Pangolin hijacks the operating system’s DNS routing by capturing the DNS request at the beginning of its lifecycle. It builds native clients for macOS, Windows, Linux, iOS, and Android to tap into platform-specific networking APIs, such as leveraging System Extensions on macOS to dynamically set a private DNS server. Once the OS-level hook is established, the client starts a tiny local DNS server listening inside the virtual network interface.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The process of hijacking the operating system’s DNS routing is described as the most brittle and complex part of the codebase because every operating system handles DNS configuration differently.

## Related

- [Cloudflare](../entities/cloudflare.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://pangolin.net/news/building-a-peer-to-edge-peer-reverse-proxy](https://pangolin.net/news/building-a-peer-to-edge-peer-reverse-proxy)
