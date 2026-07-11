---
name: fortress
type: entity
category: browser
first_seen: 2026-07-11
last_updated: 2026-07-11
sources:
  - blog-cloudflare-blocks-agents.md
---

# Fortress

## What it is

Fortress is an open-source stealth browser designed to bypass various anti-bot measures encountered on websites. It is built to ensure that agents can successfully read content even when sites employ sophisticated bot protection systems.

## How it works

Fortress employs various techniques to navigate protected sites. A single stealth fetch is sufficient for bypassing challenges like those from Cloudflare, CloudFront, and PerimeterX, allowing it to wait patiently through JavaScript challenges. For content that requires rendering, it handles Single Page Applications (SPA) and JavaScript-gated content by rendering the whole page to structured markdown. Furthermore, it utilizes a recon pass to monitor private API traffic, which can be effective for retrieving real JSON data from backend services.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The open-source build does not reach DataDome and click-walls, as these systems close the door before the application even boots, preventing any XHR requests from firing.

## Sources

- [https://tilion.dev/blog/cloudflare-blocks-agents](https://tilion.dev/blog/cloudflare-blocks-agents)
