---
name: math-tanh
type: entity
category: library
first_seen: 2026-07-13
last_updated: 2026-07-13
sources:
  - posts-browser-math-os-fingerprint.md
---

# Math.tanh

## What it is

The implementation of the `Math.tanh` function varies between operating systems, which serves as a subtle signal for browser fingerprinting.

## How it works

The exact bits returned by a `Math.tanh` call depend on the operating system that computes it. Genuine macOS Chrome uses Apple’s math library (`libsystem_m`), Linux uses glibc, and Windows uses the Universal C Runtime (UCRT). These three implementations produce distinct sets of bits, agreeing almost everywhere but splitting just often enough to classify the OS. This variation occurs because IEEE 754 defines how a `double` is stored, and each vendor ships a `libm` implementation that trades a fraction of a ULP for speed using its own minimax coefficients and lookup tables.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Reimplementing Mac functions can break for several reasons, including the fact that only some math leaks.

## Sources

- [https://scrapfly.dev/posts/browser-math-os-fingerprint/](https://scrapfly.dev/posts/browser-math-os-fingerprint/)
