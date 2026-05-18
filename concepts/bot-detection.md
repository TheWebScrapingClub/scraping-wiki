---
name: Bot Detection
type: concept
first_seen: 2024-01-01
last_updated: '2026-05-18'
sources:
- dbi-everything-about-user-agent.md
- dbi-facebookexternalhit.md
- dbi-go-http-client.md
- dbi-linkedin-bot.md
- 2026-01-29-fossil-captcha-solver.md
- blog-best-proxy-for-twitter-2026.md
- insights-rotational-bot-identity-detection.md
---

# Bot Detection

## Definition

Bot detection is the umbrella discipline of identifying automated traffic on a website and distinguishing it from legitimate human visitors. It sits opposite to web scraping: the same fingerprints, behaviors, and protocol-level traces that scrapers try to hide are what detection systems look for. Reading the detection literature is the most direct way for a scraper engineer to understand which signals actually leak.

## How It Works

Bot detection operates at multiple layers, often in combination:

**Network layer.** TLS handshake signatures (JA3, JA4), TCP/IP stack fingerprints, IP reputation against datacenter and known proxy ranges. Reveals automated clients before any HTTP traffic is sent.

**Protocol layer.** HTTP/2 and HTTP/3 frame ordering, header order and casing, missing or out-of-order Client Hints (`sec-ch-ua`, `sec-ch-ua-platform`, `sec-ch-ua-form-factors`). Curl, Python requests, and Go's net/http produce distinguishable patterns from real Chrome.

**Browser layer.** Headless markers (`navigator.webdriver`, missing `window.chrome`, plugins/permissions defaults), CDP channel detection (`Runtime.enable` side effects), automation extension presence, missing browser features that real Chrome ships with.

**Fingerprint layer.** Canvas rendering, WebGL parameters, audio context, font enumeration, screen and timezone consistency, GPU info from WebGPU. Anti-bot vendors maintain large databases of "human" fingerprint distributions and flag outliers.

**Behavioral layer.** Mouse movement profile, scroll patterns, click cadence, time-on-page distributions, navigation graph. Hard to fake convincingly without dedicated emulation libraries.

[ML-Based Bot Detection](ml-bot-detection.md) covers the model-driven side that combines all these layers into a risk score.

## Where It Matters

Every commercial anti-bot vendor TWSC tracks ([Cloudflare](../entities/cloudflare.md), [DataDome](../entities/datadome.md), [Akamai](../entities/akamai.md), [Kasada](../entities/kasada.md), [PerimeterX](../entities/perimeterx.md), [F5](../entities/f5-bot-defense.md), [AWS WAF](../entities/aws-waf.md)) implements some combination of these layers. The product differences are mostly about which layers they emphasize and how aggressive their scoring is.

Researchers like Antoine Vastel (DataDome) and the team behind Castle.io publish detection-side techniques openly. These articles are foundational reading for anyone building scrapers, because each technique they describe corresponds to a signal that needs to be neutralized on the scraper side.

## What We Tested

TWSC articles routinely benchmark anti-bot products to see which scraping configurations they catch and which they pass. Findings flow into individual entity pages ([DataDome](../entities/datadome.md), [Cloudflare](../entities/cloudflare.md), etc.) and concept pages on specific signals ([CDP Detection](cdp-detection.md), [Browser Fingerprinting](browser-fingerprinting.md), [TLS Fingerprinting](tls-fingerprinting.md), [Mouse Movement Emulation](mouse-movement-emulation.md)).

## Current State

Bot detection has moved from rule-based filtering (User-Agent blocklists, IP reputation) to integrated multi-layer ML scoring across the last decade. The dominant pattern in 2026 is per-request risk score that combines passive signals (TLS, HTTP) with active challenges (Turnstile, Captcha, JS sensors) when risk is elevated. Stealth scrapers that pass at one anti-bot may fail at another because the layered weights differ.

## Related

- [ml-bot-detection](ml-bot-detection.md)
- [browser-fingerprinting](browser-fingerprinting.md)
- [cdp-detection](cdp-detection.md)
- [tls-fingerprinting](tls-fingerprinting.md)
- [websocket-bot-detection](websocket-bot-detection.md)
- [anti-detect-browsers](anti-detect-browsers.md)
- [DataDome](../entities/datadome.md)
- [Cloudflare](../entities/cloudflare.md)
