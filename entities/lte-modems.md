---
name: lte-modems
type: entity
category: proxy-provider
first_seen: 2026-06-02
last_updated: 2026-06-02
sources:
  - writing-lte-proxy-pool.md
---

# LTE Modems

## What it is

The LTE modems serve as the physical source for a production residential IP proxy pool. The fleet consists of nine TP-Link M7000/M7200 LTE modems, which are used to generate residential IP addresses for AI products. Each modem is physically labeled with its subnet identifier to maintain stable modem identity across reboots, as the firmware reports an identical fake serial number for every device.

## How it works

Two Raspberry Pis host the pool, with each modem appearing on its Pi as a dedicated USB network interface. Each modem runs its own GOST HTTP-proxy instance bound to that interface, allowing clients to reach the pool over WireGuard.

The rotation engine is a headless Chromium instance supervised by pm2. This instance logs into each modem's web admin UI, clicks Reboot, monitors the device bouncing, and verifies the new public IP via ipify. An escalating recovery ladder is in place for failures, involving `nmcli` commands, USB power-cycling through sysfs, and potentially a host reboot.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The honest limitation is that the pool is not 100% available.

## Related

* [playwright](../entities/playwright.md)
* [proxy-server](../entities/proxy-server.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://www.hilgard.cz/writing/lte-proxy-pool](https://www.hilgard.cz/writing/lte-proxy-pool)
