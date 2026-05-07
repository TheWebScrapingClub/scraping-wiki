# TWSC Wiki Index

Last updated: 2026-05-07

## Visual maps and views

- `canvases/`: JSON Canvas (`.canvas`) visual maps of landscapes and ecosystems
  - `agentic-browsers-landscape-2026.canvas` — full agentic-browser landscape from the May 2026 DataDome lab article
- `views/`: Obsidian Bases (`.base`) live queries over wiki content
  - `all-entities.base` — every entity, grouped by category
  - `anti-bot-vendors.base` — anti-bot category only
  - `recently-touched.base` — wiki pages updated in the last 90 days
  - `tools-and-browsers.base` — tools, browsers, and libraries

## Entities

### Anti-bot systems
- [Akamai](entities/akamai.md) - TLS/JA3-heavy detection with behavioral JS sensor. Silent drop on mismatch. Nike.com catalog uses Akamai only; TLS impersonation sufficient.
- [AWS WAF](entities/aws-waf.md) - Amazon WAF with JavaScript challenge. Cookie factory pattern works: browser gets aws-waf-token, Scrapy reuses it.
- [Cloudflare](entities/cloudflare.md) - Multi-layer defense (TLS, JSD, Turnstile, ML scoring). Most tested anti-bot in TWSC corpus.
- [DataDome](entities/datadome.md) - Behavioral analysis focus. Hermes.com is the canonical hard target. Chrome leaks automation signals that Firefox/Brave do not.
- [F5 Bot Defense](entities/f5-bot-defense.md) - Enterprise anti-bot from F5 Networks. AI/behavioral focus. Second largest by market share (2022).
- [Kasada](entities/kasada.md) - Australian company. 429 signature. Hardware fingerprinting. Zero-trust first-request philosophy.
- [PerimeterX](entities/perimeterx.md) - Now HUMAN Security. More IP-focused than fingerprint-focused (as of 2023). Scrapy Impersonate documented as a working bypass (2024).
- [reCAPTCHA](entities/recaptcha.md) - Google CAPTCHA system (v1/v2/v3). v3 is invisible risk scoring. Camoufox bypasses it; open-source token extractors do not.

### Tools and libraries
- [Algolia](entities/algolia.md) - Client-side search API. EndClothing full catalog with no anti-bot despite Akamai on site.
- [AnyCrawl](entities/anycrawl.md) - MIT-licensed LLM-ready scraping API. JSON extraction mode, MCP server. No anti-bot bypass. Comparable to FireCrawl.
- [Botasaurus](entities/botasaurus.md) - Python scraping framework with decorator-based API. Works locally against Cloudflare/DataDome/Kasada. Fails from server (SwiftShader exposure).
- [Camoufox](entities/camoufox.md) - Custom Firefox build. Best performer on strict Cloudflare/DataDome configs. Bypasses reCAPTCHA v3 (2025).
- [curl_cffi](entities/curl-cffi.md) - Python HTTP client with TLS impersonation. Critical for hybrid scraping. Also covers scrapy-impersonate and hrequests.
- [Dolphin{anty}](entities/dolphin-anty.md) - Anti-detect browser for multi-account workflows. Scenarios builder, Profile Synchronizer, REST API. Free tier (10 profiles).
- [Ghost Cursor](entities/ghost-cursor.md) - Bezier/Fitts's Law mouse movement for Playwright. OxyMouse is a newer alternative with Gaussian and Perlin noise options.
- [GoLogin](entities/gologin.md) - Anti-detect browser, Orbita engine. Top benchmark performer 223/260 in 2024.
- [hRequests](entities/hrequests.md) - TLS-fingerprinted HTTP with embedded headless browser. Akamai/Cloudflare/PX pass; DataDome/Kasada fail.
- [JA3Proxy](entities/ja3proxy.md) - Go-based TLS Client Hello rewriter via uTLS.
- [Kadoa](entities/kadoa.md) - Commercial AI scraping workflow platform. UI-driven, anti-bot included, 5 proxy locations.
- [Kameleo](entities/kameleo.md) - Anti-detect browser. Junglefox + Chroma. First to support Selenium + Playwright + Puppeteer simultaneously.
- [Nodriver](entities/nodriver.md) - Chrome automation without WebDriver layer. Passes CDP tests natively but cannot forge hardware fingerprint.
- [Playwright](entities/playwright.md) - Microsoft browser automation. Detectable by default, patchable via Patchright/Undetected Playwright.
- [Pydoll](entities/pydoll.md) - Async CDP Chrome automation. Stability issues in 2026 benchmarks.
- [Rayobrowse](entities/rayobrowse.md) - Rayobyte's stealth Chromium fork. Closed-source, Docker-based, CDP compatible. C++ patching. 100% benchmark score. Beta (2026).
- [ScrapeGraphAI](entities/scrapegraphai.md) - LLM-powered scraping library and commercial API. Non-deterministic, best for horizontal multi-site extraction.
- [Scrapling](entities/scrapling.md) - Python library with three fetchers (static, dynamic, stealth). 1735x faster than BS4. Fetcher class achieves 100% on Nike/Akamai without browser overhead.
- [Scrapoxy](entities/scrapoxy.md) - Open-source proxy aggregator. Unifies providers and cloud VM egress. ~20% cost savings vs. pure cloud.
- [Undetected-chromedriver](entities/undetected-chromedriver.md) - Patched Selenium. Stagnant repo, succeeded by Nodriver/Zendriver.

