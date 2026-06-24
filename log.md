# TWSC Wiki Log

Chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] operation | subject`

Operations: `ingest`, `query`, `lint`, `update`, `create`

---

## [2026-04-22] create | Wiki bootstrap from 30 articles

Source: batch ingest of 30 TWSC articles covering anti-bot systems, tools, fingerprinting, proxies, and LLM scraping.
 
Articles processed:
- cloudflare-how-to-scrape.md
- bypassing-cloudflare-in-2026.md
- cloudflare-turnstile-what-is-that.md
- bypass-akamai-bot-protection.md
- the-lab-30-how-to-bypass-akamai-protected.md
- bypass-datadome-bot-protection.md
- scraping-datadome-camoufox.md
- bypassing-kasada-2025-open-source.md
- the-lab-35-bypassing-perimeterx-with.md
- the-lab-56-bypassing-perimeterx-3.md
- browser-fingerprinting-how-it-works.md
- understanding-browser-fingerprint.md
- the-lab-33-fingerprinting-at-different.md
- fingerprint-injection-playwright.md
- anti-detect-browsers-vs-browsers-as-a-service.md
- scrapling-hands-on-guide.md
- pydoll-webdriver-scraping.md
- playwright-stealth-cdp.md
- the-stealth-stack-web-scraping.md
- undetected-chromedriver-cloudflare-datadome.md
- everything-about-proxies.md
- choosing-proxy-provider-scraping.md
- five-secrets-of-the-proxy-industry.md
- the-unit-economics-of-proxy-providers.md
- hybrid-scraping-camoufox-curl-cffi.md
- intercepting-api-traffic-for-scraping.md
- the-lab-94-using-cookies-and-session.md
- scraping-with-llms-gpt-vision.md
- how-to-use-llms-in-scraping.md
- bypass-datadome-mouse-movements-in-playwright.md

Pages created:
- 5 entity pages (anti-bot): cloudflare, akamai, datadome, perimeterx, kasada
- 8 entity pages (tools): camoufox, playwright, pydoll, undetected-chromedriver, scrapling, curl-cffi, ghost-cursor, ja3proxy
- 8 concept pages: browser-fingerprinting, tls-fingerprinting, cdp-detection, homepage-first-navigation, hybrid-scraping, cookie-session-reuse, proxy-fundamentals, llm-scraping
- 1 comparison page: firefox-vs-chrome-stealth
- 1 timeline page: cloudflare-bypass-evolution

Total: 23 wiki pages from 30 source articles.

---

## [2026-04-22] ingest | 20 articles — Datadome, Kasada, PerimeterX, AWS WAF, reCAPTCHA, WebSocket detection, ML detection

Source: second batch ingest of 20 TWSC articles.

Articles processed (with findings):

**Datadome (4 articles)**
- scraping-datadome-api-hermes.md (2022-09-15): Mobile impersonation bypass on Hermes.com; XSRF token cycling pattern; Datadome cookie obtained via mobile client.
- how-to-scrape-datadome-2023.md (2023-04-14): Playwright+Chrome blocked; Playwright+Firefox passes locally and on datacenter; Playwright+Brave passes. Chrome leaks automation signals.
- bypassing-datadome-2023-scraping.md (2023-12-06): Footlocker.co.uk; Ghost Cursor + residential UK proxies + Playwright required for multi-page scraping.
- scraping-idealista-bypass-datadome.md (2024-08-06): Sponsored/tutorial article. Confirms Datadome on Idealista. ScraperAPI as commercial solution. Limited unique technical findings; sources noted but article mostly tutorial-level.

**Kasada (5 articles)**
- scraping-a-kasada-website.md (2022-08-05): First encounter; canadagoose.com; Playwright+stealth blank page; robots.txt misconfiguration/Screaming Frog workaround; SEO impact noted.
- scraping-kasada-protected-websites.md (2023-03-12): Chrome + `ignore_default_args=["--enable-automation"]` + `--disable-blink-features=AutomationControlled` passes locally; Firefox passes; GoLogin passes; Bright Data Web Unblocker works from server.
- how-to-by-pass-kasada-bot-mitigation.md (2023-03-13): Same findings as above (companion article). GoLogin and Bright Data as commercial solutions.
- bypassing-kasada-web-scraping.md (2024-01-25): Undetected-chromedriver works locally not from datacenter; Playwright+Brave same result; Bright Data Scraping Browser confirmed working from server.
- octo-browser-bypass-kasada.md (2024-04-16): Sponsored/Octo Browser article. Hyatt.com on Kasada documented. Octo Browser bypasses it; standard Chrome/Playwright blocked.

**PerimeterX (3 articles)**
- scraping-perimeterx-websites.md (2022-11-24): First PerimeterX Lab article. neimanmarcus.com API found. Scrapy with proper headers works on API; Playwright with mouse simulation reduces 424 errors.
- bypassing-perimeterx-2023.md (2023-08-17): Undetected-chromedriver+Brave works on neimanmarcus.com. Playwright+Firefox works. Playwright+Chrome needs specific flags. Session reset needs new profile directory.
- bypassing-perimeterx-scrapy.md (2024-02-22): Scrapy Impersonate bypasses PerimeterX on booking.com and neimanmarcus.com without browser automation. Key finding.

**AWS WAF (1 article)**
- bypassing-aws-waf-scraping.md (2024-06-06): Traveloka.com target. aws-waf-token cookie identified. Scrapy alone fails to get token. Playwright+Scrapy hybrid: browser fetches token, Scrapy reuses it for 4 days.

**reCAPTCHA (3 articles)**
- are-captchas-still-a-thing.md (2023-08-27): Historical overview of CAPTCHA evolution. Not unique test findings; contextual/background article.
- bypassing-recaptcha-v3.md (2025-06-20): Open-source token extraction fails (low score, fingerprint mismatch). rnet/hrequests also fail. Camoufox works transparently on completedns.com.
- bypassing-recaptchas-with-open-source.md (2025-08-03): Part 2. NextCaptcha tested; returns token but POST request still fails (score or fingerprint insufficient).

**Anti-detect matrix and AI vs AI (2 articles)**
- anti-detect-anti-bot-matrix.md (2023-02-02): Structured benchmark. Chrome worst performer, Firefox best free performer. UC outperforms standard Playwright. First systematic multi-anti-bot comparison. F5 documented as a tested anti-bot.
- the-lab-21-bypass-anti-bot-challenges.md (2023-06-22): Nimble AI browser vs Cloudflare, Datadome, Kasada, F5, PerimeterX. AI vs AI framing. Results not fully detailed in processed excerpt.

**WebSocket bot detection (1 article)**
- websocket-bot-detection-scraping.md (2026-03-22): Comprehensive conceptual overview. Handshake fingerprinting, honeypot events, lifecycle analysis, binary data, continuous fingerprinting via persistent connection, TLS+WS combined fingerprint.

**ML-based bot detection (1 article)**
- machine-learning-for-detecting-bots.md (2025-06-15): Conceptual article from detection (defender) perspective. Feature categories: request patterns, session behavior, headers, fingerprint. Supervised/unsupervised/semi-supervised paradigms explained. Not a bypass article.

Articles skipped:
- scraping-idealista-bypass-datadome.md: Sponsor/tutorial article (ScraperAPI). No unique empirical findings beyond confirming Datadome presence on Idealista.
- are-captchas-still-a-thing.md: Historical background article. No unique test findings. Contextual information folded into reCAPTCHA entity page.
- octo-browser-bypass-kasada.md: Partially sponsored (Octo Browser). Hyatt.com/Kasada finding is notable and incorporated into kasada.md. Rest is general anti-detect browser overview.

Pages updated:
- entities/datadome.md — Added mobile impersonation finding, Chrome/Firefox distinction, behavioral scoring details, detection method overview, Idealista confirmation
- entities/kasada.md — Added 2022-2024 chronological experience, SEO impact finding, Octo Browser/hyatt.com finding, undetected-chromedriver proxy auth limitation, polymorphic obfuscation detail
- entities/perimeterx.md — Added 2022 neimanmarcus API-first approach, 2023 tool matrix results, 2024 Scrapy Impersonate bypass, booking.com unprotected API pattern

Pages created:
- entities/aws-waf.md — New entity. Cookie factory bypass pattern documented.
- entities/recaptcha.md — New entity. reCAPTCHA v1/v2/v3 mechanics, bypass approaches, alternatives.
- entities/f5-bot-defense.md — New entity. Preliminary; limited TWSC coverage.
- concepts/websocket-bot-detection.md — New concept. Six detection techniques documented.
- concepts/ml-bot-detection.md — New concept. Feature categories, learning paradigms, arms race dynamic.

Total changes: 3 pages updated, 5 pages created.

---

## [2026-04-22] ingest | Cloudflare + Akamai bypass articles (batch 3)

Source: 18 TWSC articles on Cloudflare and Akamai bypass techniques.

Articles processed (with original content):
- bypass-cloudflare-scraping-playwright.md (2023-01): GoLogin + Playwright vs Antonioli.eu; anti-detect browsers as a class introduced.
- bypassing-cloudflare-gologin-playwrigh.md (2024-01): GoLogin fingerprint masking isolation; WebGL vendor/renderer is the critical Cloudflare signal on Harrods; indeed.com Turnstile on AWS bypassed by Orbita browser alone.
- bypassing-cloudflare-with-kameleo.md (2024-01): Kameleo anti-detect browser tested on Harrods; Windows-only server requirement; pricing constraints documented.
- bypassing-cloudflare-with-nodriver.md (2024-09): Nodriver passes CDP tests natively; fails from datacenter due to unmasked hardware fingerprint; works locally.
- cloudflare-bypass-2026.md (The Lab article): Same test data as bypassing-cloudflare-in-2026.md; Pydoll API inconsistencies documented in detail (tab.page_source, tab.current_url).
- cloudflare-web-unblocker-benchmark.md (2024-09): Indeed.com benchmark; Zyte API fastest (6.5s) and cheapest ($0.063); ZenRows 99% first-try accuracy; Infatica incomplete renders.
- the-lab-29-bypass-cloudflare-bot.md (2023-10): scrapy-impersonate 100% on Harrods from datacenter with residential proxy; TLS fingerprint sufficient on some Cloudflare configs.
- how-to-bypass-cloudflare-turnstile.md (2025-01): Botasaurus bypasses Indeed Turnstile locally; Patchright bypasses it; Camoufox inconsistent; Playwright and Cloudscraper fail.
- testing-bright-data-unblockler-cloudflare.md (2023-03): Bright Data Web Unblocker 88/100 across Cloudflare, PerimeterX, Kasada, F5, DataDome.
- bypassing-akamai-for-free.md (2025-03): scrapy-impersonate bypasses Gucci.com/Akamai ~90% of cases; clearance cookie persists for days.
- bypassing-akamai-proxidize.md (2023-08): H&M/Akamai at scale with Proxidize mobile proxy hardware; IP rotation strategy for 100k+ requests.
- scraping-akamai-protected-website.md (2023-07): Zalando/Akamai; basic Scrapy with standard headers sufficient for public data; 1.3M product scope.
- scraping-akamai-protected-websites.md (2024-05): Versace/Loewe/Zalando/NewBalance/Rakuten; updated headers bypass Akamai; Azure IPs less blocked than AWS; outdated User-Agent (Chrome 54) alone triggers blocks.
- hrequests-bypass-akamai-with-python.md (2023-11): hrequests library; Go-based TLS backend; Akamai-specific HTTP/2 fingerprint documented.

Articles skipped:
- bypass-cloudflare-browser-check.md (2023-02): Introductory overview article; no original test results; all content covered elsewhere.
- bypassing-cloudflare-free-tools.md (2024-05): Summarizes existing content (scrapy-impersonate, Browserforge, CloudflareBypassForScraping); partially tested; covered by other articles with more depth.
- scraping-cloudflare-websites-2023-q1-update.md (2023-03): Early partial results on Harrods (Q1 2023); findings superseded by later articles; no unique claims not covered elsewhere.
- scraping-cloudflare-websites-an-api.md (2024-07): PixelWhisperer API test; private unreleased tool; 100% success claimed but non-reproducible; tool not publicly available.

Pages updated:
- entities/cloudflare.md: 12 new sources; comprehensive TWSC experience section with per-target behavioral data; WebGL vendor as critical signal documented; rate limiting vs bot detection distinction; web unblocker benchmark results.
- entities/akamai.md: 6 new sources; expanded known deployments (Gucci, Versace, Loewe, H&M, Zalando, Rakuten, NewBalance); scrapy-impersonate as primary bypass tactic; Azure vs AWS IP reputation; hrequests tool added; outdated User-Agent finding.
- entities/camoufox.md: 2 new sources; fingerprint rotation inconsistency on Indeed Turnstile (2025) documented.
- entities/curl-cffi.md: 3 new sources; scrapy-impersonate documented as Scrapy wrapper for curl_cffi; hrequests documented.
- timelines/cloudflare-bypass-evolution.md: 6 new sources; 5 new timeline entries added: GoLogin 2023, scrapy-impersonate 2023, Nodriver 2024, web unblocker benchmark 2024, open-source tool comparison 2025.
- comparisons/firefox-vs-chrome-stealth.md: 2 new sources; Patchright Indeed result added; Botasaurus finding noted; local vs datacenter distinction clarified.
- index.md: Nodriver entity and Anti-Detect Browsers concept added.

Pages created:
- entities/nodriver.md: New tool entity. Nodriver by ultrafunkamsterdam; CDP-free approach; September 2024 Harrods test results.
- concepts/anti-detect-browsers.md: New concept. GoLogin and Kameleo systematically tested against Cloudflare; WebGL vendor as critical fingerprint signal; commercial vs open-source cost/capability comparison.

Total changes: 6 pages updated, 2 pages created.

---

## [2026-04-22] ingest | 57 articles — AI/LLM scraping, legal landscape, business economics

Source: batch ingest of 57 TWSC articles covering AI-powered scraping tools and workflows, web scraping legal cases, and the economics of the scraping business.

Articles processed with original findings:

**AI/LLM scraping tools (12 articles)**
- scraping-with-llms-scrapegraphai.md (2024-05): ScrapeGraphAI with GPT-3.5-turbo on Net-A-Porter; zero correct prices; inconsistent results day-to-day. GPT-4o on TripAdvisor better.
- llm-scrapegraphai-costs-web-scraping.md (2024-06): ScrapeGraphAI SmartScraperGraph and ScriptCreatorGraph pipeline architecture documented. Cost analysis. Self-healing pipeline concept introduced.
- writing-scrapers-with-llms.md (2024-09): GPT-4o, Llama 3.1, Mistral compared via ScriptCreatorGraph. GPT-4o best on GitHub repos. All models unreliable on e-commerce/BBC.
- the-lab-84-ai-driven-web-scraping.md (2025-05): OpenAI Codex (no internet, unusable), Cursor+MCP, ScrapeGraphAI API, Firecrawl, Zyte API compared. Zyte uses composite AI architecture (ML models + LLMs).
- building-self-healing-scrapers-with-gpt.md (2025-02): GPT-4o self-healing pipeline implemented. Works on JSON-embedded product data (Mrporter.com). Fails on pure HTML (Balenciaga, Gucci).
- kadoa-review-ai-powered-scraping.md (2026-03): Kadoa platform hands-on. Yahoo Finance test. AI schema detection accurate. 5 proxy locations. Some websites unsupported.

**AI scraping assistants / Cursor+MCP (3 articles)**
- cursor-mcp-web-scraping-assistant.md (2025-03): MCP Python SDK + Camoufox MCP server built. Three-tool pipeline: fetch_page_content, generate_xpaths, write_camoufox_scraper. Claude 3.7 Sonnet used. Gucci.com PLP scraper generated and ran successfully.
- claude-cursor-ai-scraping-assistant.md (2025-04): Full Scrapy coding assistant with Cursor rules. Cookie inspection for anti-bot detection (Kasada→stop, Akamai→scrapy_impersonate, else proceed). Open-source repo released.
- the-lab-84-ai-driven-web-scraping.md (2025-05): Cursor+MCP framed as the best development-time pattern; ScrapeGraphAI API for multi-site horizontal extraction.

**Legal articles (14 articles)**
- is-web-scraping-legal.md (2023-02): Overview of CFAA, copyright, ToS, GDPR; hiQ v. LinkedIn and Craigslist v. 3Taps cited.
- meta-vs-bright-data-court-ruling.md (2024-02): Court dismissed Meta's ToS claims; logged-out scraping of public data not "use" of the platform. CAPTCHA circumvention not ruled on definitively.
- x-vs-bright-data-case-scraping.md (2024-07): X's trespass and fraud claims dismissed. IP rotation not deceptive. ToS breach for scraping preempted by copyright law (X doesn't own user content). Leave to amend granted.
- google-vs-serpapi-web-scraping-case.md (2026-03): Google sued SerpApi under DMCA 1201. SearchGuard deployed Jan 2025. SerpApi motion to dismiss filed Feb 2026. Hearing May 19, 2026.
- google-vs-serpapi-scraping-industry-implications.md (2026-03): Reddit v. SerpApi (Oct 2025) documented. Honeypot test post finding. Ziff Davis v. OpenAI: robots.txt not DMCA protection measure (Dec 2025). DMCA 1201 scraping strategy analysis.
- understanding-robots-txt-implications.md + understanding-robotstxt-and-its-implications.md: robots.txt as voluntary advisory protocol. Legal standing for scraping comes from ToS, not robots.txt. Ziff Davis ruling confirmed.

**Business/economics articles (8 articles)**
- from-0-to-2-billion-prices-scraped.md (2022-08): Re Analytics scaling story. Principles: KISS, standardize, modular processes, two-layer monitoring.
- is-web-scraping-a-profitable-industry.md (2024-10): Business model analysis — alternative data, SaaS monitoring, market intelligence. Scaling constraint: every new customer adds ~20% more websites. Web data as commodity thesis.
- make-money-with-web-scraping.md (2025-04): Freelance platforms (Upwork: 2,600+ open jobs). Data marketplaces: Datarade, AWS Data Exchange, Databoutique (30% fee, $5–$3,000 dataset range). Apify Store: 4,500+ Actors.
- the-state-of-web-scraping-and-ai.md (2023-06): AI as industrializer of scraping. Nimble's AI-powered parsing. Databoutique marketplace concept introduction.
- the-web-data-landscape-map.md (2024-04): Databoutique ecosystem map. Actors: data providers, enablers, users, integrators. Solutions catalog.
- the-lab-15-deep-diving-into-apify.md (2023-03): Apify platform hands-on. CLI, actors, dashboard, Apify Store monetization. Scrapy integration via Python SDK.

Articles skipped (no original technical content):
- ai-and-web-data.md, ai-and-webscraping-lesson-learned.md, ai-powered-web-scrapers-nimble-browser.md, how-ai-is-changing-the-web-scraping.md, llms-ai-web-scraping.md, ai-web-scraping.md, the-state-of-web-scraping-and-ai.md (partially — used for economics section): general overview/intro articles with no direct test findings.
- llm-fine-tuning-for-scraping.md: fine-tuning concept overview, no practical test results from TWSC.
- web-dragon-llm-powered-web-scraping.md, web-scraping-ai-tools-landscape.md: tool landscape overviews without empirical testing.
- writing-a-web-scraper-with-chatgpt.md, create-scraper-with-chatgpt.md: tutorial articles; findings subsumed by other LLM articles.
- build-an-ai-agent-for-scraping-papers.md, building-a-custom-web-scraping-gpt.md, web-scraping-assistant-gpt.md: GPT wrapper tutorials.
- from-rag-to-mcp.md, ingest-web-data-rag-llm.md, querying-web-data-llms.md, why-scraping-return-markdown-llm-ai.md, detect-pattern-scraped-data-with-ai.md, building-knowledge-base-scraping.md, fuel-obsidian-with-llms.md: data pipeline/RAG articles; no scraping-specific technical findings.
- is-it-legal-to-scrape-social-networks.md, web-scraping-legal-context.md, web-scraping-and-ai-2023-legal-wrap-up.md, assessing-legal-compliance-of-web-scraping.md, avoid-copyright-violations-scraping.md, can-i-scrape-any-public-data.md, overview-eu-ai-act.md, indexing-data-in-the-web-robots-file.md: folded into web-scraping-legal-landscape.md.
- selling-web-scraped-data.md, monetize-web-scraping-databoutique.md, the-dirty-little-secret-of-internets.md, the-state-of-public-web-data-in-2024.md, pay-to-crawl-is-it-feasible.md, do-not-scrape-like-ai-companies.md: folded into scraping-economics.md.
- google-vs-ipidea-takedown.md: folded into web-scraping-legal-landscape.md sources.

Pages updated:
- concepts/llm-scraping.md: major update. Added ScrapeGraphAI architecture details, four usage patterns (code generation, self-healing added), per-experiment results for GPT-4o/Llama/Mistral on GitHub, BBC, Mrporter, Balenciaga. OpenAI Codex verdict. Current state section restructured.

Pages created:
- concepts/ai-scraping-assistants.md: New concept. Cursor+MCP+Claude workflow, MCP architecture, three-tool server, Cursor rules, Claude 3.7 Sonnet selection rationale, Gucci.com test result, Scrapy assistant rules.
- entities/scrapegraphai.md: New entity. Pipeline architecture (FetchNode, ParseNode, RAGNode, GenerateAnswerNode, ScriptCreatorGraph), TWSC test results across six experiments, limitations.
- entities/kadoa.md: New entity. Workflow creation steps, AI schema detection, scheduling, error handling, limitations (5 proxy locations, unsupported sites).
- concepts/web-scraping-legal-landscape.md: New concept. CFAA, DMCA 1201, ToS, robots.txt framework. Six key cases documented with findings and current status. Practical rules for scrapers.
- concepts/scraping-economics.md: New concept. Three cost categories, scaling constraints, five business models, data commodity thesis, Databoutique model, Re Analytics operational principles.

Total changes: 1 page updated, 5 pages created. 32 articles skipped (overview/tutorial/hub content).

---

## [2026-04-22] ingest | 37 articles — proxies, web unblockers, scraping infrastructure

Source: batch ingest of 37 TWSC articles covering proxy types and economics, mobile proxy farming, web unblocker benchmarks, scraping infrastructure (compute, scheduling, monitoring), and related topics.

Articles processed:

**Proxy types, economics, and operations (15 articles)**
- differences-residential-mobile-proxies.md (2025-06): Mobile vs residential on 6 criteria; mobile "low" Scamalytics score vs residential "very risky"; CGNAT advantage documented.
- building-mobile-proxy-farm.md (2025-02): USB modem farm architecture overview; hardware options; 3proxy/Squid; localtonet, iproxy, ProxySmart, Proxidize; Italian mobile plan math.
- how-build-mobile-proxy-farm-airproxy.md (2025-09): Airproxy origin story (2018); 2000+ USB modems; custom 10-port USB hubs with per-port power switching; 3proxy + Django + Zabbix; redundant dual-ISP fiber + online UPS + generators.
- mobile-proxy-raspberry.md (2023-01): DIY Raspberry Pi 3 + Waveshare 4G HAT + Squid + SSH reverse tunnel; upgraded to Mini-PC; Italian 500GB plan at $25/mo.
- evaluating-proxy-providers-ips.md (2024-09): Testing methodology (50 req/provider to US+France); ASN tool for IP analysis; provider selling datacenter IPs from ipxo.com as residential.
- how-many-ip-needed-scraping.md (2025-04): Formula: Hourly Volume ÷ Safe Limit × Safety Buffer; 100 quality IPs > thousands of burned ones; Amazon scenarios up to 3,000 IPs.
- costs-web-scraping-proxy.md (2024-01): Stone Island disaster with Nimble; 3rd-party resources consuming 5x target bandwidth; lessons on per-site credentials and Playwright routing.
- optimizing-proxy-costs.md (2024-12): Proxy Ladder concept; Scrapoxy for free DC IPs; pay-per-GB vs pay-per-request guidance.
- proxy-pricing-playbook-september.md (2024-09): September 2024 pricing: DC $0.6/GB; Residential $6-8/GB; ISP $14-15/GB; Mobile $8/GB (was $40); Unblocker $14/GB or $3/1000 req.
- where-do-proxy-companies-take-ip.md (2025-02): SDK-sourced P2P IPs; transparent vs hidden SDK; botnets; router/SIM farming; reseller identification.
- x-forwarded-for-header-proxies.md (2025-09): XFF syntax; transparent vs elite proxy behavior; httpbin.io test method.
- reverse-proxies-and-webscraping.md (2025-07): Forward vs reverse proxy distinction; WAF/CDN as reverse proxies; rate limiting at reverse proxy layer.
- managing-proxy-bans-proxy-retries.md (2025-07): Soft/hard/network-wide ban types; status codes; exponential backoff; retry pattern.
- bypassing-geo-fencing-scraping.md (2024-03): IP-based geolocation; EU Geo-blocking Regulation 2018/302; WebRTC leak via Browserleaks; Cettire/Algolia bypass.
- scraping-using-tor.md (2025-05): Tor as SOCKS5 on port 9050; 50-instance trick; exit IPs publicly listed = blocked by most anti-bots.

**Infrastructure and cost (8 articles)**
- the-costs-of-web-scraping.md (2022-09): AWS vs Azure vs GCP VM pricing; storage cost math (500K pages × 200KB × 30 days = 750GB/mo).
- optimizing-costs-for-web-scraping.md (2025-03): Lambda vs Fargate vs VMs vs bare metal; Hetzner as cost leader; 15-20% of e-commerce has bot protection.
- scraping-aws-lambda-serverless.md (2024-04): Lambda Selenium scraper via docker-selenium-lambda; 15-min max execution limit; rotating AWS datacenter IPs; Clarks.com tested.
- running-scrapers-on-github-actions.md (2025-01): GitHub Actions YAML workflow; 6-hour limit workaround via parameterized executions; datacenter IPs from GitHub runners.
- scheduling-scrapers-airflow.md (2024-11): Apache Airflow DAG for Scrapy; TriggerDagRunOperator for multi-DAG pipelines; email failure notifications; S3 upload step.
- scrapyd-manage-schedule-scrapers.md (2022-10): Scrapyd setup on port 6800; deploy via scrapyd-deploy; schedule via API; Scrapeops as UI + scheduler layer on top.
- scrapeops-managing-scrapers-execution.md (2023-03): Scrapeops dashboard for Scrapy and requests scrapers; fake browser headers API; Playwright/Selenium not yet supported.
- scrapoxy-proxy-aggregator.md (2024-02): Scrapoxy architecture; Scrapy integration; 3 project types (DC/residential/mobile); ~20% cost savings vs pure AWS.

**Web unblockers (9 articles)**
- web-unblocker-benchmark-march-2024.md (2024-03): 5 unblockers × 4 targets; Cloudflare all pass; DataDome only Zenrows partially; Kasada: BD/Oxylabs/Smartproxy pass; PX all pass.
- the-web-unblocker-cost-benchmark.md (2023-12): Zalando (31GB/30K req) vs Zara (1.6GB/44K req) pricing model comparison; Zyte weighted avg $1.974/1000 req.
- web-unblocker-test-kasada.md (2024-06): 101 URLs canadagoose.com; BD 96% $0.303; NetNut 97%; Oxylabs 96% $0.10; Smartproxy 92% $0.13; Zenrows 95% $0.70; Infatica/Zyte failed.
- web-unblocker-vs-browser-as-a-service-scraping.md (2025-04): 13 unblockers listed; 8 BaaS platforms listed; distinction documented.
- testing-smartproxy-site-unblocker.md (2023-07): 80/100; Kasada 0%; $12/GB.
- oxylabs-web-unblocker-test.md (2023-08): 96/100; all antibots passed; $15/GB; X-Oxylabs-Render header.
- hands-on-2-testing-the-new-zyte-api.md (2023-04): 100/100 with rendering; 81/100 raw; scrapy-zyte-api integration.
- hands-on-6-testing-the-infatica-web.md (2023-10): 80/100; Kasada fails; $1/1000 req; POST endpoint model.

**LLM-adjacent / AI tools (3 articles)**
- anycrawl-llm-ready-web-scraping.md: AnyCrawl overview; /v1/scrape, /v1/search, /v1/crawl; Cheerio/Playwright/Puppeteer engines; JSON extraction mode; MCP server.
- anycrawl-testing-the-llm-ready-web.md (2026-01): MIT-licensed, 2.5K stars; no custom headers/cookies; no anti-bot; not comparable to unblockers.
- when-browsers-think-chatgpt-atlas-cursor-browserbase.md (2025-11): ChatGPT Atlas (Chromium+ChatGPT); Browserbase Stagehand V3 (LLM→Playwright); Cursor network inspection for API discovery.

**Benchmark (1 article)**
- nike-scraping-benchmark.md (2026): 1000 Nike product URLs; Rnet 100% 530s; undetected-httpx 100% 458s; Scrapling Fetcher 100% ~510s; Pydoll 100% 12781s; Camoufox 75.4% 6794s. HTTP clients 27x faster than browsers. Akamai bypassed with TLS impersonation only. No JS challenges on Nike product pages.

Articles skipped:
- proxy-vendor-benchmark.md (2022-10): Just a spreadsheet announcement with minimal technical content; no findings worth extracting.
- the-true-costs-of-a-web-scraping.md (2023-11): Cost framework article; content incorporated into scraping-infrastructure concept page.

Pages updated:
- concepts/proxy-fundamentals.md: Major update with 14 additional sources. Added: CGNAT/mobile advantage, X-Forwarded-For header, forward vs reverse proxy distinction, Tor limitations, ban management, Proxy Ladder framework, September 2024 pricing, IP pool quality testing, Stone Island cost lesson, IP volume vs quality formula.
- entities/akamai.md: Added Nike.com finding (Akamai on catalog only; TLS impersonation sufficient; no JS challenges).
- entities/scrapling.md: Added Nike benchmark result (Fetcher class 100% on Akamai with TLS only).
- concepts/llm-scraping.md: Added AI browsers section (ChatGPT Atlas, Browserbase Stagehand, Cursor network inspection), AnyCrawl reference. Updated sources list.

Pages created:
- concepts/mobile-proxy-farming.md: New concept. DIY hardware options, Airproxy at scale, cost economics, mobile vs residential comparison.
- concepts/web-unblockers.md: New concept. Definition vs proxies vs BaaS, benchmark results (2023-2024), per-provider scores, pricing model comparison.
- concepts/scraping-infrastructure.md: New concept. All four compute types, four scheduling tools, fleet monitoring, cost comparisons (AWS vs Hetzner), Lambda and GitHub Actions test results.
- entities/scrapoxy.md: New entity. Architecture, three project types, Scrapy integration, cost comparison.
- entities/zyte-api.md: New entity. Two modes (raw/rendering), Kasada failure documented across two tests, per-request pricing.
- entities/oxylabs-unblocker.md: New entity. 96/100, Kasada cheapest ($0.10/101 URLs), best dashboard.
- entities/smartproxy-unblocker.md: New entity. 80/100, Kasada evolution (0% 2023 → 92% 2024), $12/GB.
- entities/anycrawl.md: New entity. JSON extraction mode, MCP server, limitations (no anti-bot, no custom headers).

Total changes: 4 pages updated, 8 pages created. 2 articles skipped (hub/minimal content).


---

## [2026-04-22] ingest | 34 articles — anti-detect browsers, Camoufox deployment, browser protocols, mouse movement, Botasaurus

Source: batch ingest of 34 TWSC articles covering anti-detect browser benchmarks, Docker/AWS Camoufox deployment, browser automation protocols (WebDriver/CDP/BiDi), mouse movement emulation, Botasaurus, Nodriver, Rayobrowse, and browser fingerprinting research.

Articles processed with findings:

**Anti-detect browser benchmarks (4 articles)**
- anti-detect-browsers-fingerprint-tests.md (2024): 8-browser CreepJS/BrowserScan benchmark. GoLogin 223/260, NSTBrowser 218/260, Undetectable.io 209/260, MultiLogin 203/260, MoreLogin 198/260, Kameleo 175/260*, Octo Browser 164/260, Incogniton 139/260. Real Mac baseline 226/260. *Kameleo WebRTC was tester configuration error.
- anti-detect-browser-royal-rumble-comments.md: MultiLogin clarification (Stealthfox/Firefox engine).
- kameleo-anti-detect-browser.md: Junglefox + Chroma engines; macOS support added May 2024; START €29/mo, SCALE €279/mo.
- dolphin-anty-product-review.md: 20+ fingerprint parameters; Scenarios builder; Profile Synchronizer; REST API only; free tier 10 profiles.

**Camoufox Docker and AWS (3 articles)**
- camoufox-server-docker.md + how-to-create-camoufox-docker-image.md: Ubuntu 22.04 base; port 59001; FastAPI/Uvicorn/websockets/Xvfb; BrowserScan passes from Docker.
- camoufox-server-in-aws.md: ECR + EC2 ASG + NLB (not ALB); NLB required for TCP WebSocket pass-through at port 59001.

**Browser automation protocols (1 article)**
- webdriver-vs-cdp-vs-bidi.md: Three protocols documented. Firefox dropping CDP in Nightly 141 for WebDriver BiDi.

**Mouse movement emulation (2 articles)**
- oxymouse-and-playwright-mouse-movements.md: OxyMouse; Gaussian and Perlin noise algorithms; all three methods pass DataDome.
- bezier-curves-web-scraping.md: Bezier curve math; Fitts's Law speed model.

**Botasaurus (2 articles)**
- botasaurus-web-scraping-framework.md + testing-the-new-botasaurus-4.md: @browser/@request/@task decorators; passes locally, fails from server (SwiftShader + zero media devices).

**Browser fingerprinting research (2 articles)**
- browser-fingerprinting-test-online.md: CreepJS and BrowserScan tool descriptions. BrowserScan CDP detection test.
- the-latest-papers-about-browser-fingerpinting.md: Academic findings. WebGPU-SPY 90% GPU cache timing attack. Picasso/DataDome canvas technique.

**Playwright additions (5 articles)**
- playwright-tips-tricks-scraping.md: BrowserContext vs Persistent Context; connect_over_cdp.
- advanced-logging-in-playwright.md: psutil + RabbitMQ + S3/boto3 logging stack.
- how-to-start-with-scrapy-and-playwright.md: Anti-bot routing heuristic documented.
- playwright-scrapers-undetected.md: Patchright named; stealth launch args.
- 5-features-playwright-web-scraping.md: slow_mo; network interception; iFrame/device/geo emulation.

**Rayobrowse (2 articles)**
- rayobrowse-browser-scraping.md: C++ patching; real device fingerprint DB; CDP compatible; 100% benchmark; beta 2026.
- two-stealth-browsers-proxy-prices.md: Brief mentions of Rayobrowse and Owl Browser.

**Other (4 articles)**
- open-source-python-libraries-scraping.md: Nodriver as UC successor; Zendriver as active fork.
- three-web-scraping-tools-just-discovered.md: curl_cffi first TWSC mention 2023-10-08.
- antidetect-browser-webscraping.md: 2022 GoLogin early reference.
- browser-automation-landscape-2025.md + anti-detect-pricing-comparison.md: Pricing data folded into anti-detect-browsers.md.

Articles skipped (no unique empirical findings):
- the-journey-from-traditional-browsers.md (Nimble vendor guest post)
- rethinking-the-web-browser.md (Lightpanda guest post)
- which-web-scraping-tool-is-best.md (beginner course)
- browser-api-an-introduction.md (general API overview)
- the-2025-web-scraping-tech-stack.md (stack overview)
- playwright-vs-selenium.md (high-level comparison)

Pages created:
- entities/kameleo.md
- entities/gologin.md
- entities/dolphin-anty.md
- entities/botasaurus.md
- entities/rayobrowse.md
- concepts/webdriver-vs-cdp-vs-bidi.md
- concepts/mouse-movement-emulation.md
- comparisons/anti-detect-browser-benchmark-2024.md

Pages updated:
- entities/camoufox.md: Docker/AWS deployment section added; Ubuntu 22.04 requirement; NLB vs ALB distinction; 3 new sources.
- entities/playwright.md: BrowserContext vs Persistent Context; CDP remote connection; stealth launch args; Scrapy routing heuristic; logging patterns; 5 new sources.
- entities/ghost-cursor.md: OxyMouse as alternative (Gaussian + Perlin); anti-bot mouse tracking observations; 2 new sources.
- entities/nodriver.md: 1 additional source.
- entities/curl-cffi.md: first_seen corrected to 2023-10-08; three-web-scraping-tools source added.
- concepts/browser-fingerprinting.md: CreepJS/BrowserScan tool descriptions; Picasso/DataDome; academic research summary; WebGPU-SPY; benchmark reference; 4 new sources.
- concepts/cdp-detection.md: Patchright named explicitly; WebDriver BiDi context; Firefox CDP removal in Nightly 141; 2 new sources.
- concepts/anti-detect-browsers.md: Benchmark results table; pricing reference; 10 new sources.
- index.md: 8 new entities, 3 new concepts, 1 new comparison added; updated descriptions.

Total changes: 8 pages created, 9 pages updated. 6 articles skipped.

---

## [2026-04-22] ingest | Final batch — API patterns, inventory, location, real-time, platform techniques

Source: 27 remaining TWSC articles covering API discovery methodology, inventory tracking, location-based scraping, WebSocket/real-time data collection, and high-frequency API performance.

Articles processed with generalizable findings:

**API discovery (3 articles)**
- the-lab-26-from-internal-api-to-insights.md (2023-08): Internal API discovery via XHR filter. Triggering pagination exposes calls not visible on first load. Autoscout24 20-page cap. HTML can contain more data than the API.
- scraping-linkedin-public-data.md (2025-06): LinkedIn Jobs API `https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search`. Login wall triggered by `trk=` query parameter on direct URL but not on navbar link. Wayback Machine technique for endpoints removed from current page interaction.
- scraping-food-delivery-apps.md (2025-04): Glovo geo-targeting via request headers. Mobile app version differs from web; same menu/contact endpoints shared. `glovo-request-id` can be forged as random hex; `glovo-dynamic-session-id` stays constant per device session.

**Location data (2 articles)**
- the-lab-31-scraping-location-data.md (2023-11): Radius and bounding-box API patterns. Earth-radius-corrected grid algorithm. 100km outer grid → ~10,000 world squares. Google Places API for pruning. Recursive subdivision. Grid is reusable across projects.
- the-lab-28-deep-dive-on-inventory.md (2023-09): Playwright geolocation injection (`context.set_geolocation()`) to select a store on IP-localized sites. Page reload required after pagination on some sites to refresh stale embedded JSON.

**Inventory tracking (3 articles)**
- scraping-inventory-level.md (2023-09): Lululemon `/api/inventory` and `/api/stores` endpoints documented. Revenue estimation via depletion rate.
- scraping-inventory-data.md (2024-02): Four inventory data locations: product list (rare), PDP (common), click-and-collect (store-level), add-to-cart (last resort).
- scraping-inventory-levels.md (2024-08): Stone Island 4-warehouse regional structure. Sum of store inventories = e-commerce total. Double-counting risk across countries. Inventory granularity spectrum.

**Real-time / WebSocket (1 article)**
- scraping-real-time-data-bitstamp.md (2024-04): `websocket-python` callback pattern. Bitstamp JSON subscriptions. Sofascore uses NATS protocol. PING/PONG keepalive required for NATS.

**High-frequency API performance (2 articles)**
- how-fast-can-you-call-polymarket-apis.md and how-to-get-data-from-polymarket-fast.md (2026-04): Polymarket three-API architecture (Gamma, CLOB, Data). HTTP/1.1 pooled (50 connections, aiohttp) beats HTTP/2 multiplexing 6.7x. Server co-location in eu-west-2 (London) provides 6x throughput vs us-east-1. Connection pre-warming reduces p99 from 111ms to 32ms. Optimization priority: location > connection strategy > I/O model > language.

**Platform-specific (generalizable findings only)**
- scraping-booking-playwright.md (2025-08): Prices hidden in headless mode, visible in headful. `data-testid` attributes as stable selectors.
- scraping-flight-data.md (2025-02): Fill rate estimation via maximum-tickets-bookable method. Booking.com low-seat alert at ≤9 remaining.
- how-we-scraped-global-hotel-data.md (2024-12): APR as ADR proxy. Total stock via incremental room-count queries. Tetris Rule. Next Day Published Rate. Top 1,000 cities scope. 9AM local time standardization.

Articles skipped:
- scraping-booking-using-apiss.md, how-to-scrape-booking-and-airbnb.md, the-lab-5-scraping-airbnbcom-using.md, scraping-nike-with-open-source.md, scraping-depop-cost-effective.md, how-to-scrape-vinted.md, tik-tok-scraping-how-to-do-it-properly.md (sponsored), scraping-telegram-channels.md, ikea-scraping-kallax.md (findings folded into inventory-tracking.md), scraping-zillow-real-estate-data.md, scraping-opensea-bored-ape-nft.md, how-to-scrape-reddit-with-scrapy.md, scraping-the-dark-web-playwright.md: target-specific or no unique generalizable findings.

Pages updated:
- concepts/api-scraping.md: LinkedIn Wayback Machine technique; geo-targeted API headers section; 3 new sources.
- concepts/http-performance.md: HTTP/1.1 vs HTTP/2 concurrency finding (6.7x gap); connection pre-warming; server co-location impact; 3 new sources.
- entities/curl-cffi.md: HTTP/3 support section; HTTP caching/ETags note; Polymarket HTTP/1.1 pooled vs HTTP/2 finding; Polymarket source added.

Pages created:
- concepts/websocket-scraping.md: WebSocket mechanics, JSON vs NATS protocols, Bitstamp/Sofascore/Polymarket cases.
- concepts/location-data-scraping.md: Radius and bounding-box patterns, Earth-radius-corrected grid algorithm, Glovo geo-headers, Playwright geolocation injection.
- concepts/inventory-tracking.md: Five data location patterns, revenue estimation, warehouse vs store interpretation, Stone Island/Lululemon/On/Burberry/Farfetch cases.
- entities/hrequests.md: (documented in batch 3) TLS-fingerprinted HTTP + headless browser; 5-anti-bot benchmark.
- entities/algolia.md: (documented in batch 3) Three URL parameters, two payload formats, EndClothing and Michelin Guide.

Total changes: 3 pages updated, 5 pages created. 13 articles skipped (target-specific or sponsored).

---

## [2026-04-22] ingest | 33 news articles — reverse proxy concurrency, adversarial proxy use, landing pages

Source: batch ingest of 33 scraped news/product articles.

Articles with real technical content (3 of 33):

- `en-tech-dumb-vibe-coders.md` (harshanu.space, 2026-03-01): Technical analysis of India's ISP DNS poisoning block on `*.supabase.co` and the security risks of routing production traffic through third-party reverse proxies (JioBase/Cloudflare Workers). TLS termination mechanics, JWT exposure, analytics metadata logging, open-source deployment trust problem documented.
- `2026-02-starkiller-phishing-service-proxies-real-login-pages-mfa.md` (krebsonsecurity.com, 2026-02-20): Krebs/Abnormal AI analysis of Starkiller phishing-as-a-service. Uses Docker + headless Chrome as real-time man-in-the-middle reverse proxy against real login pages. `@` sign URL trick, MFA bypass via token relay, session cookie capture, real-time screen streaming.
- `2026-03-09-concurrent-requests-reverse-proxyhtml.md` (singh-sanjay.com, 2026-03-09): Technical deep-dive on ATS/HAProxy/Envoy concurrency models. Thread-per-connection vs event loop distinction, epoll/kqueue, per-connection memory arithmetic, graceful restart, circuit breaking. ATS continuation system, HAProxy `SO_REUSEPORT` + spinlocks, Envoy worker isolation + xDS.

Pages updated:
- `concepts/proxy-fundamentals.md`: Added two new subsections — "Third-Party Reverse Proxy Trust Model (2026-03)" and "Adversarial Reverse Proxy: Starkiller Phishing Kit (2026-02)". Two new sources added.
- `concepts/http-performance.md`: Added "Reverse Proxy Concurrency Models (ATS, HAProxy, Envoy)" subsection. One new source added.

Articles skipped (30 of 33) — all landing pages, product pages, or content with no verifiable technical claims:
browserbeam-com, crawl4ai-dev, detail-blueprint-mcp-for-chrome, en-blog-why-llms-hate-fake-data-token-proxy, getstack-run, getwick-dev, gist-1mb-dev, gitdelivr-net, go-llm-proxy-com, humaverify-com, lobsterhelper-com, lucidextractor-liceron-in, mcpsaas-co-uk, meshscrape-com, pinboard-download-vercel-app, promptguard-co, proxy.md (Senthex product), r-emacs-comments (Reddit nav), tokensurf-io, try.md (interview tool), vpn-or-proxy-which-is-safer (affiliate/VPN comparison), www-context-dev, www-devutilityhub-me, www-meter-sh, www-openlegion-ai, www-skyblobs-com, www-toqen-app, www-yourfinanceworks-com, blog-7-essential-use-cases-for-web-scraping (generic marketing), blog-why-your-ai-agent-needs-a-proxy (ProxyBase marketing).

Total changes: 2 pages updated, 0 pages created. 30 articles skipped.

---

## [2026-04-22] ingest | 33 news articles + 4 GitHub repos — adversarial mouse detection, DNS leaks, IPIDEA takedown, tarpits, legal cases, browser extension detection, keystroke dynamics, iOS 26 WebPage API, split-DNS bypass, 1B-page crawl benchmark

Source: second news batch ingest, 33 scraped news/product articles + 4 GitHub repository pages.

Articles with real technical content processed:

**Akamai mouse movement (MACT) detection**
- mimic.sbs reverse-engineering article (2024): MACT algorithm reverse-engineered from leaked source. Piecewise-constant velocity + EWMA smoothing (λ=0.955). Two-year bypass window for undetected behavior generators. Detection via velocity segment-constancy testing and gradient boosting classifier.

**DNS/ASN consistency as detection signal**
- voidmob.com DNS leak article: ASN consistency check between IP and DNS resolver. Active DNS probing via unique subdomains embedded in page resources. Architecture comparison across four provider types. `socks5h` vs `socks5` critical distinction.
- free-VPNs article: supplementary residential proxy material.

**IPIDEA botnet takedown**
- Google TIG / IPIDEA documentation (2026-01): 9M Android devices enrolled as residential proxies via SDK. 550+ threat groups using the network. Google TIG disruption documented. Proxidize banned from promotional link.

**Scraping economics additions**
- ScrapeOps scraping-shock article: anti-bot cost escalation staircase. E-commerce (DC proxies): 9/10 → 4/10; Social: 4/5 → 0/5; Travel: 8/10 → 3/10; Real Estate: 10/10 → 3/10. Four tiers: open → low-cost proxies → residential → browser automation/unblocker.
- foura.ai tarpits article: Nepenthes/Locaine as AI crawler traps. 60% of analyzed sites actively blocking AI crawlers by May 2025. Rutgers: 23.1% traffic decline. Wharton: 13.9% organic traffic decline. Tarpit content bleeds into real scrapers due to poor bot discrimination.

**Legal cases**
- TWSC Google v. SerpApi article + companion article: DMCA 1201 theory. SearchGuard deployed Jan 2025. 25,000% increase claim in searches. No cease-and-desist prior to lawsuit. SerpApi direct quote documented. Reddit v. SerpApi: honeypot test post evidence. 1.8B SERPs accessed over 2 weeks. Forty-fold citation increase after C&D.

**Browser extension detection**
- castle.io blog post (2026-01-14): LinkedIn direct resource probing via `chrome-extension://<id>/<path>`. web_accessible_resources exploitation. Grammarly extension ID `kbfnbcaeplbcioakkpcpgfkobkghlhen` example. Castle side-effect detection (DOM mutations, JS globals) as alternative approach.

