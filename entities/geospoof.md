---
name: geospoof
type: entity
category: browser
first_seen: 2026-07-03
last_updated: 2026-07-03
sources:
  - geospoof-com.md
---

# GeoSpoof

## What it is

GeoSpoof is a browser extension and application designed to match the user's VPN IP address to the browser's reported location, allowing it to spoof the geographical identity of the user. It functions as a VPN companion, ensuring that the browser's reported location accurately reflects the location associated with the active VPN server, even when switching servers.

## How it works

GeoSpoof overrides multiple browser APIs used by websites to detect location, such as `navigator.geolocation`, `Date`, `Intl.DateTimeFormat`, and the Temporal API, to spoof the user's coordinates and timezone. It also implements WebRTC protection to prevent IP leaks, ensuring that the browser's real IP address is not exposed.

The extension automatically detects the VPN exit region and syncs the spoofed location to match the current VPN server, providing consistent geographical identity across browsing sessions.

## TWSC experience

Not yet tested by TWSC.

## Related

- [browser-use](../entities/browser-use.md)
- [device-and-browser-info](../entities/device-and-browser-info.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)


## Sources

- [https://geospoof.com/](https://geospoof.com/)
