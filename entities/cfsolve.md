---
name: cfsolve
type: entity
category: library
first_seen: 2026-10-29
last_updated: 2026-10-29
sources:
  - chris124567-cfsolve.md
---

# cfsolve

## What it is

cfsolve is a Rust library and command line tool designed to solve Cloudflare Turnstile widgets and challenge pages without requiring a full headless browser. It is capable of returning a Turnstile token for widgets or a `cf_clearance` cookie for challenge pages.

## How it works

The tool utilizes browser profiles, which are JSON files containing recorded responses to browser checks, to solve challenges. It can solve Turnstile widgets using the page URL, the sitekey, and optionally the page's HTML. Challenge pages require a direct fetch or the HTML content of the page to be solved.

Browser profiles are created by solving challenges in a real web browser while using a proxy to record the decoded payloads sent to Cloudflare. Concurrent operations utilize separate connections and cookies for each instance.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Producing browser profiles requires some manual (or AI) effort, although this process can be greatly aided by solving challenges in a real web browser with the proxy set to the address of a running `capture-proxy`. Currently, only Safari and Chrome(ium) profile types are supported.

## Related

* [Cloudflare](../entities/cloudflare.md)
* [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/chris124567/cfsolve](https://github.com/chris124567/cfsolve)
