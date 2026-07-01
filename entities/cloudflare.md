---
name: Cloudflare
type: entity
category: anti-bot
first_seen: 2023-01-01
last_updated: '2026-06-29'
sources:
- cloudflare-how-to-scrape.md
- https://konstantinlebedev.com/bypassing-automated-traffic-detection/
- bypassing-cloudflare-in-2026.md
- cloudflare-turnstile-what-is-that.md
- fingerprint-injection-playwright.md
- undetected-chromedriver-cloudflare-datadome.md
- scrapling-hands-on-guide.md
- the-stealth-stack-web-scraping.md
- bypass-cloudflare-browser-check.md
- bypass-cloudflare-scraping-playwright.md
- bypassing-cloudflare-free-tools.md
- bypassing-cloudflare-gologin-playwrigh.md
- bypassing-cloudflare-with-kameleo.md
- bypassing-cloudflare-with-nodriver.md
- cloudflare-bypass-2026.md
- cloudflare-web-unblocker-benchmark.md
- scraping-cloudflare-websites-2023-q1-update.md
- scraping-cloudflare-websites-an-api.md
- the-lab-29-bypass-cloudflare-bot.md
- how-to-bypass-cloudflare-turnstile.md
- testing-bright-data-unblockler-cloudflare.md
- https://medium.com/@smitgharat0001/cloudflare-bypass-origin-server-deserves-some-love-too-e8bd2182cfea
- posts-rise-of-vibe-coded-anti-bot-systems.md
---

## What it is

Cloudflare is a CDN and network security provider whose bot management layer sits in front of a large portion of the web. Its anti-bot capabilities are layered and independently configurable per zone, which means two sites protected by Cloudflare can behave entirely differently toward scrapers.

## How it works

Cloudflare operates several detection mechanisms that can be active simultaneously or in isolation depending on how the site owner has configured their zone.

At the network level, Cloudflare inspects TLS handshake characteristics and HTTP/2 fingerprints. A mismatch between the declared user-agent and the actual TLS signature is enough to flag a request before any content is served. When a request is rejected at this layer, Cloudflare answers from its own edge: you get a Cloudflare error page with a Ray ID and a 403, not a response from the origin. That distinct error page is the diagnostic that the block happened before the request reached the application, which separates a TLS or edge rejection from an origin-level or application error (documented by Konstantin Lebedev, 2026).

The JS Detection (JSD) layer runs client-side JavaScript that collects browser environment signals and issues the `cf_clearance` cookie to sessions that pass. The `__cf_bm` cookie is issued separately by Bot Management and has a shorter lifespan.

The I'm Under Attack Mode (IUAM) challenge is an interstitial page that delays access while JavaScript runs. It was historically the main Cloudflare mechanism; it has become less common as Turnstile replaced it for many deployments.

Turnstile, announced in September 2022, is Cloudflare's "no CAPTCHA" CAPTCHA. It operates in three modes: managed (may show a challenge), non-interactive (silent, challenge-free), and invisible (fully embedded, no user interaction). It is free to deploy, which accelerated its adoption. Turnstile collects fingerprint data that feeds Cloudflare's AI training pipeline. The `cf_clearance` cookie issued after Turnstile can in some configurations persist for up to six months.

On top of these, Cloudflare's ML-based bot scoring assigns each session a score from 1 to 99. Scores above the operator-configured threshold trigger blocking or challenges. The threshold and the consequences of crossing it are zone-specific.

## TWSC experience

Configuration variance across sites is the most practically important thing about Cloudflare. We found this varies from near-irrelevant to aggressively blocking across sites we tested.

**Harrods.com** runs Cloudflare essentially as a CDN. The bot detection footprint is minimal. In early 2023, standard Playwright with Chrome worked locally but was blocked from AWS. By March 2024, fingerprint injection via Browserforge with WebGL renderer replacement was sufficient - no residential proxy needed. In our 2026 benchmark, Camoufox achieved 99% success rate on 100 direct URL requests with no CAPTCHA or rate limiting triggered. Even undetected-chromedriver reached 89% on the lenient config (failures were navigation timeouts, not blocks). The key finding: on harrods.com, WebGL vendor/renderer string is the critical fingerprint check. Replacing the datacenter SwiftShader value with a realistic consumer GPU string was sufficient to pass.

