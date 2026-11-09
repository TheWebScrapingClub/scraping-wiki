---
name: dzt-s-captcha-harvester
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - anatomy-of-a-supreme-bot-part-2.md
---

# dzt's captcha-harvester

## What it is

dzt's captcha-harvester is a tool designed for captcha harvesting, specifically to store the `g-recaptcha-response` token for use during checkout processes.

## How it works

The tool operates on the principle of captcha harvesting, where a bot user completes captchas, and the harvester stores the resulting `g-recaptcha-response` token. This stored token can then be utilized in subsequent checkout requests, bypassing the need for manual captcha completion for each transaction.

## TWSC experience

Not yet tested by TWSC.

## Related

* [reCAPTCHA](../entities/recaptcha.md)


## Sources

- [https://nullpt.rs/anatomy-of-a-supreme-bot-part-2](https://nullpt.rs/anatomy-of-a-supreme-bot-part-2)
