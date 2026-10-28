---
name: pw-repl
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - arcanemachine-pw-repl.md
---

# pw-repl

## What it is

pw-repl is a Playwright-powered tool designed to allow users and AI agents to share control over a Chromium browser session through command-line interaction. It functions as a swiss-army knife for interacting with a browser, enabling collaborative control over a running or headless Chromium instance.

## How it works

The tool connects to a Chromium instance via the Chrome DevTools Protocol (CDP), either connecting to a browser session the user already uses or starting a new one. Users interact with the browser by typing commands at a `pw>` prompt. Agents can send the same commands from a shell using the `pw-repl send` command.

Every command executed is displayed in the REPL, showing who sent it, ensuring transparency for both the user and the agents.

## TWSC experience

Not yet tested by TWSC.

## Related

- [playwright](../entities/playwright.md)


## Sources

- [https://github.com/arcanemachine/pw-repl](https://github.com/arcanemachine/pw-repl)