### Web Unblockers
- [Oxylabs Unblocker](entities/oxylabs-unblocker.md) - 96/100 overall. Cheapest on Kasada benchmark ($0.10/101 URLs). Best dashboard.
- [Smartproxy Unblocker](entities/smartproxy-unblocker.md) - 80/100 overall. $12/GB. Kasada improved from 0% (2023) to 92% (2024).
- [Zyte API](entities/zyte-api.md) - 100/100 with browser rendering. Fails Kasada. Per-request dynamic pricing. Scrapy integration via scrapy-zyte-api.


### Added 2026-05-06
- [FingerprinterJS](entities/fingerprinterjs.md) — FingerprinterJS v2.0 is a browser fingerprinting and bot detection tool.
- [iherb-cli](entities/iherb-cli.md) — A Rust command-line tool for querying product data from iHerb using a headless browser.
- [FPScanner](entities/fpscanner.md) — A lightweight browser fingerprinting library for bot detection.
- [chaser-oxide](entities/chaser-oxide.md) — A Rust-based fork of `chromiumoxide` for hardened, undetectable browser automation.
- [proxelar](entities/proxelar.md) — A Rust-based MITM proxy for intercepting and modifying HTTP/HTTPS traffic.
- [Obscura](entities/obscura.md) — A headless browser engine written in Rust for web scraping and AI agent automation.
- [MasterHttpRelayVPN](entities/masterhttprelayvpn.md) — A domain-fronted HTTP/SOCKS5 proxy tool that tunnels traffic through Google Apps Script for scraping
- [TransparentTorProxy](entities/transparenttorproxy.md) — A Linux CLI utility that transparently routes all system traffic through the Tor network using nftab
- [wxpath](entities/wxpath.md) — wxpath is a Python library for declarative web crawling using XPath.
- [Libretto](entities/libretto.md) — A toolkit for building robust web integrations and maintaining browser automations.
- [GoScrapy](entities/goscrapy.md) — A high-performance web scraping framework for Go, designed with the familiar architecture of Python'
- [Feedstock](entities/feedstock.md) — A high-performance web crawler and scraper for TypeScript, powered by Bun and Playwright.
- [Crawl4AI](entities/crawl4ai.md) — An open-source web crawler and scraper for LLM-friendly Markdown output.
- [Reader](entities/reader.md) — An open-source, production-grade web scraping engine built for LLMs.
- [Proxy Server](entities/proxy-server.md) — A service that brokers connections between the browser and phone.
- [Kimurai](entities/kimurai.md) — A Ruby-based web scraping framework that uses AI to assist in data extraction.


