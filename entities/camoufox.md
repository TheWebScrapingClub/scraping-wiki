---
name: camoufox
type: entity
category: tool
first_seen: 2024-10-01
last_updated: 2026-06-04
sources:
  - scraping-datadome-camoufox.md
  - bypassing-cloudflare-in-2026.md
  - bypassing-kasada-2025-open-source.md
  - hybrid-scraping-camoufox-curl-cffi.md
  - scrapling-hands-on-guide.md
  - cloudflare-bypass-2026.md
  - how-to-bypass-cloudflare-turnstile.md
  - camoufox-server-docker.md
  - camoufox-server-in-aws.md
  - how-to-create-camoufox-docker-image.md
  - lab-camoufox-forks-cloverlabs-draft.md
---

# Camoufox

## What it is

Camoufox is a custom Firefox build created by daijro, released as open-source. It is not a Playwright wrapper or a stealth plugin layered on top of a stock browser. The entire Firefox binary is patched and recompiled, which means fingerprint manipulation happens at the engine level rather than through JavaScript injection.

## How it works

Camoufox ships with [BrowserForge](../concepts/browser-fingerprinting.md) embedded directly into the browser. BrowserForge generates realistic browser fingerprint profiles and injects them at the binary level, covering canvas, WebGL, audio, fonts, screen dimensions, and hardware concurrency. Because the forging happens inside the browser process itself, there is no detectable injection layer visible to the page.

Mouse movement is handled through a patched version of the Juggler protocol. Juggler is the custom Firefox automation protocol originally developed by the Playwright team as an alternative to CDP for Firefox. Camoufox ships a modified Juggler implementation that generates human-like cursor trajectories instead of instant coordinate jumps.

Playwright JS isolation is preserved: internal automation JavaScript runs in a sandboxed agent context that is invisible to page scripts. A page cannot enumerate or detect Camoufox's internal JS through standard DOM inspection.

GeoIP matching is built in. When a proxy is configured, Camoufox automatically aligns the browser timezone and WebRTC IP to the proxy's exit IP geolocation, preventing the common mismatch signals that anti-bot systems flag.

Headless operation on Linux uses `headless="virtual"` mode, which runs the browser through xvfb rather than a true headless flag. This avoids the headless-specific rendering differences that some fingerprinting probes detect.

## TWSC experience

Camoufox is consistently our best open-source performer against [Cloudflare](cloudflare.md). In the 2026 benchmark across 100 requests, it achieved 99% success on Harrods (Cloudflare managed challenge) and 31% on Indeed, where the failure rate was caused by rate limiting rather than bot detection.

Against [Kasada](kasada.md), Camoufox bypasses the challenge without additional configuration. Against [Datadome](datadome.md) on hermes.com, it works with workarounds. In October 2024, a configuration change on hermes.com broke the direct approach overnight and required identifying an alternate entry point that bypassed the Datadome-protected route entirely.

We also use Camoufox in a hybrid scraping pattern: the browser handles authentication and cookie acquisition, then [curl_cffi](curl-cffi.md) takes over for bulk requests. This combination successfully handled [Akamai](akamai.md) on Net-a-Porter.

Fingerprint signals observed in testing:

- CreepJS trust score: 68% (for reference, a real Mac running Brave scores 7%, so lower is not always better)
- BrowserScan: identified as legitimate Firefox on consumer hardware with no anomaly flags

## Docker and server deployment

Camoufox can be containerized and deployed as a remote browser server, replacing the need for a local Camoufox installation in each scraper.

**Docker image requirements**: Ubuntu 22.04 base (not 24.04 — this matters; Ubuntu 24.04 introduces library incompatibilities). The full Firefox installation must be present inside the container. The `camoufox[geoip]` pip package installs both the Python bindings and the GeoIP database. Supporting packages: FastAPI, Uvicorn, websockets, Xvfb.

