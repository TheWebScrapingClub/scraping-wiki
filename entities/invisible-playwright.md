---
name: invisible-playwright
type: entity
category: browser
first_seen: 2026-05-20
last_updated: 2026-05-20
sources:
  - feder-cr-invisibleplaywright.md
---

# invisible_playwright

## What it is

invisible_playwright is a patched replacement for Playwright designed specifically for Firefox that is engineered to pass advanced bot detection tests. It functions as a stealth browser by spoofing numerous browser and system-level signals to present a coherent and human-like profile to anti-bot systems.

## How it works

Unlike commercial anti-detect browsers that patch Chromium at the JavaScript level, invisible_playwright patches Firefox at the C++ level. This approach ensures that spoofed values are returned through the normal Gecko paths, meaning the browser is effectively telling the truth from its perspective, which prevents anti-bot lie-detectors from latching onto inconsistencies.

The tool coherently spoofs all relevant layers, including Navigator, screen, GPU/WebGL, Canvas, fonts, audio, WebRTC, timezone, DevTools detection, SOCKS5 authentication, and more. These spoofed values are driven by preferences, allowing users to change one setting to modify the spoofed value.

## TWSC experience

Not yet tested by TWSC.

## Related

* [playwright](../entities/playwright.md)
* [fingerprinterjs](../entities/fingerprinterjs.md)


## Sources

- [https://github.com/feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright)
