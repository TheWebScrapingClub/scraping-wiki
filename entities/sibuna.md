---
name: sibuna
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - insanai-sibuna.md
---

# Sibuna

## What it is

Sibuna is an open-source web application firewall (WAF) designed to provide web protection against unwanted bot traffic. It functions by requiring clients to solve a proof-of-work puzzle before granting access to a website or API. It can forward requests to an application or operate alongside existing reverse proxies like Caddy, nginx, or Traefik.

## How it works

Sibuna implements a proof-of-work mechanism to introduce an admission cost for clients attempting to access the protected resource. This puzzle is designed so that the cost of proof creation exceeds the cost of verification, making automated clients share the burden of access. Admitted clients receive a signed session, allowing them to return without solving a new puzzle on every request, with access controlled by access rules and local rate limits.

The system includes application inspection capabilities for built-in checks against vulnerabilities such as SQL injection, XSS, and path traversal. It utilizes a browser solver based on WebAssembly to handle browser challenges.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Sibuna does not prove that a visitor is human or stop every attack.

## Related

- [bot-detection-system](../entities/bot-detection-system.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/insanai/sibuna](https://github.com/insanai/sibuna)
