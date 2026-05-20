---
name: childflow
type: entity
category: tool
first_seen: 2026-05-20
last_updated: 2026-05-20
sources:
  - blacknon-childflow.md
---

# childflow

## What it is

childflow is a per-command-tree network sandbox designed for Linux environments. It allows users to run a single command and all its child processes within an isolated network context, providing granular control over network settings.

## How it works

The tool runs one command tree in an isolated network context, applying controls such as DNS configuration, host settings, proxy behavior, sandbox policies, and traffic capture only to that specific tree. It is designed to force proxying at the command tree's network path, rather than relying on environment variables like `HTTP_PROXY` or `LD_PRELOAD` interception.

childflow utilizes two Linux backends: `rootless-internal` for the default operation and `rootful` (activated via the `--root` flag) for scenarios requiring host-integrated behavior, such as using `--iface` or transparent interception.

## TWSC experience

Not yet tested by TWSC.

## Related

- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/blacknon/childflow](https://github.com/blacknon/childflow)
