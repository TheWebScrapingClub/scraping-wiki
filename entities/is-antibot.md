---
name: is-antibot
type: entity
category: library
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - antibot-microlink-io.md
---

# is-antibot

A library that detects antibot and CAPTCHA challenges from 30+ providers using signals.

## How it works

At a high level, **is-antibot** classifies challenge responses using:

- **HTTP status patterns**: Certain platforms use unusual status codes when blocking automation; for example, LinkedIn can return `999` and Reddit can return `403` on challenge flows.
- **Known challenge signatures**: Challenge pages often include recognizable artifacts like CAPTCHA widgets, interstitial templates, or verification scripts.
- **Response headers and body markers**: Blocking responses usually expose hints in headers and HTML, such as mitigation headers, challenge tokens, or provider-specific script references.
- **Provider-specific fingerprints**: Each provider leaves a distinct combination of signals; for example, Cloudflare commonly surfaces `cf-mitigated: challenge`, while other providers rely more on cookie, URL, or HTML fingerprints.

Each provider has unique fingerprints across one or more of these signals. The library checks them in priority order and returns the first match.

## TWSC experience

Not yet tested by TWSC.

## Related

- [Cloudflare](../entities/cloudflare.md)
- [AWS WAF](../entities/aws-waf.md)


## Sources

- [https://antibot.microlink.io/](https://antibot.microlink.io/)
