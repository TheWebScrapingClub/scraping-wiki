---
name: farmfence
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - package-farmfence.md
---

# farmfence

## What it is

farmfence is a TypeScript package that provides functions for detecting and flagging traffic originating from known bot farms, scrapers, and headless probes. It is designed to help identify traffic that resembles installs or visits but does not originate from a real user.

## How it works

The package provides install helpers that combine IP, locale, geo, and funnel signals to determine bot likelihood. It also offers web and IP-only checks for coarser detection. Users can utilize functions to check specific signals, such as identifying datacenter crawler IPs, likely bot IPs, or specific headless probe payloads.

## TWSC experience

Status: experimental `0.x`. It was extracted from a real product and is useful for dogfooding, but it is not yet a general-purpose bot filter.

## Known limitations

*   `isDatacenterCrawlerIp` includes large AWS us-west-2 and us-east-1 EC2 ranges, not only Device Farm or Facebook fetchers. This footprint covers a lot of Oregon and Northern Virginia EC2 (VPNs, backends, corporate egress).
*   Coarse `isLikelyBotIp` Google/Apple prefixes should be used as soft signals, not drop rules. Ashburn city/region alone is never a bot signal; only EC2 CIDRs, or Ashburn plus UTC/headless/POSIX corroboration on the web probe helper are signals.
*   `Boardman / The Dalles / Falkenstein (Hetzner) city + shallow visit` is a bot signal due to the lack of residential web egress.
*   `zh-CN alone` is never a bot signal (due to diaspora or VPN usage).

## Related

- [bot-detection-system](../entities/bot-detection-system.md)
- [playwright](../entities/playwright.md)
- [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)


## Sources

- [https://www.npmjs.com/package/farmfence](https://www.npmjs.com/package/farmfence)