**Indeed.com** applies Turnstile plus rate limiting and is one of the harder Cloudflare configurations. A [homepage-first navigation](../concepts/homepage-first-navigation.md) strategy was critical from at least 2023 onward: hitting a job listing URL directly triggered blocks, while visiting the homepage first established session cookies that allowed subsequent navigations. The Turnstile challenge on the homepage itself can fail (returning 403) but still set valid session cookies. In our 2026 benchmark, Camoufox achieved 31% success on 100 URLs (rate limiting kicked in after URL 29, not bot detection). All Chrome-based tools achieved 0%: undetected-chromedriver returned 46 KB block pages, Pydoll returned 46 KB pages with incomplete rendering.

**Antonioli.eu** (early testing, 2023): Playwright with Chrome and persistent context worked locally but was blocked from AWS datacenter. Adding GoLogin (anti-detect browser) with a Mac fingerprint including proper WebGL vendor/renderer resolved the datacenter blocking. Later superseded by scrapy-impersonate as the preferred approach for this type of target.

**TLS-only approach (2023-2024):** Scrapy Impersonate (a scrapy wrapper for curl_cffi) bypassed Cloudflare on Harrods.com with 100% success rate on both local and datacenter environments when combined with residential proxies. This was surprising - it implies TLS fingerprint carries significant weight in Cloudflare's decision tree, and a correct TLS fingerprint with no browser fingerprint at all is sufficient on some configurations.

**Open-source tools tested against Indeed.com Turnstile (2025):** Botasaurus (with `bypass_cloudflare=True`) bypassed it. Patchright (drop-in Playwright replacement) bypassed it. Camoufox worked but inconsistently - some fingerprint profiles in its rotation are detected, requiring retries.

**Web unblocker benchmark vs Indeed.com (September 2024):** All major commercial unblockers bypassed Cloudflare on Indeed. The most notable result was Zyte API: fastest at 6.5 seconds per request average (vs 25-34 seconds for competitors) and cheapest at $0.063 for the full extraction. ZenRows had the best first-try accuracy (99%). Bright Data scored 79/100 (21% retry rate). Oxylabs 97% first-try. Smartproxy 96.8% first-try. Infatica had mixed results with incomplete renders on some pages.

[Camoufox](camoufox.md) (Firefox-based) consistently outperformed Chrome-based tools on strict Cloudflare configurations. The difference traces to Firefox's TLS stack and HTTP/2 fingerprint being less scrutinized than Chrome's at this layer.

### Origin Server IP Exposure via Split-DNS (2025-11)

A documented recon technique exploits organizations that use Cloudflare for the `www` subdomain but leave the apex domain (root domain, e.g., `example.com`) in DNS-only (grey cloud) mode for operational reasons (email routing, legacy infrastructure). When this happens, a DNS lookup on the apex returns the real origin IP rather than Cloudflare's proxy IPs.

The pattern observed across ~40,000 targets: large, older organizations frequently have `www.example.com` behind Cloudflare (orange cloud) while `example.com` resolves directly to the origin server. Confirming the exposure with curl:

```bash
# Forces example.com to resolve to the discovered IP, bypassing Cloudflare
curl -vk --resolve example.com:443:52.44.185.177 https://example.com/
```

If the response arrives without Cloudflare headers (`CF-Ray`, `cf-mitigated`), the origin is accessible directly. A working origin connection bypasses all Cloudflare WAF rules, rate limiting, bot detection, and Turnstile challenges entirely — Cloudflare never sees the traffic.

Mitigations: keep apex domain behind Cloudflare's proxy (orange cloud), or ensure the origin server accepts connections only from Cloudflare's published IP ranges.

This technique does not work when the operator consistently uses the orange cloud on all subdomains, or when the origin server validates the incoming IP against Cloudflare's ranges.

Source: medium.com/@smitgharat0001/cloudflare-bypass-origin-server-deserves-some-love-too-e8bd2182cfea (2025-11-04)

## Known limitations

Undetected ChromeDriver has been blocked on Cloudflare-protected datacenter IPs since 2023. The repository has been largely stagnant and has not kept pace with Cloudflare's detection updates.

