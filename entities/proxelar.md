---
name: proxelar
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - emanuele-em-proxelar.md
---

# proxelar

A programmable MITM proxy written in Rust that intercepts HTTP/HTTPS traffic, allowing you to inspect and modify it with Lua scripting, a TUI, and a web interface.

## How it works

Proxelar sits between your application and the internet, giving you full visibility into every HTTP/HTTPS request and the power to transform it on the fly with Lua. It supports HTTPS interception, forward and reverse proxy modes, and provides a terminal, TUI, and web GUI for interaction.

## TWSC experience

Not yet tested by TWSC.

## Related

- [playwright](../entities/playwright.md)
- [ja3proxy](../entities/ja3proxy.md)
- [kadoa](../entities/kadoa.md)


## Sources

- [https://github.com/emanuele-em/proxelar](https://github.com/emanuele-em/proxelar)
