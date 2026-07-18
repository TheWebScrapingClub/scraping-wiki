---
name: latch
type: entity
category: proxy-provider
first_seen: 2026-07-18
last_updated: 2026-07-18
sources:
  - itsVentie-Latch.md
---

# Latch

## What it is

Latch is a lightweight, high-performance infrastructure proxy server designed to tunnel legacy TCP traffic securely. It utilizes hybrid post-quantum cryptography, specifically combining X25519 and ML-KEM-768, to secure traffic against interception and future quantum cryptanalysis.

## How it works

Latch establishes a multi-layered security perimeter starting with Mutual TLS (mTLS) for network authentication, which verifies both endpoints before executing the post-quantum handshake. Upon successful authorization, a hybrid exchange of X25519 and ML-KEM-768 derives a 256-bit master key. Packets are then encapsulated in custom binary frames and encrypted using ChaCha20-Poly1305 authenticated encryption.

To maximize throughput, Latch employs a Control Plane / Data Plane separation model. The Go Control Plane handles configuration, mTLS, and the PQC handshake, while a dedicated Rust Data Plane processes the actual TCP/UDP streams using high-speed, zero-copy ring buffers and AEAD crypto.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/itsVentie/Latch](https://github.com/itsVentie/Latch)