### Added 2026-05-07
- [is-antibot](entities/is-antibot.md) — A library that detects antibot and CAPTCHA challenges from 30+ providers using signals.
- [BlankTrace](entities/blanktrace.md) — A cross-platform Rust CLI proxy that anonymizes browser traffic by randomizing digital fingerprints 
- [IPIDEA](entities/ipidea.md) — A residential proxy network that enrolled 9 million Android devices into a botnet.
- [ClashMac](entities/clashmac.md) — A macOS native proxy tool with real-time traffic monitoring, topology visualization, and multi-hop t
- [Ricci Flow – AI Web Scraper](entities/ricci-flow-ai-web-scraper.md) — A Chrome extension for AI-powered web scraping that extracts data from websites and exports it to Ex
- [Wick](entities/wick.md) — Wick is an open-source tool that allows AI agents to access web pages as if they were real browsers.
- [Kampala](entities/kampala.md) — Kampala is a tool for intercepting and automating web traffic.
- [Konform Browser](entities/konform-browser.md) — Konform Browser is a stealth browser based on Firefox ESR for web scraping and automation.
- [Lightpanda](entities/lightpanda.md) — Lightpanda is a browser built for AI and automation, offering faster execution and lower memory usag
- [LucidExtractor](entities/lucidextractor.md) — An enterprise web scraping and SEO analysis platform.
- [MeshScrape](entities/meshscrape.md) — A service that offers a distributed IP network for web scraping to avoid blocks and rate limits.
- [Owl Browser](entities/owl-browser.md) — A self-hosted browser automation engine for automation at scale with 256 parallel contexts and undet
- [NyxProxy](entities/nyxproxy.md) — A tool for building a self-hosted, rotating proxy gateway using IPv6 /64 subnets.
- [Browser Use](entities/browser-use.md) — Browser Use is a cloud-based browser automation platform that aims to create undetectable browsers.
- [ScrapingDuck](entities/scrapingduck.md) — A scraping API that handles IP rotation, JavaScript rendering, and provides a free tier for web scra
- [ScrapingSandbox](entities/scrapingsandbox.md) — A web scraping sandbox for learning and testing web scraping techniques.
- [SpiderSuite](entities/spidersuite.md) — A powerful web crawler and security testing tool for penetration testers and security researchers.
- [Spidra](entities/spidra.md) — A web scraping platform that uses AI to extract data from websites.
- [Tadpole](entities/tadpole.md) — A language for writing declarative, modular scraping code.
- [obscrd](entities/obscrd.md) — An open-source content protection system for React that scrambles HTML and blocks AI crawlers.


### Added 2026-05-07 (Pass 3)
- [AIOHTTP](entities/aiohttp.md) — AIOHTTP is an asynchronous HTTP Client/Server for asyncio and Python, used for creating bots and scr
- [Device and Browser Info](entities/device-and-browser-info.md) — A platform offering tools and articles for browser fingerprinting and bot detection.
- [Puppeteer](entities/puppeteer.md) — A Node.js library which provides a high-level API to control Chrome or Chromium over the DevTools Pr
- [Canvas fingerprint defender](entities/canvas-fingerprint-defender.md) — A browser extension that defends against canvas fingerprinting.
- [python-requests](entities/python-requests.md) — A Python HTTP library for making HTTP(s) requests.
- [downloadListPhoneNumbers.js](entities/downloadlistphonenumbers-js.md) — A JavaScript script for scraping temporary phone numbers from a website.
- [Open Bullet 2](entities/open-bullet-2.md) — A credential stuffing tool that can be used for web scraping and automation.
- [Simple Selenium Chrome Crawler](entities/simple-selenium-chrome-crawler.md) — A Python script that uses Selenium and Chrome to crawl web pages and extract links.

## Concepts

