---
name: kittybrowser
type: entity
category: browser
first_seen: 2026-11-13
last_updated: 2026-11-13
sources:
  - graiz-kittybrowser.md
---

# KittyBrowser

## What it is

KittyBrowser is a web browser designed to run within a terminal pane. It leverages the kitty graphics protocol to render headless Chrome content directly in the terminal, allowing for interactive browsing with visual fidelity, including layouts, fonts, and images. It is built to complement coding agents by providing a visual interface for tasks such as loading development servers, checking console errors, or navigating documentation.

## How it works

KittyBrowser drives a headless instance of Chrome (or compatible browsers like Chromium, Edge, or Brave). Instead of rendering the browser's output to a separate window, it captures the graphical output and transmits it as pixels to a compatible terminal emulator that supports the kitty graphics protocol. This allows the browser content to be displayed directly within a terminal pane, alongside other terminal-based tools or agents.

Users can interact with the rendered web pages using keyboard shortcuts and mouse actions within the terminal pane. This includes navigating back and forth, reloading pages, editing the address bar, searching within the page, and even inspecting elements using Chrome DevTools.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

*   Requires a terminal emulator that supports the kitty graphics protocol (e.g., Ghostty, kitty, WezTerm). It does not work within tmux or screen, and terminals like Terminal.app and iTerm2 are not supported.
*   Does not run natively on Windows; requires WSL 2 with a compatible terminal.

## Related

*   [browser-use](../entities/browser-use.md)


## Sources

- [https://github.com/graiz/kittybrowser](https://github.com/graiz/kittybrowser)
