---
name: molehill
type: entity
category: proxy-provider
first_seen: 2026-11-01
last_updated: 2026-11-01
sources:
  - nicorobinreal-molehill.md
---

# molehill

## What it is

molehill is a tool that utilizes the Mullvad VPN service to function as a rotating HTTP CONNECT proxy. It supports sticky sessions and country-specific routing capabilities for proxy connections.

## How it works

The tool operates by leveraging Mullvad as a rotating HTTP CONNECT proxy, providing session persistence through sticky sessions and country support. Setup requires registering a WireGuard key on a Mullvad account and configuring the proxy details, which are then passed to the running Docker container.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-provider](../entities/3rd-party-proxy.md)


## Sources

- [https://github.com/nicorobinreal/molehill](https://github.com/nicorobinreal/molehill)
