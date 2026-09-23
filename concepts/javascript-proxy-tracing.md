---
name: JavaScript Proxy tracing
type: concept
first_seen: 2026-09-22
last_updated: 2026-09-22
sources:
  - https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing
  - https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system
---

# JavaScript Proxy tracing

## Definition

A reverse-engineering technique that enumerates every browser property an anti-bot script reads without reversing the script. The script is executed with a JavaScript `Proxy` standing in for the global object, so each property read, `in` check and function call is logged, including reads of names that do not exist, which is exactly where automation probes live and what an ordinary getter override cannot catch.

## How it works

The opening is in how many challenge scripts install themselves: `(function(){ ... }).call(this)`. The interpreter receives the global object as its single argument and keeps it in an ordinary variable, so everything it considers "the window" is whatever it was handed at startup. Hand it a Proxy over `window` with `get` and `has` traps and every access is recorded. Self-references (`window`, `self`, `globalThis`, `parent`, `top`, `frames`) must be swapped back to the Proxy, otherwise the script escapes the trap on the first `window.window`.

A flat stand-in is not enough. The first run in the [SearchGuard](../entities/google-searchguard.md) teardown logged 51 accesses and nothing inside `navigator`, `screen` or `document`, because once the script pulled `navigator` out it read `navigator.webdriver` off the real object. The fix is to wrap nested objects too, and to derive their list from a first pass rather than writing it by hand (a hand-written list is the same list of names you are trying to discover). With nested wrapping the run logged 84 accesses. Functions handed out are wrapped as well so that calls and constructor invocations are recorded with their arguments, and `document` gets its own stand-in because calling a document method through a plain Proxy throws an illegal invocation.

The technique is only valid if the script does not notice it. The SearchGuard probe runs the challenge twice, tapped and untapped, and compares the two tokens byte for byte; the report header prints `invisible: YES` only on equality. Token length is not evidence: a stand-in that folds self-references incorrectly still yields a normal-length token with four fifths of the characters matching and the rest wrong. On SearchGuard a detected interference collapses the output to exactly 871 characters instead of the usual ~1,660.

## Where it matters

Anywhere a detection script is shipped as a VM or under heavy obfuscation, so that reading its source for property names is impractical. The teardown's author estimated weeks to months to reverse the SearchGuard VM, against a day to enumerate its reads through a Proxy. The output is the list of signals you need to make coherent in a stealth browser, and the list of absent names that must stay absent.

The approach has a structural weakness that [camoufox-reverse](../entities/camoufox-reverse.md) does not: a Proxy lives in JavaScript and can in principle be detected by the script (wrong `toString`, identity checks, prototype checks), which is why the byte-equality control is mandatory. camoufox-reverse records getter access below the JavaScript layer in SpiderMonkey, invisible to the page but tied to Firefox. The two are complementary instruments.

## What we tested

Nothing yet. The published probe (`probe-proxy.js` in [google-search-guard-vm-reversing](../entities/google-search-guard-vm-reversing.md)) runs under jsdom against a saved challenge page, so `ABSENT` results need to be split by hand into names that exist nowhere and names that exist in Chrome but not in jsdom.

## Current state

As of September 2026 the technique works against SearchGuard with the tapped/untapped control passing. The author warns that a VM can detect modification and switch to a fail-safe branch that collects different data, so every trace must carry its own control.

## Related

- [Google SearchGuard](../entities/google-searchguard.md)
- [google-search-guard-vm-reversing](../entities/google-search-guard-vm-reversing.md)
- [camoufox-reverse](../entities/camoufox-reverse.md)
- [browser-fingerprinting](./browser-fingerprinting.md)
- [vm-based-javascript-obfuscation](./vm-based-javascript-obfuscation.md)
- [cdp-detection](./cdp-detection.md)

## Sources

- [https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing](https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing)
- [https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system](https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system)
