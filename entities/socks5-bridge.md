---
name: socks5-bridge
type: entity
category: tool
first_seen: 2026-07-14
last_updated: 2026-07-14
sources:
  - proxybasehq-socks5-bridge.md
---

# socks5-bridge

## What it is

`socks5-bridge` is a local HTTP-to-SOCKS5 proxy bridge designed for Chrome. It addresses the limitation that Chrome does not natively support SOCKS5 username/password authentication by running a local HTTP proxy on loopback. Chrome connects to this local HTTP proxy using a configuration it understands, and the bridge handles the authenticated SOCKS5 connection to the upstream server on Chrome's behalf.

## How it works

The architecture involves Chrome connecting to a local listener (loopback TCP), which is parsed by an HTTP proxy module. This module performs policy checks before initiating a SOCKS5 connection to the upstream server, handling the necessary authentication. Data is then relayed bidirectionally between the client and the upstream SOCKS5 server.

Key modules include `listener` for TCP binding, `http_proxy` for request parsing and policy checks, `socks5` for the protocol handling, and `relay` for bidirectional data copying.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The configuration option `allow_loopback_only` can be set to `false`, but this should be done with extreme caution.

## Sources

- [https://github.com/proxybasehq/socks5-bridge](https://github.com/proxybasehq/socks5-bridge)
