---
name: who-1ms-dog
type: entity
category: tool
first_seen: 2026-11-14
last_updated: 2026-11-14
sources:
  - who-1ms-dog.md
---

# who.1ms.dog

## What it is

1ms.dog is a website that tests and reveals browser fingerprinting signals to users. It aims to help users understand how websites identify them by collecting and displaying a comprehensive list of signals that can be used to create a unique browser fingerprint.

## How it works

The website collects various signals from the user's browser and device, including IP address, location, language, screen resolution, fonts, browser type, and TLS/HTTP fingerprints. It then presents these signals in a human-readable format, explaining what each signal means and how it contributes to a browser's fingerprint. The site also provides statistics on how often certain signals are used to identify users and offers tools to compare fingerprints over time or across different browsers.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The website notes that if a user is accessing it through an in-app browser (like those in WeChat or other applications), the results will reflect the fingerprint of that in-app browser, not the user's primary browser (e.g., Safari or Chrome). Users are advised to copy the link and open it in their preferred browser for a more accurate test of their usual browsing environment.

## Related

- [browser-fingerprint-scanner](../entities/browser-fingerprint-scanner.md)
- [Cloudflare](../entities/cloudflare.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)


## Sources

- [https://who.1ms.dog/](https://who.1ms.dog/)
