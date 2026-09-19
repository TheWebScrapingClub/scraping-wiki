---
name: shellroute-cli
type: entity
category: tool
first_seen: 2026-09-19
last_updated: 2026-09-19
sources:
  - shellroute-shellroute-cli.md
---

# shellroute CLI

## What it is

The shellroute CLI is a command-line interface designed to route terminal commands through a configured proxy. It allows users to select a country or city to route a shell session or a single command through a proxy, ensuring that other applications and terminals maintain their normal network connections.

## How it works

Shellroute implements each active route as a local HTTP proxy, providing standard proxy environment variables to the shell or child process. Clients utilizing these variables send their requests through the selected proxy. Shellroute manages the credentials, rotation, usage, and cleanup for each session independently.

The overall flow involves the user's terminal connecting to the shellroute CLI (acting as a local proxy), which communicates with the shellroute API, which then routes the request through a Gateway to an Exit IP before reaching the Internet.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)
- [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://github.com/shellroute/shellroute-cli](https://github.com/shellroute/shellroute-cli)
