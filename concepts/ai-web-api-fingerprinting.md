---
name: AI Web API Fingerprinting
type: concept
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
- https://datadome.co/threat-research/how-chromes-new-ai-web-apis-enable-hardware-fingerprinting/
---

# AI Web API Fingerprinting

## Definition

Chrome's on-device AI Web APIs (Translator, Language Detector, Summarizer, and the upcoming LanguageModel) only function on hardware that meets specific minimum specifications. Querying whether these APIs are available, and measuring how fast they run, turns them into a hardware capability probe. The signal is harder to spoof than declarative properties like `navigator.hardwareConcurrency` because it reflects what the device can actually do, not what it claims. Documented by Anthony Manikhouth (DataDome R&D) in April 2026.

## How It Works

### Capability tier detection via availability

The Summarizer API (shipped in Chrome 138) requires a minimum hardware profile to run Gemini Nano locally:

- 22GB free storage on the Chrome profile volume
- GPU with strictly more than 4GB VRAM, OR CPU with 16GB+ RAM and 4+ cores
- Windows 10/11, macOS 13+, Linux, or ChromeOS on Chromebook Plus

Calling `await Summarizer.availability()` returns one of:

- `unavailable` — device has <4GB VRAM, <16GB RAM, or <4 CPU cores
- `downloadable` / `available` — device meets the threshold

This single call segments traffic into capability tiers. In DataDome's measurements, only **4% of global traffic** could run the Summarizer API, 50% could not due to insufficient hardware, and 46% was undefined (non-Chrome or unsupported). Because the feature is Chrome-exclusive, availability also reliably isolates genuine Chrome sessions.

### Cross-checking for spoofing inconsistencies

API availability is compared against other exposed properties to catch contradictions:

- If `navigator.hardwareConcurrency` reports fewer than 4 cores but Summarizer reports as available, the core count was likely spoofed.
- If the WebGL `UNMASKED_RENDERER_WEBGL` string suggests a recent MacBook and `navigator.deviceMemory` reports 16GB+, but Summarizer is unavailable, the session warrants scrutiny.

Maintaining a coherent hardware story across all of these surfaces simultaneously is the difficulty this imposes on a spoofed profile.

### Granular GPU class inference (LanguageModel)

The LanguageModel API (scheduled for Chrome 148) exposes multimodal text/image/audio support whose thresholds map to GPU performance classes. From the Chromium source (`components/optimization_guide/core/model_execution/performance_class.cc`):

- No support: GPU <3GB VRAM and CPU with <4 cores / <15GB RAM
- Text and image only: GPU 3–6GB VRAM and CPU below the threshold
- Text, image, and audio: GPU ≥6GB VRAM, or CPU with ≥4 cores and ≥15GB RAM

Each supported modality is a threshold test for a different hardware tier, giving a finer view than a single binary availability check.

### Inference timing fingerprinting

`LanguageModel.promptStreaming` streams the model response chunk by chunk. Two metrics, both measurable from JavaScript with `performance.now()`, characterize the device:

- **Time to First Token (TTFT)**: latency from prompt submission to first output chunk, reflecting input processing speed
- **Decode throughput**: output generation rate in tokens/second

The measurement approach mirrors the public PoC: wrap a `promptStreaming` loop in `performance.now()` timing, run warm-up passes to load model weights, then record TTFT and approximate throughput (≈4 characters per token). Mapping throughput and TTFT ranges to hardware clusters produces a performance fingerprint, conceptually similar to Google's Picasso or AudioContext timing fingerprinting. DataDome reports the values are relatively stable over time despite thermal throttling and load noise.

This connects directly to the [WebAssembly SIMD](../entities/webassembly-simd.md) timing approach: both measure real execution speed rather than declarative attributes, and both characterize the physical CPU/GPU.

## Where It Matters

For scrapers, this is a coherence trap. A scraper claiming to be a high-end MacBook while running on a low-spec cloud VM (or vice versa) is contradicted by the AI API availability and inference timing. The three options for an attacker are all costly:

- Actually own the hardware claimed (expensive at scale)
- Perfectly simulate AI inference timing (very hard)
- Accept that spoofed properties will be inconsistent with the performance tests (easily detected)

The technique is experimental as of April 2026: browser implementations are still evolving, timing is noisy, and future privacy mitigations may reduce precision. DataDome frames it as a cost-increase for attackers rather than a flawless identifier.

This signal exists because of the tension noted in [browser privacy fingerprinting defenses](./browser-privacy-fingerprinting-defenses.md): as classic declarative fingerprinting surfaces are being hardened, defenders shift toward signals tied to actual execution capability, which new browser features keep introducing.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [browser-privacy-fingerprinting-defenses](./browser-privacy-fingerprinting-defenses.md)
- [webassembly-simd](../entities/webassembly-simd.md)
- [Datadome](../entities/datadome.md)
- [canvas-fingerprinting](./canvas-fingerprinting.md)

## Sources

- Anthony Manikhouth (DataDome R&D) — "How Chrome's New AI Web APIs Are Enabling Hardware Fingerprinting," [https://datadome.co/threat-research/how-chromes-new-ai-web-apis-enable-hardware-fingerprinting/](https://datadome.co/threat-research/how-chromes-new-ai-web-apis-enable-hardware-fingerprinting/) (April 2026)
