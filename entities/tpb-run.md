---
name: tpb-run
type: entity
category: proxy-provider
first_seen: 2026-11-20
last_updated: 2026-11-20
sources:
  - thepiratebay-proxy-list.md
---

# TPB.Run

## What it is

TPB.Run is a proxy website that provides access to The Pirate Bay. It features a retro theme and is described as being very fast. The site aims to bypass geographical restrictions and ISP blocks that prevent direct access to The Pirate Bay.

## How it works

TPB.Run functions as an intermediary between the user and The Pirate Bay. When a user visits the TPB.Run website, their request is first sent to the TPB.Run proxy server. This server then fetches the requested content from The Pirate Bay's servers.

The proxy server subsequently modifies the content, rewriting any links to point back to itself, before delivering the content to the user. This process allows users to access The Pirate Bay's content even if it is blocked in their region or by their ISP, as their traffic appears to be directed only to the proxy site.

## TWSC experience

Not yet tested by TWSC.
## Related

The Pirate Bay is a website that hosts torrent files and magnet links. Accessing such content can sometimes involve navigating anti-bot measures or utilizing proxy services.

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://bout2bus.github.io/thepiratebay-proxy-list/](https://bout2bus.github.io/thepiratebay-proxy-list/)
