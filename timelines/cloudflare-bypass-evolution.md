---
name: Cloudflare Bypass Evolution
type: timeline
subject: cloudflare
last_updated: 2026-04-22
sources:
  - cloudflare-how-to-scrape.md
  - cloudflare-turnstile-what-is-that.md
  - bypassing-cloudflare-in-2026.md
  - undetected-chromedriver-cloudflare-datadome.md
  - fingerprint-injection-playwright.md
  - scrapling-hands-on-guide.md
  - bypass-cloudflare-scraping-playwright.md
  - the-lab-29-bypass-cloudflare-bot.md
  - bypassing-cloudflare-gologin-playwrigh.md
  - bypassing-cloudflare-with-nodriver.md
  - cloudflare-web-unblocker-benchmark.md
  - how-to-bypass-cloudflare-turnstile.md
---

## Subject

How [Cloudflare](../entities/cloudflare.md) bypass techniques have evolved as Cloudflare has progressively tightened its defenses. This timeline tracks what worked, what stopped working, and what replaced it, based on TWSC's direct testing.

## Timeline

### September 2022 - Turnstile announced

Cloudflare introduced Turnstile as a "No CAPTCHA" alternative to reCAPTCHA. Three deployment modes: managed, non-interactive, invisible. Free for site owners, funded by fingerprint data collection for Cloudflare's ML models.

Source: cloudflare-turnstile-what-is-that.md

### January 2023 - Anti-detect browsers enter the workflow