**FPScanner self-hosted bot detection**
- github.com/antoinevastel/fpscanner (2026-02-21): Anti-replay protection (timestamp+nonce), build-time key injection, optional obfuscation, consistency-over-breadth philosophy. Castle-sponsored.

**Keystroke dynamics: isHumanCadence**
- github.com/RoloBits/isHumanCadence (2026-02-09): 6-signal scoring (dwell variance, flight fit, timing entropy, correction ratio, burst regularity, rollover rate). Aalto 136M keystrokes dataset (Dhakal et al., CHI 2018). Correction ratio asymmetry documented. Zero GC, requestIdleCallback, KS statistical test.

**iOS 26 / macOS 26 WebPage API**
- folding-sky.com article: SwiftUI WebKit `WebPage` class for on-device headless browser. Uses real Safari engine and device residential IP. `#available(iOS 26.0, macOS 26.0, *)`. `socks5h://` proxy syntax. Cumbersome app `openWebPageLocally` tool demonstrated.

**Cloudflare split-DNS origin IP exposure**
- medium.com/@smitgharat0001 article (2025-11-04): Apex domain vs www split-DNS misconfiguration. curl `--resolve` bypass technique. ~40,000 target scan. Origin exposure bypasses all Cloudflare WAF rules, rate limiting, bot detection. Mitigation: orange cloud on all subdomains or IP whitelist at origin.

