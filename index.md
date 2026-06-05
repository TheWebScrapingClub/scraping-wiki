# TWSC Wiki Index

Last updated: 2026-06-05

## Visual maps and views

- `canvases/`: JSON Canvas (`.canvas`) visual maps of landscapes and ecosystems
  - `agentic-browsers-landscape-2026.canvas`
- `views/`: Obsidian Bases (`.base`) live queries over wiki content
  - `all-entities.base` — see file for details
  - `anti-bot-vendors.base` — see file for details
  - `recently-touched.base` — see file for details
  - `tools-and-browsers.base` — see file for details

## Entities

### Anti-bot systems
- [ai-agent-reader-page](entities/ai-agent-reader-page.md) — This page is designed to present different content versions of a web page, distinguishing between what a human reader sees and what a software agent reads.
- [Akamai Bot Manager](entities/akamai.md) — TLS/JA3-heavy detection with behavioral JS sensor. Silent drop on mismatch. Nike.com catalog uses Akamai only; TLS impersonation sufficient.
- [AWS WAF](entities/aws-waf.md) — Amazon WAF with JavaScript challenge. Cookie factory pattern works: browser gets aws-waf-token, Scrapy reuses it.
- [Cloudflare](entities/cloudflare.md) — Multi-layer defense (TLS, JSD, Turnstile, ML scoring). Most tested anti-bot in TWSC corpus.
- [cloudflare-bot-management](entities/cloudflare-bot-management.md) — BotScope is a platform designed to audit anti-agentic defenses for any website, utilizing advanced heuristics to detect anti-bot and anti-agent measures with precision.
- [Datadome](entities/datadome.md) — Behavioral analysis focus. Hermes.com is the canonical hard target. Chrome leaks automation signals that Firefox/Brave do not.
- [F5 Bot Defense](entities/f5-bot-defense.md) — Enterprise anti-bot from F5 Networks. AI/behavioral focus. Second largest by market share (2022).
- [Kasada](entities/kasada.md) — Australian company. 429 signature. Hardware fingerprinting. Zero-trust first-request philosophy.
- [PerimeterX (HUMAN Bot Defender)](entities/perimeterx.md) — Now HUMAN Security. More IP-focused than fingerprint-focused (as of 2023). Scrapy Impersonate documented as a working bypass (2024).
- [reCAPTCHA](entities/recaptcha.md) — Google CAPTCHA system (v1/v2/v3). v3 is invisible risk scoring. Camoufox bypasses it; open-source token extractors do not.
- [sec-ch-ua-form-factors](entities/sec-ch-ua-form-factors.md) — A new HTTP client hint supported by Chrome that describes the user's device type (e.g., Desktop, Mob
- [selenium-headless-chrome-detection](entities/selenium-headless-chrome-detection.md) — Describes four methods to detect bots using Selenium running in headless Chrome environments.

### Browsers
- [browserbase-chrome](entities/browserbase-chrome.md) — Browserbase Chrome is utilized for running real-browser Quality Assurance (QA) against deployed previews of projects.
- [camoufox-reverse](entities/camoufox-reverse.md) — A Camoufox fork (WhiteNightShadow) that adds an engine-level PropertyTracer recording which DOM getters a page reads. A reverse-engineering instrument, not a stealth build. TWSC used it to watch Datadome read canvas/WebGL/navigator on leboncoin.
- [invisible-playwright](entities/invisible-playwright.md) — invisible_playwright is a patched replacement for Playwright designed specifically for Firefox that is engineered to pass advanced bot detection tests.
- [konform-browser](entities/konform-browser.md) — Konform Browser is a stealth browser based on Firefox ESR for web scraping and automation.
- [lightpanda](entities/lightpanda.md) — Lightpanda is a browser built for AI and automation, offering faster execution and lower memory usag
- [rayobrowse](entities/rayobrowse.md) — Rayobyte's stealth Chromium fork. Closed-source, Docker-based, CDP compatible. C++ patching. 100% benchmark score. Beta (2026).

