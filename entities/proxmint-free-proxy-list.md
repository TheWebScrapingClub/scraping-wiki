---
name: proxmint-free-proxy-list
type: entity
category: proxy-provider
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - proxmint-free-proxy-list.md
---

# proxmint/free-proxy-list

## What it is

This repository provides a dynamically updated and re-validated list of free network proxies supporting HTTP, HTTPS, SOCKS4, and SOCKS5 protocols. The list is re-validated every 30 minutes to ensure the quality and liveness of the entries.

## How it works

Every proxy in the list is re-tested every 30 minutes by sending a real HTTP request through it to the project's echo endpoint. Entries that fail to respond to this test are dropped from the list.

The project publishes data in both text and JSON formats, including metrics such as uptime percentage, latency, reliability score, and anonymity rating. Anonymity is measured by comparing the forwarding headers received through the proxy against those of a direct request.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

These are free public proxies run by strangers, and they are described as slow, short-lived, and potentially honeypots that log or tamper with traffic. Users are warned never to send logged-in or sensitive traffic through these proxies. Furthermore, the anonymity rating may be misleading; for instance, a proxy that leaks an IP only through the `X-Forwarded-For` header without setting `Via` or `Forwarded` may be rated as "elite."

## Related

- [socks5-proxy](../entities/socks5-proxy.md)
- [proxy-server](../entities/proxy-server.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/proxmint/free-proxy-list](https://github.com/proxmint/free-proxy-list)
