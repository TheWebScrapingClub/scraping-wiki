---
name: ghx
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - ghx.md
---

# ghx

## What it is

ghx is a caching proxy designed for the GitHub CLI that utilizes singleflight coalescing to ensure that repeated commands are executed instantly. It functions as a drop-in replacement for the standard `gh` command, automatically starting a daemon to manage caching and request coalescing.

## How it works

When a user runs a command via `ghx`, the client resolves the context (repo, branch, auth) and forwards the request to the `ghxd` daemon over a Unix socket. The daemon checks a context-aware cache key to see if a valid, time-to-live (TTL) cached response exists. If a hit occurs, the response is returned instantly. If a cache miss occurs, the daemon executes the underlying `gh` command once, and all concurrent requests from different agents wait for and share that single result.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://brunoborges.github.io/ghx/](https://brunoborges.github.io/ghx/)
