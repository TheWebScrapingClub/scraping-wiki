---
name: productivityproxy
type: entity
category: proxy-provider
first_seen: 2026-06-11
last_updated: 2026-06-11
sources:
  - Vaccarini-Lorenzo-ProductivityProxy.md
---

# ProductivityProxy

## What it is

ProductivityProxy is a local macOS application that runs a proxy on the user's machine, allowing them to define custom request and response policies using a visual graph interface. It operates in the macOS menu bar and keeps all traffic local to the machine, ensuring privacy as nothing leaves the device.

## How it works

The system allows users to build policies by drawing graphs on a canvas, defining a starting condition, logic, and an action such as blocking or redirecting a request. Every node within this graph is a small Python file that contains custom logic, enabling users to read, rewrite, block, or compute based on the request details.

Policies are grouped into "modes" (e.g., Deep Work, Chill), and only the active mode runs. Policies are executed sequentially from top to bottom, and the first policy that produces a response typically takes effect. The application drives `mitmproxy` under the hood to manage the traffic flow.

## TWSC experience

Not yet tested by TWSC.

## Related

* [mitmproxy](../entities/mitmproxy.md)


## Sources

- [https://github.com/Vaccarini-Lorenzo/ProductivityProxy](https://github.com/Vaccarini-Lorenzo/ProductivityProxy)
