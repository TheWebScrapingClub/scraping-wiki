---
name: chromiumfish
type: entity
category: browser
first_seen: 2026-06-10
last_updated: 2026-06-10
sources:
  - arman-bd-chromiumfish.md
---

# ChromiumFish

## What it is

ChromiumFish is a stealth Chromium fork designed to present a consistent browser identity through fingerprint hardening. It achieves this by performing spoofing within the C++ engine rather than relying on injected JavaScript, which prevents detection mechanisms from identifying tampering artifacts.

## How it works

ChromiumFish is a Chromium fork where patches and assets are applied over an upstream checkout and then built. It utilizes a drop-in Playwright harness to drive the browser for both Python and Node environments.

The browser spoofs various signals, including UA, Client Hints, fonts, audio, screen, and WebRTC inside Chromium itself. This approach ensures that indicators like `navigator.webdriver` remain `false` even under CDP, eliminating automation artifacts.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The Canvas and WebGL spoofing features require an optional bridge running on Windows, as these signals are difficult to fake from a headless Linux environment.

## Sources

- [https://github.com/arman-bd/chromiumfish](https://github.com/arman-bd/chromiumfish)
