---
name: Static ISP Proxies
type: concept
first_seen: 2026-06-23
last_updated: '2026-06-24'
sources:
- https://www.youtube.com/watch?v=MQ1zpnlMMUc
- https://spur.us/blog/how-proxy-providers-co-opt-entire-networks
- femboyisp-purroute.md
---

# Static ISP Proxies

## Definition

Static ISP proxies are a hybrid category between datacenter and residential proxies. The IP addresses belong to real ISP allocations (Comcast, RCN, AT&T, Verizon) or to fabricated ISPs with fictional names. In both cases the server handling traffic is physically in a datacenter. The distinguishing characteristic is that the address block carries ISP reputation rather than datacenter ASN reputation, and the IP stays assigned to a single customer for weeks or months rather than rotating.

Two distinct subcategories exist. The first uses genuine ISP space leased from organizations that own legacy IP blocks — universities, small regional ISPs, school districts — via IP leasing marketplaces or direct BYOP (bring your own prefix) arrangements with real ISPs. The second uses address blocks allocated to fake ISPs: fictitious organizations with a website that fails even a cursory legitimacy test, routed through datacenter infrastructure.
 
## How It Works

### Sourcing from Real ISPs

Two main paths for obtaining genuine ISP space:

**BYOP (Bring Your Own Prefix)**: An operator acquires a subnet (typically a /24) via a leasing service such as [IPXO](../entities/ipxo.md), registers an organization name, and presents it to a real ISP as a business customer. The ISP announces the prefix through its own ASN. The resulting traffic appears to originate from that ISP's network. AT&T terminated this arrangement for operators without their own ASN in September 2025 — customers were required to bring a dedicated ASN or lose the route. The number of AT&T-based static ISP proxies dropped sharply after that change, though some legacy arrangements persist.

**Business line acquisition**: Operators obtain a subnet by registering as a small Comcast business customer or similar. A claimed small business (a coffee shop, for instance) can receive a /24 through this channel.

**Leasing from existing IP holders**: Organizations holding large, unused legacy allocations can lease those blocks to IP leasing intermediaries without transferring ownership. This lets the original holder monetize an idle asset and reclaim it when needed. Pricing for a /16 in the United States is around $13,000/month. The negative reputation accumulated during the lease period typically persists in threat intelligence and blocklist databases even after reclamation.

### Fake ISPs

Some static ISP proxies use fabricated ISP identities — invented names, a minimal website, no actual customers. These often advertise service tiers (fiber speeds, coverage areas) whose backend returns a hardcoded "not available" response regardless of input. Their IP blocks are almost exclusively leased through IPXO. Geo feeds from fake ISPs are unreliable: a provider claiming nationwide coverage may route all traffic through a single datacenter in Los Angeles.

### Sale Structure

Static ISP proxies are sold per IP address rather than per bandwidth:

- **Shared**: multiple customers use the same IP simultaneously
- **Semi-dedicated**: sold to a maximum of 2–3 customers
- **Dedicated**: one customer per IP for the lease duration

Bandwidth cost is roughly one-tenth of equivalent residential proxy bandwidth because there is no end user being compensated for network usage. The IPs are available full-time without the churn caused by DHCP reassignment in real residential networks.

## Where It Matters

**Account management**: A static IP held for months lets an operator build stable platform reputation tied to that address. Rotating residential proxies lose session continuity and force re-authentication. Account management workflows frequently require one IP per account.

**Anti-bot evasion**: The IP carries ISP reputation rather than datacenter ASN reputation. IP reputation lookups classify it as residential or ISP, not cloud infrastructure. The addresses are absent from standard datacenter ASN blocklists.

**Performance**: Because there is no callback infrastructure (unlike rotating residential proxies), response times are comparable to datacenter proxies — milliseconds rather than hundreds of milliseconds.

**No bandwidth billing**: Unlike residential proxies, static ISP proxies are not billed per GB. High-bandwidth activities do not carry disproportionate cost.

## Detection

### Traditional Static ISP Proxies (Tunnel Classification)

When the entire surrounding subnet is used exclusively for proxying and contains no real users, threat intelligence systems classify these IPs as **tunnels**. The tunnel label indicates that blocking the IP carries no collateral damage risk to legitimate users.

The presence of `abuse.radar.com` (IPXO's abuse reporting mechanism) as the abuse contact in WHOIS is a strong indicator that a block is IPXO-leased and proxy-destined. Ashburn, Virginia concentrates a disproportionate share of static ISP proxy infrastructure. Filtering what routes through Ashburn is a practical high-recall heuristic for the US market.

### Fake ISP Detection

Fake ISPs share a consistent set of indicators: datacenter routing despite ISP branding, IPXO-leased ranges, geo feeds that contradict the actual server location, and websites with non-functional signup forms.

### GRE Tunnel Variant (Client Proxy Classification)

A separate architecture co-opts real ISP border routers through GRE tunnels and policy-based routing, installed on the partner ISP's own equipment by an intermediary that resells the resulting capacity. Because real users exist on those ISP allocations, these IPs cannot be treated as pure tunnels. Threat intelligence systems classify them as **client proxies** instead, indicating collateral damage risk if blocked at the IP level.

Outbound connections from this architecture use TCP source ports in the range **40,000–40,200**. The partner ISP's edge router matches return traffic by destination port (same range) and routes it through the GRE tunnel via connection marks. Observing multiple connections from the same IP where every source port falls within this 200-wide window is a reliable detection signal. The infrastructure is also discoverable via passive DNS, since each partner ISP is given a dedicated GRE endpoint subdomain following an `rtr-<isp-name>` naming pattern, most of them resolving to a small number of centralized PoPs.

## Current State

As of late 2025 / early 2026:

- AT&T's policy change requiring BYOP operators to supply their own ASN has reduced AT&T-based static ISP proxy inventory. Some legacy arrangements persist.
- RCN is the dominant US provider of real ISP space used for static ISP proxying.
- Ashburn, Virginia remains the primary concentration point for US static ISP infrastructure.
- The border router co-option model described above represents a distinct and harder-to-block trajectory from the traditional leasing approach.

## Related

- [proxy-fundamentals](./proxy-fundamentals.md)
- [IPXO](../entities/ipxo.md)
- [mobile-proxy-farming](./mobile-proxy-farming.md)
- [web-unblockers](./web-unblockers.md)

## Sources

- Spur research team (Riley Kilmer, Sean) — YouTube webinar on static ISP proxy sourcing and detection, [https://www.youtube.com/watch?v=MQ1zpnlMMUc](https://www.youtube.com/watch?v=MQ1zpnlMMUc) (2025/2026)
- Spur — "How Proxy Providers Co-opt Entire Networks," [https://spur.us/blog/how-proxy-providers-co-opt-entire-networks](https://spur.us/blog/how-proxy-providers-co-opt-entire-networks)