GoLogin was used to bypass Cloudflare on Antonioli.eu when Playwright with Chrome could not handle the datacenter fingerprint even with residential proxies. Connecting Playwright to an Orbita browser profile (GoLogin's browser) via CDP provided a Windows fingerprint that passed Cloudflare. This established anti-detect browsers as a valid approach for datacenter deployment when TLS impersonation alone was insufficient.

Source: bypass-cloudflare-scraping-playwright.md

### September 2022 - Firefox + stealth + behavioral mimicry

TWSC tested three Cloudflare-protected fashion sites. Firefox with Playwright stealth consistently outperformed Chromium. Key discoveries: click flow integrity matters (direct URL access triggers blocks on some configs), persistent browser context improves success, and the Screaming Frog User-Agent paradoxically performed better than standard Chrome UA on brownsfashion.com. Running from EC2 triggered hardware fingerprinting that did not occur locally.

Source: cloudflare-how-to-scrape.md

### October 2023 - TLS-only approach via scrapy-impersonate

TWSC discovered that scrapy-impersonate (a Scrapy wrapper for curl_cffi) bypassed Cloudflare on Harrods.com with 100% success from both local and datacenter environments with residential proxies. This was unexpected: a fully browserless approach with no JavaScript execution, only accurate TLS fingerprinting, was sufficient for Harrods. The finding suggested that for some Cloudflare configurations, TLS fingerprint carries more weight than browser fingerprinting. Scrapy-impersonate uses `meta={'impersonate': 'chrome110'}` to select the browser profile.

Source: the-lab-29-bypass-cloudflare-bot.md

### July 2023 - Undetected-chromedriver local vs datacenter gap

TWSC tested [undetected-chromedriver](../entities/undetected-chromedriver.md) against five anti-bots. Cloudflare was bypassed from local machine (consumer hardware fingerprint) but blocked immediately from AWS datacenter. Adding residential proxies did not help because Cloudflare detected the datacenter hardware fingerprint (SwiftShader GPU, zero audio/video devices).

Source: undetected-chromedriver-cloudflare-datadome.md

### March 2024 - Fingerprint injection as a targeted fix

TWSC tested [Browserforge](../entities/playwright.md) fingerprint injection on Harrods.com (Cloudflare + Turnstile). Plain Chromium blocked by Turnstile. Any Browserforge injection bypassed it. Key finding: WebGL renderer was the critical parameter Cloudflare checked on Harrods. Replacing SwiftShader with an Nvidia GeForce string was sufficient.

Source: fingerprint-injection-playwright.md

### September 2024 - Nodriver passes CDP tests but fails datacenter fingerprint

Nodriver bypassed standard CDP detection tests without patches but was blocked on Harrods from AWS due to unmasked hardware fingerprint. From a local machine, it worked. This confirmed that on Harrods, CDP detection is not evaluated and hardware fingerprint is the operative signal.

Source: bypassing-cloudflare-with-nodriver.md

### September 2024 - Web unblocker benchmark on Indeed.com

All major commercial web unblockers successfully bypassed Cloudflare on Indeed. Zyte API was fastest (6.5s average/request vs 25-34s for others) and cheapest ($0.063 for 100 URLs). ZenRows best first-try accuracy (99%). Bright Data 79/100 (21% retry rate). Oxylabs 97%. Smartproxy 96.8%. Infatica had incomplete rendering on some pages.

Source: cloudflare-web-unblocker-benchmark.md

### January 2025 - Open-source tool comparison on Indeed Turnstile

Testing against Indeed Burger King reviews page from local machine: Botasaurus (with `bypass_cloudflare=True`) succeeded. Patchright (drop-in Playwright replacement) succeeded. Plain Playwright with stealth args: failed. Cloudscraper: failed (stale, not updated in 2 years). Camoufox: inconsistent - some fingerprint profiles detected, requiring retries.

Source: how-to-bypass-cloudflare-turnstile.md

### October 2025 - Scrapling StealthyFetcher

[Scrapling](../entities/scrapling.md) v0.3+ with StealthyFetcher (modified Camoufox internally) bypassed Cloudflare Turnstile even in headless mode, with solve_cloudflare=True and humanize=True.

Source: scrapling-hands-on-guide.md

### January 2026 - Camoufox dominance, Chrome-based tools fail

TWSC benchmark of three tools on two Cloudflare-protected targets. [Camoufox](../entities/camoufox.md): 99% on Harrods, 31% on Indeed (rate limiting after URL 29, not detection). [Pydoll](../entities/pydoll.md): 0% on Indeed (silent failure), 1% on Harrods (CDP crashes). Undetected-chromedriver: 0% on Indeed (403), 89% on Harrods (timeouts, not detection). Firefox-based tools now clearly outperform Chrome-based on strict configurations. The [homepage-first strategy](../concepts/homepage-first-navigation.md) was confirmed critical for Indeed.

Source: bypassing-cloudflare-in-2026.md

## Current state

As of early 2026, Cloudflare's defenses require a layered approach: Firefox-based automation (Camoufox or Scrapling StealthyFetcher) with residential proxies handles most configurations. Lenient configs (like Harrods) can be bypassed with simpler fingerprint injection. Strict configs (like Indeed) still impose rate limiting even on successful sessions. Chrome-based stealth tools are increasingly ineffective against Cloudflare specifically, though they remain viable for other anti-bot systems.

The undetected-chromedriver repository has been inactive for 7+ months, signaling the end of its relevance for Cloudflare bypass.

## Related

- [Firefox vs Chrome Stealth](../comparisons/firefox-vs-chrome-stealth.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [TLS Fingerprinting](../concepts/tls-fingerprinting.md)
- [Homepage-first Navigation](../concepts/homepage-first-navigation.md)

## Sources

- [https://substack.thewebscraping.club/p/cloudflare-how-to-scrape](https://substack.thewebscraping.club/p/cloudflare-how-to-scrape)
- [https://substack.thewebscraping.club/p/cloudflare-turnstile-what-is-that](https://substack.thewebscraping.club/p/cloudflare-turnstile-what-is-that)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026](https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026)
- [https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome](https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome)
- [https://substack.thewebscraping.club/p/fingerprint-injection-playwright](https://substack.thewebscraping.club/p/fingerprint-injection-playwright)
- [https://substack.thewebscraping.club/p/scrapling-hands-on-guide](https://substack.thewebscraping.club/p/scrapling-hands-on-guide)
- [https://substack.thewebscraping.club/p/bypass-cloudflare-scraping-playwright](https://substack.thewebscraping.club/p/bypass-cloudflare-scraping-playwright)
- [https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot](https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-gologin-playwrigh](https://substack.thewebscraping.club/p/bypassing-cloudflare-gologin-playwrigh)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-with-nodriver](https://substack.thewebscraping.club/p/bypassing-cloudflare-with-nodriver)
- [https://substack.thewebscraping.club/p/cloudflare-web-unblocker-benchmark](https://substack.thewebscraping.club/p/cloudflare-web-unblocker-benchmark)
- [https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile](https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile)
