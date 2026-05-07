---
name: blanktrace
type: entity
category: proxy-provider
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - blanktrace.md
---

# BlankTrace

## What it is

BlankTrace is a powerful, cross-platform (Linux/macOS) Rust CLI/daemon MITM proxy that anonymizes browser traffic by randomizing digital fingerprints, blocking invasive trackers, and stripping identifying cookies.

## How it works

BlankTrace randomizes User-Agent and Accept-Language headers to hide your unique browser signature. It blocks all cookies and strips them from requests, applying regex-based domain blocking with full whitelist control. The proxy runs as an HTTP/HTTPS proxy on `localhost:8080` and logs all activity, blocks, and rotations asynchronously using an Async SQLite database.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Manual CA certificate installation is required for HTTPS interception to work.

## Related

- [proxy-server](../concepts/proxy-fundamentals.md)
- [cookie-session-reuse](../concepts/cookie-session-reuse.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)


## Sources

- [https://mrorigo.github.io/blanktrace/](https://mrorigo.github.io/blanktrace/)
