---
name: ncro
type: entity
category: proxy-provider
first_seen: 2026-05-26
last_updated: 2026-05-26
sources:
  - posts-nix-cache-proxy.md
---

# ncro

## What it is

Nix Cache Route Optimizer, or ncro, is a small HTTP proxy written in Rust that functions as an intermediary between the `nix-daemon` and configured substituters. Its primary purpose is to quickly determine the best response for a given path by racing multiple upstream hosts in parallel.

## How it works

On a `narinfo` lookup, ncro races all configured upstreams in parallel using `HEAD` requests and records which host succeeds. When a NAR fetch is requested, it streams the body directly to the client without writing to disk or using a buffer.

It maintains a small, bounded SQLite table to store route decisions, ensuring that a restart does not require relearning the entire routing world.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://notashelf.dev/posts/nix-cache-proxy](https://notashelf.dev/posts/nix-cache-proxy)
