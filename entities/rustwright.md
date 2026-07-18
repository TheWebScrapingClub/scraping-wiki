---
name: rustwright
type: entity
category: library
first_seen: 2026-07-18
last_updated: 2026-07-18
sources:
  - Skyvern-AI-rustwright.md
---

# Rustwright

## What it is

Rustwright is a browser automation library designed for Python and Node.js that maintains the familiar Playwright API while driving Chromium using a native Rust engine. It is an alpha project that is interoperable with Playwright but operates on an in-process Rust CDP engine, offering performance improvements and eliminating the need for a separate Node driver subprocess.

## How it works

The architecture consists of a single Rust core, which is an asynchronous CDP client built on Tokio (supporting WebSocket and optional Unix-pipe transport). This core communicates directly with Chromium. Thin bindings, such as PyO3 for Python and napi-rs for Node, expose this functionality in-process.

This approach allows Rustwright to bypass the traditional driver subprocess model, resulting in faster execution and the absence of Playwright automation fingerprints. It also ensures trusted input by routing clicks and typing through real CDP input events.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Only a subset of the API surface is bridged.

## Sources

- [https://github.com/Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright)
