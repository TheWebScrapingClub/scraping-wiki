---
name: underclass
type: entity
category: proxy-provider
first_seen: 2026-09-21
last_updated: 2026-09-21
sources:
  - ghuntley-underclass.md
---

# underclass

## What it is

underclass is a local, OpenAI-compatible proxy designed to pool multiple subscriptions, such as ChatGPT/Codex and GitHub Copilot, behind a single endpoint. It manages these subscriptions by pinning sessions to specific accounts, cooling down quota-exhausted subscriptions until their usage window resets, and ensuring that the proxy behaves like one well-provisioned provider to the client.

## How it works

The proxy pools various subscriptions into a single endpoint, allowing clients to interact with it using a standard OpenAI-compatible interface. Sessions are sticky, meaning requests carrying a `prompt_cache_key` are always routed to the same subscription, which keeps upstream prompt caches warm.

When an account exhausts its quota, it enters a cooling state until its window resets. If all eligible accounts are cooling, the proxy fails fast by returning the earliest `Retry-After` time instead of queuing requests. This mechanism ensures that the proxy avoids hanging when all resources are exhausted.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [llm-shield-proxy](../entities/llm-shield-proxy.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/ghuntley/underclass](https://github.com/ghuntley/underclass)
