---
name: layer3-intel
type: entity
category: tool
first_seen: 2026-11-14
last_updated: 2026-11-14
sources:
  - security-2026-11-05-the-white-house-is-apparently-a-popular-residential-proxy-ex.md
---

# Layer3 Intel

## What it is

Layer3 Intel is a security firm that launched a Residential Proxy Observatory. This tool is designed to detect illicit activity involving residential proxy exit nodes.

## How it works

The Residential Proxy Observatory functions as a public interface to data Layer3 Intel has been collecting for approximately a year. This data is used to identify instances where devices on a network are acting as residential proxy exit nodes.

Residential proxies utilize IP addresses associated with residential internet connections as their exit nodes, distinguishing them from datacenter proxies. While many such services are legitimate, they can be exploited by threat actors for various cybercrimes, including concealing command-and-control infrastructure, conducting phishing attacks, and disguising malicious traffic.

## TWSC experience

Not yet tested by TWSC.
## Related

- [residential-proxy-observatory](../entities/residential-proxy-observatory.md)
- [residential-proxy](../entities/residential-proxy.md)
- [3rd-party-proxy](../entities/3rd-party-proxy.md)


## Sources

- [https://www.theregister.com/security/2026/11/05/the-white-house-is-apparently-a-popular-residential-proxy-exit-spot/5307969](https://www.theregister.com/security/2026/11/05/the-white-house-is-apparently-a-popular-residential-proxy-exit-spot/5307969)
