---
name: sec-ch-ua-form-factors
type: entity
category: anti-bot
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-sec-ch-ua-forms-factor.md
---

# Sec-CH-UA-Form-Factors

## What it is

Sec-CH-UA-Form-Factors is a new client hint supported by Chrome, introduced starting from version 124, as part of the privacy sandbox project. This hint describes how a user interacts with the browser or device, such as whether the interaction is occurring on a desktop, automotive device, mobile device, tablet, XR device, EInk device, or a watch.

## How it works

This client hint is designed to help websites customize resources and presentation based on the type of device the user is employing, aiming to provide a better user experience. It helps websites avoid relying on fragile user-agent detection methods.

The possible values for this hint include "Desktop", "Automotive", "Mobile", "Tablet", "XR", "EInk", or "Watch". Google concluded that there is no risk of active fingerprinting, as these factors can already be retrieved from the user agent.

## TWSC experience

Not yet tested by TWSC.

## Related

* [device-and-browser-info](../entities/device-and-browser-info.md)
* [http_headers](../entities/hrequests.md)
* [browser-fingerprinting](../concepts/browser-fingerprinting.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/sec-ch-ua-forms-factor](https://deviceandbrowserinfo.com/learning_zone/articles/sec-ch-ua-forms-factor)
