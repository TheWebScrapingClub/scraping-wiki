---
name: botasaurus
type: entity
category: tool
first_seen: 2024-01-01
last_updated: 2026-04-22
sources:
  - botasaurus-web-scraping-framework.md
  - testing-the-new-botasaurus-4.md
---

# Botasaurus

## What it is

Botasaurus is a Python web scraping framework built around a decorator pattern. Rather than providing a browser or HTTP client directly, it wraps them in task-oriented decorators that handle stealth configuration, parallelization, and proxy rotation automatically. The design philosophy is to reduce boilerplate so that scraping logic can focus on what to extract rather than how to stay undetected.

## How it works

Three decorators form the core of the API:

- `@browser`: wraps a function to execute inside a stealth Chromium session (AntiDetectDriver). Handles fingerprint patching, user-agent setting, and optional proxy assignment.
- `@request`: wraps a function to execute via AntiDetectRequests, an HTTP client layer with TLS fingerprint spoofing.
- `@task`: wraps a function for parallel execution across multiple inputs with automatic retry logic.

Chrome extensions can be installed into the browser session at runtime by passing extension paths to the browser decorator. This is useful for routing traffic through proxy extensions or injecting custom JS early in page load.

The framework's parallelization is handled transparently: passing a list of URLs to a `@browser`-decorated function spawns parallel browser instances up to a configurable limit.

For larger deployments, Botasaurus has Kubernetes support for scaling scraping tasks across multiple nodes.

## TWSC experience

We tested Botasaurus 4 locally against Cloudflare, DataDome, and Kasada. All three passed when run from a developer laptop. This is consistent with what the tool claims: the browser patches address JS-level detection signals well enough to pass standard anti-bot challenges on consumer hardware.

The failure mode becomes apparent when deploying to a server. When the same setup runs inside a datacenter environment, the browser exposes SwiftShader (the CPU-based GPU fallback for headless Chromium) and zero audio/video devices from `MediaDevices.enumerateDevices()`. Both are hard signals that anti-bot systems immediately flag. The tool itself has no mechanism to suppress these signals because they originate from the execution environment, not from browser configuration.

This means Botasaurus is a local scraping tool in practice. It works against anti-bots when run from hardware with a real GPU and real media devices, and fails in the same automated server deployments where the stealth wrapper would matter most.

The decorator API is clean and the task parallelization genuinely reduces code complexity compared to managing concurrent browser pools manually.

## Known limitations

- Not viable from standard cloud server environments (AWS, GCP, DigitalOcean) without hardware GPU pass-through. SwiftShader and zero media devices are exposed automatically in those environments and are reliably detected.
- Depends on Chrome's anti-detect patches, which do not address the execution environment signals that hardware fingerprinting probes.
- Does not support Firefox-based stealth (compare to [Camoufox](camoufox.md)).
- Kubernetes scaling addresses concurrency but does not resolve the server hardware problem.

## Related

- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [camoufox](camoufox.md)
- [nodriver](nodriver.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)

## Sources

- [https://substack.thewebscraping.club/p/botasaurus-web-scraping-framework](https://substack.thewebscraping.club/p/botasaurus-web-scraping-framework)
- [https://substack.thewebscraping.club/p/testing-the-new-botasaurus-4](https://substack.thewebscraping.club/p/testing-the-new-botasaurus-4)
