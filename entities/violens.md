---
name: violens
type: entity
category: tool
first_seen: 2026-11-17
last_updated: 2026-11-17
sources:
  - MarkSPowell-VioLens.md
---

# VioLens

## What it is

VioLens is an open-source, MIT-licensed HTTP/HTTPS debugging proxy and network analysis tool. It is designed as a successor to Fiddler Classic, offering similar functionality for Windows, macOS, and Linux.

## How it works

VioLens captures HTTP and HTTPS traffic by acting as a local proxy. It decrypts HTTPS traffic using a root certificate installed for the user, similar to Fiddler Classic. The tool supports HTTP/2 and WebSocket traffic, displaying messages in dedicated tabs and reassembling fragmented or compressed messages. It can also forward traffic through existing network proxies, including those using PAC scripts or WPAD, and supports authentication methods like Negotiate, NTLM, or username/password.

The tool provides various ways to inspect captured traffic, including live filtering of session lists, detailed timing information comparable to browser developer tools, and multiple inspector tabs for viewing headers, raw data, JSON, Markdown, images, and more. It can decompress various compression formats and offers a session comparison feature to highlight differences. VioLens also includes a TextWizard for encoding/decoding various formats and handling JWTs and SAML.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The project is currently in its release candidate phase for version 1.0. Final testing on macOS and KDE Plasma is pending.

## Related

- [mitmproxy](../entities/mitmproxy.md)


## Sources

- [https://github.com/MarkSPowell/VioLens](https://github.com/MarkSPowell/VioLens)