The container runs `launch_server.py`, which starts a Camoufox browser server listening on port 59001 via a WebSocket protocol. Remote clients connect to this port to receive a remote browser context. Xvfb provides the virtual display required for headful mode in a headless container environment.

**BrowserScan result from Docker test**: A Camoufox instance running in Docker, tested against BrowserScan, returned results consistent with a legitimate Firefox browser on consumer hardware with no anomaly flags. The containerization itself did not add detectable signals.

**AWS deployment architecture**: TWSC documented a production deployment pattern using ECR (Elastic Container Registry) for image storage, an EC2 Auto Scaling Group for compute, and a Network Load Balancer (NLB) for traffic distribution. The choice of NLB over ALB is required: NLB operates at layer 4 (TCP) and passes WebSocket connections through without modification. ALB operates at layer 7 (HTTP) and introduces WebSocket handling complexity at port 59001.

The NLB routes TCP traffic directly to EC2 instances. The Auto Scaling Group manages capacity based on load. The ECR stores versioned images, and deployment involves pulling the latest image on each new EC2 instance.

This architecture allows Camoufox capacity to scale horizontally while maintaining the stateless browser-per-request model.

## Project governance and fork ecosystem (2026)

Development of Camoufox moved to a company. As of 2026, the daijro README states that active browser development happens at CloverLabsAI/camoufox and VulpineOS, while the daijro repository is the source-of-truth that merges checkpoint releases. Clover Labs is a Toronto venture studio building AI agents, listed among the project sponsors alongside Scrapfly. Alpha features (per-context fingerprints, hardware spoofing) ship first in the `cloverlabs-camoufox` pip package; the stable `camoufox` package is released on a delay.

The public repository has more than 750 forks, but the large majority are mirror bots with no commits of their own (identical `pushed_at` to the parent). Reading the commit history of the active forks narrows the field to three that change anti-detect behavior:

