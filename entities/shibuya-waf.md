---
name: shibuya-waf
type: entity
category: anti-bot
first_seen: 2026-09-06
last_updated: 2026-09-06
sources:
  - theghostshinobi-shibuya.md
---

# Shibuya WAF

## What it is

Shibuya WAF is a Web Application Firewall written in Rust that functions as a reverse proxy. It inspects every incoming request before it reaches the application, utilizing the OWASP Core Rule Set (ModSecurity format) along with custom rules. It includes a dashboard for monitoring activity and making changes without requiring a service restart.

## How it works

The WAF sits in front of the target site, acting as a reverse proxy to inspect all traffic. It processes requests against the loaded OWASP Core Rule Set and any custom rules defined by the user.

The system uses Redis for distributed rate limiting, rejecting concurrent requests based on defined thresholds. It measures performance metrics, reporting a p99 latency of 1.60 ms end-to-end through the WAF.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

*   Request-body DoS protections are not active, as the module for body size capping, per-IP memory quota, and slow-POST detection has been written but not compiled.
*   It does not inspect responses; it only analyzes incoming requests.
*   It does not read XML/SOAP bodies, meaning services using these formats are not covered by the ruleset.
*   The machine learning classifier is disabled by default because it was trained on a different feature schema than the one the WAF produces, making it systematically incorrect.
*   It does not manage HTTPS certificates itself; users must provide certificates or terminate HTTPS in front of the WAF.
*   Multi-tenancy is only supported with PostgreSQL; SQLite is not used for tenant data isolation.

## Related

*   [3rd-party-proxy](../entities/3rd-party-proxy.md)
*   [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/theghostshinobi/shibuya](https://github.com/theghostshinobi/shibuya)