**Billion-page crawl benchmark**
- andrewkchan.dev/posts/crawler.html: 1.005B pages crawled, 25.5 hours, $462. ~12 independent nodes with Redis per-domain frontiers. HTML-only, robots.txt compliance, 70-second domain delay. Parsing identified as biggest bottleneck; NVMe SSDs critical. Decentralized cluster eliminates coordination overhead.

**AI browser tools**
- github.com/vercel-labs/agent-browser (14.7k stars, Apache-2.0): headless browser CLI for AI agents.
- github.com/vifreefly/kimuraframework: Ruby scraping framework with LLM-assisted DSL. Caches discovered selectors after initial LLM pass.

Articles skipped (all landing pages, product pages, or no verifiable claims):
All remaining 15+ news articles were marketing landing pages or product-only pages with no testable technical claims.

Pages updated:
- concepts/mouse-movement-emulation.md: Added "Defender's Perspective: Akamai MACT Detection (2024)" section. 1 new source.
- entities/akamai.md: Added "Mouse Movement (MACT) Detection Mechanics" section. 1 new source.
- concepts/proxy-fundamentals.md: Added "DNS Leak as a Detection Signal" section (provider architecture comparison table, `socks5h` distinction, CLI test method). Added "IPIDEA Takedown (January 2026)" section. 2 new sources.
- concepts/scraping-economics.md: Added "Scraping Shock: The Anti-Bot Escalation Curve" section (4-tier staircase, success rate table). Added "Tarpits: AI Crawler Collateral Damage" section (Nepenthes/Locaine, Rutgers 23.1% / Wharton 13.9% findings). 2 new sources.
- concepts/web-scraping-legal-landscape.md: Enhanced Google v. SerpApi entry (25,000% increase, no C&D, direct quote, SearchGuard). Enhanced Reddit v. SerpApi entry (1.8B SERP figure, honeypot post, forty-fold citation jump, motion to dismiss). 1 new source.
- concepts/browser-fingerprinting.md: Added "Browser Extension Detection" section (LinkedIn probing, web_accessible_resources, Grammarly example, Castle side-effect approach). Added "FPScanner" section (anti-replay, build-time key injection, consistency focus). 2 new sources.
- concepts/ml-bot-detection.md: Added "Keystroke Dynamics: isHumanCadence" section (6-signal table, Aalto dataset, correction ratio finding, implementation details). 1 new source.
- concepts/llm-scraping.md: Added "Additional AI Browser Tools (2026)" section (Vercel agent-browser, iOS 26 WebPage API, Kimurai). 3 new sources.
- entities/cloudflare.md: Added "Origin Server IP Exposure via Split-DNS (2025-11)" section (apex vs www misconfiguration, curl bypass, mitigation). 1 new source.
- concepts/scraping-infrastructure.md: Added "Billion-Page Crawl Benchmark (2025)" section (1.005B pages, $462, 25.5 hours, Redis per-domain frontiers, parsing bottleneck). 1 new source.

