---
name: Anti-Detect Browsers
type: concept
first_seen: 2022-01-01
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/bypass-cloudflare-scraping-playwright
  - https://substack.thewebscraping.club/p/bypassing-cloudflare-gologin-playwrigh
  - https://substack.thewebscraping.club/p/bypassing-cloudflare-with-kameleo
  - https://substack.thewebscraping.club/p/bypassing-cloudflare-free-tools
  - https://substack.thewebscraping.club/p/anti-detect-browsers-fingerprint-tests
  - https://substack.thewebscraping.club/p/anti-detect-browser-royal-rumble-comments
  - https://substack.thewebscraping.club/p/antidetect-browser-webscraping
  - https://substack.thewebscraping.club/p/dolphin-anty-product-review
  - https://substack.thewebscraping.club/p/browser-automation-landscape-2025
  - https://substack.thewebscraping.club/p/anti-detect-pricing-comparison
---

# Anti-Detect Browsers

## Definition

Anti-detect browsers are Chromium or Firefox forks engineered to present a consistent, plausible fingerprint from a database of real device profiles. Unlike standard browser automation which exposes the actual hardware and software environment of the machine running the scraper, anti-detect browsers attach a pre-built fingerprint from a real consumer device to the automation session, regardless of the actual underlying hardware.

## How it works

An anti-detect browser typically holds a database of fingerprints collected from real devices. When a new scraping profile is created, the tool selects a base profile from this database and uses it as a template. The actual fingerprint values exposed to websites (WebGL renderer, canvas hash, audio context, navigator.platform, screen dimensions, media device list) are sourced from the real device record rather than the running machine.

Profiles are then connected to automation frameworks through CDP. Playwright and Selenium can both drive anti-detect browsers by specifying the browser executable path or connecting to an already-launched debugging port:

```python
# Example: connecting Playwright to an anti-detect browser via CDP
browser = playwright.chromium.connect_over_cdp("http://" + debugger_address)
```

Key fingerprint dimensions managed by these tools:
- WebGL vendor and renderer strings
- Canvas fingerprint
- Audio context hash
- Media device count and IDs
- Navigator platform and User-Agent
- Screen resolution
- Client rects

## Where it matters

Anti-detect browsers are the primary countermeasure when a scraper works correctly from a local consumer machine but fails from a datacenter environment, even when a residential proxy is added. This pattern indicates that IP reputation is not the problem - the hardware fingerprint is.

[Cloudflare](../entities/cloudflare.md) is the most commonly encountered anti-bot where device fingerprinting is the operative detection signal. The WebGL renderer string is specifically identified as the critical field on stricter Cloudflare deployments.

## What we tested

**GoLogin (2023, Orbita browser).** Used against Antonioli.eu (Cloudflare). Standard Playwright with Chrome was blocked after a few pages even from a local machine. GoLogin with a Windows profile and no fingerprint masking bypassed Indeed.com Cloudflare Turnstile on an AWS machine. Against Harrods.com (stricter Cloudflare), no masking was not sufficient. Enabling Audio Context noise and Canvas noise was also insufficient. The winning configuration was a Mac fingerprint with specific WebGL vendor and renderer values copied from a real Mac. Success rate was still inconsistent, which led to switching to scrapy-impersonate for Harrods production work.

**GoLogin fingerprint investigation (2024, The Lab #36, against Harrods.com).** Systematic isolation of which fingerprint dimension bypasses Cloudflare:
- Profile with no masking (Linux machine): blocked on Harrods, passed on Indeed.
- Adding Audio Context noise + Client Rects noise: still blocked.
- Adding media devices + Canvas noise: still blocked.
- Mac profile with real WebGL vendor + renderer from a Mac: bypassed. Low success rate in practice.
- Switched to scrapy-impersonate: worked reliably for Harrods production.

**Kameleo (2024, The Lab #37, against Harrods.com).** Kameleo was tested against Harrods. Key characteristics: Windows-only installation (the browser runs on a Windows machine; the scraper can run elsewhere and connect via API). Uses a database of base profiles from real devices. Profiles are created from these base profiles with limited customization to maintain coherence. Both Mac OS and Windows profiles on Kameleo passed Harrods when residential proxies were added via the web interface.

Kameleo assessment:
- More effective than GoLogin on Harrods in TWSC testing (passed on first try vs inconsistent with GoLogin).
- Requires a Windows machine to run the browser (significant infrastructure constraint).
- API requires connecting the scraper to the Windows machine via network.
- Pricing: 199 USD/month per user (Windows machine). At 5 concurrent machines with 10 scrapers each, this exceeds 1000 USD/month.
- Best use case: few high-value targets requiring clean fingerprints; sneaker bots, luxury retail.
- Not cost-effective at scale.

## Benchmark results (2024)

TWSC ran a structured benchmark of 8 anti-detect browsers using CreepJS and BrowserScan as fingerprinting probes. A real Mac running Chrome was used as the baseline (226/260). Scores represent the composite pass rate across all fingerprinting signal categories tested.

| Browser | Score (2024) |
|---|---|
| Real Mac (baseline) | 226/260 |
| GoLogin (Orbita) | 223/260 |
| NSTBrowser | 218/260 |
| Undetectable.io | 209/260 |
| MultiLogin | 203/260 |
| MoreLogin | 198/260 |
| Kameleo | 175/260* |
| Octo Browser | 164/260 |
| Incogniton | 139/260 |

*Kameleo's WebRTC leak was due to a tester configuration error. The actual score may be higher when WebRTC is properly configured.

After publication, MultiLogin noted that their browser (Stealthfox) is Firefox-based, not Chromium, which may affect how CreepJS scores it relative to Chromium-based tools. Scores across engine families may not be directly comparable.

[GoLogin](../entities/gologin.md) and NSTBrowser scored within 4% of the real device baseline. [Incogniton](../entities/incogniton.md) scored 38% below.

## Current state

As of 2025, open-source alternatives have significantly narrowed the gap with commercial anti-detect browsers for most Cloudflare bypass use cases. [Camoufox](../entities/camoufox.md) provides built-in fingerprint rotation from a real device database with no per-seat licensing cost, covers Firefox (which has better Cloudflare pass rates than Chrome), and integrates directly with Playwright. For Cloudflare specifically, Camoufox outperforms or matches what GoLogin and Kameleo offer at far lower cost.

Commercial anti-detect browsers remain relevant for use cases requiring a Chrome fingerprint specifically, or where the target's anti-bot configuration specifically favors Chrome over Firefox.

Pricing reference (2024):
- GoLogin: $49/mo and up for plans with meaningful automation access
- Kameleo: €29/mo (START, rate-limited), €279/mo (SCALE, unlimited)
- Octo Browser: $29/mo (Starter), $79/mo (Base), $169/mo (Team)
- MultiLogin: enterprise-oriented, higher floor price

## Related

- [Camoufox](../entities/camoufox.md)
- [Browser Fingerprinting](./browser-fingerprinting.md)
- [Cloudflare](../entities/cloudflare.md)
- [Firefox vs Chrome Stealth](../comparisons/firefox-vs-chrome-stealth.md)
- [GoLogin](../entities/gologin.md)
- [Kameleo](../entities/kameleo.md)
- [Dolphin Anty](../entities/dolphin-anty.md)
- [anti-detect-browser-benchmark-2024](../comparisons/anti-detect-browser-benchmark-2024.md)
