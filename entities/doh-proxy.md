---
name: doh-proxy
type: entity
category: proxy-provider
first_seen: 2026-09-05
last_updated: 2026-09-05
sources:
  - afonsofrancof-doh-proxy.md
---

# doh-proxy

## What it is

doh-proxy is an extremely simple DNS-over-HTTPS (DoH) proxy server written in Go. It functions as an intermediary, sitting between a DNS client and one or more DNS-over-HTTPS servers, responsible for forwarding DNS queries over HTTP/2 and handling the resulting responses.

## How it works

The proxy supports both TCP and UDP for handling DNS queries. It is configured to use multiple upstream DoH servers, allowing for flexible routing of requests. Communication between the client and the upstream servers utilizes HTTP/2, which is employed for faster and more secure data transfer.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The proxy requires the user to run it as root to utilize lower ports, such as port 53. Additionally, at least one upstream DoH server URL must be specified for the proxy to function. If the proxy is used as the system's default DNS resolver and the upstream server URL is a domain name, another DNS server must be specified as an IP address to prevent circular dependency issues.

## Sources

- [https://github.com/afonsofrancof/doh-proxy](https://github.com/afonsofrancof/doh-proxy)
