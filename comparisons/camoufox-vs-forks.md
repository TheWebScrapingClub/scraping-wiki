---
name: Camoufox vs its forks
type: comparison
subjects:
- camoufox
- camoufox-reverse
- LeooNic/camoufox
- JWriter20/camoufox
last_updated: '2026-06-04'
sources:
- lab-camoufox-forks-cloverlabs-draft.md
---

# Camoufox vs its forks

## What is being compared

After development of [Camoufox](../entities/camoufox.md) moved to CloverLabs in 2026, its public repository grew past 750 forks. Most are mirror bots with no commits of their own. This page compares stock Camoufox against the three forks that actually change anti-detect behavior, and records which one to run against a real target. The comparison is grounded in our 2026-06 testing against [Datadome](../entities/datadome.md) on leboncoin.fr, not on the forks' stated goals.

## Comparison table

| | Official Camoufox | [camoufox-reverse](../entities/camoufox-reverse.md) | LeooNic/camoufox | JWriter20/camoufox |
|---|---|---|---|---|
| Base Firefox | 135 stable, 146 (v146-hardware) | 135 | 149 | 146 |
| Headline change | baseline fingerprint DB + Juggler | engine-level PropertyTracer | content-aware canvas noise, humanized mouse, RDPBrowser | WebRTC-leak fix, system-ui font, pytest suite |
| Runs under standard Playwright stack | yes | yes (raw Playwright + CAMOU_CONFIG) | no, RDP only | yes |
| Canvas noise | off by default | n/a (tracer) | content-aware in source, not activatable in published build | inherits stock behavior |
| WebRTC under HTTP proxy | leaks real WAN IP (srflx) | n/a | not tested at runtime | no candidates, no leak |
| Datadome on leboncoin ad pages | ~0 to 5% blocked | n/a | not runnable | 100% blocked |
| What it is good for | default scraping | analyzing detectors | reading the canvas technique in source | closing a WebRTC leak with SOCKS |

## Key differences

The counterintuitive result is the one that matters. JWriter20 is the fork built to be stealthier, and it was blocked on every leboncoin ad page while stock Camoufox passed almost all of them. The block reproduced in both run orders and with the spoofed OS pinned, and the JS, TLS/JA3-JA4, and HTTP/2 fingerprints were identical between the two builds. So the signal Datadome reacts to is structural to the JWriter20 build, in its request or connection behavior, not in any static fingerprint. A more-patched fork is not automatically a safer one. See [webrtc-ip-leak](../concepts/webrtc-ip-leak.md) for the leak JWriter20 does fix.

LeooNic is the most ambitious on paper. Its content-aware canvas noise is a genuine answer to the WWW'25 Pixel-Recovery attack (see [canvas fingerprinting](../concepts/canvas-fingerprinting.md)), but the published Firefox 149 build does not launch under the standard Playwright stack and only runs through the author's own RDP tooling, and we could not activate the canvas seed externally. The innovation lives in the source, not yet in a usable artifact.

camoufox-reverse is not a contender at all. It is a measurement instrument: an engine-level PropertyTracer that shows which DOM getters a detector reads. We used it to watch Datadome on leboncoin, not to scrape.

## When to use which

For scraping a Datadome or Cloudflare target today, run stock official Camoufox on a clean residential IP, navigating from the homepage rather than deep-linking. It outperformed every fork in our testing. Reach for [camoufox-reverse](../entities/camoufox-reverse.md) when you want to understand what a detector reads, not to run production traffic. Consider JWriter20 only when a WebRTC leak under a proxy is your specific problem and you are on SOCKS5, and even then weigh it against its much higher Datadome block rate. Treat LeooNic as a source to read rather than a build to deploy until its Firefox 149 port stabilizes.

## Related

- [Camoufox](../entities/camoufox.md)
- [camoufox-reverse](../entities/camoufox-reverse.md)
- [canvas-fingerprinting](../concepts/canvas-fingerprinting.md)
- [webrtc-ip-leak](../concepts/webrtc-ip-leak.md)
- [Datadome](../entities/datadome.md)
- [anti-detect-browsers](../concepts/anti-detect-browsers.md)

## Sources

- TWSC Lab article, forthcoming 2026: "Is Camoufox still effective, and do the forks help?" (draft: `drafts/lab-camoufox-forks-cloverlabs-draft.md`)
- [daijro/camoufox](https://github.com/daijro/camoufox)
- [LeooNic/camoufox](https://github.com/LeooNic/camoufox)
- [JWriter20/camoufox](https://github.com/JWriter20/camoufox)
- [WhiteNightShadow/camoufox-reverse](https://github.com/WhiteNightShadow/camoufox-reverse)
