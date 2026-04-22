---
name: PerimeterX (HUMAN Bot Defender)
type: entity
category: anti-bot
first_seen: 2022-11-24
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with
  - https://substack.thewebscraping.club/p/the-lab-56-bypassing-perimeterx-3
  - https://substack.thewebscraping.club/p/fingerprint-injection-playwright
  - https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome
  - https://substack.thewebscraping.club/p/bypassing-perimeterx-2023
  - https://substack.thewebscraping.club/p/bypassing-perimeterx-scrapy
  - https://substack.thewebscraping.club/p/scraping-perimeterx-websites
  - https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix
  - https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges
---

## What it is

PerimeterX rebranded to HUMAN Security and its product is now called HUMAN Bot Defender. The rebrand reflects the acquisition into HUMAN Security's broader platform. The underlying technology and cookie naming conventions (still using `_px3` and `_pxhd`) remained in use as of TWSC's testing period.

## How it works

HUMAN Bot Defender is structured as three components. The HUMAN Sensor is a JavaScript payload deployed on the protected site that collects browser and behavioral signals. The HUMAN Detector is a cloud ML service that evaluates sensor data and assigns a verdict. The HUMAN Enforcer acts at the CDN layer to enforce that verdict by allowing, challenging, or blocking the request.

The system scores every page load in real time, considering behavior, path, fingerprints, and ML model output. If the score falls below threshold, the challenge triggers.

The primary challenge mechanism is a press-and-hold button interaction (the "Human Challenge"). For high-value pages (product drops, limited inventory), a more aggressive variant called the Hype Sale challenge is used. Both require simulated interaction to pass without a real user. The press-and-hold design is reported to be 5x faster for humans to solve than reCAPTCHA and produces 10-15x lower abandonment rates.

Detection cookies include `_px3` (PerimeterX v3) and `_pxhd`. Related infrastructure uses a set of known domains: perimeterx.net, px-cdn.net, px-cloud.net, pxchk.net, and px-client.net. Blocking these domains in a scraping environment breaks the sensor and typically results in a hard block.

As of TWSC's 2022-2023 testing, HUMAN Bot Defender was more IP-focused than fingerprint-focused compared to systems like [Datadome](datadome.md). Residential proxies alone were sufficient to pass detection on several targets without fingerprint manipulation. This characterization may shift over time with product updates.

Some PerimeterX-protected sites leave their internal APIs unprotected, even when HTML pages are protected. Booking.com was identified as one such target: the HTML was nominally protected but the product APIs returned data without challenge. This is likely intentional to allow API partners and partner integrations.

## How to identify it

Wappalyzer detects PerimeterX in the security section for supported sites. Without Wappalyzer, inspect cookies for `_pxhd` or `_px3` on the first page load. The press-and-hold challenge button is a distinctive visual indicator when it appears.

## TWSC experience

**neimanmarcus.com (2022)**: API-first approach. Browsing the women's clothing category revealed a JSON product API (`/c/dt/api/productlisting?categoryId=...`). A plain Scrapy spider with proper request headers accessed this API successfully, though with intermittent 424 errors after extended crawling. Playwright with random mouse movement and scroll simulation reduced the 424 frequency. A homepage-first visit was required. Covered in [scraping-perimeterx-websites](https://substack.thewebscraping.club/p/scraping-perimeterx-websites).

**neimanmarcus.com, crunchbase.com, stockx.com (2023)**: Undetected Chromedriver with Brave Browser worked on NeimanMarcus both locally and on a datacenter with residential proxies. Playwright with Firefox worked without proxies from local, required proxies from a datacenter. Playwright with Chrome required `ignore_default_args=["--enable-automation"]` and `--disable-blink-features=AutomationControlled` flags plus slow_mo to pass. Crunchbase required no proxy even from AWS. Session reset requires a full new browser profile directory, not just cookie clearing. Covered in [bypassing-perimeterx-2023](https://substack.thewebscraping.club/p/bypassing-perimeterx-2023).

**booking.com and neimanmarcus.com (2024)**: Scrapy Impersonate (`scrapy-impersonate` package, `meta={'impersonate': 'chrome110'}`) bypassed PerimeterX on both targets without a browser. Booking.com HTML is accessible with a good header set in standard Scrapy. NeimanMarcus.com works with Scrapy Impersonate. This is the first documented case of bypassing PerimeterX without headful browser automation. Covered in [bypassing-perimeterx-scrapy](https://substack.thewebscraping.club/p/bypassing-perimeterx-scrapy).

A homepage-first strategy was required across all tested targets. Direct navigation to protected interior pages triggered blocks; entering through the homepage and navigating normally did not.

Session resets require a new browser context folder, not just cookie clearing. Clearing cookies within an existing context left enough residual signals for the sensor to correlate the new session with the blocked one. Covered in [the-lab-35-bypassing-perimeterx-with](https://substack.thewebscraping.club/p/the-lab-35-bypassing-perimeterx-with) and [the-lab-56-bypassing-perimeterx-3](https://substack.thewebscraping.club/p/the-lab-56-bypassing-perimeterx-3).

Crunchbase.com was the most lenient configuration we encountered. Even Brave browser's partial noise reduction was sufficient there, and no proxy was required when running from AWS infrastructure. This illustrates how much variance exists in how operators configure the product.

Fingerprint injection (Browserforge) was explored in [fingerprint-injection-playwright](https://substack.thewebscraping.club/p/fingerprint-injection-playwright) in the context of PerimeterX alongside other systems.

## Known limitations

The press-and-hold challenge requires realistic interaction simulation. A programmatic mouse-down/mouse-up sequence without appropriate timing and trajectory is typically caught.

Session correlation survives cookie clearing if the browser profile directory is reused. This is a common mistake when resetting sessions: wiping cookies is insufficient if other persistent state (local storage, IndexedDB, cache) remains.

As detection has evolved since 2023, the IP-focused characterization may no longer hold uniformly. The balance between IP reputation and fingerprint analysis in the ML model is not publicly documented and shifts with product updates.

Site-level variance is high. Crunchbase, Booking, and NeimanMarcus all behave differently under the same anti-bot vendor. Configuration by the site operator matters as much as the underlying detection capabilities.

## Related

- [Camoufox](camoufox.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)
- [Kasada](kasada.md)
- [Homepage-first Navigation](../concepts/homepage-first-navigation.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
