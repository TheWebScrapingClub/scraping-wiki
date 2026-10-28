---
name: mozprox
type: entity
category: proxy-provider
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - mozprox-io.md
---

# mozprox

## What it is

mozprox is a session-scoped, memory-safe web proxy designed for private research and threat inspection. It rewrites every origin through HMAC-signed tokens, incorporating pre-connect SSRF verification and per-session cookie and storage jars that are automatically wiped when the session concludes.

## How it works

The proxy operates with a defense-in-depth architecture, validating every request at the socket layer before rewriting it in a single streaming pass. It implements Pre-Connect SSRF Control by inspecting resolved IPs prior to the TCP handshake, blocking targets such as RFC1918 ranges, loopback addresses, link-local addresses, cloud metadata, and DNS-rebinding attacks.

Target URLs are sealed inside Base64URL tokens and signed using a truncated 128-bit HMAC-SHA256 signature, binding them to the session key. Furthermore, session state, including upstream `Set-Cookie` headers and origin DOM storage, is held in in-memory jars that are destroyed upon session termination.

## TWSC experience

Not yet tested by TWSC.

## Related

* [proxy-server](../entities/proxy-server.md)
* [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)
* [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://mozprox.io/](https://mozprox.io/)
