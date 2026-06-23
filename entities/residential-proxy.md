---
name: residential-proxy
type: entity
category: proxy-provider
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
  - blog-smart-tv-apps-residential-proxy-sdks.md
---

# Residential Proxy

## What it is

A residential proxy is software designed to route other people's internet traffic out through a user's home network. These proxies are often embedded within applications, such as smart TV apps, to monetize the user's internet connection in the background.

## How it works

Proxy SDKs are inserted into applications to allow them to monetize the connection without degrading the user experience with constant ads. This allows the app to keep running calmly while the TV's internet connection generates revenue in the background.

These applications often operate under a consent model where users are asked once, and the background clause dictates that the proxy can continue running even after the application is closed.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The risk associated with using a TV app as a proxy is that if the proxy provider allows requests to private or local addresses, or if their filtering fails, the app running inside the home network could pose a security risk.

## Related

* [proxy-server](../entities/proxy-server.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://spur.us/blog/smart-tv-apps-residential-proxy-sdks](https://spur.us/blog/smart-tv-apps-residential-proxy-sdks)
