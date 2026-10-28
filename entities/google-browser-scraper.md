---
name: google-browser-scraper
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - nodemaven-google-browser-scraper.md
---

# google-browser-scraper

## What it is

google-browser-scraper is a Python tool designed to scrape Google search results by utilizing a real browser session routed through a user-provided sticky proxy. It functions as a self-hosted alternative to SerpApi, offering an HTTP API and an MCP server interface for integration.

## How it works

The process begins by establishing a new identity consisting of a sticky proxy session and a fresh browser profile. This identity undergoes a warm-up phase involving ordinary browsing and the Google front page. Once warmed up, the specified query is submitted, and the system checks the response before parsing. Captchas or blocks are reported as failures rather than empty results.

The tool manages traffic by reusing successful proxy exits for subsequent queries, dropping refused exits and retrying the query on a new exit if necessary. Link resolution is handled by a separate short-lived proxy session to ensure it does not interfere with the main browser session. Traffic usage is tracked via a local relay that counts bytes.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The first query requires a few minutes because a new exit must be warmed up first, which incurs noticeably more traffic than a standard search. Additionally, SOCKS5 proxies require an IP-whitelisted endpoint because Chrome cannot send a SOCKS5 username and password.

## Related

* [proxy-benchmark](../entities/proxy-benchmark.md)


## Sources

- [https://github.com/nodemaven/google-browser-scraper](https://github.com/nodemaven/google-browser-scraper)
