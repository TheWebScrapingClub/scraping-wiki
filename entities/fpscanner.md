---
name: fpscanner
type: entity
category: library
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - antoinevastel-fpscanner.md
---

# FPScanner

## What it is

FPScanner is a lightweight browser fingerprinting library for bot detection. It is designed to be self-hosted and up-to-date, providing solid building blocks that reflect how bots actually behave today. The library includes practical considerations such as anti-replay protections, payload encryption, and optional obfuscation to make reverse-engineering more difficult.

## How it works

FPScanner combines fingerprinting and bot detection in a single library. It focuses on self-hosted fingerprinting and bot detection primitives, providing a lightweight and up-to-date solution for real-world fraud and bot prevention. The library is designed to be transparent while also including hardening mechanisms to prevent trivial forgery and reverse-engineering.

## TWSC experience

Not yet tested by TWSC.
## Related

- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [botasaurus](../entities/botasaurus.md)


## Sources

- [https://github.com/antoinevastel/fpscanner](https://github.com/antoinevastel/fpscanner)
