---
name: Mouse Movement Emulation
type: concept
first_seen: 2024-01-01
last_updated: 2026-04-22
sources:
  - bypass-datadome-mouse-movements-in-playwright.md
  - oxymouse-and-playwright-mouse-movements.md
  - bezier-curves-web-scraping.md
  - https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering
---

# Mouse Movement Emulation

## Definition

Mouse movement emulation is the practice of generating pointer trajectories that match the statistical properties of human hand movement during browser automation. Anti-bot systems that monitor mouse events can distinguish between the instantaneous or straight-line movements produced by automation frameworks and the curved, velocity-varied paths that humans produce. Emulation attempts to make automated mouse behavior indistinguishable from real user input at the event listener level.

## How it works

Three algorithms appear in the TWSC source archive:

**Bezier curves (ghost-cursor approach)**

A Bezier curve defines a smooth path between a start point and an endpoint by pulling the trajectory toward one or more control points. The shape of the path varies based on control point placement; random control point selection produces organic-looking variety. Speed along the path follows a Fitts's Law model: fast during approach, decelerating near the target. The output is a sequence of intermediate coordinates sent to the browser's pointer event system via `mouse.move()`.

This is the approach used by [ghost-cursor](../entities/ghost-cursor.md) and its Python port `python_ghost_cursor`.

**Gaussian algorithm (OxyMouse)**

OxyMouse uses a Gaussian distribution to generate the random deviations that make the path look human. The path still travels from start to end, but small perturbations are drawn from a normal distribution rather than control-point-based curve interpolation. The result has slightly different statistical properties than Bezier curves: more granular noise rather than broad arcs.

**Perlin noise (OxyMouse)**

OxyMouse also implements a Perlin noise option. Perlin noise generates smooth, correlated random sequences rather than independent random samples, producing movement that has local continuity. The cursor does not jitter randomly between adjacent frames; instead, the deviations are locally smooth while varying over longer paths.

OxyMouse is a Python library specifically built for Playwright mouse emulation. It supports all three algorithms and is newer than ghost-cursor.

## Where It Matters

Which anti-bot systems actively use mouse movement for detection is not uniformly documented, but TWSC testing established the following:

- **DataDome**: actively monitors mouse events on hermes.com. Playwright's native `page.mouse.move()` produced linear, non-human trajectories that triggered a challenge. Substituting ghost-cursor's Bezier paths for the same navigation sequence passed the behavioral check. Mouse movement is a live detection signal for DataDome on at least this target.

- **Cloudflare**: does NOT use mouse event listeners, based on inspection of the injected JavaScript on tested pages. Mouse movement emulation has no effect on Cloudflare detection outcomes and can be omitted when targeting Cloudflare-protected pages.

- **Kasada**: has a `kpsdk-load` event that is triggered at load time. The role of mouse movement in Kasada's scoring was not specifically characterized in TWSC testing, but the presence of custom event monitoring indicates Kasada watches behavioral signals beyond mouse events.

## What We Tested

We used `python_ghost_cursor` with Playwright to bypass DataDome on hermes.com. The target required navigating dropdown menus that DataDome monitors. Native `page.mouse.move()` failed. Replacing it with ghost-cursor paths succeeded. The fix was surgical: only the mouse movement calls were changed, everything else in the script remained identical.

We also tested OxyMouse with Playwright against DataDome. The Gaussian and Perlin noise variants were both tested. Results confirmed that multiple algorithm implementations can satisfy DataDome's behavioral filter, suggesting DataDome is not looking for a specific movement curve shape but for signals of organic, velocity-varied motion in general.

The Bezier curve mathematical background: a cubic Bezier is defined by four points (P0, P1, P2, P3) where P0 and P3 are endpoints and P1, P2 are control points. The curve parameter t sweeps from 0 to 1. For mouse movement, the number of intermediate steps determines event resolution; more steps produce smoother apparent movement. The number of steps needed depends on the distance: longer paths need more steps to maintain realistic pixel-per-event density.

## The Defender's Perspective: Akamai MACT Detection (2024)

A detailed reverse-engineering post from mimic.sbs documents how a leaked Akamai mouse movement generator (called MACT — Akamai's internal term for mouse movement data) remained effective for two full years before Akamai managed to detect it.

The MACT algorithm works by generating anchor points along the trajectory at intervals determined by a cycle count, then linearly interpolating between them. A smoothing function using EWMA (Exponential Weighted Moving Average, λ=0.955) is applied to the result. This smoothing step caused the velocity profile to inadvertently mimic human movement by pure chance — because EWMA blends successive velocity values, the transitions between constant-speed segments look like natural acceleration curves.

The key fingerprinting insight: after applying the EWMA, the underlying piecewise-constant velocity structure can be partially reconstructed by inverting the smoothing formula. The reconstructed signal reveals that velocity is approximately constant within each segment — a statistical property that real human movement does not share. Akamai's delayed detection of the technique was attributed to a lack of a dedicated Threat Intelligence team focused on reverse-engineering bypass methods.

The practical implication for bot developers: the two attack vectors a defender would use are (1) comparing the smoothed signal to a smoothed version of the original (detecting the step-function structure), and (2) using a gradient-boosted decision tree on extracted velocity features. The correct countermeasure from the bot developer's side is to introduce genuinely non-constant velocity within each movement segment, not merely to smooth an otherwise mechanical pattern.

Akamai's mouse data is collected in 100-point samples. The cycle count parameter controls how many "stars" (velocity inflection points) appear in the trajectory.

## Current State

As of 2024-2025, mouse movement emulation is a solved problem for DataDome specifically: ghost-cursor and OxyMouse both work. The more important finding is that Cloudflare does not use mouse events at all, which means implementing Bezier curves for Cloudflare targets adds complexity with no benefit. Anti-bot-specific research is required to determine whether mouse emulation is necessary for a given target.

As of 2024-2026, Akamai's MACT analysis reveals that the defender's toolbox for detecting synthetic mouse movements includes: velocity profile reconstruction via EWMA inversion, gradient-boosted decision trees on velocity features, and simple segment-constancy tests. A mouse movement that passes velocity smoothness checks may still fail segment-uniformity checks if the underlying generation algorithm produces piecewise-constant motion.

## Related

- [ghost-cursor](../entities/ghost-cursor.md)
- [DataDome](../entities/datadome.md)
- [Cloudflare](../entities/cloudflare.md)
- [Kasada](../entities/kasada.md)
- [browser-fingerprinting](./browser-fingerprinting.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright](https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright)
- [https://substack.thewebscraping.club/p/oxymouse-and-playwright-mouse-movements](https://substack.thewebscraping.club/p/oxymouse-and-playwright-mouse-movements)
- [https://substack.thewebscraping.club/p/bezier-curves-web-scraping](https://substack.thewebscraping.club/p/bezier-curves-web-scraping)
- [https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering/](https://www.mimic.sbs/antibot/Improving-Antibot-Biometric-Protections-Through-Threat-Intelligence-And-Reverse-Engineering/)
