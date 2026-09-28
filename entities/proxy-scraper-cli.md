---
name: proxy-scraper-cli
type: entity
category: tool
first_seen: 2026-09-28
last_updated: 2026-09-28
sources:
  - maximilianfeix-proxy-scraper.md
---

# proxy-scraper-cli

## What it is

proxy-scraper-cli is a command-line tool written in Python designed to scrape and verify free HTTP, SOCKS4, and SOCKS5 proxies. It maintains a live list of working proxies and utilizes a rotating proxy server, alongside an MCP server for AI agents.

## How it works

The tool collects public HTTP, SOCKS4, and SOCKS5 proxies from over 700 sources. It rigorously verifies every proxy hit using checks such as honeypots, injected scripts, and TLS verification. Based on these checks, the scraper learns which sources are reliable and can consolidate the results into a single rotating proxy.

## TWSC experience

Not yet tested by TWSC.

## Related

* [socks5-proxy](../entities/socks5-proxy.md)
* [proxy-server](../entities/proxy-server.md)
* [proxy-benchmark](../entities/proxy-benchmark.md)


## Sources

- [https://github.com/maximilianfeix/proxy-scraper](https://github.com/maximilianfeix/proxy-scraper)
