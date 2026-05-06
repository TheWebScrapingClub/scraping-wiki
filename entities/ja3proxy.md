---
name: ja3proxy
type: entity
category: tool
first_seen: 2025-05-01
last_updated: 2026-04-22
sources:
  - bypass-akamai-bot-protection.md
---

# JA3Proxy

## What it is

JA3Proxy is a Go-based local proxy that rewrites TLS Client Hello messages to match specific browser TLS fingerprint profiles. It uses uTLS, a Go library that provides low-level control over TLS handshake construction, to produce Client Hello messages that are structurally identical to real Chrome or Firefox.

## How it works

JA3Proxy runs locally and intercepts outbound HTTPS traffic. For each connection, it rewrites the TLS Client Hello before forwarding the request to the actual destination. The rewriting changes the cipher suite ordering, extensions, and other TLS parameters to match a specific browser profile. The result is that the target server sees a TLS fingerprint consistent with a real browser, regardless of what HTTP library made the original request.

Because it operates as a proxy, it is client-agnostic: any HTTP library that supports proxy configuration can route traffic through JA3Proxy and benefit from the fingerprint rewriting. This is the key difference from [curl-cffi](curl-cffi.md), which requires using curl-cffi itself as the HTTP client.

The typical chain is: local HTTP client → JA3Proxy (local) → residential proxy (SOCKS5) → target server.

HTTPS interception requires a self-signed certificate. The HTTP client must be configured to trust this certificate, which usually means disabling SSL verification or adding the certificate to the trust store.

At the time of the article covering it (May 2025), JA3Proxy supported Chrome profiles up to version 133.

## TWSC experience

We used JA3Proxy on [Akamai](akamai.md) targeting mrporter.com. The HTTP client used was httpx rather than requests, because Akamai's bot detection uses HTTP/2 signals and requests does not support HTTP/2. JA3Proxy handled the TLS fingerprint layer while httpx handled the HTTP/2 framing.

The Docker installation was broken at the time of testing. We built JA3Proxy from source using Go, which also had dependency issues that required manual resolution before the build succeeded.

The setup worked: requests routed through JA3Proxy with the Chrome profile passed Akamai's TLS fingerprint checks where the same requests without JA3Proxy did not.

## Known limitations

- Docker installation was broken at time of testing. Manual Go builds require resolving dependency issues.
- Chrome profile support has a version ceiling. As Chrome updates its TLS configuration, new profile support requires updates to JA3Proxy.
- The self-signed certificate requirement adds setup friction, particularly in environments with strict SSL policies.
- Does not address JavaScript execution or browser-level fingerprinting. Works only at the TLS layer.
- For Python-based scraping where curl-cffi is an option, curl-cffi is simpler to set up and covers the same TLS fingerprinting problem without the proxy infrastructure.

## Related

- [curl-cffi](curl-cffi.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [Akamai](akamai.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-akamai-bot-protection](https://substack.thewebscraping.club/p/bypass-akamai-bot-protection)
