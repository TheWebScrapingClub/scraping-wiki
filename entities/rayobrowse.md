---
name: rayobrowse
type: entity
category: browser
first_seen: 2026-01-01
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/rayobrowse-browser-scraping
  - https://substack.thewebscraping.club/p/two-stealth-browsers-proxy-prices
---

# Rayobrowse

## What it is

Rayobrowse is a stealth Chromium browser developed by Rayobyte (the proxy provider). It is closed-source and self-hostable via Docker. The design target is scrapers who need a stealth browser they can deploy on their own infrastructure rather than paying per-session fees to a browser-as-a-service provider.

As of 2026, Rayobrowse is in beta.

## How it works

Rayobrowse is a Chromium fork with anti-detection patches applied at the C++ level rather than through JavaScript injection. This is a significant architectural distinction: patches at the engine level are structurally harder to detect than JavaScript-side spoofing, because the patching happens before page scripts have an opportunity to probe the browser.

Fingerprints are sourced from a database of real device fingerprints, not generated procedurally. This means the values passed to fingerprinting APIs correspond to real hardware and real browser configurations, rather than synthetic values that approximate plausible ranges.

The Docker image includes a noVNC viewer, allowing visual observation of browser sessions from any machine with network access to the container.

CDP compatibility is preserved. Playwright, Puppeteer, and other tools that use `connect_over_cdp` can connect to a running Rayobrowse session without modification.

## TWSC experience

In a benchmark run, Rayobrowse achieved 100% on the composite fingerprinting test. This is the highest result in the TWSC benchmark set. The score reflects the combination of C++ patching and real-device fingerprint sourcing.

Windows and Android fingerprints are noted as the strongest configurations. The specific baseline for other OS profiles was not evaluated.

The Docker deployment workflow is: pull the image, run the container with port mapping for CDP and noVNC, connect your automation client to the CDP endpoint.

## Known limitations

- Closed-source. There is no visibility into how the fingerprint database is populated, how frequently it is updated, or what the patching scope covers.
- Beta status means the API surface and Docker image may change without notice.
- Rayobyte is primarily a proxy provider. Rayobrowse is a secondary product. Long-term investment and maintenance trajectory are uncertain.
- Like all Chromium-based tools, server deployment without a real GPU exposes SwiftShader. The benchmark result reflects a controlled local or GPU-equipped environment. Server deployments face the same hardware fingerprint problem as other Chromium tools unless GPU pass-through is configured.
- Not open-source means external auditing of the anti-detection claims is not possible.

## Related

- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [camoufox](camoufox.md)
- [anti-detect-browsers](../concepts/anti-detect-browsers.md)
- [cdp-detection](../concepts/cdp-detection.md)
