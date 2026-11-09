---
name: botid
type: entity
category: anti-bot
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - reversing-botid.md
---

# BotID

## What it is

BotID is an invisible CAPTCHA system developed by Vercel designed to protect against sophisticated bots without presenting visible challenges or requiring manual user intervention. It operates by collecting client-side signals to identify and block automated traffic.

## How it works

BotID functions by integrating a JavaScript script, referred to as `c.js`, into web pages. This script collects various client-side signals to assess the likelihood of a request originating from a bot. The obfuscated nature of the script, with its indirect function calls and mangled names, suggests an effort to make reverse engineering more challenging.

The script utilizes browser APIs, such as the `crypto` API, to gather information. It appears to perform cryptographic operations, potentially for generating unique identifiers or performing checks that are difficult for bots to replicate accurately. The collected signals are then used to determine if the visitor is a bot or a human.

## TWSC experience

Not yet tested by TWSC.
## Related

The following pages are related to BotID:
- [client-side-bot-detection](../entities/client-side-bot-detection.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [Kasada](../entities/kasada.md)


## Sources

- [https://nullpt.rs/reversing-botid](https://nullpt.rs/reversing-botid)
