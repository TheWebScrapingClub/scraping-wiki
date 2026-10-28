---
name: vericto-proxy
type: entity
category: proxy-provider
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - vericto-vericto-proxy.md
---

# Vericto Proxy

## What it is

Vericto Proxy is a transparent wire-protocol proxy designed to stop destructive SQL statements before they reach a PostgreSQL or MySQL database, requiring no code changes in the application.

## How it works

The proxy sits between clients and the database, operating on the database's native wire protocol. It uses the vericto-engine AST parser to parse every query, checks it against defined rules, and either forwards the query to the real database or blocks it by returning a standard SQL error.

The architecture positions the vericto-proxy between the application's SQL wire protocol and the real database upstream. The application connects to the proxy instead of the database directly, and the proxy handles the query evaluation via the vericto-engine before forwarding the request.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Vericto Proxy supports native wire protocols only for PostgreSQL (default) and MySQL. Other dialects such as Oracle, SQL Server, Snowflake, and SQLite must be evaluated via the HTTP API, CLI, or MCP, as there is no wire proxy for them. Snowflake has no TCP wire protocol, and SQLite's SQL is checked within the application before execution.

## Related

- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/vericto/vericto-proxy](https://github.com/vericto/vericto-proxy)
