---
name: x-twitter-ui-metrics
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-x-former-twitter-login-flow-reconstruction-episode-2-ui-metrics.md
---

# x-twitter-ui-metrics

## What it is

x-twitter-ui-metrics is a GitHub repository containing Node.js, Go, and Python implementations designed to reconstruct and bypass X (formerly Twitter)'s UI metrics login flow challenge. This challenge involves a dynamic JavaScript script that X serves to collect specific metrics before allowing a login.

## How it works

The process begins when X's login API returns a `LoginJSInstrumentationSubtask` identifier. This triggers the loading of a JavaScript script from `https://twitter.com/i/js_inst?c_name=ui_metrics`. This script, when executed, generates a complex, obfuscated JavaScript code. This obfuscated code performs calculations using bitwise operations on several numeric variables. It then creates a hidden HTML input field named `ui_metrics` and populates it with a JSON object containing computed values (`rf`) and a static signature (`s`).

The obfuscation techniques employed include a "Prototype XOR" pattern that leverages JavaScript's prototype chain for XOR operations, a "DOM Tree Calculation" where computations are hidden within DOM manipulation, and a "Date XOR" pattern that XORs a value with the UTC day derived from a timestamp generated from that value. By understanding and reimplementing these specific obfuscation patterns, it's possible to bypass the need for a browser and execute the logic natively in other programming languages.

## TWSC experience

Not yet tested by TWSC.
## Related

* [browser-fingerprinting](../entities/browser-fingerprint-scanner.md)
* [client-side-bot-detection](../entities/client-side-bot-detection.md)
* [playwright](../entities/playwright.md)


## Sources

- [https://takionapi.tech/blog/x-former-twitter-login-flow-reconstruction-episode-2-ui-metrics](https://takionapi.tech/blog/x-former-twitter-login-flow-reconstruction-episode-2-ui-metrics)
