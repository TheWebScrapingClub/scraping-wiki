---
name: llm-shield-proxy
type: entity
category: anti-bot
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - ninadphalak-LLM-Shield-Proxy.md
---

# LLM-Shield-Proxy

## What it is

LLM-Shield-Proxy is a stateless, zero-latency reverse proxy designed for real-time Personally Identifiable Information (PII) redaction within Large Language Model (LLM) streams. It functions as an AI Gateway and LLM Firewall deployed within a corporate VPC, intercepting OpenAI-compatible LLM API requests to secure data before it leaves the infrastructure.

## How it works

The proxy intercepts LLM API requests, performing data loss prevention (DLP) by redacting PII and raw secrets using format-preserving substitution techniques involving Regex, Shannon Entropy, and ONNX NER. This ensures that sensitive information never traverses the public internet.

It also handles the real-time aspect by using a sub-millisecond SSE rehydration mechanism to reconstruct fragmented sensitive tokens across Server-Sent Events without introducing network lag. Furthermore, it utilizes zero-data stateless cryptography (AES-256-GCM) and supports service mesh native gRPC sidecar communication via Envoy's `ext_proc` over Unix Domain Sockets for zero HTTP network hops.

## TWSC experience

Not yet tested by TWSC.

## Related

* [3rd-party-proxy](../entities/3rd-party-proxy.md)
* [aiohttp](../entities/aiohttp.md)
* [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/ninadphalak/LLM-Shield-Proxy](https://github.com/ninadphalak/LLM-Shield-Proxy)
