---
name: webrtc-ip-leak
type: concept
first_seen: 2024-03-01
last_updated: '2026-06-04'
sources:
- bypassing-geo-fencing-scraping.md
- lab-camoufox-forks-cloverlabs-draft.md
---

# WebRTC IP Leak

## Definition

A WebRTC IP leak is when a page learns a client's real LAN or WAN IP address through the WebRTC API, even though the client's HTTP traffic is routed through a proxy. It happens because WebRTC gathers network candidates over UDP, on a path that an ordinary HTTP proxy does not control. For a scraper this is a coherence failure: the site sees one IP for the page requests (the proxy) and a different IP for WebRTC (the real machine), and the mismatch is a strong automation and evasion signal.

### Terms used on this page

**ICE candidate.** When a script opens an `RTCPeerConnection`, the browser collects the network addresses it could use for a peer-to-peer connection. Each address is an ICE candidate, exposed to JavaScript through the `onicecandidate` event as a text string.

**Host candidate.** A candidate built from a local network interface, so it carries the LAN IP (for example `192.168.1.45`).

**Server-reflexive candidate (srflx).** A candidate obtained by asking a STUN server "what IP do you see me coming from", which returns the public WAN IP. This is the real-IP leak that survives an HTTP proxy.

**STUN.** A small UDP protocol a browser uses to discover its public-facing address. The reflexive candidate comes from a STUN round trip.

## How It Works

A page does not need permission to enumerate candidates. It creates an `RTCPeerConnection` pointed at a public STUN server, opens a dummy data channel, calls `setLocalDescription`, and reads the candidate strings as they arrive. Each string contains an IP. Host candidates expose the LAN address, server-reflexive candidates expose the WAN address.

The proxy is the catch. An HTTP or HTTPS proxy tunnels TCP through a CONNECT, but the STUN exchange is UDP, which the proxy does not carry. The browser therefore talks to the STUN server directly from its real interface, and the reflexive candidate comes back with the real WAN IP. A SOCKS5 proxy can carry UDP and is the proxy type that WebRTC proxy-routing settings assume, which is why the same defense behaves differently depending on proxy type.

The defenses are Firefox preferences. `media.peerconnection.ice.no_host` suppresses host (LAN) candidates. `default_address_only` limits gathering to the default route. `proxy_only_if_behind_proxy` and `proxy_only_if_pbmode` force ICE to use only the proxy when one is set. `obfuscate_host_addresses` replaces host IPs with mDNS `.local` names. [Camoufox](../entities/camoufox.md) additionally documents spoofing the WebRTC IP to the proxy exit when GeoIP is enabled.

## Where It Matters

Any scraper that drives a real browser through a proxy is exposed if WebRTC is not handled. The leak is part of the fingerprint coherence checks that systems like [Datadome](../entities/datadome.md) run, and it sits in the same family as the IP and timezone consistency signals covered under [browser fingerprinting](./browser-fingerprinting.md). The earliest TWSC mention was in the context of geo-fencing, where a WebRTC leak through Browserleaks revealed a real location behind a proxy.

## What We Tested

In our 2026-06 Camoufox fork analysis we measured the leak directly. The probe matters: running the `RTCPeerConnection` on `about:blank` showed both builds leaking, because Camoufox's content-level injection is not active on `about:blank`. Moving the probe onto a real https origin gave the true picture.

Official Camoufox on a Firefox 146 build, behind an HTTP residential proxy with GeoIP on, emitted one server-reflexive candidate carrying the real WAN IP (the proxy exit IP rotated per run, so the constant real IP in the candidate was unmistakable). The host/LAN candidate was suppressed, but the WAN address leaked. The [JWriter20 Camoufox fork](../entities/camoufox.md) on the same Firefox 146, which bakes in `default_address_only`, `proxy_only_if_behind_proxy`, `proxy_only_if_pbmode`, and `obfuscate_host_addresses`, gathered zero ICE candidates behind the same proxy, so nothing leaked. Reproduced across two runs.

The mechanism behind the fork's result is worth stating plainly: behind an HTTP proxy that cannot carry the UDP, the `proxy_only` preferences make WebRTC gather no candidates at all. The fix neutralizes WebRTC under a proxy rather than tunneling it. Tunneling would require a SOCKS5 proxy.

## Current State

As of 2026-06, stock Camoufox 146 still surfaces the real WAN IP through the reflexive candidate when driven behind an HTTP proxy, despite the documented GeoIP WebRTC alignment. This is recorded as a dated note on the [Camoufox](../entities/camoufox.md) page. The reliable mitigations are the `proxy_only_*` preferences (which the JWriter20 fork ships) or routing through a SOCKS5 proxy that can actually carry the WebRTC traffic. The practical rule is to test the WebRTC surface per build and per Firefox version rather than assuming a stealth browser handles it.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [proxy-fundamentals](./proxy-fundamentals.md)
- [Camoufox](../entities/camoufox.md)
- [Datadome](../entities/datadome.md)
- [Camoufox vs forks](../comparisons/camoufox-vs-forks.md)

## Sources

- [https://substack.thewebscraping.club/p/bypassing-geo-fencing-scraping](https://substack.thewebscraping.club/p/bypassing-geo-fencing-scraping)
- TWSC Lab article, forthcoming 2026: "Is Camoufox still effective, and do the forks help?" (draft: `drafts/lab-camoufox-forks-cloverlabs-draft.md`)
- [daijro/camoufox issue #538: Proxy detection on FF146, WebRTC Leak](https://github.com/daijro/camoufox/issues/538)
