---
name: retroweb-2-0
type: entity
category: proxy-provider
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - retroweb-now-works-as-a-real-web-proxy.md
---

# RetroWEB 2.0

## What it is

RetroWEB is a forwarding proxy designed to bridge the gap between old web browsers and modern websites. It fetches HTTPS pages using a modern connection, processes the content by removing scripts and styling, rewrites links, and returns a simplified page over ordinary HTTP that legacy browsers can understand.

## How it works

RetroWEB 2.0 functions as a public HTTP forwarding proxy, sitting between the old browser and the modern website. It terminates the modern HTTPS connection and translates the result into old-fashioned HTTP, as it deliberately does not support the HTTPS `CONNECT` method. This allows the old browser to maintain a connection it can handle.

The proxy performs further processing before sending the page back, attempting to find the main content and converting useful parts of modern layouts into formats like HTML 2.0, HTML 3.2, or basic HTML 4.01, depending on the selected browser profile. It also rewrites simple forms, allowing basic GET and URL-encoded POST forms, while disabling password fields and file uploads.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Old links from the first version may no longer work.

## Related

- [proxy-server](../entities/proxy-server.md)
- [residential-proxy](../entities/residential-proxy.md)
- [browser-use](../entities/browser-use.md)


## Sources

- [https://bjornsblog.nl/retroweb-now-works-as-a-real-web-proxy/](https://bjornsblog.nl/retroweb-now-works-as-a-real-web-proxy/)
