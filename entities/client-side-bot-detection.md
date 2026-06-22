---
name: client-side-bot-detection
type: entity
category: anti-bot
first_seen: 2026-06-22
last_updated: 2026-06-22
sources:
  - blog-reverse-once-run-forever.md
---

# Client-side bot detection

## What it is

Client-side bot detection involves running detection logic within the browser environment, which presents an asymmetry where the code executes in an environment controlled by the attacker, including their CPU, debugger, and clock. This means that any signals used to detect automation, such as mouse kinematics, rendering quirks, or timing jitter, are invisible to the server-side detection system.

## How it works

The core challenge is that the code must reside in the page where the bot is operating, as this is the only place the signals exist. Instead of relying on obfuscation to hide the logic, the approach treats obfuscation as a cost, aiming to make reverse-engineering the code worthwhile for the attacker. This is achieved by making the internal encoding and mapping of operations regenerate with every build, ensuring that static signatures extracted from one version do not apply to the next.

A second principle is to avoid branching decisions in critical security checks. Instead of using conditional statements like `if (debuggerDetected) { ... }`, the system uses cryptography to fold the signal into key material. If the execution environment is legitimate, the derived key is correct; if tampering occurs, the derived key is wrong, causing the program to fail without providing an explicit "caught" flag.

## TWSC experience

Not yet tested by TWSC.

## Related

* [browser-use](../entities/browser-use.md)
* [bot-detection-system](../entities/bot-detection-system.md)
* [browserbase-chrome](../entities/browserbase-chrome.md)


## Sources

- [https://trustsig.eu/blog/reverse-once-run-forever/](https://trustsig.eu/blog/reverse-once-run-forever/)