Total changes: 10 pages updated, 0 pages created.

## [2026-05-06] schema-update | Add canvases and views as first-class wiki types

Operation: schema and infrastructure update.
Changes:
- `wiki/schema.md`: added `canvases/` and `views/` to the directory layout; documented two new page types (`Canvas pages` for JSON Canvas visual maps, `View pages` for Obsidian Bases queries).
- `wiki/canvases/`: new directory; first canvas `agentic-browsers-landscape-2026.canvas` mapping the agentic-browser landscape from the lab-datadome-2026-leroymerlin article (32 nodes, 6 edges, 4 group clusters).
- `wiki/views/`: new directory; four starter Obsidian Bases queries (`all-entities`, `anti-bot-vendors`, `recently-touched`, `tools-and-browsers`).
- `skills/wiki-ingest/SKILL.md`: now delegates page writes to the `obsidian-markdown` skill and preprocesses URL sources through `defuddle`.
- `skills/wiki-lint/SKILL.md`: structural audit now runs through `obsidian-cli`; canvas wikilinks and `.base` view properties added to lint coverage.
- `skills/the-lab-article-reviewer/SKILL.md` (step 10): fact-check step now prefers `defuddle` over `WebFetch` for long-form vendor pages.

These changes integrate the kepano/obsidian-skills bundle (defuddle, obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli) into the existing TWSC writing and ingestion workflow.

