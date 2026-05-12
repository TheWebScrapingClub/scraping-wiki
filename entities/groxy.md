---
name: groxy
type: entity
category: library
first_seen: 2026-05-12
last_updated: 2026-05-12
sources:
  - SalzDevs-groxy.md
---

# Groxy

## What it is

Groxy is a small Go library designed for building forward proxy servers. It provides functionality for HTTP request forwarding, HTTPS tunneling using the CONNECT method, and supports features such as middleware hooks, request/response blocking, header helpers, request/response body transforms, and configurable timeouts.

## How it works

The library operates as a forward proxy, allowing traffic to be routed through it. It supports standard HTTP request forwarding and HTTPS tunneling via the `CONNECT` method. Groxy includes middleware hooks that allow users to inspect, modify, or block traffic at various stages of the request and response lifecycle.

For HTTPS inspection, Groxy utilizes local TLS interception (MITM), which is an opt-in feature. This requires users to load and trust a specific Groxy CA certificate to inspect encrypted traffic.

## Known limitations

HTTPS inspection is opt-in only. Without enabling HTTPS inspection configuration, Groxy tunnels HTTPS traffic normally and cannot read encrypted request or response bodies. Users must install and trust the Groxy CA certificate in their browser or operating system to enable inspection.

## Related

- [proxy-server](../entities/proxy-server.md)
- [go-http-client](../entities/go-http-client.md)


## Sources

- [https://github.com/SalzDevs/groxy](https://github.com/SalzDevs/groxy)
