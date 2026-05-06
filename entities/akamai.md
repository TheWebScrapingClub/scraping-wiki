---
name: Akamai Bot Manager
type: entity
category: anti-bot
first_seen: 2023-01-01
last_updated: 2026-04-22
sources:
  - bypass-akamai-bot-protection.md
  - the-lab-30-how-to-bypass-akamai-protected.md
  - hybrid-scraping-camoufox-curl-cffi.md
  - bypassing-akamai-for-free.md
  - bypassing-akamai-proxidize.md
  - scraping-akamai-protected-website.md
  - scraping-akamai-protected-websites.md
  - hrequests-bypass-akamai-with-python.md
  - nike-scraping-benchmark.md
  - https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering
---

## What it is

Akamai Bot Manager is the anti-bot product within Akamai's edge platform. It combines network-level fingerprinting with a behavioral JavaScript sensor and cloud-based ML classification. It is deployed by a number of luxury and high-value e-commerce sites, which is where TWSC has encountered it most consistently. Known deployments include Zalando, Gucci, Versace, Loewe, H&M, Net-a-Porter, LuisaViaRoma, Rakuten, and NewBalance.

## How it works

Detection starts at the TLS layer. Akamai inspects JA3 fingerprints and HTTP/2 characteristics. A mismatch between the declared client and the actual TLS signature causes a silent drop: no 403, no redirect, just a timeout. This makes diagnosis harder than with systems that return explicit error codes.

The behavioral sensor is a JavaScript payload that collects interaction signals and populates session cookies. The primary cookies are `_abck` and `ak_bmsc`, with `bm_sz` and `bm_s` also present depending on configuration. Some of these cookies have observed expiries of up to six months, which makes manual extraction and reuse a viable tactic. The `bm_sz` cookie specifically can be found documented in Net-a-Porter's cookie policy.

Akamai scores sessions from 0 (human) to 100 (bot) based on more than 30 billion bots analyzed per day. The score rises as more requests come from the same bot. Operators configure three response zones: Cautious (watch), Strict (challenge), and Aggressive (mitigate), each with configurable thresholds.

A notable deception in Akamai's architecture: a 401 Unauthorized response can appear before bot detection has even evaluated credentials. The 401 is triggered by the bot classification, not by a failed login attempt. Testing authentication flows without accounting for this leads to false conclusions about what is actually failing.

IP reputation is evaluated alongside fingerprinting and behavioral signals. Datacenter IPs face a substantially higher bar than residential ones. AWS IPs are blocked faster than Azure or GCP, likely because cloud providers publish their IP ranges making classification trivial.

Detection can be identified by looking for the `_abck` and `bm_sz` cookies after loading a page, or via Wappalyzer which lists "Akamai Bot Manager" under Security.

## TWSC experience

**TLS fingerprint as the primary lever.** For public data scraping (no login required), TLS fingerprinting is consistently the most important signal. Using scrapy-impersonate (which wraps curl_cffi and sends browser-accurate TLS fingerprints) bypasses Akamai in roughly 90% of cases across tested targets. Confirmed to work on Gucci.com (2025). The clearance cookie established with the first successful request persists for days, meaning subsequent requests in the same session can use standard Scrapy without scrapy-impersonate for every request.

**Zalando (2023).** Basic Scrapy with modified headers worked for public product data with no browser automation required. The website's product listing pages embed JSON data inside the HTML (`<script type="application/json" class="re-data-el-hydrate">`), so no rendering was needed. IP rotation via residential proxies was sufficient for scale.

**Versace, Loewe, Zalando, NewBalance, Rakuten (2024).** Updated User-Agent string (Chrome 125) plus a coherent set of modern sec-ch-ua headers was sufficient to bypass Akamai on all five targets when running from a local machine. From AWS, the first request was blocked immediately due to IP classification. Moving to Azure IPs worked without any proxy, as Azure and GCP are less aggressively blocked than AWS. The key learning: an outdated User-Agent string (e.g., Chrome 54) was enough for Akamai to flag a request even before fingerprinting.

**H&M (2023).** Product detail pages required mobile proxy rotation (Proxidize hardware setup with 4G modems). Akamai temporarily bans IPs after a few requests, so frequent rotation was necessary. With four mobile modems, 100k+ requests across 20k+ products was achievable.

**LuisaViaRoma.** JA3Proxy (written in Go) impersonated a legitimate TLS fingerprint, chained with a residential proxy over SOCKS5. This combination addressed both the network fingerprint check and the IP reputation component.

**Net-a-Porter.** A hybrid approach worked: [Camoufox](camoufox.md) handled authentication, then a lightweight HTTP client (curl_cffi) was used for the data collection phase. Cookie injection was viable; manually extracted `_abck` and `ak_bmsc` cookies remained usable for multiple days.

