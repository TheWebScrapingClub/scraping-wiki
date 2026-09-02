---
name: rama
type: entity
category: library
first_seen: 2026-09-02
last_updated: '2026-09-02'
sources:
- blog-rama-0-4.md
- blog-rama-cli-0-5-proxy-inspector.md
---

# Rama

## What it is

Rama is a framework designed to support various proxy protocols and configuration methods for network clients. It provides mechanisms for configuring proxies directly, via environment variables, and through system-wide settings, including support for HTTP, HTTP over TLS (HTTPS), and SOCKS5 proxies.

## How it works

Proxies can be configured directly using `ProxyRoute`(s) or exposed via application settings. Applications can also utilize environment variables such as `HTTP_PROXY`, `ALL_PROXY`, `HTTPS_PROXY`, and `NO_PROXY`, which are managed through the `ProxyEnvLayer` and `NoProxyEnvLayer`.

For system-wide configuration, Rama supports HTTP, HTTPS, and SOCKS5 proxies, along with bypass rules, via the `SystemProxyLayer`. Furthermore, Rama 0.4 introduced support for Proxy Auto Configuration (PAC) via the `rama-pac` crate, allowing users to evaluate PAC scripts or generate scripts for domain routing.

## Known limitations

Previously, network clients built using Rama did not inherently respect system configuration settings for proxies, though this behavior is now supported out of the box via the `SystemProxyLayer` in version 0.4.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-server](../entities/proxy-server.md)
- [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://plabayo.tech/blog/rama-0-4](https://plabayo.tech/blog/rama-0-4)