## [2026-05-06] create | Pass 2 batch ingest from GitHub news

Created 16 new entity pages from RELEVANT GitHub news classified by Qwen2.5-7B on llama.cpp/DGX:

- fingerprinterjs (tool) — FingerprinterJS
- iherb-cli (tool) — iherb-cli
- fpscanner (library) — FPScanner
- chaser-oxide (tool) — chaser-oxide
- proxelar (tool) — proxelar
- obscura (tool) — Obscura
- masterhttprelayvpn (tool) — MasterHttpRelayVPN
- transparenttorproxy (tool) — TransparentTorProxy
- wxpath (library) — wxpath
- libretto (tool) — Libretto
- goscrapy (library) — GoScrapy
- feedstock (tool) — Feedstock
- crawl4ai (tool) — Crawl4AI
- reader (tool) — Reader
- proxy-server (tool) — Proxy Server
- kimurai (tool) — Kimurai

Skipped (entity page already exists): scrapling


## [2026-05-07] update | Pass 3 source linking

Created 20 new entity pages from orphan RELEVANT news:
- is-antibot (library) — is-antibot
- blanktrace (proxy-provider) — BlankTrace
- ipidea (proxy-provider) — IPIDEA
- clashmac (proxy-provider) — ClashMac
- ricci-flow-ai-web-scraper (tool) — Ricci Flow – AI Web Scraper
- wick (tool) — Wick
- kampala (proxy-provider) — Kampala
- konform-browser (browser) — Konform Browser
- lightpanda (browser) — Lightpanda
- lucidextractor (tool) — LucidExtractor
- meshscrape (proxy-provider) — MeshScrape
- owl-browser (tool) — Owl Browser
- nyxproxy (proxy-provider) — NyxProxy
- browser-use (tool) — Browser Use
- scrapingduck (tool) — ScrapingDuck
- scrapingsandbox (tool) — ScrapingSandbox
- spidersuite (tool) — SpiderSuite
- spidra (tool) — Spidra
- tadpole (tool) — Tadpole
- obscrd (tool) — obscrd