### Proxy networks and tools
- [atproxy](entities/atproxy.md) — atproxy is a program written in Rust designed to transparently proxy TCP traffic originating from an Android application.
- [blanktrace](entities/blanktrace.md) — A cross-platform Rust CLI proxy that anonymizes browser traffic by randomizing digital fingerprints
- [clashmac](entities/clashmac.md) — A macOS native proxy tool with real-time traffic monitoring, topology visualization, and multi-hop t
- [firehol](entities/firehol.md) — A community-driven project that aggregates multiple IP lists, including open proxies, Tor exit nodes
- [hysteria](entities/hysteria.md) — Hysteria is a powerful, lightning fast, and censorship-resistant proxy.
- [ipidea](entities/ipidea.md) — A residential proxy network that enrolled 9 million Android devices into a botnet.
- [kampala](entities/kampala.md) — Kampala is a tool for intercepting and automating web traffic.
- [lte-modems](entities/lte-modems.md) — The LTE modems serve as the physical source for a production residential IP proxy pool.
- [meshscrape](entities/meshscrape.md) — A service that offers a distributed IP network for web scraping to avoid blocks and rate limits.
- [momoproxy](entities/momoproxy.md) — MoMoProxy is a service that provides free and paid proxy lists for various protocols, including HTTP, HTTPS, and SOCKS.
- [ncro](entities/ncro.md) — Nix Cache Route Optimizer, or ncro, is a small HTTP proxy written in Rust that functions as an intermediary between the `nix-daemon` and configured substituters.
- [nyxproxy](entities/nyxproxy.md) — A tool for building a self-hosted, rotating proxy gateway using IPv6 /64 subnets.
- [pangolin](entities/pangolin.md) — Pangolin is a peer-to-peer alternative to Cloudflare Tunnels that utilizes a client-to-site VPN combined with an edge reverse proxy to provide cloaked HTTPS traffic.
- [squid](entities/squid.md) — Squid is a network proxy server that was historically used by IT administrators to block various sites deemed unproductive or out of bounds for education.

