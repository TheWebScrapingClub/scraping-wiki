---
name: Browser Privacy Fingerprinting Defenses
type: concept
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
- https://datadome.co/threat-research/end-of-fingerprinting-how-browser-privacy-reshaping-bot-detection/
---

# Browser Privacy Fingerprinting Defenses

## Definition

Apple, Mozilla, and Brave have shipped browser-level anti-fingerprinting protections that partition storage and add noise to or remove the very APIs that bot detection vendors relied on for high-entropy device identification. The consequence for both tracking and bot detection is that classic client-side fingerprinting is becoming low-entropy: previously distinctive signals now return generic or randomized values across users. Documented by Anthony Manikhouth (DataDome R&D) in December 2025.

This is the defensive counterpart to [AI Web API fingerprinting](./ai-web-api-fingerprinting.md): as these classic surfaces are hardened, detection vendors move toward behavioral signals, server-side telemetry, and execution-capability probes.

## What Each Browser Changes

### Safari — Advanced Fingerprinting Protection

Enabled by default for all browsing sessions starting with iOS 26.

- **Storage partitioning**: LocalStorage, IndexedDB, Cache API, SessionStorage, and Blob URLs are partitioned so data stored by one site cannot be read by another, blocking cross-site tracking.
- **Canvas, WebGL, WebAudio noise**: values are perturbed. For example `AudioContext.sampleRate` falls back to a generic 48000 instead of the real value.
- **Randomized screen properties**: `window.inner{Width,Height}`, `screen.avail{Width,Height}`, and `window.outer{Width,Height}` were observed altered between Safari Tahoe (macOS 26) and the prior version on machines with identical effective height.

### Safari — Lockdown Mode

An optional extreme-protection mode that deactivates several Web APIs entirely: Audio, WASM, GamePad, and WebRTC. Rare in normal traffic, so its presence is itself a signal.

### Firefox — resistFingerprinting

Enabled via `about:config`. Observed effects:

- `AudioContext.sampleRate` fixed to 44100
- `hardwareConcurrency` fixed
- timezone fixed to UTC (offset 0)
- installed fonts list modified
- screen properties modified (`window.inner/outer`, `screen.avail`, `screen.orientation`, `screen.colorDepth`)
- WebGL `UNMASKED_RENDERER_WEBGL` fixed to `Mozilla`
- WebCodecs APIs removed entirely: `ImageDecoder`, `VideoDecoder`, `AudioEncoder`, `VideoColorSpace`, `VideoEncoder`, `AudioDecoder`, `AudioData`, `EncodedVideoChunk`, `VideoFrame`, `EncodedAudioChunk`, `ImageTrackList`, `ImageTrack`
- speech voices removed
- CSS media queries `device-aspect-ratio` and `device-screen` fixed to unsupported

### Brave — Farbling

Randomization-based defense that adjusts canvas and audio values to produce a different fingerprint on every session. Three levels: Off, Standard (small randomness, maximum compatibility), and Maximum (more protection, may break sites).

### Chrome — the opposite direction

Chrome (~70% market share) removed fingerprinting language from its policies in 2025. Its February 2025 Platforms policy update does not mention fingerprinting at all, reversing its 2021 anti-fingerprinting stance in Google Ads. As Chromium's main contributor, Google shapes the API surface available to all Chromium-based browsers (Edge, Opera, Brave, and others), so the base architecture keeps fingerprinting feasible even where individual forks add their own protections.

## Where It Matters

For scrapers, the practical effect cuts both ways. A privacy-hardened browser profile (Safari iOS 26, Firefox resistFingerprinting, Brave Maximum) now returns the same generic values as many real users, so blending in on those specific surfaces is easier. But anti-detect tools that spoof toward a real-device profile must now match the randomized or fixed values these browsers produce, or they create a different kind of inconsistency. A tool that reports a real `AudioContext.sampleRate` while claiming to be Firefox with resistFingerprinting (which forces 44100) is incoherent.

The strategic shift matters more. As fingerprinting entropy drops, detection vendors that depended on it lose ground, while those built on behavioral analytics and server-side telemetry are largely unaffected.

## How DataDome Responds

DataDome states these privacy measures do not degrade its detection, because:

1. Data from hardened APIs is reclassified from a high-confidence identifier to a low-entropy signal, still useful for detecting deviation from a normalized baseline rather than for unique identity.
2. Behavioral analytics (mouse movements, clicks) and server-side telemetry (IP reputation, header analysis) are functionally immune to client-side API restrictions.
3. Many less-obvious Web APIs beyond the actively-hardened ones (screen resolution, GPU details, font lists) remain useful fingerprinting surfaces, and the research team continuously probes new and old APIs for fresh signals.

The takeaway for scrapers is consistent with TWSC's own testing: behavioral and server-side signals are the resilient detection vectors, and a stealth stack that only fixes client-side fingerprint values addresses a shrinking part of the problem. See [Datadome](../entities/datadome.md) for the behavioral and CDP detection detail.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [ai-web-api-fingerprinting](./ai-web-api-fingerprinting.md)
- [Datadome](../entities/datadome.md)
- [canvas-fingerprinting](./canvas-fingerprinting.md)
- [Anti-Detect Browsers](./anti-detect-browsers.md)
- [tls-fingerprinting](./tls-fingerprinting.md)

## Sources

- Anthony Manikhouth (DataDome R&D) — "The End of Fingerprinting As We Know It: How Browser Privacy Protections Are Reshaping Bot Detection," [https://datadome.co/threat-research/end-of-fingerprinting-how-browser-privacy-reshaping-bot-detection/](https://datadome.co/threat-research/end-of-fingerprinting-how-browser-privacy-reshaping-bot-detection/) (December 2025)