- [camoufox-reverse](camoufox-reverse.md) (WhiteNightShadow) adds an engine-level PropertyTracer that records which DOM getters a page reads. It is an instrument for observing detectors, not a better disguise.
- LeooNic/camoufox adds content-aware [canvas](../concepts/canvas-fingerprinting.md) noise, a sigma-lognormal humanized mouse engine, and RDPBrowser, an automation path over the Firefox Remote Debugging Protocol instead of Juggler. Its published Firefox 149 build did not launch under the standard Playwright stack in our 2026-06 testing — it aborts at startup before Juggler attaches, and LeooNic issue #1 confirms the FF149 port is still in progress. It runs only through its own RDP tooling.
- JWriter20/camoufox ships targeted stealth fixes, the headline being a closed WebRTC IP leak under a proxy on Firefox 146 (daijro issue #538), plus a real pytest suite.

A counterintuitive result came out of testing these against [Datadome](datadome.md) on leboncoin.fr in 2026-06. The JWriter20 fork, the one that improves stealth, was blocked on 100% of ad pages while the official build passed almost all of them. This reproduced in both run orders and with the spoofed OS pinned identically. The page-level JS fingerprint, the TLS/JA3-JA4 ClientHello, and the HTTP/2 fingerprint were all identical between the two builds, so the block is structural to the JWriter20 build and lives in its request or connection behavior, not in any static fingerprint. The practical lesson is that a more-patched fork is not automatically a safer choice: stock Camoufox on a clean residential IP outperformed the forks here.

## Known limitations

- Anti-bot vendors can still detect behavioral patterns if request velocity is high. The 31% on Indeed reflects this.
- Canvas pixel noise is disabled by default in current builds, consistent with a CloverLabs "Disable Canvas Noise" commit. When forced on via `canvas:seed`, the stock algorithm perturbs roughly half of all pixels including flat solid fills (9105 of 18240 interior pixels in our two-block probe), which is the reversible style the WWW'25 Pixel-Recovery attack targets (see [canvas fingerprinting](../concepts/canvas-fingerprinting.md)). Stock Camoufox relies on a realistic fingerprint and a clean IP rather than on canvas randomization.
- WebRTC IP under a proxy: previously documented above that GeoIP aligns the WebRTC IP to the proxy exit. As of 2026-06, on a Firefox 146 build behind an HTTP proxy, we observed a [WebRTC IP leak](../concepts/webrtc-ip-leak.md), with the reflexive STUN (srflx) candidate still exposing the real WAN IP while the host/LAN candidate was suppressed. The JWriter20 fork closes this with `default_address_only` and `proxy_only_*` prefs that make WebRTC gather no candidates behind a proxy. Test the WebRTC surface per build and per Firefox version.
- On leboncoin.fr the homepage passes cleanly, but the ad detail pages return 403 on a direct connection. Through a clean residential proxy, official Camoufox 146 passed about 95 to 100% of ad pages, and a short burst of blocked requests from one IP heated the address quickly.
- Hermes.com demonstrated that vendor-side configuration changes can break a working bypass without any change on our end. Monitoring and fast response are required.
- The `headless="virtual"` mode requires xvfb on Linux, which adds infrastructure overhead compared to true headless tools.
- Fingerprint rotation means some profiles in the database are detected by strict configurations. In 2025 testing against Indeed.com Turnstile (run locally), Camoufox required multiple retries before landing on a clean profile. This inconsistency makes it less reliable than Botasaurus or Patchright in that specific scenario when running locally without a proxy.
- The `geoip=False` setting disables geographic alignment. This is fine when no proxy is used but should not be combined with a proxy without GeoIP enabled, as timezone/IP mismatches will be flagged.

## Related

- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [Canvas Fingerprinting](../concepts/canvas-fingerprinting.md)
- [WebRTC IP Leak](../concepts/webrtc-ip-leak.md)
- [camoufox-reverse](camoufox-reverse.md)
- [Camoufox vs forks](../comparisons/camoufox-vs-forks.md)
- [Cloudflare](cloudflare.md)
- [Datadome](datadome.md)
- [Kasada](kasada.md)
- [curl-cffi](curl-cffi.md)
- [scrapling](scrapling.md)
- [playwright](playwright.md)

## Sources

- [https://substack.thewebscraping.club/p/scraping-datadome-camoufox](https://substack.thewebscraping.club/p/scraping-datadome-camoufox)
- [https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026](https://substack.thewebscraping.club/p/bypassing-cloudflare-in-2026)
- [https://substack.thewebscraping.club/p/bypassing-kasada-2025-open-source](https://substack.thewebscraping.club/p/bypassing-kasada-2025-open-source)
- [https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi](https://substack.thewebscraping.club/p/hybrid-scraping-camoufox-curl-cffi)
- [https://substack.thewebscraping.club/p/scrapling-hands-on-guide](https://substack.thewebscraping.club/p/scrapling-hands-on-guide)
- [https://substack.thewebscraping.club/p/cloudflare-bypass-2026](https://substack.thewebscraping.club/p/cloudflare-bypass-2026)
- [https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile](https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile)
- [https://substack.thewebscraping.club/p/camoufox-server-docker](https://substack.thewebscraping.club/p/camoufox-server-docker)
- [https://substack.thewebscraping.club/p/camoufox-server-in-aws](https://substack.thewebscraping.club/p/camoufox-server-in-aws)
- [https://substack.thewebscraping.club/p/how-to-create-camoufox-docker-image](https://substack.thewebscraping.club/p/how-to-create-camoufox-docker-image)
- TWSC Lab article, forthcoming 2026: "Is Camoufox still effective, and do the forks help?" (draft: `drafts/lab-camoufox-forks-cloverlabs-draft.md`)
- [daijro/camoufox (README: CloverLabs/VulpineOS handoff)](https://github.com/daijro/camoufox)
- [CloverLabsAI/camoufox](https://github.com/CloverLabsAI/camoufox)