The `cf_clearance` cookie is session-bound and not straightforwardly reusable across IPs or user-agents. Attempting to inject it into a mismatched session context reliably fails.

Turnstile's invisible mode makes it impossible to detect visually during testing, which complicates diagnosing whether a block originates from Turnstile or another detection layer.

Cloudflare's ML scoring threshold is opaque and zone-specific. A technique that clears one site's threshold will not necessarily clear another's.

Rate limiting is enforced independently of bot detection. Camoufox can pass Cloudflare's anti-bot layers on Indeed yet still hit rate limiting after ~30 requests in a session. This is not a bypass failure - it is the site's volume policy.

Camoufox's fingerprint rotation means some profiles from its database are detected by strict configurations. Multiple retries are sometimes necessary before landing on a clean profile.

## Related

- [Camoufox](camoufox.md)
- [Playwright](playwright.md)
- [Undetected-chromedriver](undetected-chromedriver.md)
- [Pydoll](pydoll.md)
- [TLS Fingerprinting](../concepts/tls-fingerprinting.md)
- [Homepage-first Navigation](../concepts/homepage-first-navigation.md)
- [Datadome](datadome.md)
- [PerimeterX](perimeterx.md)
- [Cloudflare Bypass Evolution](../timelines/cloudflare-bypass-evolution.md)

## Sources

- [https://substack.thewebscraping.club/p/cloudflare-how-to-scrape](https://substack.thewebscraping.club/p/cloudflare-how-to-scrape)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026](https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026)
- [https://substack.thewebscraping.club/p/cloudflare-turnstile-what-is-that](https://substack.thewebscraping.club/p/cloudflare-turnstile-what-is-that)
- [https://substack.thewebscraping.club/p/fingerprint-injection-playwright](https://substack.thewebscraping.club/p/fingerprint-injection-playwright)
- [https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome](https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome)
- [https://substack.thewebscraping.club/p/scrapling-hands-on-guide](https://substack.thewebscraping.club/p/scrapling-hands-on-guide)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/bypass-cloudflare-browser-check](https://substack.thewebscraping.club/p/bypass-cloudflare-browser-check)
- [https://substack.thewebscraping.club/p/bypass-cloudflare-scraping-playwright](https://substack.thewebscraping.club/p/bypass-cloudflare-scraping-playwright)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-free-tools](https://substack.thewebscraping.club/p/bypassing-cloudflare-free-tools)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-gologin-playwrigh](https://substack.thewebscraping.club/p/bypassing-cloudflare-gologin-playwrigh)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-with-kameleo](https://substack.thewebscraping.club/p/bypassing-cloudflare-with-kameleo)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-with-nodriver](https://substack.thewebscraping.club/p/bypassing-cloudflare-with-nodriver)
- [https://substack.thewebscraping.club/p/cloudflare-bypass-2026](https://substack.thewebscraping.club/p/cloudflare-bypass-2026)
- [https://substack.thewebscraping.club/p/cloudflare-web-unblocker-benchmark](https://substack.thewebscraping.club/p/cloudflare-web-unblocker-benchmark)
- [https://substack.thewebscraping.club/p/scraping-cloudflare-websites-2023-q1-update](https://substack.thewebscraping.club/p/scraping-cloudflare-websites-2023-q1-update)
- [https://substack.thewebscraping.club/p/scraping-cloudflare-websites-an-api](https://substack.thewebscraping.club/p/scraping-cloudflare-websites-an-api)
- [https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot](https://substack.thewebscraping.club/p/the-lab-29-bypass-cloudflare-bot)
- [https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile](https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile)
- [https://substack.thewebscraping.club/p/testing-bright-data-unblockler-cloudflare](https://substack.thewebscraping.club/p/testing-bright-data-unblockler-cloudflare)
- [https://medium.com/@smitgharat0001/cloudflare-bypass-origin-server-deserves-some-love-too-e8bd2182cfea](https://medium.com/@smitgharat0001/cloudflare-bypass-origin-server-deserves-some-love-too-e8bd2182cfea)
- [https://konstantinlebedev.com/bypassing-automated-traffic-detection/](https://konstantinlebedev.com/bypassing-automated-traffic-detection/)
