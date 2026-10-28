---
name: proxium
type: entity
category: proxy-provider
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - koldakov-proxium.md
---

# Proxium

## What it is

Proxium is a self-hosted HTTP and SOCKS5 proxy gateway that includes an administrative user interface for managing accounts, access control lists (ACLs), TLS settings, quotas, and outgoing IP pools. It is designed to be open source and run via Docker, offering a comprehensive solution for various proxy use cases.

## How it works

Proxium functions as an HTTP and SOCKS5 proxy, capable of detecting the protocol based on the first byte received. It supports TLS connections to the proxy on the same ports, ensuring credentials are never transmitted in the clear. The system manages all configurations, including accounts, policies, and IP pools, through a database and an API accessible via a web admin panel.

## TWSC experience

Not yet tested by TWSC.

## Related

- [socks5-proxy](../entities/socks5-proxy.md)
- [mitmproxy](../entities/mitmproxy.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/koldakov/proxium](https://github.com/koldakov/proxium)
