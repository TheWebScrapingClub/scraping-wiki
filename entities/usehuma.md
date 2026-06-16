---
name: usehuma
type: entity
category: anti-bot
first_seen: 2026-06-16
last_updated: 2026-06-16
sources:
  - blog-anatomy-of-a-55k-bot-attack.md
---

# useHUMA

## What it is

useHUMA is an anti-bot startup that provides bot detection services. The system is designed to verify human behavior by analyzing various metrics, aiming to provide transparent bot detection without relying on CAPTCHAs, puzzles, or Personally Identifiable Information (PII).

## How it works

The system scores behavior by analyzing metrics such as mouse movement, keystroke cadence, scroll rhythm, and touch patterns. These behavioral signals are used by the engine to determine if the activity is human or automated.

When the system was called without behavioral signals, such as only a `userId`, the engine returned a neutral score, which cleared the threshold and allowed bots to pass detection. The goal is to pass real behavioral signals through the signup flow so the product functions as designed.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The system failed when called without behavioral signals, resulting in a neutral score that allowed bots to pass detection. The fix involves passing real behavioral signals through the signup flow to ensure the system is used as designed.

## Related

* [bot-detection-system](../entities/bot-detection-system.md)
* [Mouse Movement Emulation](../concepts/mouse-movement-emulation.md)
* [browser-fingerprinting](../concepts/browser-fingerprinting.md)


## Sources

- [https://humaverify.com/blog/anatomy-of-a-55k-bot-attack](https://humaverify.com/blog/anatomy-of-a-55k-bot-attack)
