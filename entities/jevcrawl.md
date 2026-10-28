---
name: jevcrawl
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - RayenMlayeh-jevcrawl.md
---

# Jevcrawl

## What it is

Jevcrawl is an MCP server and CLI tool designed to crawl websites specifically for AI agents. Its primary function is to efficiently find the answer page rather than simply fetching all pages, aiming to reduce token usage and cost associated with LLM-driven crawling.

## How it works

The crawler utilizes a small decision model that evaluates every link and passage encountered during the crawl. This model determines which content is relevant to the user's question, allowing the agent's LLM to read only the necessary answer passages.

This approach allows Jevcrawl to be 2x faster than an LLM-driven crawl and significantly cheaper per task, as the crawl decisions themselves cost only a few cents. Every passage copied is verbatim, including its URL, heading path, and character offsets.

## TWSC experience

Not yet tested by TWSC.

## Related

- [crawl4ai](../entities/crawl4ai.md)


## Sources

- [https://github.com/RayenMlayeh/jevcrawl](https://github.com/RayenMlayeh/jevcrawl)
