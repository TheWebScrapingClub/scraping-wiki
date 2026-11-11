---
name: pg-interleave
type: entity
category: tool
first_seen: 2026-11-11
last_updated: 2026-11-11
sources:
  - alt-f6-pg-interleave.md
---

# pg-interleave

## What it is

pg-interleave is a wire-protocol proxy for PostgreSQL. It is designed to sit between an application and a PostgreSQL database, allowing for the pausing, reordering, and fuzzing of queries. This capability is particularly useful in concurrency integration tests to deterministically test race conditions.

## How it works

The tool operates by intercepting the PostgreSQL wire protocol. It provides a control plane, accessible via HTTP, which allows tests to manipulate the flow of queries. This includes the ability to freeze specific statements, hold their responses, terminate connections immediately after a commit, or inject specific error conditions like deadlocks.

The proxy facilitates deterministic testing by controlling the order of operations at the protocol level. This means tests can precisely dictate when statements are executed relative to each other, enabling the reliable reproduction of concurrency bugs that might otherwise occur sporadically.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The project is currently in alpha status. It supports plaintext connections only. The server component is written in Rust, and there is a TypeScript SDK available. APIs are subject to change.

## Related

- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/alt-f6/pg-interleave](https://github.com/alt-f6/pg-interleave)
