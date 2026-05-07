---
name: browser-use
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - posts-bot-detection.md
---

# Browser Use

## What it is

Browser Use is a cloud-based browser automation platform that aims to create undetectable browsers. It maintains a custom Chromium fork with numerous patches at the C++ and OS level, ensuring that the browser is undetectable by major antibot systems such as Cloudflare, DataDome, Kasada, Akamai, PerimeterX, and Shape Security.

## How it works

Browser Use achieves undetectability by forking Chromium and making fundamental changes to the browser's behavior. When the browser reports `navigator.webdriver === false`, it is because the value was never true in the first place. Every function returns `[native code]` when stringified, and every prototype chain is intact. This means that the browser is engineered to be undetectable, not just by JavaScript fingerprinting but also by other layers of antibot systems such as IP reputation, timezone and locale, hardware consistency, API availability, and behavioral signals.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

OMIT

## Related

- [Cloudflare](../entities/cloudflare.md)
- [DataDome](../entities/datadome.md)
- [Kasada](../entities/kasada.md)


## Sources

- [https://browser-use.com/posts/bot-detection](https://browser-use.com/posts/bot-detection)
