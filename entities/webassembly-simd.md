---
name: webassembly-simd
type: entity
category: library
first_seen: 2026-05-20
last_updated: 2026-06-23
sources:
  - writing-wasm-simd-fingerprinting.md
  - https://blog.azerpas.com/writing/wasm-simd-fingerprinting
---

# WebAssembly SIMD

## What it is

WebAssembly SIMD refers to Single Instruction, Multiple Data operations introduced to the WebAssembly specification. These operations define a portable subset of vector instructions that typically map directly to hardware-native instructions on the host CPU. The execution latency of those instructions varies across CPU models by physical circuit design, pipeline depth, and execution unit efficiency — a variation that can be measured from within a browser and used for hardware fingerprinting.

## How the fingerprinting works

Browser engines (V8 in Chrome, JavaScriptCore in Safari) compile WASM SIMD operations to native machine code. For operations like complex byte permutations (`i32x4_shuffle`, `i64x2_shuffle`), CPUs without a dedicated hardware path emit a multi-instruction software emulation fallback. The latency gap between the hardware-native path and the emulation path is stable, hardware-specific, and measurable.

The measurement method: chain the SIMD operations in a dependency loop so each output feeds the next, then run that loop for millions of iterations. Dividing the total elapsed time by the iteration count reduces the impact of `performance.now()`'s 0.1ms quantization floor. The result is a per-operation latency profile that characterizes the underlying CPU.

Operations tested include floating-point (`f32x4_div`, `f32x4_*`), integer (`i16x8_*`), permutation (`i8x16_shuffle`, `i64x2_shuffle`), bitwise, and type conversion groups.

## Empirical results (azerpas, May 2026)

Anthony Manikhouth built and evaluated this system across 2,124 unique devices: 1,501 mobile, 623 desktop. Source platforms: BrowserStack real devices, AWS/GCP/Vast.ai bare metal.

Classification model: K-Nearest Neighbors (k=5) with distance weighting, using per-operation timing vectors as features. Evaluation method: Leave-One-Out (LOO) cross-validation.

Results after iterative model improvements (filtering CPUs with <10 training runs, using fastest-raw-sample per op instead of median, grouping Apple Pro/non-Pro variants):

| Engine | CPU accuracy | Brand accuracy |
|--------|-------------|----------------|
| V8 (Chrome) | 82.1% | 95.2% |
| JSC (Safari) | ~80% | 100% |

Per-CPU highlights for V8:
- AMD Ryzen 5 9600X: 100% (29/29)
- Snapdragon 8 Elite: 94% (247/264)
- Google Tensor G2: 58% (73/125) — shares architecture with G3, frequently confused
- Intel Core i7-7700K: 25% — low training count, not representative

PCA of V8 runs shows Intel and AMD clusters clearly isolated, with the first two principal components capturing 92% of variance. t-SNE distinguishes AMD EPYC generations from 2021 to 2025. Apple A19 family is well isolated from earlier chips in JSC runs; A16 and M2 (both 2022) cluster closely due to architectural overlap.

## Spoofing and stability

**Performance.now() jitter**: injecting noise into the timer would appear as an unknown trace rather than a known CPU profile, which is counterproductive for an attacker trying to impersonate a real user's device.

**Relative ratio robustness**: the signal relies on ratios between dozens of operation latencies, not absolute timing. Random jitter on start/end timestamps does not destroy the ratio structure.

**Compiler drift**: if V8 optimizes its `i8x16_shuffle` lowering, the baseline shifts overnight. Stable fingerprinting requires operations that map 1:1 to native instructions across all engines, minimizing the compilation layer between measurement and hardware.

**Dynamic challenge defense**: a server could issue a parameterized benchmark challenge that forces the client to recompute the trace for a specific operation set, preventing pre-harvested replay.

## Engine variance

The same physical hardware yields different timing profiles depending on the engine. On an M3 MacBook, `f32x4_div` varies by ~25% between V8 and JSC. Any classifier must be engine-specific; a model trained on V8 data does not generalize to JSC runs.

## Implications for scraping

A fingerprinting system using WASM SIMD timing can identify the CPU model powering a scraper with ~82% accuracy. Device farms (AWS, GCP, Vast.ai) expose their server CPU models (AMD EPYC, Intel Xeon generations) through this signal. A scraper claiming to be a consumer iPhone while running on a Xeon would be contradicted by the SIMD timing profile.

This technique is not yet deployed in production bot detection stacks as of May 2026 — it is at the research/PoC stage. The author is collecting organic telemetry from real users to refine the training data.

## TWSC experience

Not tested by TWSC. Research documented here is from Anthony Manikhouth (azerpas.com, May 2026).

## Related

- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [canvas-fingerprinting](../concepts/canvas-fingerprinting.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)

## Sources

- Anthony Manikhouth — "Fingerprinting CPUs from the Browser with WebAssembly SIMD," [https://blog.azerpas.com/writing/wasm-simd-fingerprinting](https://blog.azerpas.com/writing/wasm-simd-fingerprinting) (May 2026)
