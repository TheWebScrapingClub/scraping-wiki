---
name: Mobile Proxy Farming
type: concept
first_seen: 2023-01-15
last_updated: '2026-06-02'
sources:
- mobile-proxy-raspberry.md
- building-mobile-proxy-farm.md
- how-build-mobile-proxy-farm-airproxy.md
- differences-residential-mobile-proxies.md
- writing-lte-proxy-pool.md
---

# Mobile Proxy Farming

## Definition

Mobile proxy farming is the practice of building and operating infrastructure that routes proxy traffic through real cellular network connections — typically USB modems or SIM-equipped hardware — to produce genuine mobile IP addresses with CGNAT-level trust properties. Unlike SDK-sourced residential proxies, which borrow device connections from consumer apps, a proxy farm gives the operator full control over the hardware, IP rotation, and connectivity.

## How It Works

The fundamental stack has not changed much since 2019, though the hardware options have expanded.

Each "node" consists of a cellular modem or SIM-equipped device connected to a server. The server runs a proxy process (most commonly 3proxy or Squid) that accepts inbound connections and routes them through the cellular interface. An IP rotation script — the modem watchdog — disconnects and reconnects the cellular link to trigger a new IP assignment from the carrier. Because mobile networks use CGNAT, the IP is shared with other subscribers, which makes blocking it a risk for the carrier's legitimate users.

### Hardware Options

The three main paths TWSC has tested and documented:

**Raspberry Pi + cellular HAT (2019 DIY approach)**: Raspberry Pi 3 with a Waveshare 4G HAT, running Squid proxy and a modem watchdog script. SSH reverse tunnel used to expose the proxy port externally. Functional and cheap, but limited to one SIM per device. Now uplifted to Mini-PC for better performance.

**USB modem + USB hub + server**: Multiple USB 4G/LTE modems plugged into a hub connected to a standard server or mini-PC. Tools like localtonet (for tunneling), iproxy, ProxySmart, or Proxidize handle the proxy software layer. This is the standard DIY farm architecture.

**Airproxy-scale operation (2018, documented 2025)**: 2,000+ USB modems distributed across 6 server rooms in Italy. Custom 10-port USB hubs with per-port power switching capability (allows soft-rebooting individual modems without physical access). Infrastructure: 3proxy for the proxy layer, Django for the management API, Zabbix for monitoring. Network: redundant dual-ISP fiber per location, online UPS plus diesel generators for power continuity.

### IP Rotation

The modem watchdog disconnects the cellular interface and reconnects it. The carrier issues a new IP from the CGNAT pool. Rotation speed depends on carrier and modem model. The modem watchdog script in the Raspberry Pi implementation polls connection state and forces reconnection on a schedule or on request.

### Cost Economics

Italian carrier math (as documented): a 500GB SIM plan at €29/month. Commercial mobile proxies in 2024 sell at approximately $8/GB. At scale, the unit cost of DIY mobile bandwidth is a small fraction of commercial pricing. The capital cost is hardware and setup time; the ongoing cost is carrier plans plus hosting.

## Where It Matters

Mobile proxies are the highest-trust IP type available for scraping. Anti-bot systems are reluctant to block CGNAT mobile IPs because doing so would deny access to large populations of legitimate mobile users sharing the same IP. Targets that block datacenter IPs, residential IPs, and ISP IPs often still serve mobile IPs without challenge.

Luxury fashion, ticketing, and limited-release retail (sneakers, etc.) are the canonical hard targets where mobile IPs provide meaningful lift. These sites weigh IP-level signals heavily relative to fingerprinting signals because they are optimized to stop high-volume bot operations.

Building a farm makes economic sense when: (a) commercial mobile proxy costs at required volume exceed the capital and operational cost of owned infrastructure, or (b) control over IP rotation timing and modem identity is required for the specific use case.

## What We Tested

### Raspberry Pi Build (2019, updated 2023)

TWSC built and operated a Raspberry Pi 3 + Waveshare 4G HAT proxy node. The modem watchdog script handled reconnection. SSH reverse tunnel exposed the proxy. This worked as a single-node proof of concept. The setup was upgraded to a Mini-PC for better stability and throughput. Italian mobile plan cost at time of update: approximately $25/month for 500GB.

### Mobile vs. Residential Comparison (2025)

Six evaluation criteria applied to commercial mobile vs. residential proxy providers:

- **Fraud score**: Mobile scored "low" on Scamalytics. Residential scored "very risky." This is counterintuitive — residential IPs carry heavy abuse history, while mobile IPs are harder to block without collateral damage.
- **CGNAT**: Mobile inherently; residential only sometimes.
- **IP stability**: Mobile IPs reassign frequently on reconnect. Residential IPs are more persistent per session but rotate across provider pool on each new request.
- **Cost**: Mobile ~$8/GB (2024). Residential ~$6-8/GB. The gap has narrowed significantly from historical differences.
- **Bandwidth throughput**: Mobile is constrained by cellular link capacity. Residential depends on host device connection.
- **Geographic precision**: Mobile IPs reflect carrier regions, which may not align precisely with city-level targeting.

### Airproxy Operation

Airproxy started in 2018 as an internal tool for the operator's own scraping needs and grew to a commercial service. The defining infrastructure detail is the custom USB hub with per-port power control, which allows remote modem resets without physical intervention. At 2,000+ modems across 6 locations, Zabbix monitors uptime and connectivity. The redundant power setup (online UPS + generators) reflects the operational reality that cellular modems are sensitive to power interruptions that reset modem state.

## Current State

As of 2025, commercial mobile proxy pricing has dropped to approximately $8/GB from historical highs near $40/GB. DIY farming remains economically viable for high-volume operators who can amortize hardware costs. USB modem farms remain the standard architecture. The proxy software layer (3proxy, Squid, ProxySmart) has stabilized; the main ongoing challenge is carrier plan management and modem watchdog reliability.

## Related

- [proxy-fundamentals](./proxy-fundamentals.md)
- [web-unblockers](./web-unblockers.md)
- [Cloudflare](../entities/cloudflare.md)
- [Akamai](../entities/akamai.md)

## Sources

- [https://substack.thewebscraping.club/p/mobile-proxy-raspberry](https://substack.thewebscraping.club/p/mobile-proxy-raspberry)
- [https://substack.thewebscraping.club/p/building-mobile-proxy-farm](https://substack.thewebscraping.club/p/building-mobile-proxy-farm)
- [https://substack.thewebscraping.club/p/how-build-mobile-proxy-farm-airproxy](https://substack.thewebscraping.club/p/how-build-mobile-proxy-farm-airproxy)
- [https://substack.thewebscraping.club/p/differences-residential-mobile-proxies](https://substack.thewebscraping.club/p/differences-residential-mobile-proxies)
