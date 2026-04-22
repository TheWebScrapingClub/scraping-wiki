---
name: playwright
type: entity
category: tool
first_seen: 2023-01-01
last_updated: 2026-04-22
---

# Playwright

## What it is

Playwright is a browser automation framework developed by Microsoft. It supports Chromium, Firefox, and WebKit through a unified API. It is the most widely used modern browser automation library and the foundation on which most TWSC browser-based scraping work is built, either directly or as the underlying engine for higher-level tools.

## How it works

Playwright controls browsers through the Chrome DevTools Protocol (CDP) for Chromium-based targets and through Juggler for Firefox. The framework exposes async Python, JavaScript, TypeScript, Java, and .NET APIs.

Standard Playwright emits several signals that anti-bot systems use for detection:

- The CDP `Runtime.enable` command is sent during session initialization and is observable by pages instrumented to watch for it.
- `navigator.webdriver` is set to `true` by default in automation contexts.
- Default window dimensions and viewport sizes differ from real user distributions.

The stealth plugin that existed for Playwright (playwright-stealth) is no longer maintained and does not cover current detection vectors.

Two patched alternatives address the most critical detection issues:

**Undetected Playwright Python** (by Kaliiiiiiiiii): patches the `Runtime.enable` detection vector through an import-swap mechanism. Drop-in compatible with standard Playwright.

**Patchright**: a full drop-in replacement for Playwright that fixes the known detection flaws in the standard distribution, including CDP signals, webdriver flags, and related leaks.

## TWSC experience

We use Playwright in almost every browser-based scraping context, either directly or as the automation layer inside [Camoufox](camoufox.md), [Scrapling](scrapling.md), or other tools.

Alone, standard Playwright fails against all strict anti-bot configurations. With Brave as the browser binary and stealth patches applied, it handles medium-difficulty configurations. Against [Datadome](datadome.md), the key additional requirement is realistic mouse movement: Playwright's native pointer events are insufficient without a Bezier curve implementation. We used [ghost-cursor](ghost-cursor.md) on top of Playwright to navigate hermes.com menus under Datadome protection where native mouse events failed.

Playwright has been tested against [PerimeterX](perimeterx.md) (Labs 35 and 56), [Datadome](datadome.md), and [Cloudflare](cloudflare.md). Results vary significantly by configuration and whether additional stealth layers are applied.

## BrowserContext vs Persistent Context

Playwright offers two session models relevant to scraping:

**BrowserContext** creates an isolated in-memory context within a running browser. Each context has its own cookies, localStorage, and cache. It is ephemeral by default: when the context is closed, all session data is discarded. This is the standard mode for stateless scraping.

**Persistent Context** (`launch_persistent_context`) writes session data to a directory on disk, which persists across browser restarts. This is required when the scraper needs to maintain a warmed session across runs — for example, when a cookie factory deposits authentication cookies that must survive a script restart. The persistent context is also useful for reducing cold-start overhead on targets where the homepage-first navigation or cookie warming is time-consuming.

## CDP remote connection

Playwright can connect to an already-running browser via `playwright.chromium.connect_over_cdp(endpoint_url)`. This is the integration mechanism used by [anti-detect browsers](../concepts/anti-detect-browsers.md) (GoLogin, Kameleo, Dolphin{anty}): the anti-detect browser launches a profile and exposes a local CDP endpoint; the Playwright script connects to that endpoint and drives the pre-configured browser.

The same mechanism connects Playwright to remote Camoufox instances running in Docker containers.

## Stealth launch arguments

When launching Chromium-based browsers directly (without an anti-detect tool), these Chrome flags suppress the most visible automation signals:

- `--disable-blink-features=AutomationControlled`: removes the `navigator.webdriver` flag and the associated Blink automation override
- `ignore_default_args=["--enable-automation"]`: prevents Playwright from passing the `--enable-automation` flag, which is one of the earliest JS-visible automation markers

These arguments do not resolve CDP-level detection or TLS fingerprint issues, but they address the simplest JS-level signals without additional libraries.

The `slow_mo` parameter (milliseconds between actions) adds timing delays between interactions. It is useful for targets that score interaction velocity, though it should be combined with randomized delays rather than used as a fixed value, since fixed-interval timing is itself a detectable pattern.

## Scrapy integration: anti-bot routing heuristic

When combining Playwright with Scrapy via `scrapy-playwright`, TWSC documented an anti-bot-specific routing heuristic based on which protection system is present:

- PerimeterX: scrapy-impersonate with residential proxies
- Akamai: scrapy-impersonate with residential proxies
- Cloudflare: Playwright with Firefox (Camoufox) and residential proxies
- Kasada: Playwright with anti-detect browser
- DataDome: Camoufox directly

This heuristic reflects the relative detection sophistication of each system and which tool category addresses the primary detection vector for each.

## Logging patterns

For production Playwright deployments, TWSC documented a logging architecture using psutil for process-level metrics (CPU, memory per browser instance), RabbitMQ for event queuing (scraping job dispatch and result collection), and S3/boto3 for log storage. This stack allows visibility into browser resource consumption across concurrent scraping sessions.

Playwright's built-in `request` and `response` events on the page object provide HTTP-level request logging without a proxy. Network interception (`page.route`) can be combined with this for request modification or filtering.

## Known limitations

- The stealth plugin is deprecated and should not be relied upon.
- Standard Playwright is reliably detected by all major anti-bot vendors without additional patches.
- CDP-based detection (`Runtime.enable`) is a structural issue that requires patched distributions to fix.
- Even with patches, Playwright on Chromium carries TLS fingerprint signals that differ from real users. Pairing with [curl_cffi](curl-cffi.md) for the data extraction phase addresses this at the HTTP layer.

## Related

- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [Camoufox](camoufox.md)
- [Scrapling](scrapling.md)
- [ghost-cursor](ghost-cursor.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)
- [PerimeterX](perimeterx.md)
- [pydoll](pydoll.md)

## Sources

- [https://substack.thewebscraping.club/p/playwright-stealth-cdp](https://substack.thewebscraping.club/p/playwright-stealth-cdp)
- [https://substack.thewebscraping.club/p/fingerprint-injection-playwright](https://substack.thewebscraping.club/p/fingerprint-injection-playwright)
- [https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright](https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright)
- [https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with](https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with)
- [https://substack.thewebscraping.club/p/the-lab-56-bypassing-perimeterx-3](https://substack.thewebscraping.club/p/the-lab-56-bypassing-perimeterx-3)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/playwright-scrapers-undetected](https://substack.thewebscraping.club/p/playwright-scrapers-undetected)
- [https://substack.thewebscraping.club/p/how-to-start-with-scrapy-and-playwright](https://substack.thewebscraping.club/p/how-to-start-with-scrapy-and-playwright)
- [https://substack.thewebscraping.club/p/advanced-logging-in-playwright](https://substack.thewebscraping.club/p/advanced-logging-in-playwright)
- [https://substack.thewebscraping.club/p/playwright-tips-tricks-scraping](https://substack.thewebscraping.club/p/playwright-tips-tricks-scraping)
- [https://substack.thewebscraping.club/p/5-features-playwright-web-scraping](https://substack.thewebscraping.club/p/5-features-playwright-web-scraping)
