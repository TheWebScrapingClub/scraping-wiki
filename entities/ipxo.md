---
name: IPXO
type: entity
category: proxy-provider
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
- https://www.youtube.com/watch?v=MQ1zpnlMMUc
- https://spur.us/blog/how-proxy-providers-co-opt-entire-networks
---

# IPXO

## What It Is

IPXO is an IP address leasing marketplace. Organizations holding large IPv4 allocations — universities, school districts, regional ISPs, and other early adopters with legacy blocks — can monetize unused space by leasing it through IPXO without permanently transferring ownership. Operators building static ISP proxy infrastructure use IPXO to acquire prefixes, which they then announce via BYOP arrangements with real ISPs.
 
## How It Works

A lessee acquires a prefix through IPXO, registers an organization name or customer identifier, and takes the prefix to an ISP for routing under a BYOP arrangement. The traffic produced by those IPs appears to originate from a genuine ISP network. IPXO facilitates the IP address supply side; the lessee handles downstream routing and proxy infrastructure.

IPXO operates its own abuse reporting infrastructure at `abuse.radar.com`. This URL appearing as the abuse contact in a WHOIS record is a reliable indicator that a block is IPXO-leased. Spur researchers report that the overwhelming majority of static ISP proxy abuse investigations they encounter trace back to this abuse contact, making it a high-precision filter for identifying IPXO-leased proxy infrastructure.

## TWSC Experience

No direct TWSC testing of IPXO as a platform. IPXO ranges were identified incidentally during a 2024 proxy provider quality benchmark, where one provider was found selling datacenter IPs from IPXO ranges while marketing them as residential. See [proxy-fundamentals](../concepts/proxy-fundamentals.md).

## Known Limitations

- IP blocks leased through IPXO accumulate negative reputation as they are used for proxying. When the original holder reclaims a block, that reputation persists in most threat intelligence and blocklist services. Reclamation does not reset the abuse history.
- Multiple organizations appearing in abuse reports for the same block (the original IP holder, IPXO, and a downstream reseller) create ambiguity about the correct escalation path for abuse resolution.

## Related

- [static-isp-proxies](../concepts/static-isp-proxies.md)
- [netnut](./netnut.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)

## Sources

- Spur research team (Riley Kilmer, Sean) — YouTube webinar on static ISP proxy sourcing and detection, [https://www.youtube.com/watch?v=MQ1zpnlMMUc](https://www.youtube.com/watch?v=MQ1zpnlMMUc) (2025/2026)
