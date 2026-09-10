---
name: socklight
type: entity
category: proxy-provider
first_seen: 2026-09-10
last_updated: 2026-09-10
sources:
  - kosmrljt-socklight.md
---

# sockLight

## What it is

sockLight is a development SOCKS5 proxy featuring a live Terminal User Interface (TUI) that allows users to monitor, block, and throttle every outbound connection in real time. It is designed to provide visibility into network traffic without requiring certificate installation or HTTPS decryption.

## How it works

sockLight operates at the connection level, observing details such as the hostname, port, bytes transferred, and speed. It works directly with any SOCKS5h client, allowing tools like `curl`, `wget`, and Podman/Docker containers to route traffic through it.

The proxy provides features such as pre-defined categories for traffic filtering, live speed metrics per connection, and the ability to apply rules instantly to block or throttle traffic without restarting applications. It also queries DNS and GeoIP information in the background to provide detailed connection inspection.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

sockLight is not a replacement for tools like mitmproxy if the requirement is to inspect or rewrite request bodies, as it deliberately stops at the connection level. Furthermore, while developed and tested on Linux, support for macOS and Windows is not yet tested.

## Related

- [mitmproxy](../entities/mitmproxy.md)


## Sources

- [https://github.com/kosmrljt/socklight](https://github.com/kosmrljt/socklight)
