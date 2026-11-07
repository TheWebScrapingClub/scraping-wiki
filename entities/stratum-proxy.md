---
name: stratum-proxy
type: entity
category: proxy-provider
first_seen: 2026-11-07
last_updated: 2026-11-07
sources:
  - Modanez-HomeMinerProxy.md
---

# Stratum proxy

## What it is

The Stratum proxy is a component designed to facilitate home solo Bitcoin mining operations. It acts as an intermediary, forwarding miner traffic to a pool while simultaneously computing the block difficulty on the way. It is used in conjunction with various miners such as Bitaxe, NerdMiner, ESP32 boards, and cpuminer.

## How it works

The Stratum proxy (`src/proxy.js`) allows miners to connect to a home server instead of directly to the mining pool. The proxy forwards all traffic unchanged and rebuilds each share's block header to compute the difficulty reached. It operates without relying on pool APIs or device firmware.

The proxy supports various Stratum V1 pools, and most ports have a backup pool configured for failover. If the main pool stops responding, connected miners are redirected to the backup, and a health check monitors the main pool to restore connectivity.

## TWSC experience

Not yet tested by TWSC.

## Related

* [nodejs-based-scraper](../entities/nodejs-based-scraper.md)


## Sources

- [https://github.com/Modanez/HomeMinerProxy](https://github.com/Modanez/HomeMinerProxy)
