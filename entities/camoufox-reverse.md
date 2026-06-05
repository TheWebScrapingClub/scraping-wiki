---
name: camoufox-reverse
type: entity
category: browser
first_seen: 2026-06-04
last_updated: 2026-06-04
sources:
  - lab-camoufox-forks-cloverlabs-draft.md
---

# camoufox-reverse

## What it is

camoufox-reverse is a fork of [Camoufox](camoufox.md) by WhiteNightShadow that adds a PropertyTracer: an engine-level instrument that records which DOM getters a page reads while it runs. It inverts the usual goal. Instead of hiding the browser better, it watches what a detector script looks at. That makes it a research tool for reverse-engineering anti-bot fingerprinting rather than a daily-driver stealth browser.

## How it works

The tracer lives in the SpiderMonkey C++ layer, inside the getter implementations for navigator, screen, window, canvas, WebGL, audio, plugins, storage, and related objects. Because the recording happens below the JavaScript layer, the page cannot see it. No JavaScript object, prototype, or descriptor is modified and no Proxy is introduced, so the instrumentation is invisible to a JS-VM detector.

It is driven through the standard Camoufox config. Set a `propertyTrace` block in the `CAMOU_CONFIG` environment variable with `enabled: true` and a `logDir`, launch the browser with raw Playwright (or the project's MCP server), and the build writes one JSON line per getter access to the log directory, each shaped like `{"o": "navigator", "p": "hardwareConcurrency", ...}`. On macOS the build also requires `MOZ_DISABLE_CONTENT_SANDBOX=1` for the tracer to write. When tracing is off the overhead is a single atomic load.

## TWSC experience

We used camoufox-reverse to see what [Datadome](datadome.md) reads on leboncoin.fr. The trace confirmed the canvas and WebGL surface is part of the live fingerprint (`toDataURL`, `getImageData`, `webgl.getParameter`, `offscreenCanvas.getContext`), alongside the navigator core and screen geometry. It also exposed that Datadome runs a much heavier probe on ad detail pages than on the homepage (584 reads vs 140, with `document.cookie.get` jumping from 1 to 220). This is the first time TWSC has watched a detector's property access from inside the engine rather than inferring it from network traffic. See [canvas fingerprinting](../concepts/canvas-fingerprinting.md) for how that connects to the canvas defenses.

## Known limitations

- The published build is based on Firefox 135, older than the official 146 and the LeooNic 149 builds. It is a measurement instrument, not a build to run scrapers on.
- It is driven through raw Playwright with a hand-set `CAMOU_CONFIG`, not the convenience launcher, and the macOS build needs the content sandbox disabled.
- It does not improve stealth on its own. Its value is diagnostic: knowing which properties a detector reads tells you where spoofing has to be coherent.

## Related

- [Camoufox](camoufox.md)
- [canvas-fingerprinting](../concepts/canvas-fingerprinting.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [Datadome](datadome.md)
- [Camoufox vs forks](../comparisons/camoufox-vs-forks.md)

## Sources

- TWSC Lab article, forthcoming 2026: "Is Camoufox still effective, and do the forks help?" (draft: `drafts/lab-camoufox-forks-cloverlabs-draft.md`)
- [WhiteNightShadow/camoufox-reverse](https://github.com/WhiteNightShadow/camoufox-reverse)
