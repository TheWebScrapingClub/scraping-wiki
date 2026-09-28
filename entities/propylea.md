---
name: propylea
type: entity
category: tool
first_seen: 2026-09-28
last_updated: 2026-09-28
sources:
  - xuoxod-propylea.md
---

# Propylea

## What it is

Propylea is a sovereign, ultra-low-memory L7 reverse proxy, multi-domain SNI TLS multiplexer, and active perimeter defense gateway written in pure Rust.

## How it works

Propylea addresses memory bloat by operating without a garbage collector and featuring an autonomous memory vacuum that periodically returns unused heap pages to the Linux kernel via `libc::malloc_trim`, maintaining a constant RSS under 15 MB. It utilizes a sovereign defense pipeline, powered by `phylax`, which evaluates incoming request paths against an in-memory threat trie in under 15 nanoseconds to serve stealth `404 Not Found` responses to automated crawlers and vulnerability sprayers before they reach upstream services.

It also provides automated threat intelligence by asynchronously dispatching forensic dossiers to AbuseIPDB and custom webhooks, incorporating built-in token-bucket rate limiting to adhere to free-tier quotas.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [bot-detection-system](../entities/bot-detection-system.md)
- [proxy-benchmark](../entities/proxy-benchmark.md)


## Sources

- [https://github.com/xuoxod/propylea](https://github.com/xuoxod/propylea)
