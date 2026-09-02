---
name: agent-web-crawlers
type: entity
category: tool
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - tools-agent-census.md
---

# Agent web crawlers

## What it is

Agent web crawlers are named bots and agents designed to probe, grade, index, and scrape endpoints for various purposes. A census of these agents revealed 60 distinct named crawlers discovering and interacting with a specific endpoint, categorized by their function such as liveness monitoring, directory indexing, security research, and price-quote scraping.

## How it works

These agents perform various tasks, including checking endpoint health, ingesting catalogs to list services, scanning for security risks, and performing conventional web indexing. Many agents operate in specific modes, such as liveness-only checks or reading price quotes without making payments.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Many observed agents operate in modes such as "liveness-only, never invokes tools" or "reads-402-price-quotes-only-never-pays," indicating that many crawlers are designed to monitor status or gather information without executing transactions or invoking tools.

## Related

* [bot-detection-system](../entities/bot-detection-system.md)
* [browser-use](../entities/browser-use.md)
* [proxy-server](../entities/proxy-server.md)


## Sources

- [https://fetchgate.dev/tools/agent-census](https://fetchgate.dev/tools/agent-census)
