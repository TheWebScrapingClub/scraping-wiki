---
name: botdeflector-solver-chrome-extension
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-botdeflector-solver-chrome-extension.md
---

# botdeflector-solver-chrome-extension

## What it is

The BotDeflector Solver Chrome Extension is a tool designed to automatically detect and solve the BotDeflector captcha. This captcha is commonly encountered in Queue-IT waiting rooms and other custom implementations.

## How it works

The extension operates with a content script injected into every page and a service worker running in the background. When a BotDeflector captcha is detected on a page, the extension captures the captcha's images. These images are then sent to TakionAPI for solving. Once the solution is received, the extension executes the necessary actions, such as clicking on specific elements, based on the instructions provided by the API.

The extension provides non-invasive notifications in the top-right corner of the browser to keep the user updated on the captcha-solving process. It can be configured with a TakionAPI key, which can be obtained through a trial.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Branded Google Chrome ignores the `--load-extension` argument since version 137. For such cases, it is recommended to use Chrome for Testing or Chromium.

## Related

- [cloudflare](../entities/cloudflare.md)


## Sources

- [https://takionapi.tech/blog/botdeflector-solver-chrome-extension](https://takionapi.tech/blog/botdeflector-solver-chrome-extension)
