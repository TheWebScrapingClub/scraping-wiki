---
name: claw-patrol
type: entity
category: anti-bot
first_seen: 2026-06-10
last_updated: 2026-06-10
sources:
  - denoland-clawpatrol.md
---

# Claw Patrol

## What it is

Claw Patrol is a security firewall designed to sit between agents and production environments. It parses agent traffic at the wire level and enforces custom rules written in HCL to gate specific protocol actions, such as blocking destructive SQL commands or pausing Kubernetes operations until human approval is granted.

## How it works

The firewall extracts wire-level facts from the traffic based on the protocol being used. For example, it extracts SQL verbs and table names for Postgres or ClickHouse, resource, verb, and namespace for Kubernetes, and method, path, headers, or body for HTTP traffic. These extracted facts are then evaluated against rules defined in HCL using CEL expressions.

Users can deploy Claw Patrol in several ways: running the proxy itself via `clawpatrol gateway config.hcl`, joining a WireGuard tunnel with `clawpatrol join <gateway-url>`, or wrapping a single agent's process tree using `clawpatrol run claude`.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/denoland/clawpatrol](https://github.com/denoland/clawpatrol)
