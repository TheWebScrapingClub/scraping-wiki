---
name: coorl
type: entity
category: library
first_seen: 2026-06-29
last_updated: 2026-06-29
sources:
- https://konstantinlebedev.com/bypassing-automated-traffic-detection/
---

# coorl

## What it is

coorl is a curl-compatible command-line HTTP client that mimics Chrome's TLS fingerprint instead of advertising the standard OpenSSL signature that scripted tools send. It was written by Konstantin Lebedev. The scope is deliberately narrow: produce a `ClientHello` that hashes to a Chrome JA3/JA4 fingerprint, so the connection looks like a real browser at the layer anti-bot systems inspect first.

## How it works

A normal HTTP client gives itself away during the TLS handshake, because the shape of its `ClientHello` is set by the TLS library it was built on, not by anything in the request code. See [tls-fingerprinting](../concepts/tls-fingerprinting.md) for the mechanism. coorl performs the handshake the way Chrome does, so the JA3/JA4 fingerprint on the wire is a Chrome fingerprint rather than an OpenSSL one.

It does not run a headless browser, execute JavaScript, or carry Chromium. It mirrors curl's flags (`-X`, `-H`, `-d`, `-b`, and so on), so adopting it is mostly a matter of swapping the command name. By design it implements only the most-used subset of curl's flags over HTTP and HTTPS, not curl's full protocol and flag surface.

## TWSC experience

We have not tested coorl directly. It surfaced through Lebedev's June 2026 write-up on TLS-layer bot detection. Conceptually it sits in the same niche as [curl-cffi](curl-cffi.md): swap the TLS stack so the handshake matches a browser. The difference is scope and form. curl-cffi is a Python library (and the engine under scrapy-impersonate and hrequests) with selectable Chrome and Firefox impersonation profiles. coorl is a standalone CLI focused on a Chrome handshake and a curl-compatible flag set. For pipelines already in Python, curl-cffi remains the documented TWSC choice. coorl is relevant when what you want is a drop-in curl replacement on the command line.

## Known limitations

- It addresses only TLS-layer detection, the JA3/JA4 check that blocks a request before it reaches the origin. It is not a CAPTCHA solver and does not execute JavaScript challenges, so any target that gates content behind a full browser challenge still needs a real browser.
- It implements a subset of curl's flags, so it is not a complete drop-in for every existing curl invocation.
- Untested by TWSC. The claims here come from the author's documentation, not our own benchmarks.

## Related

- [curl-cffi](curl-cffi.md)
- [ja3proxy](ja3proxy.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)
- [Cloudflare](cloudflare.md)
- [Akamai](akamai.md)

## Sources

- [https://konstantinlebedev.com/bypassing-automated-traffic-detection/](https://konstantinlebedev.com/bypassing-automated-traffic-detection/)
