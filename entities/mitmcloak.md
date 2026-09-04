---
name: mitmcloak
type: entity
category: tool
first_seen: 2026-09-04
last_updated: 2026-09-04
sources:
  - sardanioss-mitmcloak.md
---

# mitmcloak

## What it is

mitmcloak is a drop-in mitmproxy addon designed to replace mitmproxy's upstream leg by mirroring the client's real TLS and HTTP/2 fingerprints. It allows the origin server to see a browser that handshakes like a Python script, ensuring that the telemetry leaving the proxy reflects the genuine client characteristics.

## How it works

The mechanism involves reading the client's ClientHello and HTTP/2 preface when traffic enters the proxy. Based on this information, mitmcloak mints an httpcloak preset at runtime. It then serves the request through the proxy using this mirrored fingerprint, ensuring that the client's real handshake is read on the way in and replayed on the way out within the same request cycle.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

A client speaking QUIC/HTTP3 bypasses an HTTP proxy entirely, meaning the proxy shows nothing from that traffic. Additionally, a client that pins certificates will not trust the CA used by the proxy.

## Related

* [mitmproxy](../entities/mitmproxy.md)
* [tls-fingerprinting](../concepts/tls-fingerprinting.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/sardanioss/mitmcloak](https://github.com/sardanioss/mitmcloak)
