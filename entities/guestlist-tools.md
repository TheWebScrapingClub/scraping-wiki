---
name: guestlist-tools
type: entity
category: library
first_seen: 2026-06-09
last_updated: 2026-06-09
sources:
  - guestlist-tools.md
---

# guestlist-tools

## What it is

guestlist is a free Python library and HTTP API designed to check whether AI agents and computer-use agents can access specific websites. It provides tier ratings (green, yellow, orange, red) to indicate the likelihood of successful access for browser agents and helps prevent silent failures caused by anti-bot vendors such as Cloudflare, Akamai, DataDome, Imperva, and PerimeterX.

## How it works

The service continuously probes the web using real browsers to grade every domain from green to red based on the success rate of crawls. This allows users to determine whether AI agents are likely to get through a specific URL.

Users can utilize the library via a Python client to check access before spending requests. The results categorize domains into tiers: green (almost always access), yellow (usually access, expect retries), orange (sometimes access, use a stealth/proxy fallback), red (rarely access), and unknown (untested).

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://guestlist.tools](https://guestlist.tools)
