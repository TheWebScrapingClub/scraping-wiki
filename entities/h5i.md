---
name: h5i
type: entity
category: browser
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - Koukyosyumei-i-built-a-headless-browser-for-ai-agents-entirely-in-rust-no-chromi.md
---

# h5i

## What it is

h5i is a lightweight, open-source headless browser implemented entirely in Rust. It is designed for AI agents and avoids using Chromium or the V8 JavaScript engine, offering an alternative for tasks requiring web interaction and data extraction.

## How it works

h5i is assembled from several Rust components, including Blitz for handling HTML, the DOM, CSS, layout, and rendering, and Boa for optional JavaScript execution. It utilizes a custom Rust networking and policy layer that checks every request against a defined policy before any data is sent.

Instead of providing a full DOM dump, h5i produces a structured snapshot containing compact element references, allowing agents to interact through references such as `@e3` and inspect allowed or denied network activity. A complete session record is also provided, including navigation, clicks, page requests, and human handovers.

## Known limitations

Benchmarks on simple, document-heavy pages showed that h5i used roughly 80% less peak memory and completed cold one-shot reads around 5× faster than headless Chromium. However, this includes the caveat that Chromium’s startup cost dominates short runs, and h5i will not beat Chromium at everything.

## Related

- [rustwright](../entities/rustwright.md)
- [browser-use](../entities/browser-use.md)


## Sources

- [https://medium.com/@Koukyosyumei/i-built-a-headless-browser-for-ai-agents-entirely-in-rust-no-chromium-no-v8-3750908b8145](https://medium.com/@Koukyosyumei/i-built-a-headless-browser-for-ai-agents-entirely-in-rust-no-chromium-no-v8-3750908b8145)
