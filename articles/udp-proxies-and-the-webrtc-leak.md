---
type: article_summary
title: UDP, Proxies, and the WebRTC Leak
slug: udp-proxies-and-the-webrtc-leak
canonical_url: https://www.scraping.club/p/udp-proxies-and-the-webrtc-leak
publish_date: '2026-07-02'
visibility: premium
topics:
- http-clients
- proxies
- cloudflare
- akamai
description: How UDP-capable proxies work with HTTP/3 and WebRTC in scraping, and where the client decides whether UDP is routed through the proxy or leaks your real IP.
source_hash: cb886e5df12784a1
---

# UDP, Proxies, and the WebRTC Leak

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-07-02 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/udp-proxies-and-the-webrtc-leak?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

More of the web answers over HTTP/3, which runs on QUIC, which runs on UDP. Some proxy providers now offer UDP support, usually as a beta over SOCKS5, and pitch it as a stealth feature. But UDP reaches a browser in two ways: the HTTP/3 we want for our requests, and the WebRTC traffic the browser generates on its own, which can leak around the proxy and expose our real IP. Supporting UDP and routing it are different problems.

We tested three clients end to end: an HTTP client, a browser doing HTTP/3 and a browser doing WebRTC, with one provider that carries UDP and one that doesn't. We checked the stealth claim against the fingerprinting layers that Cloudflare, Akamai and DataDome score, and looked at whether curl_cffi can do HTTP/3 in the setup scrapers run. Then we moved to the WebRTC leak, where UDP causes real trouble.

## What's inside

- Which fingerprint layers change when a client moves from TCP to QUIC (TCP/IP stack, TLS, HTTP/2 settings) and which ones only get replaced by something else.
- Why QUIC transport parameters differ between Chrome's quiche, Firefox, quic-go and ngtcp2, and why a non-browser QUIC stack can stand out instead of blending in.
- How real HTTP/3 adoption looks, by share of traffic and by share of sites advertising it, and why most real traffic is still on TCP.
- The difference between curl_cffi's high-level requests API and its low-level Curl API when combining Chrome impersonation, HTTP/3 and a proxy.

**In the full article:** The curl_cffi test script and its per-scenario results, the comparison between the UDP-capable provider and the one without UDP, and the browser tests for HTTP/3 and the WebRTC leak.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/udp-proxies-and-the-webrtc-leak?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
