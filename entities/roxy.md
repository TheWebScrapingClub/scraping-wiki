---
name: roxy
type: entity
category: tool
first_seen: 2026-05-13
last_updated: 2026-05-13
sources:
  - TimoKats-roxy.md
---

# Roxy

## What it is

Roxy is a feature-rich RSS proxy written in Go that is designed to combine multiple RSS feeds into a single, queryable feed. It is capable of handling CORS restrictions to aggregate data from various sources.

## How it works

Roxy is implemented in Go and does not rely on external dependencies. It allows users to load a list of RSS URLs via a configuration file and then serves the combined feeds in either XML or JSON formats.

The proxy provides several API endpoints for interaction, including `/add` to add new feeds, `/xml` and `/json` to retrieve formatted feeds with optional filtering by categories, keywords, and amount, and `/refresh` to update all loaded RSS feeds.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/TimoKats/roxy](https://github.com/TimoKats/roxy)
