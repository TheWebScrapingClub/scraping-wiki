---
name: webcrack
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - reverse-engineering-browser.md
---

# Webcrack

## What it is

Webcrack is a tool designed to assist in the reverse-engineering of web pages, specifically by aiding in the deobfuscation of JavaScript snippets. It aims to streamline the process of analyzing and understanding obfuscated code encountered during web scraping or security analysis.

## How it works

Webcrack leverages the Chrome DevTools Protocol (CDP) to inject JavaScript code into web pages before the page's own scripts are executed. This is achieved using the `Page.addScriptToEvaluateOnNewDocument` command, which allows for early execution of custom scripts in every frame.

The injected script can then override or hook into native JavaScript functions, such as `Array.prototype.push`. By observing calls to these functions, Webcrack can help trace the execution flow and identify patterns within obfuscated code, facilitating deobfuscation efforts. The tool was prototyped using Electron to quickly set up a UI and inter-process communication for demonstration purposes.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The source document mentions that content scripts in Chrome extensions run in an isolated world, which prevents them from directly modifying the page's JavaScript environment in the way needed for early function hooking. While a workaround of injecting a `<script>` tag was considered, the author found it insufficient and opted for the CDP approach.

## Related

* [playwright](../entities/playwright.md)
* [puppeteer](../entities/puppeteer.md)


## Sources

- [https://nullpt.rs/reverse-engineering-browser](https://nullpt.rs/reverse-engineering-browser)
