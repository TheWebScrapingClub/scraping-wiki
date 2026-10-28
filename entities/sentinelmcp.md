---
name: sentinelmcp
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - asctttt-sentinelmcp.md
---

# SentinelMCP

## What it is

SentinelMCP is a stateless enterprise policy firewall and token-cost proxy designed for the Model Context Protocol (MCP). It functions by sitting in front of an MCP server to inspect every tool call, ensuring that requests adhere to defined identity, policy, and budget constraints before they are allowed to reach the backend infrastructure.

## How it works

SentinelMCP implements zero-trust security through origin validation on every request, mitigating DNS-rebinding risks required by the Streamable HTTP specification. It enforces ID-JAG identity by performing JWKS-backed JWT verification, including binding the `resource` claim to prevent token replay attacks.

For token economics, the system uses structural token estimation based on the JSON-RPC payload, projecting output costs from a per-tool rolling average. It enforces 7-day sliding-window budgets using a fixed-memory circular buffer and includes spike detection independent of the hard cap to catch exponential growth patterns.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [llm-shield-proxy](../entities/llm-shield-proxy.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/asctttt/sentinelmcp](https://github.com/asctttt/sentinelmcp)
