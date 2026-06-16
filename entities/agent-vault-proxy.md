---
name: agent-vault-proxy
type: entity
category: proxy-provider
first_seen: 2026-06-16
last_updated: 2026-06-16
sources:
  - inflightsec-agent-vault-proxy.md
---

# agent-vault-proxy

## What it is

agent-vault-proxy is a tool designed to provide just-in-time API keys for AI agents and other processes routed through it. It functions by ensuring that the caller only ever sees a placeholder string for a secret, substituting the real API key with the actual secret only at the last possible moment on the outbound request.

## How it works

The proxy operates as a loopback HTTPS proxy that fetches credentials from Bitwarden Secrets Manager (BWS), which can be cloud or self-hosted, using an in-memory TTL cache. On every request, it checks the destination against a binding (host, optional method, optional path scope). If a binding matches, it fetches the real secret from BWS, substitutes the placeholder with the real secret on the upstream socket, and logs an `inject_decision` audit event before the modified bytes are sent.

The system is designed to fail closed if no binding matches the destination, ensuring that the placeholder is forwarded verbatim so that the upstream service's own authentication failure response is surfaced. This mechanism keeps the real credential bytes out of the calling process's address space.

## TWSC experience

Not yet tested by TWSC.

## Related

* [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/inflightsec/agent-vault-proxy](https://github.com/inflightsec/agent-vault-proxy)
