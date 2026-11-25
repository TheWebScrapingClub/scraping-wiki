---
name: php-webvpn
type: entity
category: tool
first_seen: 2026-11-25
last_updated: 2026-11-25
sources:
  - zenkdom-php-webvpn.md
---

# PHP-WebVPN

## What it is

PHP-WebVPN is a serverless tool that transforms standard PHP web hosting into a censorship-resistant stealth VPN and multi-protocol proxy. It allows users to bypass censorship and DPI (Deep Packet Inspection) by encapsulating network traffic within standard HTTPS POST requests, making it appear as ordinary web browsing.

## How it works

The system operates by running a PHP script on any shared hosting environment, which acts as the proxy endpoint. A local client daemon on the user's device manages the connection, encapsulating traffic into HTTPS POST requests that are sent to the PHP backend. This method effectively camouflages the VPN traffic, making it indistinguishable from regular web browsing to network observers and DPI systems.

For enhanced stealth, the tool includes a "Decoy Mode" that returns a standard 404 error page to unauthorized access attempts, hiding the proxy's true nature. It also supports multiple protocols, including HTTP, HTTPS, SOCKS5, and MTProto, and can automatically configure Windows system proxy settings. Multiple PHP backends can be chained together for load balancing and resilience.

## TWSC experience

Not yet tested by TWSC.
## Related

The source document mentions "Anti-Bot JS Challenge Resolver" which is related to overcoming bot detection mechanisms. It also mentions "SOCKS5 Obfuscated2" which is a type of proxy.

- [bot-detection-system](../entities/bot-detection-system.md)
- [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://github.com/zenkdom/php-webvpn](https://github.com/zenkdom/php-webvpn)
