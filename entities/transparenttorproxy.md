---
name: transparenttorproxy
type: entity
category: tool
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - onyks-os-TransparentTorProxy.md
---

# TransparentTorProxy

A Linux CLI utility that transparently routes all system traffic through the Tor network using nftables. It enables rapid IP rotation and easy toggling of global proxy settings for privacy tasks.

## How it works

TransparentTorProxy uses nftables to route all system traffic through the Tor network. It automatically configures DNS and IPv6 to prevent leaks and ensures that the firewall rules are applied atomically to avoid intermediate states. The tool also supports IP rotation and log rotation, and it is designed to be crash-safe, with a lock file that tracks session state.

## TWSC experience

Not yet tested by TWSC.

## Related

- [Scrapoxy](../entities/scrapoxy.md)
- [ScrapeGraphAI](../entities/scrapegraphai.md)
- [Undetected Chromedriver](../entities/undetected-chromedriver.md)

Scrapoxy, ScrapGraphAI, and Undetected Chromedriver are tools and libraries that, like TransparentTorProxy, are used in web scraping and privacy tasks.


## Sources

- [https://github.com/onyks-os/TransparentTorProxy](https://github.com/onyks-os/TransparentTorProxy)
