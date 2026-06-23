---
name: otto
type: entity
category: browser
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
  - telepat-io-otto.md
---

# Otto

## What it is

Otto is a secure remote browser automation platform designed to control real browser tabs without the need to host a browser farm or manage significant infrastructure overhead. It allows developers and automation teams to execute web workflows by sending commands to live browser tabs via a WebSocket relay daemon.

## How it works

The system operates through a Controller, which sends authenticated commands over a WebSocket connection to a relay daemon running on port 8787. This relay routes the commands to a lightweight Chrome extension node, which executes the required actions on the live browser tabs.

This architecture allows for remote CLI control, meaning commands can be sent from a local machine to a browser running anywhere, as the relay handles the necessary routing and authentication between the controller and the node.

## TWSC experience

Not yet tested by TWSC.

## Related

* [browser-use](../entities/browser-use.md)
* [browserbase-chrome](../entities/browserbase-chrome.md)
* [puppeteer](../entities/puppeteer.md)


## Sources

- [https://github.com/telepat-io/otto](https://github.com/telepat-io/otto)
