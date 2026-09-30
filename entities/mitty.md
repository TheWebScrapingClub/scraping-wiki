---
name: mitty
type: entity
category: library
first_seen: 2026-09-30
last_updated: 2026-09-30
sources:
  - jcubic-mitty.md
---

# Mitty

## What it is

Mitty is a transport-agnostic proxy RPC designed for executing method chains from any isolated context, such as Web Workers, browser Tabs, or Servers, utilizing lazy evaluation. It allows developers to interact with objects that exist on the main thread from within an isolated environment.

## How it works

Mitty operates by leaving real objects, such as DOM nodes or jQuery objects, on the main thread while placing a proxy within the isolated context. This proxy records property accesses and method calls without directly touching the communication channel. The entire method chain is then replayed on the main thread when awaited.

The architecture is transport-agnostic, enabling communication between various contexts. It supports Web Workers and Service Workers, cross-tab communication (via mechanisms like BroadcastChannel), and client-server communication using WebSockets or WebRTC, allowing commands to be executed or states queried directly from the server or the browser. The wire format used is specified independently as Remote Object / Remote Procedure Call (RO/RPC).

## TWSC experience

Not yet tested by TWSC.

## Known limitations

If the worker itself is created from a `Blob`, the URL passed to `importScripts()` must be absolute. A `blob:` URL has an opaque path, meaning relative paths like `'/mitty.js'` or `'./mitty.js'` will be rejected.


## Sources

- [https://github.com/jcubic/mitty](https://github.com/jcubic/mitty)
