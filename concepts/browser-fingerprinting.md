---
name: browser-fingerprinting
type: concept
first_seen: 2010-01-01
last_updated: '2026-05-10'
sources:
- browser-fingerprinting-how-it-works.md
- understanding-browser-fingerprint.md
- the-lab-33-fingerprinting-at-different.md
- the-stealth-stack-web-scraping.md
- browser-fingerprinting-test-online.md
- the-latest-papers-about-browser-fingerpinting.md
- how-to-mask-device-fingerprint.md
- scraper-fingerprints-and-proxies.md
- https://blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle
- https://github.com/antoinevastel/fpscanner
- 404privacy-com.md
- detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle.md
- python-in-plain-english-modern-anti-bot-systems-and-how-to-bypass-them-4d2847552.md
- dbi-changelog-week-17june-2024.md
- dbi-privacy-leak-detecting-canvas-countermeasures.md
- dbi-role-of-weak-fingerprinting-signals.md
- dbi-analysis-temporary-phone-numbers.md
- dbi-analyze-open-bullet2-puppeteer-mode.md
- dbi-changelog-week-14july-2024.md
- dbi-detect-lie-os-fraud.md
- dbi-exclude-bots-from-google-analytics-2024.md
- dbi-httpheaders.md
- dbi-scraping-temporary-phone-numbers.md
- dbi-sec-ch-ua-forms-factor.md
- dbi-take-good-screenshots-with-puppeteer.md
- dbi-use-puppeteer-with-chrome-macos.md
- dbi-webglrenderervalues.md
- mochijs-com.md
---

# Browser Fingerprinting

## Definition

A stateless, cookieless tracking mechanism that identifies browsers by collecting and hashing the outputs of browser APIs. Unlike cookies, fingerprints require no storage on the client and persist across sessions, incognito modes, and cookie clears.

## How It Works

The fingerprint is assembled from multiple signal categories, each contributing to a composite identifier.

**Canvas fingerprinting** renders a hidden drawing operation and hashes the pixel output. The result varies by GPU, driver, and font rendering engine, making it highly device-specific.

**WebGL fingerprinting** extracts the GPU renderer and driver version strings, then hashes the pixel output of a 3D render. The renderer string alone (e.g., "ANGLE (Intel, Intel(R) UHD Graphics...)") is often unique enough to identify a device class.

**AudioContext fingerprinting** runs an oscillator through the browser's audio processing pipeline and hashes the output. Subtle differences in floating-point arithmetic across hardware produce distinct values.

**Font fingerprinting** infers installed fonts by measuring text dimension fallbacks through Canvas or DOM. If a character renders at an unexpected width, a specific font is present.

**DOM signals** expose automation-related properties directly: `navigator.webdriver`, `hardwareConcurrency`, `deviceMemory`, `navigator.languages`, `navigator.plugins`, and `window.chrome` are all readable from JavaScript.

**Device signals** include touch support, screen resolution, color depth, `MediaDevices.enumerateDevices()`, and Battery API readings (now deprecated in most browsers).

## Where It Matters

Any anti-bot system that needs to distinguish real users from automated scripts uses some form of fingerprinting. [Cloudflare](../entities/cloudflare.md), [Akamai](../entities/akamai.md), [DataDome](../entities/datadome.md), and [PerimeterX](../entities/perimeterx.md) all rely on fingerprint signals at varying depths.

Two signals are particularly damaging in scraping contexts. SwiftShader, the CPU-based GPU emulator that Chromium falls back to in headless environments, is a known red flag — real browsers on real hardware do not use it. Zero audio and video devices returned by `MediaDevices.enumerateDevices()` is equally suspicious; physical machines always expose at least a default output device.

Fingerprint coherence matters as much as the individual signals. If the User-Agent claims to be Chrome 124 on Windows but the WebGL renderer reports a Linux GPU string, the mismatch is flagged immediately. The same applies across TLS, canvas, and JS feature detection — all signals must form a consistent, plausible profile.

## Fingerprinting test tools

Two public tools are useful for evaluating scraper fingerprint quality:

