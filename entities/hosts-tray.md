---
name: hosts-tray
type: entity
category: tool
first_seen: 2026-11-17
last_updated: 2026-11-17
sources:
  - maxmart-hoststray.md
---

# Hosts Tray

## What it is

Hosts Tray is a local development tool designed for macOS and Windows that allows users to switch between different hosts files and provides an automatic HTTPS reverse proxy with trusted certificates. It aims to simplify local development by eliminating the need for manual certificate generation or complex proxy configurations, and preventing browser warnings.

## How it works

The tool functions by managing hosts file entries and providing a reverse proxy. When the HTTPS proxy is enabled, it listens on port 443. It automatically generates and trusts a local Certificate Authority (CA) to issue certificates for any requested hostname, enabling secure HTTPS connections for local development. This process includes support for WebSockets.

Hosts Tray also addresses a common issue where browsers maintain pooled connections to old addresses, delaying the effect of hosts file changes. It actively drops these connections to ensure browsers immediately switch to the new configurations. Users can organize hosts entries into groups, which can be toggled on or off directly from the tray menu.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The Windows build is not yet code-signed, which may trigger a security warning from Windows SmartScreen upon first execution.

## Related

- [mitmproxy](../entities/mitmproxy.md)


## Sources

- [https://github.com/maxmart/hoststray](https://github.com/maxmart/hoststray)
