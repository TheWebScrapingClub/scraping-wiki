---
name: mochi-js
type: entity
category: library
first_seen: 2026-05-10
last_updated: 2026-05-10
sources:
  - mochijs-com.md
---

# mochi.js

## What it is

mochi.js is a Bun-native, raw-CDP browser automation framework designed to create relationally-coherent fingerprints. It aims to leave no measurable fingerprints by unifying various aspects of browser behavior into a single, consistent stack.

## How it works

The framework operates on five pillars to ensure stealth and consistency. The relational consistency engine derives all fingerprint surfaces—including canvas, WebGL, audio, fonts, MediaDevices, and WebGPU—from a single profile and seed pair using a 48-rule Directed Acyclic Graph (DAG). Additionally, it utilizes a Chromium-native fetch mechanism that routes requests through Chromium via CDP, ensuring that JA4/JA3/H2 values are authentic Chrome identifiers.

Behavioral synthesis is handled through biomechanical models, synthesizing actions like `humanClick` and `humanType` using Bezier paths, Fitts-law movement times, and lognormal digraph delays. This approach replaces traditional, hand-stitched pipelines with a single, end-to-end library built exclusively with Bun.

## TWSC experience

Not yet tested by TWSC.

## Related

* [playwright](../entities/playwright.md)
* [browser-fingerprinting](../concepts/browser-fingerprinting.md)
* [cdp-detection](../concepts/cdp-detection.md)


## Sources

- [https://mochijs.com/](https://mochijs.com/)
