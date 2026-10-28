---
name: aegis
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - divinelabio-Aegis.md
---

# Aegis

## What it is

Aegis is an open-source, high-performance Web Application Firewall (WAF) and reverse proxy built in Go. It is designed to protect web applications, APIs, and microservices at the network edge by inspecting incoming HTTP and HTTPS traffic in real time. It provides real-time threat defense, Layer 7 traffic control, and a unified admin console for managing policies.

## How it works

Aegis functions as an edge gateway, inspecting traffic before it reaches upstream services to stop cyber attacks, malicious bots, and abusive traffic surges. It enforces various security measures, including OWASP Core Rule Set (CRS) defense, rate limiting, IP access control, and protocol enforcement.

Routing rules, firewall policies, rate limits, and SSL certificates are managed dynamically through an integrated web console, allowing for zero downtime and policy control without requiring configuration restarts.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/divinelabio/Aegis](https://github.com/divinelabio/Aegis)