### Tools and libraries
- [ag2b](entities/ag2b.md) — AG2B (Agent to Browser) is a client-side agentic runtime designed to allow an agent to execute its tasks directly within the user's browser.
- [aiohttp](entities/aiohttp.md) — AIOHTTP is an asynchronous HTTP Client/Server for asyncio and Python, used for creating bots and scr
- [Algolia](entities/algolia.md) — Client-side search API. EndClothing full catalog with no anti-bot despite Akamai on site.
- [AnyCrawl](entities/anycrawl.md) — MIT-licensed LLM-ready scraping API. JSON extraction mode, MCP server. No anti-bot bypass. Comparable to FireCrawl.
- [beautiful-code-screenshots-codeshot](entities/beautiful-code-screenshots-codeshot.md) — CodeShot is an API toolkit designed for developers and AI agents that facilitates code screenshotting, website scraping, and link preview generation.
- [botasaurus](entities/botasaurus.md) — Python scraping framework with decorator-based API. Works locally against Cloudflare/DataDome/Kasada. Fails from server (SwiftShader exposure).
- [browser-use](entities/browser-use.md) — Browser Use is a cloud-based browser automation platform that aims to create undetectable browsers.
- [camoufox](entities/camoufox.md) — Custom Firefox build. Best performer on strict Cloudflare/DataDome configs. Bypasses reCAPTCHA v3 (2025).
- [canvas-fingerprint-defender](entities/canvas-fingerprint-defender.md) — A browser extension that defends against canvas fingerprinting.
- [chaser-oxide](entities/chaser-oxide.md) — A Rust-based fork of `chromiumoxide` for hardened, undetectable browser automation.
- [cheerio](entities/cheerio.md) — A library used in the Node.js environment for parsing HTML and extracting data from web pages.
- [childflow](entities/childflow.md) — childflow is a per-command-tree network sandbox designed for Linux environments.
- [clashmax](entities/clashmax.md) — ClashMax is a native macOS graphical client built with SwiftUI that serves as a Mihomo proxy client.
- [crawl4ai](entities/crawl4ai.md) — An open-source web crawler and scraper for LLM-friendly Markdown output.
- [curl-cffi](entities/curl-cffi.md) — Python HTTP client with TLS impersonation. Critical for hybrid scraping. Also covers scrapy-impersonate and hrequests.
- [device-and-browser-info](entities/device-and-browser-info.md) — A platform offering tools and articles for browser fingerprinting and bot detection.
- [dolphin-anty](entities/dolphin-anty.md) — Anti-detect browser for multi-account workflows. Scenarios builder, Profile Synchronizer, REST API. Free tier (10 profiles).
- [envoy](entities/envoy.md) — Envoy is an infrastructure component discussed in the context of Reddit's feed serving path.
- [facebookexternalhit](entities/facebookexternalhit.md) — A specific user agent string used by the Facebook crawler to retrieve information about shared conte
- [feedstock](entities/feedstock.md) — A high-performance web crawler and scraper for TypeScript, powered by Bun and Playwright.
- [fingerprinterjs](entities/fingerprinterjs.md) — FingerprinterJS v2.0 is a browser fingerprinting and bot detection tool.
- [fpscanner](entities/fpscanner.md) — A lightweight browser fingerprinting library for bot detection.
- [ghost-cursor](entities/ghost-cursor.md) — Bezier/Fitts's Law mouse movement for Playwright. OxyMouse is a newer alternative with Gaussian and Perlin noise options.
- [go-http-client](entities/go-http-client.md) — An HTTP(s) client implemented in Golang used to make HTTP(s) requests from a Golang program.
- [gologin](entities/gologin.md) — Anti-detect browser, Orbita engine. Top benchmark performer 223/260 in 2024.
- [goscrapy](entities/goscrapy.md) — A high-performance web scraping framework for Go, designed with the familiar architecture of Python'
- [groxy](entities/groxy.md) — Groxy is a small Go library designed for building forward proxy servers.
- [hodor](entities/hodor.md) — Hodor is a tiny reverse proxy written in Rust designed to gate web applications behind a single shared password.
- [hRequests](entities/hrequests.md) — TLS-fingerprinted HTTP with embedded headless browser. Akamai/Cloudflare/PX pass; DataDome/Kasada fail.
- [iherb-cli](entities/iherb-cli.md) — A Rust command-line tool for querying product data from iHerb using a headless browser.
- [is-antibot](entities/is-antibot.md) — A library that detects antibot and CAPTCHA challenges from 30+ providers using signals.
- [ja3proxy](entities/ja3proxy.md) — Go-based TLS Client Hello rewriter via uTLS.
- [Kadoa](entities/kadoa.md) — Commercial AI scraping workflow platform. UI-driven, anti-bot included, 5 proxy locations.
- [kameleo](entities/kameleo.md) — Anti-detect browser. Junglefox + Chroma. First to support Selenium + Playwright + Puppeteer simultaneously.
- [kimurai](entities/kimurai.md) — A Ruby-based web scraping framework that uses AI to assist in data extraction.
- [libretto](entities/libretto.md) — A toolkit for building robust web integrations and maintaining browser automations.
- [linkedinbot](entities/linkedinbot.md) — A scraper used by LinkedIn to gather information about shared URLs in posts or messages.
- [llmcap](entities/llmcap.md) — LLMCap is a service designed to enforce hard dollar caps on LLM API calls across various providers.
- [lucidextractor](entities/lucidextractor.md) — An enterprise web scraping and SEO analysis platform.
- [masterhttprelayvpn](entities/masterhttprelayvpn.md) — A domain-fronted HTTP/SOCKS5 proxy tool that tunnels traffic through Google Apps Script for scraping
- [mitmproxy](entities/mitmproxy.md) — mitmproxy is a small interceptor written in Python used to build a proxy, exemplified by the `simple-proxy` project.
- [mochi-js](entities/mochi-js.md) — mochi.js is a Bun-native, raw-CDP browser automation framework designed to create relationally-coherent fingerprints.
- [nodejs-based-scraper](entities/nodejs-based-scraper.md) — A previous project mentioned in the series used NodeJS to collect temporary phone numbers and messag
- [Nodriver](entities/nodriver.md) — Chrome automation without WebDriver layer. Passes CDP tests natively but cannot forge hardware fingerprint.
- [obscrd](entities/obscrd.md) — An open-source content protection system for React that scrambles HTML and blocks AI crawlers.
- [obscura](entities/obscura.md) — A headless browser engine written in Rust for web scraping and AI agent automation.
- [open-bullet-2](entities/open-bullet-2.md) — A credential stuffing tool that can be used for web scraping and automation.
- [owl-browser](entities/owl-browser.md) — A self-hosted browser automation engine for automation at scale with 256 parallel contexts and undet
- [playwright](entities/playwright.md) — Microsoft browser automation. Detectable by default, patchable via Patchright/Undetected Playwright.
- [proxelar](entities/proxelar.md) — A Rust-based MITM proxy for intercepting and modifying HTTP/HTTPS traffic.
- [proxy-server](entities/proxy-server.md) — A service that brokers connections between the browser and phone.
- [puppeteer](entities/puppeteer.md) — A Node.js library which provides a high-level API to control Chrome or Chromium over the DevTools Pr
- [pydoll](entities/pydoll.md) — Async CDP Chrome automation. Stability issues in 2026 benchmarks.
- [python-requests](entities/python-requests.md) — A Python HTTP library for making HTTP(s) requests.
- [reader](entities/reader.md) — An open-source, production-grade web scraping engine built for LLMs.
- [resurf](entities/resurf.md) — Resurf is a deterministic and reproducible test environment designed for systematically testing AI browser agents against realistic, stateful environments.
- [ricci-flow-ai-web-scraper](entities/ricci-flow-ai-web-scraper.md) — A Chrome extension for AI-powered web scraping that extracts data from websites and exports it to Ex
- [roxy](entities/roxy.md) — Roxy is a feature-rich RSS proxy written in Go that is designed to combine multiple RSS feeds into a single, queryable feed.
- [ScrapeGraphAI](entities/scrapegraphai.md) — LLM-powered scraping library and commercial API. Non-deterministic, best for horizontal multi-site extraction.
- [scrapingduck](entities/scrapingduck.md) — A scraping API that handles IP rotation, JavaScript rendering, and provides a free tier for web scra
- [scrapingsandbox](entities/scrapingsandbox.md) — A web scraping sandbox for learning and testing web scraping techniques.
- [scrapling](entities/scrapling.md) — Python library with three fetchers (static, dynamic, stealth). 1735x faster than BS4. Fetcher class achieves 100% on Nike/Akamai without browser overhead.
- [Scrapoxy](entities/scrapoxy.md) — Open-source proxy aggregator. Unifies providers and cloud VM egress. ~20% cost savings vs. pure cloud.
- [scrapy](entities/scrapy.md) — Scrapy is a Python library that is used in typical web scraping setups.
- [sensecollect](entities/sensecollect.md) — SenseCollect is a self-service platform designed to simplify web data extraction for lead generation and market intelligence.
- [simple-selenium-chrome-crawler](entities/simple-selenium-chrome-crawler.md) — A Python script that uses Selenium and Chrome to crawl web pages and extract links.
- [spidersuite](entities/spidersuite.md) — A powerful web crawler and security testing tool for penetration testers and security researchers.
- [spidra](entities/spidra.md) — A web scraping platform that uses AI to extract data from websites.
- [tadpole](entities/tadpole.md) — A language for writing declarative, modular scraping code.
- [transparenttorproxy](entities/transparenttorproxy.md) — A Linux CLI utility that transparently routes all system traffic through the Tor network using nftab
- [uaparser-js](entities/uaparser-js.md) — A JavaScript library recommended for parsing user agents to extract browser and OS information.
- [undetected-chromedriver](entities/undetected-chromedriver.md) — Patched Selenium. Stagnant repo, succeeded by Nodriver/Zendriver.
- [webassembly-simd](entities/webassembly-simd.md) — WebAssembly SIMD refers to Single Instruction, Multiple Data operations introduced to the WebAssembly specification.
- [wick](entities/wick.md) — Wick is an open-source tool that allows AI agents to access web pages as if they were real browsers.
- [wxpath](entities/wxpath.md) — wxpath is a Python library for declarative web crawling using XPath.

