---
name: browser-fingerprint-scanner
type: entity
category: anti-bot
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - fingerprint-scan-com.md
---

# Browser Fingerprint Scanner

## What it is

The Browser Fingerprint Scanner is a tool designed to run live tests to inspect browser, device, WebRTC leak exposure, network signals, headers, GPU, DRM support, and automation indicators. It generates a fingerprint hash and a bot risk score to assess the risk level of a user or session.

## How it works

Browser fingerprinting is a technique used to identify and track users by analyzing characteristics of their browser and device. This involves collecting data such as the user agent string, GPU, timezone, and system information to create a unique fingerprint of the user's browser.

The bot risk score is calculated based on several factors, including the browser fingerprint, IP reputation, and proxy detection. This score ranges from 0 to 100, indicating the likelihood of the user being a bot.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Browser fingerprinting is not 100% unique, as users with similar hardware, such as iPhones and iPads, may have similar fingerprints. While attributes can be changed, some require dedicated browser extensions. Fingerprinting lies can be detected if inconsistencies are found, such as changing the user agent string while still using a Chrome browser.

## Related

* [device-and-browser-info](../entities/device-and-browser-info.md)
* [browser-fingerprinting](../concepts/browser-fingerprinting.md)
* [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://fingerprint-scan.com/](https://fingerprint-scan.com/)
