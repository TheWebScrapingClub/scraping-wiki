---
name: ML-Based Bot Detection
type: concept
first_seen: 2023-02-02
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/machine-learning-for-detecting-bots
  - https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix
  - https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges
  - https://github.com/RoloBits/isHumanCadence
---

## Definition

ML-based bot detection refers to the use of machine learning models to classify web traffic as human or automated. Unlike rule-based systems (IP blocklists, simple rate limits, user-agent checks), ML models learn from behavioral patterns across large traffic datasets and can identify subtle automation signals that static rules miss.

All major anti-bot vendors (Cloudflare, Datadome, PerimeterX, Kasada, F5) use ML as a core component of their detection stack. The implication for scrapers is that successful bypasses must fool the model, not just pass individual rule checks.

## How it works

### Feature categories

ML bot detection models are trained on features derived from four signal categories:

**Request pattern signals**
- Request rate and velocity per IP and per session
- Sequential traversal patterns (iterating product IDs in order, paginating all pages)
- Targeted content access (only hitting data-rich endpoints, ignoring navigation assets, images, and scripts)
- Absence of engagement with dynamic content (no JavaScript execution, no ad rendering)

**Session and behavioral signals**
- Session duration relative to request volume (short sessions with many requests)
- Absence of mouse movement, scrolling, and keyboard events
- Perfectly consistent timing between requests (automation produces precise intervals; humans do not)
- No cookie acceptance, no geolocation permission responses

**Header and fingerprint signals**
- Non-standard, outdated, or generic User-Agent strings
- Missing or anomalous HTTP headers (browsers send more headers than most scraping tools)
- IP reputation (datacenter ranges, known proxy ASNs, VPN services)
- Headless browser artifacts

**Fingerprint coherence**
- Inconsistencies between claimed browser, OS, hardware, and rendered output
- SwiftShader or zero-device WebGL renderers
- Canvas fingerprint entropy anomalies

### Learning paradigms

**Supervised learning**: Models trained on labeled datasets (human vs. bot) learn a decision boundary across behavioral features. Once deployed, new traffic is classified in real time. Cloudflare claims to train on hundreds of billions of requests per day. Datadome claims to process 3 trillion data signals per day.

**Unsupervised learning**: Clustering algorithms group sessions by behavioral similarity without pre-labeled data. Sessions that form tight clusters of highly homogenous, systematic behavior are flagged for review regardless of any individual signal.

**Semi-supervised learning**: A small labeled dataset guides learning across a large unlabeled traffic corpus. Useful when confirmed bot examples are available but comprehensive labeling is impractical.

### The arms race dynamic

As ML models improve at detecting automation signals, scraping tools improve at hiding them. Anti-bot vendors observe that their models need regular retraining as new scraping techniques emerge. Conversely, scrapers observe that bypasses that work against a specific model version fail after the vendor retrains or updates.

The practical implication: the most durable bypass strategies are those that do not depend on any one model's blind spot, but instead generate traffic that is genuinely indistinguishable from human traffic across all observable dimensions. This is why browser-level fingerprint quality, residential proxy IP reputation, and realistic behavioral pacing all matter simultaneously.

## Where it matters

ML detection is present in all anti-bot systems TWSC has tested. Its weight relative to rule-based detection varies by system and target configuration. Key observations:

- Datadome is the heaviest ML/behavioral user in the TWSC corpus. It can block mid-session based on behavioral drift.
- Kasada uses ML as part of its first-request challenge evaluation.
- PerimeterX uses real-time behavioral scoring on each page load.
- Cloudflare trains on 500B+ requests per day; ML scoring produces a bot score for every request.
- F5 is described as relying heavily on AI for behavioral analysis with limited other observable signal types.

## What we tested

The anti-detect matrix (February 2023) provided the first systematic TWSC comparison of tool performance against multiple ML-backed anti-bots. Key finding: Playwright with Chrome was the worst performer across all five anti-bots tested, while Playwright with Firefox performed significantly better. Undetected-chromedriver outperformed standard Playwright. The pattern suggests that Chrome's automation surface was the primary ML detection target, while Firefox's automation signals were less well-modeled. Covered in [anti-detect-anti-bot-matrix](https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix).

The Nimble AI browser test (June 2023) demonstrated commercial AI-generated browser fingerprints against the same five anti-bots. The AI vs. AI framing reflects the vendor reality: anti-bot ML models are trained on signals from AI-generated fingerprints just as they are on human traffic. Covered in [the-lab-21-bypass-anti-bot-challenges](https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges).

The ML bot detection overview article (June 2025) documents the feature engineering side: what signals ML models use and how those signals can be manipulated. Covered in [machine-learning-for-detecting-bots](https://substack.thewebscraping.club/p/machine-learning-for-detecting-bots).

### Keystroke Dynamics: isHumanCadence

isHumanCadence (RoloBits, February 2026) is an open-source npm library implementing bot detection via keystroke rhythm analysis. It requires no CAPTCHA and is passive — it scores a user while they type normally into form fields.

The library measures six signals combined into a 0.0 (bot) to 1.0 (human) score:

| Signal | What it checks | Human | Bot |
|---|---|---|---|
| Dwell variance | How much key-hold durations vary | Varies naturally | Nearly identical |
| Flight fit | Whether inter-key timing follows a natural curve | Yes | Flat/constant |
| Timing entropy | Randomness in rhythm | Moderate | Too uniform or too constant |
| Correction ratio | Backspace/Delete usage | Human bonus (2–15%) | No signal (0%) |
| Burst regularity | Pauses between typing bursts | Irregular | Metronomic |
| Rollover rate | Key overlap (next pressed before previous released) | 25–50% | 0% |

The correction ratio finding is notable: the Aalto 136M Keystrokes study (Dhakal et al., CHI 2018) shows correction rates vary from 3.4% (fast typists) to 9.05% (slow typists). Zero corrections over 50 keystrokes is normal for roughly half of skilled typists, so the absence of corrections is treated as uninformative rather than suspicious — it scores on a [0.5, 1.0] range.

The library uses circular buffers with zero garbage collection, requestIdleCallback for async analysis, and Kolmogorov-Smirnov statistical tests. It has no dependencies and supports React (useHumanCadence hook), Vue (v-human-cadence directive), and vanilla JS.

The practical implication for scrapers: any automation that fills forms with programmatically generated keystrokes (constant inter-key intervals, zero dwell variance, no corrections, 0% rollover) will score near 0.0. Simulating realistic keystroke dynamics requires introducing variance, artificial pauses, and occasional corrections.

Source: github.com/RoloBits/isHumanCadence (2026-02-09)

## Current state (as of 2025)

AI-generated bot fingerprints (from tools like Camoufox, Patchright, anti-detect browsers) are now good enough to fool most ML models when combined with residential IP ranges and human-paced navigation. The remaining gap is hardware fingerprinting: Kasada's hardware-level signals from datacenter VMs are not yet addressable by software fingerprint manipulation alone.

The industry expectation is that ML models will continue to incorporate hardware-level signals (GPU rendering characteristics, CPU timing, memory access patterns) as the software fingerprint space becomes more saturated with convincing fakes.

## Related

- [Browser Fingerprinting](browser-fingerprinting.md)
- [TLS Fingerprinting](tls-fingerprinting.md)
- [CDP Detection](cdp-detection.md)
- [Datadome](../entities/datadome.md)
- [Cloudflare](../entities/cloudflare.md)
- [Kasada](../entities/kasada.md)
- [PerimeterX](../entities/perimeterx.md)
- [F5 Bot Defense](../entities/f5-bot-defense.md)
