# TWSC Wiki Index

Last updated: 2026-04-22 (eighth ingest)

## Entities

### Anti-bot systems
- [Cloudflare](entities/cloudflare.md) - Multi-layer defense (TLS, JSD, Turnstile, ML scoring). Most tested anti-bot in TWSC corpus.
- [Akamai](entities/akamai.md) - TLS/JA3-heavy detection with behavioral JS sensor. Silent drop on mismatch. Nike.com catalog uses Akamai only; TLS impersonation sufficient.
- [DataDome](entities/datadome.md) - Behavioral analysis focus. Hermes.com is the canonical hard target. Chrome leaks automation signals that Firefox/Brave do not.
- [PerimeterX](entities/perimeterx.md) - Now HUMAN Security. More IP-focused than fingerprint-focused (as of 2023). Scrapy Impersonate documented as a working bypass (2024).
- [Kasada](entities/kasada.md) - Australian company. 429 signature. Hardware fingerprinting. Zero-trust first-request philosophy.
- [AWS WAF](entities/aws-waf.md) - Amazon WAF with JavaScript challenge. Cookie factory pattern works: browser gets aws-waf-token, Scrapy reuses it.
- [reCAPTCHA](entities/recaptcha.md) - Google CAPTCHA system (v1/v2/v3). v3 is invisible risk scoring. Camoufox bypasses it; open-source token extractors do not.
- [F5 Bot Defense](entities/f5-bot-defense.md) - Enterprise anti-bot from F5 Networks. AI/behavioral focus. Second largest by market share (2022).

### Tools and libraries
- [Camoufox](entities/camoufox.md) - Custom Firefox build. Best performer on strict Cloudflare/DataDome configs. Bypasses reCAPTCHA v3 (2025).
- [Playwright](entities/playwright.md) - Microsoft browser automation. Detectable by default, patchable via Patchright/Undetected Playwright.
- [Pydoll](entities/pydoll.md) - Async CDP Chrome automation. Stability issues in 2026 benchmarks.
- [Undetected-chromedriver](entities/undetected-chromedriver.md) - Patched Selenium. Stagnant repo, succeeded by Nodriver/Zendriver.
- [Nodriver](entities/nodriver.md) - Chrome automation without WebDriver layer. Passes CDP tests natively but cannot forge hardware fingerprint.
- [Scrapling](entities/scrapling.md) - Python library with three fetchers (static, dynamic, stealth). 1735x faster than BS4. Fetcher class (TLS only) achieves 100% on Nike/Akamai without browser overhead.
- [Scrapoxy](entities/scrapoxy.md) - Open-source proxy aggregator. Unifies providers and cloud VM egress. ~20% cost savings vs. pure cloud.
- [AnyCrawl](entities/anycrawl.md) - MIT-licensed LLM-ready scraping API. JSON extraction mode, MCP server. No anti-bot bypass. Comparable to FireCrawl.
- [curl_cffi](entities/curl-cffi.md) - Python HTTP client with TLS impersonation. Critical for hybrid scraping. Also covers scrapy-impersonate and hrequests.
- [Ghost Cursor](entities/ghost-cursor.md) - Bezier/Fitts's Law mouse movement for Playwright. OxyMouse is a newer alternative with Gaussian and Perlin noise options.
- [JA3Proxy](entities/ja3proxy.md) - Go-based TLS Client Hello rewriter via uTLS.
- [GoLogin](entities/gologin.md) - Anti-detect browser, Orbita engine. Top benchmark performer 223/260 in 2024.
- [Kameleo](entities/kameleo.md) - Anti-detect browser. Junglefox + Chroma. First to support Selenium + Playwright + Puppeteer simultaneously. €29-€279/mo.
- [Dolphin{anty}](entities/dolphin-anty.md) - Anti-detect browser for multi-account workflows. Scenarios builder, Profile Synchronizer, REST API. Free tier (10 profiles).
- [Botasaurus](entities/botasaurus.md) - Python scraping framework with decorator-based API. Works locally against Cloudflare/DataDome/Kasada. Fails from server (SwiftShader exposure).
- [Rayobrowse](entities/rayobrowse.md) - Rayobyte's stealth Chromium fork. Closed-source, Docker-based, CDP compatible. C++ patching. 100% benchmark score. Beta (2026).
- [ScrapeGraphAI](entities/scrapegraphai.md) - LLM-powered scraping library and commercial API. Non-deterministic, best for horizontal multi-site extraction.
- [Kadoa](entities/kadoa.md) - Commercial AI scraping workflow platform. UI-driven, anti-bot included, 5 proxy locations.

### Web Unblockers
- [Zyte API](entities/zyte-api.md) - 100/100 with browser rendering. Fails Kasada. Per-request dynamic pricing. Scrapy integration via scrapy-zyte-api.
- [Oxylabs Unblocker](entities/oxylabs-unblocker.md) - 96/100 overall. Cheapest on Kasada benchmark ($0.10/101 URLs). Best dashboard.
- [Smartproxy Unblocker](entities/smartproxy-unblocker.md) - 80/100 overall. $12/GB. Kasada improved from 0% (2023) to 92% (2024).

## Concepts