### Web Unblockers
- [Oxylabs Web Unblocker](entities/oxylabs-unblocker.md) — 96/100 overall. Cheapest on Kasada benchmark ($0.10/101 URLs). Best dashboard.
- [Smartproxy Site Unblocker](entities/smartproxy-unblocker.md) — 80/100 overall. $12/GB. Kasada improved from 0% (2023) to 92% (2024).
- [Zyte API](entities/zyte-api.md) — 100/100 with browser rendering. Fails Kasada. Per-request dynamic pricing. Scrapy integration via scrapy-zyte-api.

## Concepts

- [ai-scraping-assistants](concepts/ai-scraping-assistants.md) — AI scraping assistants are setups where a large language model is embedded into the development workflow to generate, modify, or repair scrapers — rather than to extract data at runtime. The LLM acts as an accelerator for the developer, not as a replacement for the scraper itself. The canonical current form is an AI-powered IDE (Cursor) connected to custom tooling via the Model Context Protocol (MCP).
- [Anti-Detect Browsers](concepts/anti-detect-browsers.md) — Anti-detect browsers are Chromium or Firefox forks engineered to present a consistent, plausible fingerprint from a database of real device profiles. Unlike standard browser automation which exposes the actual hardware and software environment of the machine running the scraper, anti-detect browsers attach a pre-built fingerprint from a real consumer device to the automation session, regardless of the actual underlying hardware.
- [API Scraping](concepts/api-scraping.md) — API scraping is the practice of identifying and replicating the internal HTTP requests that a browser or app makes to fetch data, bypassing HTML parsing entirely. The data is already structured, usually JSON, and the endpoint is observable by monitoring network traffic in DevTools or a proxy tool.
- [Bot Detection](concepts/bot-detection.md) — Bot detection is the umbrella discipline of identifying automated traffic on a website and distinguishing it from legitimate human visitors. It sits opposite to web scraping: the same fingerprints, behaviors, and protocol-level traces that scrapers try to hide are what detection systems look for. Reading the detection literature is the most direct way for a scraper engineer to understand which signals actually leak.
- [browser-fingerprinting](concepts/browser-fingerprinting.md) — A stateless, cookieless tracking mechanism that identifies browsers by collecting and hashing the outputs of browser APIs. Unlike cookies, fingerprints require no storage on the client and persist across sessions, incognito modes, and cookie clears.
- [canvas-fingerprinting](concepts/canvas-fingerprinting.md) — Canvas fingerprinting is a stateless tracking technique that identifies a device by drawing graphics off-screen and hashing the resulting pixels. Two machines asked to render the same text and shapes produce subtly different pixel output, because the final image depends on the GPU, the graphics driver, the font rasterizer, and the anti-aliasing settings of that specific machine. The hash of those pixels becomes a high-entropy identifier that needs no cookie and survives incognito mode and cache clears.
- [cdp-detection](concepts/cdp-detection.md) — A detection technique that identifies browser automation by observing the Chrome DevTools Protocol (CDP) commands sent to the browser during page load. CDP is the underlying control protocol used by Playwright, Puppeteer, Selenium (on Chromium), and related frameworks. Anti-bot systems can detect its presence independently of any JavaScript-level signals.
- [Certificate Pinning](concepts/certificate-pinning.md) — Certificate pinning is a security mechanism in mobile apps that causes the app to reject any TLS certificate that does not match a specific expected certificate or public key, regardless of whether the device's OS trusts the certificate authority. It prevents man-in-the-middle inspection even on a device where the inspector's root CA has been installed.
- [cookie-session-reuse](concepts/cookie-session-reuse.md) — A technique where anti-bot clearance cookies obtained through one browser session are extracted and reused across multiple subsequent requests made by a browserless HTTP client. The browser absorbs the cost of the challenge once; the HTTP client amortizes that cost across many requests.
- [homepage-first-navigation](concepts/homepage-first-navigation.md) — A navigation pattern where a scraper visits the site's homepage (or another entry-point URL) before accessing any deep content pages. The purpose is to establish session state — cookies, fingerprint checks, and anti-bot challenges — in the same sequence a real user would encounter them.
- [HTTP Performance in Scraping](concepts/http-performance.md) — HTTP performance optimization for scraping covers the set of techniques that reduce execution time, bandwidth cost, and infrastructure requirements without changing the data extracted. The main levers are concurrency, protocol selection, caching, and retry behavior.
- [hybrid-scraping](concepts/hybrid-scraping.md) — An architecture that uses a full browser only for the portions of a session that require anti-bot clearance, then hands off to a lightweight HTTP client for all subsequent data requests. The browser handles authentication and challenge resolution; the HTTP client handles scale.
- [inventory-tracking](concepts/inventory-tracking.md) — Inventory tracking through web scraping is the practice of monitoring the stock levels of products on e-commerce sites and retail websites by extracting data that those sites expose for operational purposes — usually to power their own availability and pickup features. The extracted data is most valuable as a repeated time series rather than a single snapshot.
- [llm-scraping](concepts/llm-scraping.md) — Using a large language model to extract structured data from web pages, replacing or supplementing traditional CSS selector or XPath-based parsing. The LLM interprets the page content — either raw HTML, cleaned text, or a screenshot — and returns structured output matching a defined schema. A separate but related use case is using LLMs to generate scraper code rather than to parse data at runtime.
- [location-data-scraping](concepts/location-data-scraping.md) — Location data scraping covers the techniques for extracting data that is spatially indexed — store locators, accommodation listings, restaurant maps, delivery zones — where the API requires geographic inputs (coordinates, radius, or bounding box) and returns data for the area specified. The central challenge is ensuring complete geographic coverage without issuing redundant or missing queries.
- [ML-Based Bot Detection](concepts/ml-bot-detection.md) — ML-based bot detection refers to the use of machine learning models to classify web traffic as human or automated. Unlike rule-based systems (IP blocklists, simple rate limits, user-agent checks), ML models learn from behavioral patterns across large traffic datasets and can identify subtle automation signals that static rules miss.
- [Mobile App Scraping](concepts/mobile-app-scraping.md) — Mobile app scraping is the practice of intercepting the network traffic generated by a mobile app and replicating the underlying API calls in a scraper. Since mobile apps communicate with backends through the same HTTP/HTTPS protocol as browsers, the data they fetch can be captured and reproduced.
- [Mobile Proxy Farming](concepts/mobile-proxy-farming.md) — Mobile proxy farming is the practice of building and operating infrastructure that routes proxy traffic through real cellular network connections — typically USB modems or SIM-equipped hardware — to produce genuine mobile IP addresses with CGNAT-level trust properties. Unlike SDK-sourced residential proxies, which borrow device connections from consumer apps, a proxy farm gives the operator full control over the hardware, IP rotation, and connectivity.
- [Mouse Movement Emulation](concepts/mouse-movement-emulation.md) — Mouse movement emulation is the practice of generating pointer trajectories that match the statistical properties of human hand movement during browser automation. Anti-bot systems that monitor mouse events can distinguish between the instantaneous or straight-line movements produced by automation frameworks and the curved, velocity-varied paths that humans produce. Emulation attempts to make automated mouse behavior indistinguishable from real user input at the event listener level.
- [proxy-fundamentals](concepts/proxy-fundamentals.md) — Proxies route outbound HTTP requests through an intermediate IP address, changing the apparent origin of the request. In a scraping context, the proxy's IP reputation, ASN, and network type are often more consequential than any browser-level signal.
- [Scraping Infrastructure](concepts/scraping-infrastructure.md) — Scraping infrastructure encompasses the compute, storage, scheduling, monitoring, and proxy management systems that run scrapers reliably at scale. The choice of infrastructure directly determines cost structure, IP rotation capability, and operational overhead. A scraper that works on a laptop fails at 100,000 requests per day without the right infrastructure beneath it.
- [scraping-economics](concepts/scraping-economics.md) — The economics of web scraping encompass the cost structure of running scraping operations, the business models for monetizing scraped data, and the market dynamics of the web data industry. The industry spans two distinct roles: those who sell the infrastructure and tools that enable scraping ("selling shovels"), and those who scrape and sell the resulting data.
- [tls-fingerprinting](concepts/tls-fingerprinting.md) — A detection technique that identifies the client making an HTTPS request by analyzing the structure of its TLS ClientHello message, before any application-layer data is exchanged. The most common implementation is JA3, which produces an MD5 hash from five fields in the handshake: TLS version, cipher suite IDs, extension IDs, elliptic curve IDs, and elliptic curve format IDs.
- [Web Unblockers](concepts/web-unblockers.md) — A web unblocker is a managed API that accepts a target URL and returns the page content after transparently handling IP rotation, CAPTCHA solving, browser fingerprinting, and anti-bot bypass on the provider's infrastructure. The caller makes a standard HTTP request; the provider does the work of getting through the target's defenses.
- [web-scraping-legal-landscape](concepts/web-scraping-legal-landscape.md) — The legal landscape for web scraping is a contested, evolving body of case law and regulation across multiple jurisdictions. No single statute governs it. Whether any particular scraping operation is legal depends on the interaction of: the Computer Fraud and Abuse Act (CFAA), the Digital Millennium Copyright Act (DMCA), copyright law, contract law (Terms of Service), and in Europe, the GDPR. The area has shifted materially between 2022 and 2026, with courts increasingly being asked to define where public data access ends and illegal circumvention begins.
- [WebDriver vs CDP vs WebDriver BiDi](concepts/webdriver-vs-cdp-vs-bidi.md) — Three distinct protocols exist for controlling a browser programmatically. They differ in design origin, transport mechanism, browser support, and what detection surface they expose. Choosing the wrong one for a scraping context can introduce detection vectors that are independent of any fingerprint or behavior emulation.
- [webrtc-ip-leak](concepts/webrtc-ip-leak.md) — A WebRTC IP leak is when a page learns a client's real LAN or WAN IP address through the WebRTC API, even though the client's HTTP traffic is routed through a proxy. It happens because WebRTC gathers network candidates over UDP, on a path that an ordinary HTTP proxy does not control. For a scraper this is a coherence failure: the site sees one IP for the page requests (the proxy) and a different IP for WebRTC (the real machine), and the mismatch is a strong automation and evasion signal.
- [WebSocket Bot Detection](concepts/websocket-bot-detection.md) — WebSocket bot detection refers to anti-bot techniques that exploit the stateful, persistent nature of the WebSocket protocol to identify automated clients. Because WebSocket connections are long-lived and bidirectional, servers can monitor client behavior continuously over the connection lifetime, enabling detection patterns that are not possible with stateless HTTP.
- [websocket-scraping](concepts/websocket-scraping.md) — WebSocket scraping is the practice of connecting to a site's WebSocket endpoint directly, subscribing to the same channels the browser subscribes to, and receiving the same real-time data stream. Unlike HTTP scraping, which is request-response, WebSocket connections are persistent and bidirectional. The server pushes updates without the client polling.

