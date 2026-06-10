---
name: bot-detection-system
type: entity
category: anti-bot
first_seen: 2026-06-10
last_updated: 2026-06-10
sources:
  - blog-how-bot-detection-works.md
---

# Bot Detection System

## What it is

A bot detection system separates real users from unwanted automation by employing probabilistic scoring rather than relying on a single check. It gathers dozens of individually weak signals across multiple layers—including network, TLS, browser, and behavioral analysis—to generate a single risk score. This score then dictates an action, such as serving the page normally, running a silent challenge, showing a hard CAPTCHA, blocking the request, or serving degraded data.

## How it works

The system operates in layers, starting with the network connection. It analyzes IP reputation, Autonomous System Number (ASN) classification, request rate and distribution, and IP consistency within a session. Subsequent layers involve TLS and HTTP/2 fingerprinting, which examine the mechanics of connection negotiation, and browser fingerprinting. The system weights these signals, looking for contradictions—such as a Chrome User-Agent paired with a Node TLS fingerprint—to determine a high-confidence bot signal.

## TWSC experience

Not yet tested by TWSC.

## Related

* [tls-fingerprinting](../concepts/tls-fingerprinting.md)
* [bot-detection](../concepts/bot-detection.md)


## Sources

- [https://intunedhq.com/blog/how-bot-detection-works](https://intunedhq.com/blog/how-bot-detection-works)
