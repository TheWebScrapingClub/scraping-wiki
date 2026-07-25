---
name: web-bot-auth
type: entity
category: anti-bot
first_seen: 2026-07-25
last_updated: 2026-07-25
sources:
  - tools-keycheck.md
---

# Web Bot Auth

## What it is

Web Bot Auth is a system built on RFC 9421 and HTTP Message Signatures that allows a verifier like Cloudflare to authenticate a crawler from a signing-key directory that the user publishes.

## How it works

The tool checks a specified directory, which can be a domain or a full directory URL, for the existence of the `/.well-known/http-message-signatures-directory`. It performs a key-by-key check to identify mistakes that stop verification, including a leaked private key.

## Related

- [Cloudflare](cloudflare.md)


## Sources

- [https://sitedex.dev/tools/keycheck](https://sitedex.dev/tools/keycheck)
