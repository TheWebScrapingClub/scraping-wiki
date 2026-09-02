---
name: pyscrappy
type: entity
category: library
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - mldsveda-PyScrappy.md
---

# PyScrappy

## What it is

PyScrappy is an AI-native web scraping toolkit designed to transform websites into structured, LLM-ready data. It functions as a Python library that can be used directly or exposed as an MCP server for AI agents, providing clean output formats like Markdown, JSON, and DataFrames from any given URL.

## How it works

The toolkit features adaptive, self-healing selectors that allow scrapers to relocate elements by similarity when a website's markup changes, ensuring stability. It incorporates TLS-fingerprint impersonation to bypass anti-bot filters, optionally utilizing a `curl_cffi` backend.

PyScrappy also includes an MCP server that exposes its scrapers as tools, enabling AI agents (such as Claude or local LLMs) to pull structured web data by calling the scrapers directly. It supports concurrent scraping operations and integrates proxy and scraping-API support for handling blocked sites.

## TWSC experience

Not yet tested by TWSC.

## Related

* [playwright](../entities/playwright.md)
* [curl-cffi](../entities/curl-cffi.md)
* [scrapy](../entities/scrapy.md)


## Sources

- [https://github.com/mldsveda/PyScrappy](https://github.com/mldsveda/PyScrappy)
