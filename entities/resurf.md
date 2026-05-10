---
name: resurf
type: entity
category: tool
first_seen: 2026-05-10
last_updated: 2026-05-10
sources:
  - lightfeed-resurf.md
---

# Resurf

## What it is

Resurf is a deterministic and reproducible test environment designed for systematically testing AI browser agents against realistic, stateful environments. It provides a framework built on synthetic websites that incorporates failure-mode injection to simulate real-world conditions, allowing for the systematic testing of browser agents.

## How it works

The framework utilizes synthetic websites, such as the `shop_v1` e-commerce site, to provide a realistic, dynamic, and interactive environment. It incorporates modifiers that allow for failure-mode injection, toggling network latency, payment outcomes, server error rates, and session expiration on a per-task basis.

Resurf records detailed trajectory data for each step, including per-step DOM snapshots, screenshots, agent actions, token counts, and latencies. This trajectory recording is made deterministic through SQLite snapshot resets and seeded faker data.

## TWSC experience

Not yet tested by TWSC.

## Related

* [playwright](../entities/playwright.md)
* [browser-use](../entities/browser-use.md)


## Sources

- [https://github.com/lightfeed/resurf](https://github.com/lightfeed/resurf)
