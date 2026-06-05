---
name: canvas-fingerprinting
type: concept
first_seen: 2024-10-24
last_updated: '2026-06-04'
sources:
- scraping-datadome-camoufox.md
- dbi-privacy-leak-detecting-canvas-countermeasures.md
---

# Canvas Fingerprinting

## Definition

Canvas fingerprinting is a stateless tracking technique that identifies a device by drawing graphics off-screen and hashing the resulting pixels. Two machines asked to render the same text and shapes produce subtly different pixel output, because the final image depends on the GPU, the graphics driver, the font rasterizer, and the anti-aliasing settings of that specific machine. The hash of those pixels becomes a high-entropy identifier that needs no cookie and survives incognito mode and cache clears.

It is one signal inside the broader practice of [browser fingerprinting](./browser-fingerprinting.md). It is singled out here because it carries an unusually large amount of entropy and because it is the surface where the most interesting attack-and-defense work of 2025 and 2026 has happened.

### Terms used on this page

**Canvas.** The HTML `<canvas>` element is a programmable drawing surface introduced with HTML5. A script gets a drawing context with `canvas.getContext('2d')` (or `'webgl'` for 3D), then issues commands like `fillRect`, `fillText`, and `arc`. The canvas is a bitmap: every pixel holds four values, red, green, blue, and alpha (opacity), each from 0 to 255. A 500x400 canvas is therefore an array of 500 x 400 x 4 = 800,000 numbers. Nothing has to be visible on screen for this to work, so fingerprinting scripts draw into a canvas that is never attached to the page.

**Readback APIs.** A script reads the pixels back with `getImageData()`, which returns the raw RGBA array, or serializes the whole canvas to a string with `toDataURL()` or `toBlob()`. These three calls are the moment the fingerprint leaves the canvas, and they are exactly what detection scripts call and what defenses try to perturb.

**Flat region.** A contiguous block of pixels that are all the same color, or that change only gradually, like the inside of a solid `fillRect` or a smooth gradient. Formally, a pixel sits in a flat region when the largest per-channel difference between it and its neighbors is below a small threshold. Flat regions matter because they are predictable: a detector that paints a solid block knows exactly what every pixel should read back as.

**Edge / textured region.** The opposite of a flat region. Pixels around the boundary of a shape or a glyph, where neighboring colors differ sharply. Real hardware variation (anti-aliasing, sub-pixel rendering) shows up mostly here, which is why edges carry most of the genuine fingerprinting entropy.

**Noise.** The small per-pixel changes a privacy defense adds to the canvas so the hash is not stable across sites or sessions. The whole fight is about whether that noise can be predicted and removed.

## How It Works

A fingerprinting script renders a fixed payload, usually a line of text in several fonts plus a few colored shapes and curves, into an off-screen canvas. It then calls `toDataURL()` or `getImageData()` and hashes the bytes. Because the script controls the drawing commands, the only thing that varies between machines is how the device turns those commands into pixels. That variation is stable for a given device and noisy across devices, which is precisely what a tracker wants.

The technique is passive. There is no prompt, no permission, and nothing visible. It was first documented by Mowery and Shacham in 2012 and was found in active use across thousands of top sites by later measurement studies.

On its own a canvas hash is not a perfect identifier, but combined with fonts, WebGL, screen geometry, and the navigator object it pushes the joint fingerprint close to unique. Coherence is enforced across these signals: a canvas that renders like a Mac while the User-Agent claims Windows is itself a red flag, the same way a [TLS fingerprint](./tls-fingerprinting.md) that disagrees with the User-Agent is.

## Defenses, and how they break

There are four families of defense, in rough order of how disruptive they are to legitimate sites.

**Blocking.** Disable the canvas readback APIs entirely. Effective but it breaks any site that legitimately uses canvas for charts, games, or image editing, so browsers rarely do this by default.

**Fixed output.** Always return the same constant pixels. Stable, but trivially detected, because a real device never returns a perfectly constant canvas.

**Randomized output (the dominant approach).** Add a little noise to the pixels so the hash changes and cannot be correlated. This is what Brave's Farbling does, what Firefox's resist-fingerprinting mode does, what most privacy extensions do, and what anti-detect browsers such as [Camoufox](../entities/camoufox.md) do.

**Filter lists.** Block known fingerprinting scripts by URL. Useful but always behind the latest trackers.

The interesting failure is in randomized output, and it was made concrete by a 2025 academic paper. In *Breaking the Shield: Analyzing and Attacking Canvas Fingerprinting Defenses in the Wild* (Hoang Dai Nguyen and Phani Vadrevu, Louisiana State University, The Web Conference 2025), the authors tested 18 extensions and 5 browsers and showed that most randomized-output defenses can be reversed.

Their **Pixel-Recovery attack** works like this. The defenses they studied apply a single perturbation vector `P(R,G,B,A)` uniformly across the canvas for a given session, and that vector depends only on a seed and the pixel position, not on what is actually drawn. The attacker draws two canvases: a **Base Canvas** filled with a known uniform color (the paper uses `RGBA(150,150,150,0.5)`), and a **Filled Canvas** with real fingerprinting content. Because the Base Canvas values are known in advance, the attacker compares what reads back against what should be there, solves for `P`, then subtracts `P` from the Filled Canvas and recovers the true, un-noised fingerprint. The authors confirmed it by reloading ten times: the recovered Filled Canvas hash stayed constant while the Base Canvas hash changed per load, proving the noise was reversible.

