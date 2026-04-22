---
name: ghost-cursor
type: entity
category: library
first_seen: 2024-01-01
last_updated: 2026-04-22
---

# ghost-cursor

## What it is

ghost-cursor is a library originally written in JavaScript by Xetera that generates realistic mouse movement paths. The Python port is `python_ghost_cursor`. It is not a browser automation tool itself: it plugs into an existing automation session ([Playwright](playwright.md), for example) and replaces the tool's native pointer movement with human-like trajectories.

## How it works

The library generates mouse paths using Bezier curves, which produce the smooth, slightly irregular arcs characteristic of human hand movement rather than the straight-line or instant jumps that automated tools produce by default. Speed along the path follows a Fitts's Law profile: movement is fast during the initial approach to a target and slows down as the cursor gets close. This matches real motor behavior, where precision increases as the hand decelerates near the target.

The output is a sequence of intermediate coordinates that the automation tool moves through sequentially, simulating continuous cursor motion at the event level.

## TWSC experience

We used `python_ghost_cursor` with [Playwright](playwright.md) to bypass [Datadome](datadome.md) behavioral analysis on hermes.com. The target required navigating through menus that Datadome monitors for interaction quality. Playwright's native `page.mouse.move()` produces movement that Datadome classifies as automated, triggering the challenge response. Substituting ghost-cursor's Bezier paths for the same navigation sequence passed the behavioral check and allowed full menu navigation to complete.

## Alternative: OxyMouse

OxyMouse is a newer Python library for Playwright mouse emulation that provides three movement algorithm options: Bezier curves (the same model as ghost-cursor), Gaussian (random walk with normal-distribution deviations), and Perlin noise (smooth, correlated random sequences). OxyMouse was built specifically for Playwright and does not have a JavaScript equivalent.

TWSC tested OxyMouse against DataDome and found that all three algorithm variants passed DataDome's behavioral filter on the tested targets. The implication is that DataDome is not detecting a specific movement curve shape but rather the absence of velocity variation and path curvature that flat automation produces.

The mathematical basis for the Bezier approach: a cubic Bezier curve is defined by start point, two control points, and an endpoint. The curve parameter t sweeps from 0 to 1. Control point placement determines path curvature. Randomizing control point positions per movement generates variety. The number of intermediate steps scales with path distance to maintain realistic pixel-per-event density.

## Anti-bot mouse tracking observations

Based on TWSC testing:

- **DataDome**: actively monitors mouse events. Native `page.mouse.move()` fails. Ghost-cursor or OxyMouse paths pass.
- **Cloudflare**: does NOT use mouse event listeners based on inspection of injected JavaScript on tested pages. Bezier curve implementation has no effect on Cloudflare detection outcomes.
- **Kasada**: monitors a `kpsdk-load` event and other behavioral signals. The specific role of mouse movement in Kasada's scoring model was not isolated in TWSC testing.

## Known limitations

- ghost-cursor addresses only the mouse movement signal. Datadome and similar systems monitor multiple behavioral dimensions simultaneously. Passing the mouse movement check is necessary but may not be sufficient if other signals (keyboard patterns, scroll behavior, timing distributions) are flagged.
- The library generates plausible paths but they are still generated. Sufficiently sophisticated behavioral analysis that trains specifically on ghost-cursor output could identify the distribution.
- ghost-cursor is JavaScript-first. The Python port (`python_ghost_cursor`) tracks the JS version but may lag behind in updates.

## Related

- [playwright](playwright.md)
- [Datadome](datadome.md)
- [mouse-movement-emulation](../concepts/mouse-movement-emulation.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)

## Sources

- [https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright](https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright)
- [https://substack.thewebscraping.club/p/oxymouse-and-playwright-mouse-movements](https://substack.thewebscraping.club/p/oxymouse-and-playwright-mouse-movements)
- [https://substack.thewebscraping.club/p/bezier-curves-web-scraping](https://substack.thewebscraping.club/p/bezier-curves-web-scraping)
