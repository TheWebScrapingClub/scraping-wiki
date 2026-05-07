---
name: firehol
type: entity
category: proxy-provider
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-proxy-db-benchmark-firehol-may-2025.md
---

# FireHOL

## What it is

FireHOL is a community-driven project that aggregates multiple IP lists to help defenders block known malicious or unwanted traffic. While originally built as a firewall management tool, it is now best known for its curated threat intelligence feeds, including lists of open proxies, Tor exit nodes, and known spam sources. The `firehol_proxies` list is a feed updated daily that combines several open proxy datasets such as `ip2proxy_px1lite`, `socks_proxy_30d`, and `sslproxies_30d`.

## How it works

FireHOL functions by aggregating various IP lists to provide defenders with resources for blocking unwanted traffic. The specific proxy list benchmarked, `firehol_proxies`, is compiled from several open proxy datasets.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Defenders relying solely on public feeds, such as FireHOL’s proxy list, are likely to miss large segments of fast-moving or evasive proxy traffic. The FireHOL proxy list shows very limited coverage of residential and ISP proxies compared to proprietary databases.

## Related

- [device-and-browser-info](../entities/device-and-browser-info.md)
- [proxy-server](../entities/proxy-server.md)
- [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/proxy-db-benchmark-firehol-may-2025](https://deviceandbrowserinfo.com/learning_zone/articles/proxy-db-benchmark-firehol-may-2025)