The same paper shows why **Brave's Farbling resists** the attack, and this is the important part for scraping. Farbling does not use a position-only seed. It derives a per-session canvas key from three things, the session key, the domain, and the content of the canvas itself, then perturbs only one color channel (chosen from the domain) and uses an LFSR to scatter which pixels get touched. Because the key depends on the canvas content, two different canvases are perturbed differently even in the same session and domain, so there is no single `P` to solve for. Content-dependent noise cannot be subtracted out.

**Content-aware noise** is the defense that follows from this result. The idea is to skip flat regions so that a known-pixel check on a solid block sees no tampering, perturb only edge and textured pixels, and make each perturbation depend on the pixel content and its neighbors rather than on position alone. This is the design the [Camoufox](../entities/camoufox.md) fork by LeooNic implemented in its `canvas-spoofing.patch`, whose comments cite the Nguyen and Vadrevu attack by name. It is, in effect, Brave-style Farbling ported into Camoufox.

## Where It Matters

[Datadome](../entities/datadome.md) is the anti-bot in the TWSC corpus most clearly tied to canvas. It has been observed using Picasso, a Google-designed canvas technique that renders a controlled geometric pattern rather than arbitrary text, which makes it harder to defeat with blind noise because the detector knows the exact rendering it expects (see the Picasso section in [browser fingerprinting](./browser-fingerprinting.md)). The "known-pixel check" framing in the LeooNic patch comments names Datadome and Castle as the systems whose flat-region checks it tries to pass.

For a scraper the practical point is that canvas noise is a double-edged tool. Too little and the canvas is a stable identifier. Too much, applied uniformly, and a Pixel-Recovery style detector can both strip the noise and notice that a solid block was tampered with, which is itself an automation signal.

## What We Tested

During our 2026 analysis of the Camoufox fork ecosystem we instrumented the canvas surface directly. Using camoufox-reverse, a fork that adds an engine-level PropertyTracer to SpiderMonkey, we watched which DOM getters Datadome's script reads on leboncoin.fr. On a car listing page the script called `canvas.toDataURL` and `canvas2d.getImageData`, alongside `webgl.getParameter` and `offscreenCanvas.getContext`, confirming that the canvas readback is part of the live fingerprint Datadome collects, not just a theoretical surface.

We also measured how Camoufox's own canvas noise behaves. Current builds ship with canvas pixel noise disabled by default, which lines up with a CloverLabs "Disable Canvas Noise" commit. When we forced the noise on (it activates only when `canvas:seed` is non-zero), the stock algorithm perturbed roughly half of every pixel including flat solid fills (9105 of 18240 interior pixels in our two-block probe), with a per-channel delta of one and a hash that varied per session. That is the uniform, position-seeded style the Pixel-Recovery attack is built to reverse, and it is the behavior LeooNic's content-aware patch was written to replace. We confirmed the LeooNic algorithm by reading its source, but could not exercise it at runtime: the published Firefox 149 build does not launch under the standard stack (more in the Camoufox page).

## Current State

As of 2026-06, randomized canvas noise is the mainstream defense and the Pixel-Recovery result has made plain that position-seeded uniform noise is reversible. The defensive frontier is content-dependent, per-session noise in the Brave Farbling style. Among open-source anti-detect browsers, the technique exists in fork source (LeooNic's Camoufox patch) but not yet in a build that runs out of the box, so the practical state for scrapers is that stock Camoufox simply leaves canvas noise off and relies on a realistic Firefox fingerprint plus a clean IP rather than on canvas randomization.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [tls-fingerprinting](./tls-fingerprinting.md)
- [bot-detection](./bot-detection.md)
- [anti-detect-browsers](./anti-detect-browsers.md)
- [Camoufox](../entities/camoufox.md)
- [Datadome](../entities/datadome.md)
- [camoufox-reverse](../entities/camoufox-reverse.md)
- [canvas-fingerprint-defender](../entities/canvas-fingerprint-defender.md)
- [Camoufox vs forks](../comparisons/camoufox-vs-forks.md)

## Sources

- [https://substack.thewebscraping.club/p/scraping-datadome-camoufox](https://substack.thewebscraping.club/p/scraping-datadome-camoufox)
- [https://deviceandbrowserinfo.com/learning_zone/articles/privacy-leak-detecting-canvas-countermeasures](https://deviceandbrowserinfo.com/learning_zone/articles/privacy-leak-detecting-canvas-countermeasures)
- [Breaking the Shield: Analyzing and Attacking Canvas Fingerprinting Defenses in the Wild (WWW 2025)](https://dl.acm.org/doi/abs/10.1145/3696410.3714713)
- [Breaking the Shield (author PDF)](https://www.phanivadrevu.com/files/papers/canvas_fp.pdf)
- [canvas-fp-attacks (paper code)](https://github.com/madwish-lab-lsu/canvas-fp-attacks)
- [LeooNic Camoufox fork](https://github.com/LeooNic/camoufox)
- [camoufox-reverse fork (PropertyTracer)](https://github.com/WhiteNightShadow/camoufox-reverse)
