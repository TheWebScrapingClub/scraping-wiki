---
name: stop-bots
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - ivankovic-stop-bots.md
---

# stop-bots

## What it is

stop-bots is a TUI and a CLI tool written in Rust designed to configure web servers and firewalls to block malicious bots without requiring the user to hide behind a Content Delivery Network (CDN). It provides a graphical user interface for managing configurations for existing web servers like nginx, Apache, or Traefik, and firewalls such as nftables or iptables.

## How it works

The tool operates in two modes: Preventative and Responsive. The preventative mode involves downloading known bot lists and IP ranges, including Geo-blocking, to block known threats. For private servers, it can use an allowlist to block over 90% of attacks.

The responsive mode monitors access logs to detect attackers and kicks them out. While this process means a few packets may reach the server before detection, it is intended to stop attackers from escalating their activity. The tool also attempts to ensure safety by testing webserver configurations before application and never blocking IP addresses with successful SSH logins.

## TWSC experience

Not yet tested by TWSC.

## Related

- [bot-detection-system](../entities/bot-detection-system.md)
- [Cloudflare](../entities/cloudflare.md)
- [aws-waf](../entities/aws-waf.md)


## Sources

- [https://github.com/ivankovic/stop-bots](https://github.com/ivankovic/stop-bots)
