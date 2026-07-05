---
name: sandbox-proxy
type: entity
category: proxy-provider
first_seen: 2026-07-05
last_updated: 2026-07-05
sources:
  - yagop-sandbox.md
---

# sandbox-proxy

## What it is

sandbox-proxy is a zero-dependency, stdlib-only Go forward proxy designed to inject real credentials, such as GitHub tokens or npm tokens, into outbound requests on the wire. It functions as a simplified version of Infisical's agent-vault, allowing code running within a containerized sandbox to utilize necessary secrets without ever having direct access to them.

## How it works

Code executes within a container that has no network access except through the proxy. The proxy holds the actual tokens and injects them into outbound requests as they leave the system, ensuring the workload can use the credentials while never seeing the secret itself.

The proxy performs HTTPS interception by generating a CA on the first run, and the intercepted TLS traffic speaks HTTP/1.1 only (ALPN pins `http/1.1`). This mechanism ensures that a compromised workload can only use tokens against the hosts explicitly allowed by the configuration.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The proxy can be configured with `allow_all: false` for strict default-deny, meaning only listed hosts are reachable. Additionally, any volumes mounted via `SANDBOX_VOLUMES` are shared across all sandboxes and are readable by any workload.

## Related

- [proxy-server](../entities/proxy-server.md)
- [go-http-client](../entities/go-http-client.md)
- [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://github.com/yagop/sandbox](https://github.com/yagop/sandbox)