Appended 37 sources to existing wiki pages:
- concepts/ai-scraping-assistants.md: 3 new sources
- concepts/anti-detect-browsers.md: 6 new sources
- concepts/api-scraping.md: 1 new source
- concepts/browser-fingerprinting.md: 3 new sources
- concepts/http-performance.md: 2 new sources
- concepts/inventory-tracking.md: 2 new sources
- concepts/llm-scraping.md: 3 new sources
- concepts/proxy-fundamentals.md: 11 new sources
- concepts/tls-fingerprinting.md: 1 new source
- concepts/web-scraping-legal-landscape.md: 2 new sources
- entities/kasada.md: 1 new source
- entities/reader.md: 1 new source
- entities/scrapling.md: 1 new source


## [2026-05-07] update | Pass 3 source linking

Created 9 new entity pages from orphan RELEVANT news:
- aiohttp (library) — AIOHTTP
- device-and-browser-info (tool) — Device and Browser Info
- google-analytics-4 (tool) — Google Analytics 4
- puppeteer (tool) — Puppeteer
- canvas-fingerprint-defender (tool) — Canvas fingerprint defender
- python-requests (library) — python-requests
- downloadlistphonenumbers-js (tool) — downloadListPhoneNumbers.js
- open-bullet-2 (tool) — Open Bullet 2
- simple-selenium-chrome-crawler (tool) — Simple Selenium Chrome Crawler

Appended 16 sources to existing wiki pages:
- concepts/anti-detect-browsers.md: 3 new sources
- concepts/browser-fingerprinting.md: 3 new sources
- concepts/proxy-fundamentals.md: 4 new sources
- concepts/webdriver-vs-cdp-vs-bidi.md: 3 new sources
- entities/device-and-browser-info.md: 2 new sources
- entities/ipidea.md: 1 new source


## [2026-05-07] update | Pass 3 source linking

Created 9 new entity pages from orphan RELEVANT news:
- nodejs-based-scraper (tool) — NodeJS-based scraper
- uaparser-js (library) — UAParser.js
- selenium-headless-chrome-detection (anti-bot) — Selenium/Headless Chrome Detection
- facebookexternalhit (tool) — facebookexternalhit
- go-http-client (library) — Go HTTP Client
- linkedinbot (tool) — LinkedInBot
- firehol (proxy-provider) — FireHOL
- cheerio (library) — Cheerio
- sec-ch-ua-form-factors (anti-bot) — Sec-CH-UA-Form-Factors

Appended 28 sources to existing wiki pages:
- concepts/api-scraping.md: 1 new source
- concepts/bot-detection.md: 4 new sources
- concepts/browser-fingerprinting.md: 11 new sources
- concepts/cdp-detection.md: 2 new sources
- concepts/proxy-fundamentals.md: 2 new sources
- concepts/tls-fingerprinting.md: 1 new source
- entities/open-bullet-2.md: 2 new sources
- entities/puppeteer.md: 5 new sources


## [2026-05-10] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- resurf (tool) — Resurf
- mochi-js (library) — mochi.js

Appended 4 sources to existing wiki pages:
- concepts/bot-detection.md: 1 new source
- concepts/browser-fingerprinting.md: 1 new source
- concepts/proxy-fundamentals.md: 1 new source
- concepts/webdriver-vs-cdp-vs-bidi.md: 1 new source


## [2026-05-12] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- groxy (library) — Groxy

Appended 1 sources to existing wiki pages:
- concepts/scraping-infrastructure.md: 1 new source


## [2026-05-13] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- roxy (tool) — Roxy
- mitmproxy (tool) — mitmproxy

Appended 2 sources to existing wiki pages:
- concepts/proxy-fundamentals.md: 1 new source
- concepts/scraping-infrastructure.md: 1 new source


## [2026-05-14] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- hysteria (proxy-provider) — Hysteria

Appended 1 sources to existing wiki pages:
- concepts/proxy-fundamentals.md: 1 new source


## [2026-05-17] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- hodor (tool) — Hodor

Appended 1 sources to existing wiki pages:
- concepts/proxy-fundamentals.md: 1 new source


## [2026-05-18] update | Pass 3 source linking

Appended 2 sources to existing wiki pages:
- concepts/bot-detection.md: 2 new sources


## [2026-05-19] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- llmcap (tool) — LLMCap

Appended 1 sources to existing wiki pages:
- concepts/proxy-fundamentals.md: 1 new source


## [2026-05-20] update | Pass 3 source linking

Created 4 new entity pages from orphan RELEVANT news:
- childflow (tool) — childflow
- invisible-playwright (browser) — invisible_playwright
- webassembly-simd (library) — WebAssembly SIMD
- browserbase-chrome (browser) — Browserbase Chrome

Appended 4 sources to existing wiki pages:
- concepts/ai-scraping-assistants.md: 1 new source
- concepts/browser-fingerprinting.md: 2 new sources
- concepts/proxy-fundamentals.md: 1 new source


## [2026-05-23] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- momoproxy (proxy-provider) — MoMoProxy

Appended 1 sources to existing wiki pages:
- concepts/scraping-infrastructure.md: 1 new source


## [2026-05-24] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- beautiful-code-screenshots-codeshot (tool) — Beautiful Code Screenshots (CodeShot)
- scrapy (library) — Scrapy

Appended 2 sources to existing wiki pages:
- concepts/llm-scraping.md: 1 new source
- concepts/scraping-economics.md: 1 new source


## [2026-05-26] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- ncro (proxy-provider) — ncro
- sensecollect (tool) — SenseCollect

Appended 2 sources to existing wiki pages:
- concepts/scraping-infrastructure.md: 1 new source
- concepts/web-unblockers.md: 1 new source


## [2026-05-29] update | Pass 3 source linking

Created 5 new entity pages from orphan RELEVANT news:
- squid (proxy-provider) — Squid
- cloudflare-bot-management (anti-bot) — Cloudflare Bot Management
- ag2b (tool) — AG2B
- atproxy (proxy-provider) — atproxy
- pangolin (proxy-provider) — Pangolin