- [AI Scraping Assistants](concepts/ai-scraping-assistants.md) - Cursor + MCP + Claude workflow for scraper development acceleration.
- [Anti-Detect Browsers](concepts/anti-detect-browsers.md) - GoLogin, Kameleo, Orbita. Real-device fingerprint databases. 2024 benchmark: GoLogin 223/260, Incogniton 139/260.
- [API Scraping](concepts/api-scraping.md) - Internal API identification, authentication patterns (Bearer, JWT, Castle), Algolia, TLS requirement. LinkedIn Wayback Machine technique.
- [Browser Fingerprinting](concepts/browser-fingerprinting.md) - Canvas, WebGL, AudioContext, fonts, DOM signals. SwiftShader and zero-device red flags.
- [CDP Detection](concepts/cdp-detection.md) - Runtime.enable detection targeting automation protocol, not browser signals.
- [Certificate Pinning](concepts/certificate-pinning.md) - SSL pinning bypass on Android with Frida. RootAVD, frida-server, OkHttp hook.
- [Cookie and Session Reuse](concepts/cookie-session-reuse.md) - Cookie factory pattern. Anti-bot cookie lifetimes. Per-site behavioral variance.
- [Homepage-first Navigation](concepts/homepage-first-navigation.md) - Visit homepage before deep pages. Required by Cloudflare, PerimeterX, DataDome.
- [HTTP Performance](concepts/http-performance.md) - Async requests, ETags/HTTP caching, HTTP/3, connection pooling, exponential backoff. Server co-location 6x impact.
- [Hybrid Scraping](concepts/hybrid-scraping.md) - Browser for auth, HTTP client for data. 27x speed gain. TLS consistency critical.
- [Inventory Tracking](concepts/inventory-tracking.md) - Stock level extraction. Revenue estimation. Data in list page, PDP, click-and-collect, or cart APIs.
- [LLM Scraping](concepts/llm-scraping.md) - Schema extraction, vision extraction, code generation, self-healing. AI browsers (ChatGPT Atlas, Stagehand, Cursor).
- [Location Data Scraping](concepts/location-data-scraping.md) - World grid approach, radius vs bounding-box APIs, browser geolocation injection.
- [ML-Based Bot Detection](concepts/ml-bot-detection.md) - Machine learning models trained on behavioral features. Present in all major anti-bot systems.
- [Mobile App Scraping](concepts/mobile-app-scraping.md) - HTTP Toolkit interception, certificate pinning bypass, Frida setup, replicating app API calls.
- [Mobile Proxy Farming](concepts/mobile-proxy-farming.md) - DIY hardware farms (USB modems, 3proxy). Airproxy at 2000+ SIMs. Cost economics vs. commercial.
- [Mouse Movement Emulation](concepts/mouse-movement-emulation.md) - Bezier (ghost-cursor), Gaussian, Perlin noise (OxyMouse). DataDome checks mouse events; Cloudflare does not.
- [Proxy Fundamentals](concepts/proxy-fundamentals.md) - Four proxy types, CGNAT, IP reputation, Proxy Ladder, ban management, pricing (Sept 2024), Tor, XFF header.
- [Scraping Economics](concepts/scraping-economics.md) - Cost structure, business models, data commodity thesis, scaling constraints.
- [Scraping Infrastructure](concepts/scraping-infrastructure.md) - Compute options (Lambda, containers, VMs, bare metal), scheduling (Airflow, GitHub Actions, Scrapyd, Scrapeops), monitoring.
- [TLS Fingerprinting](concepts/tls-fingerprinting.md) - JA3 hash, HTTP/2 fingerprinting. Detection at TCP level before application data.
- [Web Scraping Legal Landscape](concepts/web-scraping-legal-landscape.md) - CFAA, DMCA 1201, ToS, key cases (hiQ, Meta/Bright Data, X/Bright Data, Google/SerpApi).
- [Web Unblockers](concepts/web-unblockers.md) - Managed bypass APIs. Benchmark results across Cloudflare/DataDome/Kasada/PX targets (2023-2024).
- [WebDriver vs CDP vs WebDriver BiDi](concepts/webdriver-vs-cdp-vs-bidi.md) - Three browser control protocols. CDP dominant for Chromium; BiDi the W3C cross-browser future.
- [WebSocket Bot Detection](concepts/websocket-bot-detection.md) - Stateful WS connection exploited for continuous fingerprinting and behavioral analysis.
- [WebSocket Scraping](concepts/websocket-scraping.md) - Real-time data via persistent connections. JSON and NATS protocols. Bitstamp and Polymarket.

## Comparisons

- [Anti-Detect Browser Benchmark 2024](comparisons/anti-detect-browser-benchmark-2024.md) - 8 commercial anti-detect browsers scored on CreepJS/BrowserScan. GoLogin leads at 223/260.
- [Firefox vs Chrome Stealth](comparisons/firefox-vs-chrome-stealth.md) - Camoufox vs Pydoll/UC/Patchright across anti-bot targets.

## Timelines

- [Cloudflare Bypass Evolution](timelines/cloudflare-bypass-evolution.md) - From Firefox+stealth (2022) to Camoufox dominance (2026).
