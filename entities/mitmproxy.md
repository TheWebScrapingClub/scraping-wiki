---
name: mitmproxy
type: entity
category: tool
first_seen: 2026-05-13
last_updated: 2026-05-13
sources:
  - agudulin-simple-proxy.md
---

# mitmproxy

## What it is

mitmproxy is a small interceptor written in Python used to build a proxy, exemplified by the `simple-proxy` project. It is designed to block certain telemetry providers while allowing applications to continue functioning normally.

## How it works

The bundled addon intercepts network requests and logs every intercepted request. Specifically, it returns a `202 {"status":"ok"}` response for telemetry endpoints.

## TWSC experience

Not yet tested by TWSC.

## Related

- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/agudulin/simple-proxy](https://github.com/agudulin/simple-proxy)
