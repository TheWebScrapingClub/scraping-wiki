---
name: powblock
type: entity
category: anti-bot
first_seen: 2026-09-03
last_updated: 2026-09-03
sources:
  - 8Protons-POWBlock.md
---

# POWBlock

## What it is

POWBlock is a simple, high-performance, zero-dependency, system/stack-agnostic Proof of Work microservice designed to act as a defense gate against AI scrapers, bots, and DDoS attacks. Written in pure C with EPOLL, it functions as a self-contained program that provides high-speed, high-volume, hardware-optimized proof-of-work defense.

## How it works

POWBlock is deployed behind a reverse proxy or server. A POWBlock Controller, which is configuration code, is added to the reverse proxy or webserver configuration. This controller collects client data, generates a hash to identify the client, compares that hash to the client's cookie, and passes the client and their data to POWBlock if the cookie is invalid. POWBlock then performs the proof-of-work challenge, requiring the client to mine a SHA-256 or SHA-512 hash with sufficient leading zeros. If the client succeeds, POWBlock hands back a cookie (POW_TOKEN) allowing them access to the main site and redirects them to their intended destination.

## TWSC experience

Not yet tested by TWSC.

## Related

* [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/8Protons/POWBlock](https://github.com/8Protons/POWBlock)
