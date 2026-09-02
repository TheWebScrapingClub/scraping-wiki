---
name: stunt
type: entity
category: tool
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - stuntapi-stunt.md
---

# stunt

## What it is

stunt is a local simulator that spins up stateful, realistic stand-ins for public APIs, serving as mock or stub servers for testing purposes. It allows developers to test integrations against various APIs (such as Stripe, Drive, Dropbox, gRPC services, and GraphQL APIs) locally without needing remote accounts, handling live credentials, incurring costs, or depending on network connectivity.

## How it works

stunt is implemented in Go and utilizes a sandboxed Starlark VM to run adapter logic. Adapters are directories containing `adapter.yaml`, Starlark handlers, and fixtures/schemas, which execute within the sandboxed VM. This architecture ensures that adapters are safe to install, as they run without host I/O.

The system relies on stateful primitives (Collection, KV, Blob, Identity, Events) to maintain state across requests, allowing features like creating a charge, listing it, capturing it, and firing a webhook to persist across multiple interactions.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/stuntapi/stunt](https://github.com/stuntapi/stunt)
