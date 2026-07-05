---
name: proxyboy
type: entity
category: tool
first_seen: 2026-07-05
last_updated: 2026-07-05
sources:
  - pjperez-proxyboy.md
---

# ProxyBoy

## What it is

ProxyBoy is a Windows-native HTTP/HTTPS debugging proxy designed to capture, inspect, and modify network traffic, similar to tools like Charles Proxy or Proxyman. Its key differentiator is the embedded AI assistant, powered by the GitHub Copilot SDK, which provides conversational analysis, rule creation, and debugging assistance for network traffic.

## How it works

The proxy engine is built using the `http-mitm-proxy` library and is implemented using Electron, React, and TypeScript. It handles traffic interception, automatic SSL certificate generation, and provides detailed inspection capabilities for request and response bodies, headers, and timing.

The AI assistant leverages the GitHub Copilot SDK to interact with the captured traffic. It utilizes specific tools, such as `searchTraffic` and `getFlowDetails`, to analyze patterns, find errors (4xx/5xx responses), and allow users to create breakpoint rules or mock API endpoints.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

This is a personal/experimental project. The full AI assistant functionality requires a GitHub Copilot subscription, although the core proxy functionality works without it.

## Related

- [mitmproxy](../entities/mitmproxy.md)
- [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://github.com/pjperez/proxyboy](https://github.com/pjperez/proxyboy)
