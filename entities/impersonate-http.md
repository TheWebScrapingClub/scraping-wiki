---
name: impersonate-http
type: entity
category: library
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - North-web-dev-impersonate-http.md
---

# impersonate-http

## What it is

impersonate-http is a Go `http.Client` designed to mimic the TLS handshake and HTTP/2 frames of a real browser. This allows requests to survive fingerprinting mechanisms like JA3/JA4 and Akamai HTTP/2 fingerprinting, which are often used to block automated scraping traffic.

## How it works

The library is Go-native, utilizing a stock `*http.Client` built on uTLS, eliminating the need for a headless browser, CGo, `libcurl`, or subprocesses. It achieves browser mimicry by providing profiles (such as `Chrome`, `Firefox`, or `Safari`) that set the matching uTLS ClientHello, the browser's HTTP/2 SETTINGS/WINDOW_UPDATE/pseudo-header fingerprint, and default headers.

The client can also be configured to route traffic through various proxies, including `socks5://` or `http(s)://` proxies. It captures measured fingerprints against reflectors to provide parity tables comparing the client's output against canonical browser values.

## TWSC experience

Not yet tested by TWSC.

## Related

* [cloudflare](../entities/cloudflare.md)
* [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)
* [tls-fingerprinting](../concepts/tls-fingerprinting.md)


## Sources

- [https://github.com/North-web-dev/impersonate-http](https://github.com/North-web-dev/impersonate-http)
