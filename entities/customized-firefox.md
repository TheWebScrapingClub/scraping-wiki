---
name: customized-firefox
type: entity
category: browser
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - evading-anti-debugging-techniques.md
---

# Customized Firefox

## What it is

A modified version of the Firefox browser that renames the JavaScript `debugger` keyword to `ticket_debugger`. This modification is intended to bypass anti-debugging measures implemented on websites, particularly those that use JavaScript obfuscation techniques to prevent inspection of their code.

## How it works

The customization involves patching Firefox's source code. Specifically, it modifies two header files: `js/src/frontend/ReservedWords.h` and `js/src/vm/CommonPropertyNames.h`. In these files, the `debugger` keyword is replaced with `ticket_debugger`. This change ensures that when a website's JavaScript code attempts to use the `debugger` statement, it will no longer trigger the browser's built-in debugging functionality as intended by the original keyword.

By renaming the keyword, the browser's JavaScript engine will not recognize `debugger` as a command to halt execution. This allows scripts that rely on anti-debugging techniques, which often check for the presence and functionality of the `debugger` keyword, to be executed without interruption. The authors also mention extending this custom browser to retrieve and deobfuscate encryption keys used by anti-bot scripts.

## TWSC experience

Not yet tested by TWSC.
## Related

- [browser-use](../entities/browser-use.md)
- [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)
- [client-side-bot-detection](../entities/client-side-bot-detection.md)


## Sources

- [https://nullpt.rs/evading-anti-debugging-techniques](https://nullpt.rs/evading-anti-debugging-techniques)
