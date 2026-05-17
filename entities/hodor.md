---
name: hodor
type: entity
category: tool
first_seen: 2026-05-17
last_updated: 2026-05-17
sources:
  - michidk-hodor.md
---

# Hodor

## What it is

Hodor is a tiny reverse proxy written in Rust designed to gate web applications behind a single shared password. It operates without requiring user accounts, databases, or OAuth, relying solely on one binary and a single login page for access control.

## How it works

The proxy handles incoming requests by first checking a health endpoint (`/_gate/health`). If the request has a valid session cookie, it is proxied to the upstream application. If no valid session cookie is present, the request is routed to the login page (`/_gate/login`). Upon successful login, a session cookie is set, and the user is redirected to the intended upstream resource.

Hodor implements per-IP rate limiting on login attempts (5 attempts per 60 seconds) and uses HMAC-SHA256 for signing session cookies. As a reverse proxy, it streams request and response bodies without buffering, sets necessary headers like `X-Forwarded-For`, and strips hop-by-hop headers.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

WebSocket proxying is not yet supported, resulting in a 501 response.

## Related

proxy-server


## Sources

- [https://github.com/michidk/hodor](https://github.com/michidk/hodor)
