---
name: wirepane
type: entity
category: proxy-provider
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - legostin-wirepane.md
---

# Wirepane

## What it is

Wirepane is an HTTPS debugging proxy designed to be used inside Claude Code, functioning as an alternative to tools like Proxyman or Charles. It intercepts and decrypts network traffic originating from browsers, iOS Simulators, iPhones, and Android devices, displaying the traffic in a pane alongside the conversation for analysis.

## How it works

Wirepane acts as a plugin that hooks into functions to decrypt various protocols, including HTTP/1.1, HTTP/2, gRPC, WebSockets, and Server-Sent Events. It decodes Protobuf bodies and various compression formats like gzip, brotli, deflate, and zstd.

The tool provides a rules engine that allows users to manipulate traffic by setting breakpoints, applying mocks, delays, throttling, errors, rewriting headers and URLs, or sending requests to a local server. Claude can then read this traffic, identify issues (such as missing CA certificates or pinned certificates), and write rules to fix the underlying code.

## TWSC experience

Not yet tested by TWSC.

## Related

- [mitmproxy](../entities/mitmproxy.md)
- [playwright](../entities/playwright.md)
- [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)


## Sources

- [https://github.com/legostin/wirepane](https://github.com/legostin/wirepane)