**CreepJS** (abrahamjuliot): an open-source fingerprinting library that runs a comprehensive probe suite in the browser and generates a trust score. CreepJS exposes canvas, WebGL, AudioContext, WebRTC, fonts, screen geometry, hardware concurrency, navigator properties, and behavioral markers. TWSC uses it as a benchmark tool for anti-detect browsers. A lower trust score does not mean a better browser for scraping — a real Mac running Brave scores 7%, and Camoufox scores 68%, both of which pass anti-bot challenges. The trust score is a measure of anomalousness, not stealth.

**BrowserScan**: a simpler browser fingerprint viewer that shows what signals are readable and whether specific red flags (SwiftShader, zero media devices, WebDriver flag, CDP detection) are present. It includes an explicit CDP detection test that makes `Runtime.enable` detection observable directly. More useful than CreepJS for quickly diagnosing specific signal problems.

## Browser Extension Detection

Browser extensions cannot be enumerated directly — there is no `navigator.extensions` API. However, extensions can be detected indirectly via their side effects. By 2026, NPAPI plugins are deprecated across all major browsers, making `navigator.plugins` enumeration useless. Extension detection instead relies on:

**Direct resource probing (LinkedIn's approach)**: Chromium assigns each extension a stable, unique extension ID visible in Chrome Web Store URLs and at `chrome://extensions`. Extensions can declare files as `web_accessible_resources` in their `manifest.json`, making them fetchable from any page via URLs of the form `chrome-extension://<extension_id>/<path>`. LinkedIn maintains a static list of extension ID + file path pairs. For each entry, it attempts to fetch the resource. A successful fetch confirms the extension is installed. The list includes developer tools, automation helpers, CAPTCHA solvers, and productivity tools like Grammarly.

Example: Grammarly's extension ID is `kbfnbcaeplbcioakkpcpgfkobkghlhen`. LinkedIn probes `chrome-extension://kbfnbcaeplbcioakkpcpgfkobkghlhen/src/css/gOS-sandbox.styles.css`. If it loads (HTTP 200), Grammarly is installed.

**Limitations**: only web-accessible resources can be probed. Extensions that declare no web-accessible resources cannot be detected this way. The list must be maintained as extensions update their manifests and change exposed file paths.

**Side-effect detection (Castle's approach)**: rather than probing known resource URLs, detect extensions by observing behavioral changes they cause on the page — DOM mutations, injected CSS, patched JavaScript globals, or modified prototype chains. This approach works on extensions that declare no web-accessible resources, and does not require maintaining a list of extension IDs.

**Implications for scrapers**: automation extensions (CAPTCHA solvers, scraping helpers) are visible to LinkedIn and similar sites via extension probing. A scraping stack that uses a browser extension for any purpose should consider that the extension ID may be in a detection list. Running without extensions is the safest approach for sensitive targets.

Source: blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle/ (2026-01-14)

## FPScanner: Self-Hosted Bot Detection Library

`antoinevastel/fpscanner` (GitHub, 623 stars as of early 2026, Castle-sponsored) is a self-hosted browser fingerprinting and bot detection library addressing the gap between naive open-source tools and expensive black-box CDN-based solutions. It is specifically designed for teams that cannot or do not want to route traffic through a third-party vendor.

Key design decisions:

- **Anti-replay protection**: each fingerprint payload includes a timestamp and nonce, preventing a valid fingerprint from being captured once and replayed at scale.
- **Build-time key injection**: the encryption key for the payload is injected at build time, not committed to source. An attacker cannot generate valid encrypted payloads without access to the specific build.
- **Optional obfuscation**: raises the reverse-engineering cost without relying on obscurity as the primary defense.
- **Focus on consistency over breadth**: the library checks relationships between signals across contexts and sessions. Maintaining a fully consistent fingerprint over time is significantly harder for attackers than spoofing any single signal.

The library is sponsored by Castle and its design philosophy is documented in Castle's "Roll your own bot detection" blog series (fingerprinting part 1, server-side detection part 2).

Source: github.com/antoinevastel/fpscanner (2026-02-21)

## Picasso and DataDome's canvas approach

Google developed Picasso, a canvas-based fingerprinting technique, and DataDome has been observed using it. Picasso renders a specific geometric pattern on a hidden canvas and extracts the pixel hash. The technique is designed to be more stable than generic canvas noise probes because it controls the exact rendering operation rather than relying on arbitrary text or shapes. This makes it harder to spoof with simple noise injection, because the noise must be applied consistently across a specific rendering context that the detection script controls.

## Academic research findings

TWSC reviewed recent academic work on browser fingerprinting. Key findings relevant to scraping:

- Desktop browsers are more unique than mobile browsers. More signals are exposed on desktop. A scraper impersonating a mobile profile has fewer surface area to get wrong.
- Chrome exposes more fingerprinting data than Safari or Firefox. Firefox's more restrictive API access makes it inherently less fingerprintable. This is one structural reason why Camoufox (Firefox-based) has fewer signals to spoof.
- WebGPU-SPY demonstrated ~90% cross-site tracking accuracy by measuring GPU cache timing in WebGPU. It exploits the fact that GPU texture caches are shared across browsing contexts. The attack works even in private browsing mode and across different websites. This is a newer attack vector that standard fingerprint spoofing tools do not address.

## What We Tested

The EFF's 2010 Panopticlick study tested 470,000 browsers and found that 84% had unique fingerprints using only a handful of signals. Modern implementations use dozens more.

The most revealing test scenario is the local vs. datacenter gap: a scraper that passes fingerprint checks on a developer's laptop will often fail immediately when deployed to a cloud server, because the server exposes SwiftShader and zero media devices — signals that are invisible locally but obvious remotely.

Anti-detect browsers (see [Camoufox](../entities/camoufox.md)) address browser-level fingerprinting but do not fix [TLS fingerprinting](./tls-fingerprinting.md). Treating both as the same problem is a common mistake.

In the 2024 anti-detect browser benchmark using CreepJS and BrowserScan, scores ranged from 139/260 (Incogniton) to 223/260 (GoLogin), with a real Mac at 226/260. See [anti-detect-browser-benchmark-2024](../comparisons/anti-detect-browser-benchmark-2024.md) for the full results.

## Current State

Browser fingerprinting is a mature and well-documented technique. The signals have not changed dramatically since 2020, but the scoring models that consume them have become more sophisticated. Partial fingerprint spoofing (changing only `navigator.webdriver`) is no longer sufficient against serious anti-bot deployments.

New attack vectors continue to emerge. WebGPU-SPY (GPU cache timing) represents an approach that operates below the standard fingerprinting signal layer and is not addressed by current anti-detect tools.

The practical challenge for scrapers is not understanding what is collected but achieving full coherence across all signal layers simultaneously.

## Related

- [tls-fingerprinting](./tls-fingerprinting.md)
- [cdp-detection](./cdp-detection.md)
- [hybrid-scraping](./hybrid-scraping.md)
- [Camoufox](../entities/camoufox.md)
- [Cloudflare](../entities/cloudflare.md)
- [Akamai](../entities/akamai.md)

## Sources

- [https://substack.thewebscraping.club/p/browser-fingerprinting-how-it-works](https://substack.thewebscraping.club/p/browser-fingerprinting-how-it-works)
- [https://substack.thewebscraping.club/p/understanding-browser-fingerprint](https://substack.thewebscraping.club/p/understanding-browser-fingerprint)
- [https://substack.thewebscraping.club/p/the-lab-33-fingerprinting-at-different](https://substack.thewebscraping.club/p/the-lab-33-fingerprinting-at-different)
- [https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping](https://substack.thewebscraping.club/p/the-stealth-stack-web-scraping)
- [https://substack.thewebscraping.club/p/browser-fingerprinting-test-online](https://substack.thewebscraping.club/p/browser-fingerprinting-test-online)
- [https://substack.thewebscraping.club/p/the-latest-papers-about-browser-fingerpinting](https://substack.thewebscraping.club/p/the-latest-papers-about-browser-fingerpinting)
- [https://substack.thewebscraping.club/p/how-to-mask-device-fingerprint](https://substack.thewebscraping.club/p/how-to-mask-device-fingerprint)
- [https://substack.thewebscraping.club/p/scraper-fingerprints-and-proxies](https://substack.thewebscraping.club/p/scraper-fingerprints-and-proxies)
- [https://blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle/](https://blog.castle.io/detecting-browser-extensions-for-bot-detection-lessons-from-linkedin-and-castle/)
- [https://github.com/antoinevastel/fpscanner](https://github.com/antoinevastel/fpscanner)
