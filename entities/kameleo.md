---
name: kameleo
type: entity
category: tool
first_seen: 2023-01-01
last_updated: 2026-04-22
---

# Kameleo

## What it is

Kameleo is a Hungarian anti-detect browser developed by a team led by CEO Tamas Deak. Rather than shipping a single patched browser binary, Kameleo bundles two built-in browsers: Junglefox (a patched Firefox fork) and Chroma (a patched Chromium fork). This dual-engine design allows users to create browser profiles that impersonate either browser family without relying on the user's local installation.

## How it works

Each browser profile stores a fingerprint configuration that Kameleo applies to a fresh Junglefox or Chroma session: User-Agent, screen resolution, timezone, language, WebGL parameters, canvas noise, and related signals. The profile can be assigned a proxy, which Kameleo uses to align the browser's timezone and geolocation with the proxy exit IP.

A standout feature is framework integration. Kameleo was the first anti-detect browser to expose a local WebSocket API compatible with Selenium, Playwright, and Puppeteer simultaneously. Scripts connect to the running browser profile via CDP and control it like any remote browser. The REST API for profile management covers creation, update, and deletion without requiring the desktop GUI.

Platform availability: Windows on launch; macOS support added in May 2024.

## TWSC experience

We tested Kameleo in a benchmark against six other anti-detect browsers using [CreepJS](../concepts/browser-fingerprinting.md) and [BrowserScan](../concepts/browser-fingerprinting.md). Kameleo scored 175/260 on a composite scale where a real Mac scored 226/260.

An important note on this result: the BrowserScan test flagged a WebRTC leak. After TWSC published the benchmark, Kameleo's team confirmed this was a configuration error in our test setup, not an inherent product flaw. The WebRTC setting requires explicit configuration in Kameleo profiles. The score likely underrepresents the tool's actual fingerprint quality when properly configured.

The local API integration works reliably. Connecting a Playwright script to a running Kameleo profile via `connect_over_cdp` requires no special handling beyond pointing to the local WebSocket endpoint.

## Known limitations

- Windows-only until May 2024. macOS support arrived later and may lag behind the Windows build in feature parity.
- The REST API covers profile management but does not provide an SDK. All automation must go through the local CDP/WebSocket endpoint.
- Fingerprint quality depends on how the profile is configured. Default settings may not align all parameters (the WebRTC gap in our test illustrates this).
- The START plan (€29/mo) imposes request rate limits. The SCALE plan (€279/mo) removes them.

## Related

- [anti-detect-browsers](../concepts/anti-detect-browsers.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [gologin](gologin.md)
- [dolphin-anty](dolphin-anty.md)
- [anti-detect-browser-benchmark-2024](../comparisons/anti-detect-browser-benchmark-2024.md)

## Sources

- [https://substack.thewebscraping.club/p/kameleo-anti-detect-browser](https://substack.thewebscraping.club/p/kameleo-anti-detect-browser)
- [https://substack.thewebscraping.club/p/anti-detect-browsers-fingerprint-tests](https://substack.thewebscraping.club/p/anti-detect-browsers-fingerprint-tests)
- [https://substack.thewebscraping.club/p/anti-detect-browser-royal-rumble-comments](https://substack.thewebscraping.club/p/anti-detect-browser-royal-rumble-comments)
- [https://substack.thewebscraping.club/p/anti-detect-pricing-comparison](https://substack.thewebscraping.club/p/anti-detect-pricing-comparison)
