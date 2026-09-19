---
name: proxy-benchmark
type: entity
category: tool
first_seen: 2026-09-19
last_updated: 2026-09-19
sources:
  - nodemaven-proxy-benchmark.md
---

# proxy-benchmark

## What it is

`proxy-benchmark` is a measurement harness designed to test various combinations of proxies, browser engines, and scraping targets to diagnose request failures. It aims to determine whether a request failure is caused by the proxy, the browser, the host machine, or the target itself.

## How it works

The benchmark runs the same targets across controlled combinations of several variables. These variables include different engines such as plain HTTP clients, stock Chromium, patched browsers, CDP drivers, and anti-detect frameworks. It also tests various proxy paths, including gateways, providers, countries, sticky sessions, and direct connections without a proxy.

The experiment measures these combinations in a single time window. Every attempt is recorded as a JSONL row in `data/runs/`, carrying the full parameter set used for the test. This allows users to compare performance and failure rates across controlled scenarios.

## TWSC experience

Not yet tested by TWSC.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [playwright](../entities/playwright.md)
- [residential-proxy](../entities/residential-proxy.md)


## Sources

- [https://github.com/nodemaven/proxy-benchmark](https://github.com/nodemaven/proxy-benchmark)
