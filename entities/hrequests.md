---
name: hRequests
type: entity
category: library
first_seen: 2023-11-23
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/the-lab-32-hrequests-vs-anti-bots
  - https://substack.thewebscraping.club/p/apis-in-web-scraping
---

# hRequests

## What It Is

hRequests (human requests) is a Python HTTP client library that combines browser-realistic TLS fingerprinting with optional headless browser rendering in the same session object. Built by daijro (same author as Camoufox), it acts as a hybrid between `requests` and a stripped-down Playwright, sharing the same session context across both modes.

GitHub: https://github.com/daijro/hrequests

## How It Works

hRequests sessions can make plain HTTP requests with browser-like TLS fingerprints, and then switch to a rendered browser mode within the same session using `.render()`. Cookies and other session state persist across both modes.

The `mock_human=True` parameter in the render call simulates basic human-like behavior during page interaction.

Supported browser profiles: Firefox, Chromium. The `os` parameter allows specifying the OS being emulated.

```python
session = hrequests.BrowserSession(headless=False)
session.get(url)
page = response.render(mock_human=True)
```

Or with a pre-configured browser:
```python
session = hrequests.firefox.Session(os='mac')
```

## TWSC Experience

Benchmarked against Akamai, Cloudflare, DataDome, PerimeterX, and Kasada (Lab #32, November 2023):

| Target | Result | Notes |
|--------|--------|-------|
| Akamai (luisaviaroma.com) | Pass | Headful Firefox session + headless API calls |
| Cloudflare (harrods.com) | Pass | Firefox browser with random sleep between pages |
| DataDome (footlocker.it) | Fail | Triggered CAPTCHA after first request; residential proxy did not help |
| PerimeterX (neimanmarcus.com) | Pass | Occasional "Press and Hold" CAPTCHA; API calls succeeded |
| Kasada (canadagoose.com) | Fail | Blank screen on homepage load; challenge not passed |

The key strength: the session handoff between headful and headless modes. This was useful in production against Akamai, where the headful mode solved the initial challenge and headless mode handled catalog iteration.

The key weakness: limited options in the Playwright mode compared to dedicated browser automation tools. Complex anti-bots (Kasada, strict DataDome configs) that require fine-grained control of browser behavior are not achievable with hRequests alone.

hRequests was also recommended as the HTTP client for API scraping (apis-in-web-scraping.md), where its automatic TLS fingerprint handling removes the need to configure impersonation manually.

## Known Limitations

- The browser mode offers fewer configuration points than direct Playwright or Camoufox. Mouse movement, precise timing control, and fingerprint customization are limited.
- Kasada's hardware-level fingerprinting is not passable as of the test date (Nov 2023).
- DataDome fails after the first request; the library does not sustain the behavioral score across multiple session accesses.
- The project appears to be less actively maintained than curl_cffi or Camoufox (no specific update date confirmed).

## Related

- [api-scraping](../concepts/api-scraping.md)
- [hybrid-scraping](../concepts/hybrid-scraping.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)
- [curl-cffi](curl-cffi.md)
- [camoufox](camoufox.md)
- [DataDome](datadome.md)
- [Kasada](kasada.md)
