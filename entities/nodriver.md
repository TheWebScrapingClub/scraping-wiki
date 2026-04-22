---
name: Nodriver
type: entity
category: tool
first_seen: 2024-09-01
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/bypassing-cloudflare-with-nodriver
  - https://substack.thewebscraping.club/p/open-source-python-libraries-scraping
---

# Nodriver

## What it is

Nodriver is an open-source Python browser automation library created by ultrafunkamsterdam (the same author as undetected-chromedriver). It controls Chrome directly without a WebDriver layer, connecting via the Chrome DevTools Protocol internally but in a way that avoids the CDP detection signatures that plague standard automation tools. Nodriver is async-first and positions itself as a faster, lighter successor to undetected-chromedriver. A more actively maintained fork called Zendriver also exists.

## How it works

By removing the WebDriver layer, Nodriver reduces the detectable surface area for anti-bot systems: there is no `navigator.webdriver` flag, no ChromeDriver process, and no Selenium-injected properties. The tool communicates directly with Chrome via internal CDP in a way that passes the standard CDP detection tests (such as those on deviceandbrowserinfo.com) that catch Playwright and Selenium.

The library is async and supports launching multiple browser windows and managing them concurrently within a single Python event loop.

What Nodriver does not provide:
- Fingerprint forging: the browser sends the actual hardware fingerprint of the machine it runs on.
- Authenticated proxies: Chromium has limitations in this area that Nodriver inherits.
- Human behavior emulation: no ghost-cursor style mouse movement is included.

## TWSC experience

We tested Nodriver in September 2024 against Harrods.com (Cloudflare-protected).

Against the standard bot detection tests at deviceandbrowserinfo.com, Nodriver passed all checks including the CDP detection test that fails standard Playwright. This was without any additional patches.

Against Harrods.com from a datacenter IP:
- Blocked. The device fingerprint was not masked, so the AWS server hardware (SwiftShader GPU, no audio/video devices) was visible to Cloudflare. Adding a proxy would not have helped, because the fingerprint issue was independent of IP.

Against Harrods.com from a local machine:
- Succeeded. The same script opened the homepage and was able to extract product JSON from category pages. The key extraction point was `window.__PRELOADED_STATE__` embedded in a script tag.

The core limitation is that Nodriver's stealth properties rely entirely on the environment's genuine fingerprint looking legitimate. When run locally on consumer hardware, this is fine. When deployed on a datacenter server, the hardware fingerprint is immediately a red flag regardless of the WebDriver detection properties.

A direct comparison: Playwright with the same local machine also opened Harrods without issue, despite being detectable by CDP tests. This confirms that for Harrods, the CDP test is not evaluated - IP and hardware fingerprint are the operative signals.

## Known limitations

- Cannot forge a different fingerprint. Consumer hardware is required for environments where the actual fingerprint is checked.
- Authenticated proxy support is difficult due to Chromium limitations. This means combining Nodriver with residential proxies requires workarounds.
- Not viable for production datacenter deployment on targets that check hardware fingerprints.
- TWSC assessment (2024): suitable for small projects running locally, not for production environments running on datacenter infrastructure.

## Related

- [Undetected-chromedriver](undetected-chromedriver.md)
- [Camoufox](camoufox.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [CDP Detection](../concepts/cdp-detection.md)
- [Cloudflare](cloudflare.md)