## Comparisons

- [Anti-Detect Browser Benchmark 2024](comparisons/anti-detect-browser-benchmark-2024.md) — Eight commercial anti-detect browsers evaluated against a standardized fingerprint detection test suite. The comparison measures how convincingly each browser impersonates a real consumer device when probed by the same fingerprinting methods that anti-bot systems use.
- [Camoufox vs its forks](comparisons/camoufox-vs-forks.md) — After development of [Camoufox](../entities/camoufox.md) moved to CloverLabs in 2026, its public repository grew past 750 forks. Most are mirror bots with no commits of their own. This page compares stock Camoufox against the three forks that actually change anti-detect behavior, and records which one to run against a real target. The comparison is grounded in our 2026-06 testing against [Datadome](../entities/datadome.md) on leboncoin.fr, not on the forks' stated goals.
- [Firefox-based vs Chrome-based Stealth Tools](comparisons/firefox-vs-chrome-stealth.md) — Firefox-based stealth tools (primarily [Camoufox](../entities/camoufox.md)) against Chrome-based stealth tools ([Pydoll](../entities/pydoll.md), [undetected-chromedriver](../entities/undetected-chromedriver.md), [Patchright](../entities/playwright.md)) for bypassing anti-bot systems. This comparison matters because the browser engine choice has a measurable impact on bypass success rates, independently of the stealth techniques applied on top.

## Timelines

- [Cloudflare Bypass Evolution](timelines/cloudflare-bypass-evolution.md) — How [Cloudflare](../entities/cloudflare.md) bypass techniques have evolved as Cloudflare has progressively tightened its defenses. This timeline tracks what worked, what stopped working, and what replaced it, based on TWSC's direct testing.
