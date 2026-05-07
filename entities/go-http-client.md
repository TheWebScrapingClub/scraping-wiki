---
name: go-http-client
type: entity
category: library
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-go-http-client.md
---

# Go HTTP Client

## What it is

The Go HTTP client is an HTTP(s) client implemented in Golang, designed to facilitate making HTTP(s) requests from a Golang program. By default, when unmodified, its user-agent string includes the version of the library, such as `go-http-client/1.1`.

## How it works

This client allows developers to perform standard HTTP(s) requests within a Golang application. It generates a default user-agent string that identifies the library version used for the request.

## TWSC experience

Not yet tested by TWSC.

## Related

* [tls-fingerprinting](../concepts/tls-fingerprinting.md)
* [Bot Detection](../concepts/bot-detection.md)
* [puppeteer](../entities/puppeteer.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/go-http-client](https://deviceandbrowserinfo.com/learning_zone/articles/go-http-client)
