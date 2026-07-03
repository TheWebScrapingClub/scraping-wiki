---
name: Netnut
type: entity
category: proxy-provider
first_seen: 2026-06-23
last_updated: '2026-07-03'
sources:
- https://www.youtube.com/watch?v=MQ1zpnlMMUc
- https://spur.us/blog/how-proxy-providers-co-opt-entire-networks
- 2026-07-fbi-seizes-netnut-proxy-platform-popa-botnet.md
---

# Netnut

## What It Is

Netnut is an ISP proxy provider that acquires IP space through a border router co-option model rather than through leasing or BYOP arrangements. It operates through a partner company called DiviNetworks (also referred to as Divvy Group). Netnut claims more than 150 ISP partners and over one million IP addresses sourced through this method. The IPs it sells are not datacenter tunnels: they are routed from genuine ISP networks that also serve real end users.

## How It Works

DiviNetworks deploys GRE (Generic Routing Encapsulation) tunnels paired with policy-based routing (PBR) on the border routers of partner ISPs. The configuration redirects a selected slice of traffic through DiviNetworks infrastructure, converting the partner ISP's allocated IP space into commercial proxy inventory. DiviNetworks claims the configuration affects only 0.2% of total traffic volume on partner networks.
 
### Router Configuration

For MikroTik devices, the configuration follows this structure:

```
/interface gre add name=DIVINET-GRE
/ip address add address=10.254.254.1/30
/routing table add name=DIVINET-TUNNEL
/ip firewall mangle (marks connections and routes return traffic)
```

For Juniper/Cisco deployments, the partner provisions a VM that terminates the GRE tunnel. The border router runs PBR matching: connections targeting addresses in the partner's network, using HTTP/HTTPS source ports, with destination ports in the range **40,000–40,200**. Matching packets are forwarded to the DiviNetworks VM rather than handled locally.

Each partner ISP gets a dedicated GRE endpoint subdomain under `divinetworks.com`, following the pattern `rtr-<isp-name>.divinetworks.com`. Most resolve to a small number of centralized DiviNetworks PoPs.

### Traffic Flow

1. A Netnut proxy user connects to a Netnut gateway and requests a target site.
2. Netnut sends a TCP SYN toward the target, spoofing the source IP to a legitimate address from within the partner ISP's allocation. The ephemeral source port is in the range **40,000–40,200**.
3. The target site responds to the spoofed ISP IP. When the response hits the partner ISP's edge router, the PBR matches the return packet (whose destination port is in the 40,000–40,200 range) and routes it through the GRE tunnel back to DiviNetworks.
4. Connection marks (tagged `DIVINET-RETURN`) ensure symmetric routing: traffic associated with tunnel-originated connections returns through the same tunnel, never appearing in normal routing tables.

Real users on the same ISP network coexist on the same IP allocations and are unaware of the arrangement.

### PDNS Fingerprinting

The per-ISP subdomain pattern is discoverable via passive DNS. Confirmed examples from Spur research:

- `rtr-plainsinternet.divinetworks.com` → 131.153.71.34
- `rtr-blubroadband.divinetworks.com` → 131.153.71.34
- `rtr-celltexnetworks.divinetworks.com` → 208.72.111.230
- `rtr-rioonline.divinetworks.com` → 131.153.71.90

The consistent PoP IPs (131.153.71.34, 131.153.71.90, 131.153.23.36) mean partner-specific naming does not imply distributed infrastructure — most tunnels terminate at the same endpoints.

## Case Studies

### Howard University (AS919)

Howard University's entire 138.238.0.0/16 allocation is co-opted by Netnut. In a Spur sample of ~80,000 Netnut proxy requests, approximately 17,000 (~21%) egressed through Howard's address space, producing ~15,000 distinct exit IPs.

All 224 announced /24 subnets under AS919 had at least one observed proxy exit. Exit distribution was random and uniform across the entire prefix, consistent with network-edge integration rather than individual device compromise. Three unannounced gaps (138.238.0.0/20, 138.238.208.0/21, 138.238.248.0/21) showed zero exits.

Howard's IT department did not respond to researcher contact. Whether the configuration was authorized by university administration or installed unilaterally by an individual with router access is unknown.

### Plains Internet (AS393737)

`rtr-plainsinternet.divinetworks.com` correlates with live Netnut proxy egress. Partial enrollment: proxy exits were observed in 26 of 29 announced prefixes, with three blocks showing no egress.

## Financial Model

DiviNetworks' own revenue calculator estimates $13,208/month for a US /16 at 1 GB/IP assumed usage. The financial incentive for a single engineer or contractor with edge access is substantial. Potential implementers include upstream ISP engineering teams, managed service providers, colocation partners, or internal network staff.

## Detection

### Source Port Analysis

The 40,000–40,200 source port range is the primary network fingerprint. Observing multiple consecutive or simultaneous connections from the same IP where every source port falls within this 200-wide window is a reliable detection signal. No legitimate TCP stack produces that distribution. Any operator with source port logging on inbound connections can detect this pattern.

### IP Echo Querying

Route test requests through Netnut, then query an IP geolocation API (e.g., `ip-api.com/json`) to identify the exit IP, ASN, and registered organization. Mapping these results against announced BGP prefixes distinguishes network-edge integration from scattered host infection.

### BGP Distribution Analysis

Network-edge co-option produces uniform, prefix-wide exit distribution across all announced /24 subnets. Individual device compromise (the SDK-sourced residential proxy model) produces clustered, uneven distribution. Uniform distribution across an entire /16 is a strong indicator of the DiviNetworks architecture.

## TWSC Experience

No direct TWSC testing. Findings documented here are from Spur's public research (YouTube webinar and blog post, 2025/2026).

## Known Limitations

- Slower than traditional static ISP proxies because of the GRE tunnel round-trip.
- Real users coexist on the same IP allocations. Blocking at the IP level risks collateral damage to legitimate university or ISP users.
- Threat intelligence systems classify these IPs as **client proxies** rather than **tunnels**, reflecting the collateral blocking risk. This makes safe IP-level blocking harder than with pure tunnel proxies.
- DiviNetworks markets partner recruitment as "verified corporations only," but Netnut imposes minimal KYC. Resellers typically perform no KYC, enabling anonymous proxy purchases via cryptocurrency and burner emails — directly contradicting the stated partner recruitment standards.

## Related

- [static-isp-proxies](../concepts/static-isp-proxies.md)
- [IPXO](./ipxo.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)

## Sources

- Spur research team (Riley Kilmer, Sean) — YouTube webinar on static ISP proxy sourcing and detection, [https://www.youtube.com/watch?v=MQ1zpnlMMUc](https://www.youtube.com/watch?v=MQ1zpnlMMUc) (2025/2026)
- Spur — "How Proxy Providers Co-opt Entire Networks," [https://spur.us/blog/how-proxy-providers-co-opt-entire-networks](https://spur.us/blog/how-proxy-providers-co-opt-entire-networks)
