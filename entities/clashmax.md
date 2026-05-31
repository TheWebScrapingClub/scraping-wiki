---
name: clashmax
type: entity
category: tool
first_seen: 2026-05-31
last_updated: 2026-05-31
sources:
  - marvinli001-ClashMax.md
---

# ClashMax

## What it is

ClashMax is a native macOS graphical client built with SwiftUI that serves as a Mihomo proxy client. It is designed to manage proxy profiles, runtime control, proxy groups, connections, rules, logs, and system integration workflows specifically tailored for macOS environments.

## How it works

ClashMax functions as a proxy control console, allowing users to import Clash/Mihomo YAML profiles and manage the runtime. It provides capabilities to switch between different runtime modes, inspect active connections and rules, follow logs, and manage proxy groups. The client integrates with Mihomo REST and WebSocket control APIs to manage various aspects of the proxy configuration.

It supports both standard system proxy mode and a privileged helper-backed TUN path, adapted for macOS system approval models. It also preserves original YAML files and generates a ClashMax-managed runtime YAML before launch to safely inject configurations like ports, controller, secret, DNS, TUN, and runtime mode.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The MVP core policy is intentionally single-channel, meaning only the app-owned bundled Mihomo core is supported.

## Sources

- [https://github.com/marvinli001/ClashMax](https://github.com/marvinli001/ClashMax)