- [Browser Fingerprinting](concepts/browser-fingerprinting.md) - Canvas, WebGL, AudioContext, fonts, DOM signals. SwiftShader and zero-device red flags.
- [TLS Fingerprinting](concepts/tls-fingerprinting.md) - JA3 hash, HTTP/2 fingerprinting. Detection at TCP level before application data.
- [CDP Detection](concepts/cdp-detection.md) - Runtime.enable detection targeting automation protocol, not browser signals.
- [Homepage-first Navigation](concepts/homepage-first-navigation.md) - Visit homepage before deep pages. Required by Cloudflare, PerimeterX, DataDome.
- [Hybrid Scraping](concepts/hybrid-scraping.md) - Browser for auth, HTTP client for data. 27x speed gain. TLS consistency critical.
- [Cookie and Session Reuse](concepts/cookie-session-reuse.md) - Cookie factory pattern. Anti-bot cookie lifetimes. Per-site behavioral variance.
- [Proxy Fundamentals](concepts/proxy-fundamentals.md) - Four proxy types, CGNAT, IP reputation, Proxy Ladder, ban management, pricing (Sept 2024), Tor, XFF header.
- [Mobile Proxy Farming](concepts/mobile-proxy-farming.md) - DIY hardware farms (USB modems, 3proxy). Airproxy at 2000+ SIMs. Cost economics vs. commercial.
- [Web Unblockers](concepts/web-unblockers.md) - Managed bypass APIs. Benchmark results across Cloudflare/DataDome/Kasada/PX targets (2023-2024).
- [Scraping Infrastructure](concepts/scraping-infrastructure.md) - Compute options (Lambda, containers, VMs, bare metal), scheduling (Airflow, GitHub Actions, Scrapyd, Scrapeops), monitoring.
- [LLM Scraping](concepts/llm-scraping.md) - Schema extraction, vision extraction, code generation, self-healing. AI browsers (ChatGPT Atlas, Stagehand, Cursor). AnyCrawl.
- [AI Scraping Assistants](concepts/ai-scraping-assistants.md) - Cursor + MCP + Claude workflow for scraper development acceleration.
- [Web Scraping Legal Landscape](concepts/web-scraping-legal-landscape.md) - CFAA, DMCA 1201, ToS, key cases (hiQ, Meta/Bright Data, X/Bright Data, Google/SerpApi).
- [Scraping Economics](concepts/scraping-economics.md) - Cost structure, business models, data commodity thesis, scaling constraints.
- [Anti-Detect Browsers](concepts/anti-detect-browsers.md) - GoLogin, Kameleo, Orbita. Real-device fingerprint databases. 2024 benchmark: GoLogin 223/260, Incogniton 139/260. Commercial alternative to open-source tools.
- [Mouse Movement Emulation](concepts/mouse-movement-emulation.md) - Bezier (ghost-cursor), Gaussian, Perlin noise (OxyMouse). DataDome checks mouse events; Cloudflare does not.
- [WebDriver vs CDP vs WebDriver BiDi](concepts/webdriver-vs-cdp-vs-bidi.md) - Three browser control protocols. CDP dominant for Chromium; BiDi the W3C cross-browser future; Firefox dropping CDP in Nightly 141.
- [WebSocket Bot Detection](concepts/websocket-bot-detection.md) - Stateful WS connection exploited for continuous fingerprinting and behavioral analysis.
- [ML-Based Bot Detection](concepts/ml-bot-detection.md) - Machine learning models trained on behavioral features. Present in all major anti-bot systems.
- [API Scraping](concepts/api-scraping.md) - Internal API identification, authentication patterns (Bearer, JWT, Castle), Algolia, TLS requirement. LinkedIn Wayback Machine technique. Geo-targeted APIs via headers.
- [Mobile App Scraping](concepts/mobile-app-scraping.md) - HTTP Toolkit interception, certificate pinning bypass, Frida setup, replicating app API calls.
- [Certificate Pinning](concepts/certificate-pinning.md) - SSL pinning bypass on Android with Frida. RootAVD, frida-server, OkHttp hook.
- [HTTP Performance](concepts/http-performance.md) - Async requests, ETags/HTTP caching, HTTP/3, connection pooling, exponential backoff. HTTP/1.1 pooled beats HTTP/2 by 6.7x under concurrency. Server co-location 6x impact.
- [WebSocket Scraping](concepts/websocket-scraping.md) - Real-time data via persistent connections. JSON and NATS protocols. Bitstamp and Polymarket.
- [Location Data Scraping](concepts/location-data-scraping.md) - World grid approach, radius vs bounding-box APIs, browser geolocation injection.
- [Inventory Tracking](concepts/inventory-tracking.md) - Stock level extraction. Revenue estimation. Data in list page, PDP, click-and-collect, or cart APIs.

### New entity pages (batches 3–7)
- [hRequests](entities/hrequests.md) - TLS-fingerprinted HTTP with embedded headless browser. Akamai/Cloudflare/PX pass; DataDome/Kasada fail.
- [Algolia](entities/algolia.md) - Client-side search API. `x-algolia-application-id`, `x-algolia-api-key`, `x-algolia-agent`. EndClothing full catalog with no anti-bot. Michelin Guide pagination.

## Comparisons

- [Firefox vs Chrome Stealth](comparisons/firefox-vs-chrome-stealth.md) - Camoufox vs Pydoll/UC/Patchright across anti-bot targets.
- [Anti-Detect Browser Benchmark 2024](comparisons/anti-detect-browser-benchmark-2024.md) - 8 commercial anti-detect browsers scored on CreepJS/BrowserScan. GoLogin leads at 223/260; Incogniton lowest at 139/260.

## Timelines

- [Cloudflare Bypass Evolution](timelines/cloudflare-bypass-evolution.md) - From Firefox+stealth (2022) to Camoufox dominance (2026).
