---
name: impersonate-proxy
type: entity
category: anti-bot
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - ytkoka-impersonate-proxy.md
---

# impersonate-proxy

## What it is

impersonate-proxy is a local MITM proxy implemented in Go that allows users to control various network fingerprints and headers via a single YAML configuration file. It enables manipulation of TLS fingerprints (JA3/JA4), HTTP/2 fingerprints, HTTP header order, User-Agent, and source IP headers. A Chrome extension is included for toggling the proxy and switching fingerprint profiles directly from the browser toolbar.

## How it works

The proxy operates as a local MITM intermediary, intercepting traffic from clients such as curl, browsers, or Playwright. It establishes a custom TLS connection with the client and then forwards the request to the target server.

The proxy controls traffic at multiple layers: TLS, HTTP/1.1, and HTTP/2. It can modify TLS cipher suites and extensions to control the JA3/JA4 fingerprint, manipulate HTTP headers (including User-Agent and order), and configure HTTP/2 SETTINGS frames to control the HTTP/2 fingerprint.

## TWSC experience

Not yet tested by TWSC.

## Related

* [mitmproxy](../entities/mitmproxy.md)
* [playwright](../entities/playwright.md)
* [ja3proxy](../entities/ja3proxy.md)


## Sources

- [https://github.com/ytkoka/impersonate-proxy](https://github.com/ytkoka/impersonate-proxy)
