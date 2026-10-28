---
name: apiaxess
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - apiaxess-dev.md
---

# apiaxess

## What it is

apiaxess is an open-source tool designed to capture, analyze, and interact with APIs from both mobile and web applications. It facilitates API scraping by routing traffic through a browser already routed through a proxy and an Android emulator that trusts the certificate, allowing users to capture live traffic and perform various testing operations.

## How it works

The tool sets up a session using a browser routed through a proxy and an Android emulator configured to trust the necessary certificates. This setup allows for capturing traffic from mobile applications or web services without requiring manual setup steps.

Users can interact with the captured traffic via a Workbench interface to replay requests, run full Intruder-class attacks, or intercept matching requests to forward, modify, or drop them. It supports capturing both mobile and web clients, and allows for exporting the results in formats such as OpenAPI 3.1, Postman, HAR, and a Python client.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

If an application has certificate pinning that cannot be bypassed, apiaxess will inform the user instead of returning an empty list.

## Related

- [browser-use](../entities/browser-use.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://apiaxess.dev](https://apiaxess.dev)