Appended 6 sources to existing wiki pages:
- concepts/ai-scraping-assistants.md: 1 new source
- concepts/bot-detection.md: 1 new source
- concepts/mobile-app-scraping.md: 1 new source
- concepts/proxy-fundamentals.md: 3 new sources


## [2026-05-31] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- clashmax (tool) — ClashMax
- ai-agent-reader-page (anti-bot) — AI Agent Reader Page

Appended 2 sources to existing wiki pages:
- concepts/bot-detection.md: 1 new source
- concepts/proxy-fundamentals.md: 1 new source


## [2026-06-02] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- lte-modems (proxy-provider) — LTE Modems

Appended 1 sources to existing wiki pages:
- concepts/mobile-proxy-farming.md: 1 new source


## [2026-06-04] create | canvas-fingerprinting concept page

Created concept page from the WWW'25 Pixel-Recovery paper research and our 2026 Camoufox fork analysis (in-progress Lab article, code under code/camoufox_fork_analysis/).

Pages created:
- concepts/canvas-fingerprinting.md: New concept. Explains the canvas element and readback APIs, flat vs edge regions, the four defense families, the Pixel-Recovery attack (Nguyen and Vadrevu, WWW '25) against position-seeded uniform noise, why Brave Farbling resists (content-dependent per-session noise), content-aware noise as the counter (LeooNic Camoufox patch), and our PropertyTracer observation of Datadome reading toDataURL/getImageData on leboncoin plus the official Camoufox noise behavior (9105/18240 flat pixels perturbed when seeded; noise off by default).

Pages updated (backlinks + last_updated):
- concepts/browser-fingerprinting.md: added canvas-fingerprinting to Related.
- entities/camoufox.md: added Canvas Fingerprinting to Related.
- entities/datadome.md: added Canvas Fingerprinting to Related.
- entities/canvas-fingerprint-defender.md: added canvas-fingerprinting and browser-fingerprinting to Related.
- index.md: added canvas-fingerprinting under Concepts; bumped Last updated to 2026-06-04.

Sources added: WWW'25 paper (ACM DOI + author PDF), canvas-fp-attacks repo, LeooNic and camoufox-reverse forks, existing scraping-datadome-camoufox and deviceandbrowserinfo canvas-countermeasures sources.

Total changes: 1 page created, 5 pages updated.


## [2026-06-04] ingest | Is Camoufox still effective, and do the forks help? (Lab draft)

Source: `drafts/lab-camoufox-forks-cloverlabs-draft.md` (in-progress Lab article; published URL forthcoming).

Pages created:
- entities/camoufox-reverse.md: New entity (browser). The WhiteNightShadow Camoufox fork with an engine-level PropertyTracer. What it is, how it is driven (CAMOU_CONFIG propertyTrace, raw Playwright, MOZ_DISABLE_CONTENT_SANDBOX on macOS), TWSC use (watching Datadome read canvas/WebGL on leboncoin, home vs ad pages), limitations (FF135, instrument not daily driver).

Pages updated:
- entities/camoufox.md: added "Project governance and fork ecosystem (2026)" section (CloverLabs/VulpineOS handoff, daijro source-of-truth, cloverlabs-camoufox alpha, the three notable forks, mirror-fork noise, the JWriter20 100%-blocked-vs-official structural finding). Added Known limitations: canvas noise off by default (9105/18240 when seeded), the leboncoin ad-page pass rate, and a dated WebRTC note. New source + Related (camoufox-reverse).
- entities/datadome.md: added leboncoin engine-level trace finding (home 140 reads / 30 props vs ad page 584 reads, cookie.get 1->220, new surfaces; canvas/WebGL read; ad pages 403 direct, pass via proxy) and the JWriter20 structural-detection finding. New source + Related (camoufox-reverse).
- concepts/canvas-fingerprinting.md: added camoufox-reverse to Related.
- index.md: added camoufox-reverse under Browsers.

Contradiction documented (not overwritten): camoufox.md "How it works" states GeoIP aligns the WebRTC IP to the proxy exit. Our 2026-06 test found that on a FF146 build behind an HTTP proxy the reflexive STUN candidate still exposed the real WAN IP (host candidate suppressed). Noted with date in Known limitations per schema rule 1.

Key additions: the CloverLabs governance change and fork ecosystem (new to the wiki), the engine-level view of Datadome's reads on leboncoin, and the counterintuitive result that the most-patched fork (JWriter20) is blocked 100% while stock Camoufox passes, with the cause isolated to the request/connection layer rather than any static fingerprint.

Total changes: 1 page created, 4 pages updated.


## [2026-06-04] create | WebRTC IP leak concept + Camoufox vs forks comparison

Source: `drafts/lab-camoufox-forks-cloverlabs-draft.md` and the 2026-06 fork analysis.

Pages created:
- concepts/webrtc-ip-leak.md: New concept. Defines the leak (ICE host vs server-reflexive candidates, STUN over UDP bypassing an HTTP proxy), the Firefox prefs that mitigate it, the about:blank methodological caveat, and our finding that stock Camoufox 146 leaks the real WAN IP under an HTTP proxy while the JWriter20 fork gathers zero candidates. Consolidates the earlier thin Browserleaks mention from the geo-fencing article.
- comparisons/camoufox-vs-forks.md: New comparison. Table + narrative across official Camoufox, camoufox-reverse, LeooNic, JWriter20 on base FF version, what each changes, standard-stack runnability, canvas, WebRTC, and Datadome block rate on leboncoin. Verdict: run stock official on a clean IP.

Pages updated (backlinks):
- entities/camoufox.md: linked webrtc-ip-leak in the WebRTC limitation; added webrtc-ip-leak and Camoufox vs forks to Related.
- entities/datadome.md: added webrtc-ip-leak to Related.
- entities/camoufox-reverse.md: added Camoufox vs forks to Related.
- concepts/browser-fingerprinting.md: added webrtc-ip-leak to Related.
- concepts/canvas-fingerprinting.md: added Camoufox vs forks to Related.
- index.md: added webrtc-ip-leak under Concepts and Camoufox vs its forks under Comparisons.

Total changes: 2 pages created, 6 pages updated.


## [2026-06-05] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- envoy (tool) — Envoy

Appended 3 sources to existing wiki pages:
- concepts/canvas-fingerprinting.md: 1 new source
- concepts/proxy-fundamentals.md: 1 new source
- entities/cloudflare.md: 1 new source


## [2026-06-06] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- vnc2go (proxy-provider) — VNC2Go

Appended 1 sources to existing wiki pages:
- concepts/proxy-fundamentals.md: 1 new source


## [2026-06-09] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- guestlist-tools (library) — guestlist-tools
- intuned-agent (tool) — Intuned Agent

Appended 2 sources to existing wiki pages:
- concepts/ai-scraping-assistants.md: 1 new source
- concepts/web-unblockers.md: 1 new source


## [2026-06-10] update | Pass 3 source linking

Created 3 new entity pages from orphan RELEVANT news:
- chromiumfish (browser) — ChromiumFish
- bot-detection-system (anti-bot) — Bot Detection System
- claw-patrol (anti-bot) — Claw Patrol

Appended 3 sources to existing wiki pages:
- concepts/anti-detect-browsers.md: 1 new source
- concepts/bot-detection.md: 1 new source
- concepts/scraping-infrastructure.md: 1 new source


## [2026-06-11] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- productivityproxy (proxy-provider) — ProductivityProxy

Appended 1 sources to existing wiki pages:
- concepts/scraping-infrastructure.md: 1 new source


## [2026-06-16] update | Pass 3 source linking

Created 3 new entity pages from orphan RELEVANT news:
- usehuma (anti-bot) — useHUMA
- real-browser (browser) — Real Browser
- agent-vault-proxy (proxy-provider) — agent-vault-proxy

Appended 2 sources to existing wiki pages:
- concepts/bot-detection.md: 1 new source
- concepts/web-unblockers.md: 1 new source


## [2026-06-17] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- nakshguard (proxy-provider) — NakshGuard


## [2026-06-20] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- supercrawl (library) — SuperCrawl


## [2026-06-22] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- client-side-bot-detection (anti-bot) — Client-side bot detection
- greyfox-community-edition (proxy-provider) — GreyFox Community Edition

Appended 2 sources to existing wiki pages:
- concepts/bot-detection.md: 1 new source
- concepts/scraping-infrastructure.md: 1 new source


## [2026-06-23] update | Pass 3 source linking

Created 2 new entity pages from orphan RELEVANT news:
- residential-proxy (proxy-provider) — Residential Proxy
- otto (browser) — Otto

Appended 2 sources to existing wiki pages:
- concepts/scraping-infrastructure.md: 1 new source
- concepts/websocket-scraping.md: 1 new source


## [2026-06-23] create | Static ISP proxies — concept + entities from Spur YouTube webinar

Source: Spur research team (Riley Kilmer, Sean) — YouTube webinar on static ISP proxy sourcing and detection. https://www.youtube.com/watch?v=MQ1zpnlMMUc (2025/2026). Additional source: Spur blog post on Netnut border router co-option https://spur.us/blog/how-proxy-providers-co-opt-entire-networks.

Pages created:
- concepts/static-isp-proxies.md — Hybrid proxy category. Two subcategories (real ISP space leased via IPXO/BYOP; fake ISPs in datacenters). Sold per IP, long-lived, ~10% of residential bandwidth cost. Use cases: account management, anti-bot evasion, no bandwidth billing. Detection: abuse.radar.com signature, Ashburn concentration, Netnut source port 40,000–40,200. Tunnel vs client proxy classification.
- entities/netnut.md — ISP proxy provider using border router co-option via Divvy Networks. GRE tunnel architecture (spoofed source IP, 200-port window 40,000–40,200 for return traffic matching). Howard University /16 case study (>20% of observed Netnut traffic). Detectable via source port range. Classified as client proxies, not tunnels.
- entities/ipxo.md — IPv4 leasing marketplace. Most static ISP proxy infrastructure traces back to IPXO-leased ranges. Abuse reporting via abuse.radar.com. IP reputation persists after block reclamation.

Pages updated:
- concepts/proxy-fundamentals.md: added static-isp-proxies to Related section.
- wiki/index.md: added static-isp-proxies under Concepts; added IPXO and Netnut under Proxy networks and tools.

Total changes: 3 pages created, 2 pages updated.

## [2026-06-23] ingest | Smart TV proxy SDK findings from Spur blog

Source: Spur — "Smart TV Apps & Residential Proxy SDKs," https://spur.us/blog/smart-tv-apps-residential-proxy-sdks

Pages updated:
- concepts/proxy-fundamentals.md: added "Smart TV App Proxy SDKs (2025/2026)" subsection under IP Sourcing. Content: 34% SDK prevalence (2,058 of 6,038 scanned apps on LG webOS + Samsung Tizen), three providers (Bright Data, Massive, Honeygain/Oxylabs), per-provider technical implementation (IP blocklist, socket parsing, connect-type messages), consent framing as ad-free option, SDKs persist after app close, platform policy gap (Amazon/Roku ban; LG/Samsung no policy). Source added to frontmatter; last_updated bumped to 2026-06-23.

Total changes: 1 page updated.

---

Follow-up enrichment from Spur blog post (https://spur.us/blog/how-proxy-providers-co-opt-entire-networks):
- entities/netnut.md: major update with MikroTik/Juniper config details, PDNS subdomain pattern (rtr-<isp>.divinetworks.com), confirmed PoP IPs, Howard University precise stats (17k IPs, 224/224 /24s, AS919, three unannounced gaps), Plains Internet case study, BGP distribution analysis detection method, $13,208/month financial figure, KYC gap between DiviNetworks marketing and actual reseller practice.
- concepts/static-isp-proxies.md: enriched Netnut detection section with PBR, DIVINET-RETURN marks, PDNS pattern. Both sources added.


## [2026-06-23] ingest | blog.azerpas.com and brokenbrowser.com

Sources: all posts from both blogs scraped via Firecrawl to research/azerpas/ (2 posts) and research/brokenbrowser/ (42 posts).

Pages created:
- concepts/prerender-stealth-request.md: new page documenting the `<link rel="prerender">` stealth request technique discovered by Manuel Garcia (brokenbrowser.com, May 2026). Covers: why Chrome's speculative navigation pipeline bypasses CSP, why it is invisible to the DevTools Network tab, why it sends the real User-Agent even when DevTools UA override is active. Wire signature (`Sec-Purpose: prefetch`, absent `Sec-Fetch-Dest`). Bot detection relevance: UA spoofing asymmetry, one-way exfiltration channel. Chromium-only; Modern Speculation Rules API is unaffected. Source: https://www.brokenbrowser.com/blog/2026-05-09-prerender-stealth-csp-bypass

Pages updated:
- entities/webassembly-simd.md: major enrichment from Anthony Manikhouth's PoC (azerpas.com, May 2026). Added: measurement method (dependency chain loops, millions of iterations), 2,124 device dataset, KNN classifier with LOO evaluation, final accuracy figures (V8: 82.1% CPU / 95.2% brand; JSC: ~80% CPU / 100% brand), per-CPU accuracy table (highlights and outliers), PCA / t-SNE clustering description, engine variance (M3 f32x4_div varies 25% between V8 and JSC), spoofing analysis (jitter insufficient because ratios are the signal), compiler drift risk, scraping implications (server CPUs identifiable). Source updated to canonical URL.
- concepts/browser-fingerprinting.md: added silent `<object>` tag extension detection technique from brokenbrowser (2024). Documents how `<object>` avoids the console 404 noise that `fetch()` produces, the calibration state machine (400ms timeout on invalid URL), false-positive detection in WebView environments, and 1.5s cleanup cycle. Sources frontmatter and last_updated bumped.
- wiki/index.md: added prerender-stealth-request to Concepts section; updated last_updated note.

Total changes: 1 page created, 3 pages updated. 44 source files saved to research/.

## [2026-06-23] ingest | azerpas cleanup + DataDome research by same author

Context: azerpas blog has only 2 posts. grand-canyon (personal) was removed from research/ and excluded from future scrapes. wasm-simd was already ingested (entities/webassembly-simd.md). The blog's /about page revealed the author (Anthony Manikhouth) is a DataDome R&D engineer who publishes his relevant technical writing on datadome.co. User approved ingesting both linked DataDome articles.

Sources scraped to research/datadome/:
- how-chromes-new-ai-web-apis-enable-hardware-fingerprinting.md (Apr 2026)
- end-of-fingerprinting-how-browser-privacy-reshaping-bot-detection.md (Dec 2025)

Pages created:
- concepts/ai-web-api-fingerprinting.md: Chrome on-device AI APIs (Summarizer Chrome 138, LanguageModel Chrome 148) as hardware capability probe. Summarizer.availability() tier segmentation (only 4% of global traffic qualifies), cross-checks against hardwareConcurrency/deviceMemory/WebGL renderer, GPU performance class inference from Chromium source, inference timing fingerprinting (TTFT + decode throughput via promptStreaming). Cross-linked to webassembly-simd (both measure real execution vs declarative properties).
- concepts/browser-privacy-fingerprinting-defenses.md: Safari Advanced Fingerprinting Protection (iOS 26 default), Safari Lockdown Mode, Firefox resistFingerprinting (full removed-API list), Brave farbling, Chrome moving opposite direction. Impact: classic fingerprinting becoming low-entropy; detection shifts to behavioral + server-side. Specific altered values documented (AudioContext.sampleRate 48000/44100, WebGL renderer Mozilla, removed WebCodecs APIs).

Pages updated:
- entities/datadome.md: added "Detection Research (DataDome R&D, 2025–2026)" section summarizing both articles and DataDome's philosophy ("test what they can actually do" vs "what they claim to be"). Both source URLs added to frontmatter; last_updated bumped.
- concepts/browser-fingerprinting.md: added paragraphs on AI Web API fingerprinting and browser privacy defenses in Current State; added both new concepts plus webassembly-simd to Related.
- wiki/index.md: added both new concepts under Concepts; updated last_updated note.

Both authored by Anthony Manikhouth (also author of the azerpas wasm-simd post), making the WASM SIMD research and the DataDome AI-API research a coherent cluster on hardware-timing fingerprinting.

Total changes: 2 pages created, 3 pages updated. 2 source files saved to research/datadome/. 1 file removed (research/azerpas/grand-canyon.md).

## [2026-06-23] ingest | Browser Use Firecracker cloud infrastructure

Source: Browser Use — "How We Made Cloud Browsers 3x Cheaper and Faster," https://browser-use.com/posts/firecracker-browser-infra (June 15, 2026). Scraped to research/browser-use/firecracker-browser-infra.md.

Pages updated:
- entities/browser-use.md: added "Cloud Infrastructure (Firecracker microVMs)" section. Covers: one Firecracker microVM per session on regular EC2 (nested virtualization) vs .metal; $0.02/browser-hour (3x cheaper), <400ms VM cold start, 825ms p50 / 1.35s p99 create latency over 10k-session test; migration from Unikraft for EC2 autoscaling; custom control plane vs CloudWatch; memory optimization (2MB pages + userfaultfd hot-page preload, resume-to-ready 9.8s→3.1s, ~91x fewer page faults); CPU two-phase vCPU pinning + sibling hyperthreads + real-time priority (17%→0% lost sessions in 1k test); fully headless stealth (2% headless vs 50% headful baseline; low-level Chromium fork; tens of thousands of real fingerprints; 81% own benchmark / 84.8% Halluminate BrowserBench); remaining 545ms Chromium startup bottleneck and planned post-Chromium snapshotting. last_updated and Related/Sources updated.
- concepts/scraping-infrastructure.md: added "Cloud Browser Infrastructure (microVM-per-session)" subsection under What We Tested, documenting the Browser Use Firecracker pattern as an external reference (isolation + fast-start + cheap trilemma, nested-virtualization tradeoff, key figures). Source added to frontmatter; browser-use added to Related.
- wiki/index.md: improved browser-use description (was generic); updated last_updated note.

Total changes: 2 pages updated. 1 source file saved to research/browser-use/.

## [2026-06-23] ingest | Browser Use agent sandboxing + bot-detection deep dive

Sources scraped to research/browser-use/:
- two-ways-to-sandbox-agents.md — "How We Built Secure, Scalable Agent Sandbox Infrastructure" (Feb 25, 2026)
- bot-detection.md — "Browser agent bot detection is about to change" (Feb 2, 2026; this is the post the browser-use entity was originally seeded from, now ingested in full)

Pages created:
- concepts/agent-sandboxing.md: the two patterns for sandboxing code-executing agents (isolate the tool vs isolate the agent). Pattern 2 detail: one container image (Unikraft micro-VM prod / Docker dev via sandbox_mode switch), 3-env-var trust surface, hardening (bytecode-only .pyc, root→sandbox privilege drop, os.environ stripping), control plane as credentialed proxy (LLM proxying with server-side history reconstruction, presigned-URL file sync, gateway protocol), independent scaling. Cross-linked to agent-vault-proxy, claw-patrol, nakshguard, greyfox as adjacent control-plane/credential tools.

Pages updated:
- entities/browser-use.md: substantial expansion. "How it works" now carries the strategic thesis (antibots detect more than they block; thresholds will tighten as AI agents flood) and the full multi-layer stack (IP reputation, timezone/locale, hardware consistency, API availability, behavioral). New sections: Real-world fingerprints (Windows 60/macOS 35/Linux 5 distribution; fleet-level temporal blocking risk of Linux-everywhere), Performance and efficiency patches (compositor throttling, feature stripping, V8 tuning, CDP message optimization, portable profile encryption vs --password-store=basic), In-house CAPTCHA solving (Turnstile/PerimeterX/reCAPTCHA, free), and Agent Sandbox Architecture (Unikraft Pattern 2, distinct from the Firecracker browser layer). Frontmatter sources and Related updated.
- concepts/bot-detection.md: added "Detect More Than They Block" section (conservative thresholds, monitor→block flip, fleet-level shared-fingerprint temporal blocking, real-world OS distribution). Source + last_updated updated.
- wiki/index.md: added agent-sandboxing under Concepts; updated last_updated note.

Total changes: 1 page created, 3 pages updated. 2 source files saved to research/browser-use/.

## [2026-06-24] update | Pass 3 source linking

Created 1 new entity pages from orphan RELEVANT news:
- purroute (proxy-provider) — Purroute

Appended 1 sources to existing wiki pages:
- concepts/static-isp-proxies.md: 1 new source

