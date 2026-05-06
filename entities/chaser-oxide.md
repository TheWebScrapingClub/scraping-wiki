---
name: chaser-oxide
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - ccheshirecat-chaser-oxide.md
---

# chaser-oxide

Undetectable, high-performance browser automation in Rust. Protocol-level stealth for Chromium.

**Stars:** 247 | **Forks:** 41 | **Language:** Rust | **License:** Apache License 2.0 | **Created:** 2026-01-01 | **Last pushed:** 2026-04-28

**Topics:** automation, browser, captcha-slover, chrome, chromium, cloudflare, geetest, playwright, puppeteer, rust, solver, stealth, turnstile

## What it is

Chaser-oxide is a Rust-based fork of `chromiumoxide` designed for hardened, undetectable browser automation. It modifies the Chrome DevTools Protocol (CDP) at the transport and protocol layer to reduce the detection footprint of automated browser sessions. The default profile auto-detects the host OS, Chrome version, and RAM, providing native profile stealth. Users can also opt into explicit OS spoofing with pre-configured Windows, Linux, and macOS profiles.

## How it works

Chaser-oxide operates by patching the Chrome DevTools Protocol (CDP) at the transport and protocol layer, rather than via JavaScript wrappers. This approach ensures that the browser sessions are stealthy and undetectable. The default profile auto-detects the host OS, Chrome version, and RAM, providing a native profile. Users can also apply explicit OS spoofing by configuring specific profiles with details such as Chrome version, GPU, memory, locale, timezone, and screen resolution.

## TWSC experience

Not yet tested by TWSC.

## Related

- [undetected-chromedriver](../entities/undetected-chromedriver.md)
- [playwright](../entities/playwright.md)
- [Cloudflare](../entities/cloudflare.md)


## Sources

- [https://github.com/ccheshirecat/chaser-oxide](https://github.com/ccheshirecat/chaser-oxide)
