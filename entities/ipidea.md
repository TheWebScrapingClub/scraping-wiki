---
name: ipidea
type: entity
category: proxy-provider
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - blog-free-vpns-proxies-sell-your-device.md
---

# IPIDEA

## What it is

IPIDEA is a residential proxy network that enrolled 9 million Android devices into a botnet. The network allowed threat groups to route their traffic through real people's home IP addresses, effectively using consumer devices as proxy exit nodes.

## How it works

IPIDEA operates by embedding third-party SDKs into free apps, such as free VPN utilities, casual games, and flashlight tools. Once installed, these apps request standard Android permissions and register the device's IP, carrier, geolocation, and available bandwidth with a command-and-control (C2) server. From that point, the device becomes an active exit node, routing traffic from paying proxy customers through the consumer's home IP address.

## TWSC experience

Not yet tested by TWSC.
## Related

- [Cloudflare](../entities/cloudflare.md)
- [proxelar](../entities/proxelar.md)
- [Smartproxy Site Unblocker](../entities/smartproxy-unblocker.md)


## Sources

- [https://voidmob.com/blog/free-vpns-proxies-sell-your-device](https://voidmob.com/blog/free-vpns-proxies-sell-your-device)
