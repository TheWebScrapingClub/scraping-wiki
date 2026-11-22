---
name: pqcrypta-proxy
type: entity
category: tool
first_seen: 2026-11-22
last_updated: 2026-11-22
sources:
  - PQCrypta-pqcrypta-proxy.md
---

# PQCrypta Proxy

## What it is

PQCrypta Proxy is a Layer-7 reverse proxy written in Rust that supports HTTP/1.1, HTTP/2, HTTP/3/QUIC, and WebTransport. It offers advanced features such as hybrid Post-Quantum Cryptography (PQC) TLS, JA3/JA4 fingerprinting, GeoIP blocking, circuit breaking, ML-adaptive rate limiting, and a Web Application Firewall (WAF).

## How it works

The proxy supports multiple TLS modes, including termination, re-encryption, and passthrough, and integrates hybrid PQC key exchange for enhanced security. It also features Encrypted Client Hello (ECH) support for both TCP and QUIC, aiming to protect the initial handshake from eavesdropping.

PQCrypta Proxy includes a robust WAF with pattern-based request inspection for various injection and traversal attacks, alongside OWASP Core Rule Set compatibility. It also implements advanced security measures like JA3/JA4 fingerprinting, GeoIP blocking, and a proof-of-work challenge as an alternative to heuristic blocking.

## TWSC experience

Not yet tested by TWSC.
## Related

The PQCrypta Proxy's features related to TLS fingerprinting and advanced security measures suggest a connection to the broader concepts of [tls-fingerprinting](../concepts/tls-fingerprinting.md) and [Bot Detection](../concepts/bot-detection.md). Its support for multiple HTTP protocols and load balancing also aligns with general [proxy-server](../entities/proxy-server.md) functionalities.


## Sources

- [https://github.com/PQCrypta/pqcrypta-proxy](https://github.com/PQCrypta/pqcrypta-proxy)