**hrequests (2023).** This Python library sends browser-accurate TLS fingerprints (via a Go-based backend using tls-client by bogdanfinn) and HTTP/2, bypassing Akamai on tested targets. The Akamai hash in the TLS fingerprint output (`akamai_hash`, `akamai_text`) is a specific HTTP/2 fingerprint used by Akamai for classification, distinct from JA3.

**Nike.com (2026).** Nike.com deploys Akamai Bot Manager on the public catalog (product pages, search results). Kasada protects the authenticated flows (login, checkout). For public catalog scraping, Akamai is the only system to bypass. Nike product pages are server-side rendered — the full HTML including product data is in the first response. TLS fingerprinting via curl_cffi (undetected-httpx, Scrapling Fetcher, Rnet) was sufficient to bypass Akamai at 100% success across 1,000 URLs. No JavaScript challenges were observed on product pages. This is a deliberate Nike choice: they deploy challenges on authenticated flows but not on catalog pages, accepting some scraping of public data. With TLS fingerprinting handled by an HTTP client, scrape speed is approximately 0.5 seconds per request vs. 8-13 seconds for a browser. No full browser automation is required for public catalog data.

### Mouse Movement (MACT) Detection Mechanics

Akamai's internal name for mouse movement data is MACT. A leaked MACT generator circulated in the bypass community around 2019-2020 and remained effective for approximately two years before Akamai patched detection. A reverse-engineering analysis (mimic.sbs, 2024) explains why it took so long and what eventually fingerprinted it.

The generator produced piecewise-constant velocity trajectories, then applied an EWMA smoothing function (λ=0.955). The smoothing accidentally mimicked human-like velocity curves. Akamai's eventual detection came via velocity profile analysis: after inverting the EWMA to reconstruct the original signal, the step-function structure becomes apparent — constant velocity within each segment, with instantaneous transitions. Real human movement has continuously varying, not piecewise-constant, velocity.

The defender detection strategies: (1) reconstruct the underlying velocity signal via EWMA inversion and test for segment-constancy; (2) use a gradient-boosted decision tree on velocity features. The post's main lesson for anti-bot teams: a dedicated Threat Intelligence team studying bypass techniques enables significantly faster detection, reducing the window from years to weeks.

## Known limitations

In October 2023, Akamai pushed an update that broke scraping setups simultaneously across multiple operators, including TWSC's LuisaViaRoma setup. The update affected behavioral sensor logic and invalidated cookie-based approaches that had been working. This kind of coordinated, unannounced update is an inherent risk with Akamai deployments.

TLS mismatch produces a silent timeout rather than an explicit error. There is no feedback mechanism to confirm whether a block is from TLS fingerprinting, IP reputation, or the behavioral sensor. Isolating which layer is responsible requires controlled experiments varying one factor at a time.

For scraping that requires login or checkout flow automation, the behavioral sensor is significantly more active. Cookie-based approaches that work for public data may fail entirely for authenticated flows. The anti-bot appears to apply more aggressive rules when real money or account access is involved.

The behavioral JS sensor evolves. Cookie values generated by the sensor encode interaction signals; a cookie captured from a static or minimal session may fail on pages that expect richer behavioral data.

scrapy-impersonate has a known issue when combined with proxies: network errors are sometimes not handled gracefully, causing the spider to stop rather than retry.

## Related

- [Camoufox](camoufox.md)
- [curl-cffi](curl-cffi.md)
- [TLS Fingerprinting](../concepts/tls-fingerprinting.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)
- [Cookie and Session Reuse](../concepts/cookie-session-reuse.md)
- [Hybrid Scraping](../concepts/hybrid-scraping.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-akamai-bot-protection](https://substack.thewebscraping.club/p/bypass-akamai-bot-protection)
- [https://substack.thewebscraping.club/p/the-lab-30-how-to-bypass-akamai-protected](https://substack.thewebscraping.club/p/the-lab-30-how-to-bypass-akamai-protected)
- [https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi](https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi)
- [https://substack.thewebscraping.club/p/bypassing-akamai-for-free](https://substack.thewebscraping.club/p/bypassing-akamai-for-free)
- [https://substack.thewebscraping.club/p/bypassing-akamai-proxidize](https://substack.thewebscraping.club/p/bypassing-akamai-proxidize)
- [https://substack.thewebscraping.club/p/scraping-akamai-protected-website](https://substack.thewebscraping.club/p/scraping-akamai-protected-website)
- [https://substack.thewebscraping.club/p/scraping-akamai-protected-websites](https://substack.thewebscraping.club/p/scraping-akamai-protected-websites)
- [https://substack.thewebscraping.club/p/hrequests-bypass-akamai-with-python](https://substack.thewebscraping.club/p/hrequests-bypass-akamai-with-python)
- [https://substack.thewebscraping.club/p/nike-scraping-benchmark](https://substack.thewebscraping.club/p/nike-scraping-benchmark)
- [https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering/](https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering/)
