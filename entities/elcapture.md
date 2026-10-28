---
name: elcapture
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - elcapture-com.md
---

# elcapture

## What it is

elcapture is a native HTTPS debugging proxy designed for Mac users. It allows users to inspect, pause, modify, and replay HTTPS traffic originating from various sources, including applications, phones, Android emulators, and iOS Simulators, without requiring code modification.

## How it works

The tool decrypts and makes readable HTTPS traffic, supporting protocols like HTTPS, HTTP/2, WebSocket, and gRPC, as well as raw TCP and UDP. It provides features such as breakpoints to pause requests, mocks and rewrites using regex and JSON patches, and the ability to replay entire sessions from recorded HAR files. Users can also inject scripts written in JavaScript, Python, or Rhai to execute on every request, response, or WebSocket message.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

elcapture is currently in beta, and the beta version is not yet notarized by Apple.

## Sources

- [https://elcapture.com](https://elcapture.com)
