---
name: cdp-detection
type: concept
first_seen: 2024-07-01
last_updated: 2026-04-22
sources:
  - playwright-stealth-cdp.md
  - the-stealth-stack-web-scraping.md
  - webdriver-vs-cdp-vs-bidi.md
  - playwright-scrapers-undetected.md
---

# CDP Detection

## Definition

A detection technique that identifies browser automation by observing the Chrome DevTools Protocol (CDP) commands sent to the browser during page load. CDP is the underlying control protocol used by Playwright, Puppeteer, Selenium (on Chromium), and related frameworks. Anti-bot systems can detect its presence independently of any JavaScript-level signals.

## How It Works

When automation frameworks control a Chromium browser, they communicate with it over CDP. One of the first commands sent is `Runtime.enable`, which activates the JavaScript runtime inspector. Anti-bot scripts running inside the page can detect that this command was issued, or observe its side effects, and infer that the browser is under external control.

The important characteristic of this technique is that it is generic. It does not look for Playwright-specific behavior or Selenium-specific markers — it detects the CDP channel itself. Any framework that uses CDP to control Chromium is exposed, including custom or obscure automation tools that have never been specifically fingerprinted before.

A straightforward way to verify this behavior: open the target page with no DevTools attached and pass the check. Then open Chrome DevTools on the same page — the anti-bot detects the CDP connection and reclassifies the session as automated, even though no code changed.

[BrowserScan](https://www.browserscan.net) exposes an explicit CDP detection test that makes this observable directly.

## Where It Matters

CDP detection sits below the JavaScript layer. Techniques that were previously sufficient — patching `navigator.webdriver`, hiding `window.chrome`, spoofing `navigator.plugins` — operate at the JS level and have no effect on CDP-level detection. A browser that passes every JS stealth check can still be flagged if the CDP channel is visible.

This makes CDP detection a deeper problem than most browser-level fingerprinting. Scraper operators who assumed that JS patching was the final layer of stealth discovered this gap when previously working setups started failing without any obvious change on the target side.

## What We Tested

[DataDome](../entities/datadome.md)'s engineer Antoine described this technique publicly around July 2024, which is the earliest documented reference in our sources. At the time, it was characterized as one of the latest detection layers being deployed.

Three tools address this at the framework level. Undetected Playwright (Python, by Kaliiiiiiiiii) patches the CDP detection by swapping the internal import — the change is minimal but effectively removes the `Runtime.enable` signal. Patchright is a full drop-in replacement for Playwright that fixes CDP detection along with other detection vectors including `navigator.webdriver` and related flags; it requires no code changes beyond swapping the import. Nodriver provides a native fix at the architecture level rather than as a patch on top of an existing framework.

Both patched solutions exist because patching CDP detection requires access to the browser control layer, not just the JavaScript environment exposed to page scripts.

[Camoufox](../entities/camoufox.md) sidesteps the CDP problem entirely by using a patched Juggler protocol for browser control rather than CDP. This is structurally different from patching CDP detection after the fact.

## WebDriver BiDi and the future of CDP

CDP is a Chromium-specific protocol. Firefox announced the removal of its experimental CDP support in Nightly 141, replacing it with WebDriver BiDi as the standard cross-browser automation protocol. BiDi offers the same bidirectional, event-driven communication model as CDP but is designed as a W3C standard that works across Chrome, Firefox, and Safari.

The detection implications of BiDi are not yet characterized in public anti-bot research. Anti-bot vendors have less accumulated experience with BiDi-based automation than with CDP. This is not a reliable stealth advantage in itself, but it represents an evolving surface. As Playwright and Puppeteer adopt BiDi for Firefox targets, the `Runtime.enable` detection vector (which is CDP-specific) will not apply to BiDi-controlled sessions.

For [webdriver-vs-cdp-vs-bidi](./webdriver-vs-cdp-vs-bidi.md), see the dedicated concept page.

## Current State

As of mid-2024 through 2026, CDP detection has moved from an emerging technique to an actively deployed one. Frameworks that rely on unpatched Playwright or standard Puppeteer against protected targets are exposed. The fix is well-understood but must be applied explicitly — default installations of these frameworks do not patch CDP detection automatically.

Patchright is the recommended drop-in solution for teams running Playwright on Chromium. Camoufox is the recommended solution when Firefox is acceptable as the browser engine, since it avoids CDP entirely.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [webdriver-vs-cdp-vs-bidi](./webdriver-vs-cdp-vs-bidi.md)
- [DataDome](../entities/datadome.md)
- [Camoufox](../entities/camoufox.md)
- [Playwright](../entities/playwright.md)

## Sources

- [https://substack.thewebscraping.club/p/playwright-stealth-cdp](https://substack.thewebscraping.club/p/playwright-stealth-cdp)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/webdriver-vs-cdp-vs-bidi](https://substack.thewebscraping.club/p/webdriver-vs-cdp-vs-bidi)
- [https://substack.thewebscraping.club/p/playwright-scrapers-undetected](https://substack.thewebscraping.club/p/playwright-scrapers-undetected)
