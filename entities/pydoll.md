---
name: pydoll
type: entity
category: tool
first_seen: 2026-01-01
last_updated: 2026-04-22
---

# Pydoll

## What it is

Pydoll is a Python async browser automation library built directly on the Chrome DevTools Protocol (CDP). It was created by Thalison Fernandes under the autoscrape-labs organization. Unlike [Playwright](playwright.md) or Selenium, Pydoll has no WebDriver layer: it communicates with Chrome directly via CDP. It is async-first by design.

## How it works

Pydoll opens and controls Chrome through raw CDP commands. The async architecture allows concurrent tab management, making it theoretically suitable for multi-tab scraping workloads without the overhead of separate browser processes.

The library provides browser contexts for session isolation and exposes human-like interaction primitives: click offset randomization, keystroke delays, and smooth scroll behavior.

A notable feature is `expect_and_bypass_cloudflare_captcha()`, a method that handles Cloudflare Turnstile challenges. The library's documentation also references future features including Bezier curve mouse paths, physics-based scrolling, and cognitive delays between actions, positioned as a behavioral analysis bypass layer.

## TWSC experience

We tested Pydoll in 2026 as part of the Cloudflare bypass benchmark. Results were poor across both targets:

- Indeed: 0% success. Pages loaded incompletely and the tool failed silently without raising exceptions.
- Harrods: 1% success. CDP connections crashed repeatedly, with Chrome consuming 98.9% CPU before dying.

We also found significant documentation accuracy issues. The `Browser` class referenced in multiple code examples in the official documentation does not exist. `tab.html()` does not work as documented. `tab.current_url` is an attribute, not a method, contrary to the documentation showing it called as `tab.current_url()`.

The future features listed in the documentation (Bezier curves, physics scrolling, cognitive delays) had not shipped at the time of testing.

## Known limitations

- Unreliable under real anti-bot conditions. Both test targets produced near-zero success rates.
- Chrome resource consumption is severe. The 98.9% CPU figure makes concurrent deployment impractical.
- Documentation does not accurately reflect the current API. Code copied from the docs will not run without debugging.
- Silent failure mode on incomplete pages makes error detection harder than with exception-throwing tools.
- Promised behavioral features were not available at time of testing.

## Related

- [Cloudflare](cloudflare.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [playwright](playwright.md)
- [undetected-chromedriver](undetected-chromedriver.md)

## Sources

- [https://substack.thewebscraping.club/p/pydoll-webdriver-scraping](https://substack.thewebscraping.club/p/pydoll-webdriver-scraping)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026](https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026)
