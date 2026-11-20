---
name: vpndetection
type: entity
category: tool
first_seen: 2026-11-20
last_updated: 2026-11-20
sources:
  - vpndetection-io.md
---

# VPNDetection

## What it is

VPNDetection is a service that identifies and classifies IP addresses, providing detailed information about their nature. It can detect and label IP addresses associated with VPNs, hosting servers, Tor nodes, Content Delivery Networks (CDNs), privacy relays, and various types of proxies including residential, datacenter, mobile, and public proxies. The service also aims to identify the specific operator behind these IP addresses.

## How it works

VPNDetection offers an API that returns multiple flags for a single IP address lookup. These flags indicate whether the IP is a VPN, hosting server, Tor node, CDN edge, privacy relay, or a specific type of proxy (residential, datacenter, mobile, public). For each identified category, the service provides the name of the operator, the last time the address was observed in that role, and a confidence level.

The service also provides downloadable databases in CSVGZ or MMDB formats, updated daily, which contain comprehensive lists of IP addresses categorized by their function (e.g., VPN IP, Hosting IP, Tor IP). These databases can be run locally on a user's own servers for offline lookups.

## TWSC experience

Not yet tested by TWSC.
## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [residential-proxy](../entities/residential-proxy.md)
- [residential-proxy-ips](../entities/residential-proxy-ips.md)


## Sources

- [https://vpndetection.io](https://vpndetection.io)
