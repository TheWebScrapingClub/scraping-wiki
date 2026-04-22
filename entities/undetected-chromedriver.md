---
name: undetected-chromedriver
type: entity
category: tool
first_seen: 2023-01-01
last_updated: 2026-04-22
---

# Undetected ChromeDriver

## What it is

Undetected ChromeDriver (uc) is a patched version of Selenium's ChromeDriver. It strips or obscures the most obvious WebDriver detection signals from the standard Chrome binary, making automation less detectable than vanilla Selenium. Around 2022 and 2023 it was the most commonly recommended open-source stealth scraping tool.

## How it works

The library patches the ChromeDriver binary at runtime to remove or modify the flags and properties that standard Selenium injects into Chrome. The goal is to make the controlled browser appear closer to a user-launched Chrome instance. It operates within the Selenium API, so existing Selenium code can be migrated with minimal changes.

Successors have since emerged. Nodriver dropped the Selenium dependency entirely in favor of direct CDP. Zendriver is a more actively maintained fork of Nodriver.

## TWSC experience

In 2023 testing, undetected-chromedriver worked against 4 out of 5 anti-bot systems when run from a local machine. Moving the same setup to a datacenter IP caused complete failure across all targets, which confirmed that IP reputation was already a critical variable and that the browser-level patches alone were insufficient without residential or ISP proxies.

With residential proxies applied, the tool still failed against [Cloudflare](cloudflare.md), [Datadome](datadome.md), and [Kasada](kasada.md). The failures pointed to hardware fingerprint signals that the ChromeDriver patches do not address: datacenter-class hardware produces different fingerprint distributions than consumer laptops and desktops, and anti-bot systems have learned to identify these patterns.

In the 2026 benchmark (100 requests per target), results were mixed:

- Harrods: 89% success. Harrods runs a lenient Cloudflare configuration, and the failures were caused by request timeouts, not bot detection.
- Indeed: 0% success. Indeed runs a stricter configuration and undetected-chromedriver does not get past it.

At the time of the 2026 test, the repository had not received an update in 7 months.

## Known limitations

- Fails completely from datacenter IPs regardless of proxy configuration.
- Hardware fingerprint signals are not addressed by the ChromeDriver patches.
- The repository is not actively maintained. Chrome version compatibility may drift without updates.
- Not viable against strict anti-bot configurations in 2026.
- Succeeded by more capable and maintained tools: Nodriver, Zendriver, [Camoufox](camoufox.md).

## Related

- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)
- [Kasada](kasada.md)
- [playwright](playwright.md)
- [pydoll](pydoll.md)
- [camoufox](camoufox.md)

## Sources

- [https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome](https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026](https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026)
