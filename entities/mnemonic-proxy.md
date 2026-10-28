---
name: mnemonic-proxy
type: entity
category: proxy-provider
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - lastreload-mnemonic-proxy.md
---

# mnemonic-proxy

## What it is

Mnemonic Proxy is a transparent HTTP proxy designed to sit between a coding agent and various local models or OpenAI-compatible servers. It functions by managing the agent's history, ensuring that the model reads only the relevant parts of the conversation while retaining the full, unmodified history on disk.

## How it works

The proxy speaks OpenAI Chat Completions, Anthropic Messages, and OpenAI Responses. It routes requests to local models such as llama.cpp's `llama-server`, [Strata](https://github.com/Niko1221/Strata), or other OpenAI-compatible backends. The proxy decides what the model actually reads from the history, ensuring that old material leaves the prompt but is never summarized away; every message, tool call, and output stays on disk verbatim, allowing the model to pull any of it back.

The proxy dynamically reads the context window size from various engines, including Strata, llama-server, ds4-server, Ollama, and LM Studio, and scales its thresholds accordingly. If a context window size is not written in the configuration, it defaults to 131072, or the value written in the configuration is used.

## TWSC experience

Not yet tested by TWSC.

## Related

- [aiohttp](../entities/aiohttp.md)
- [llm-shield-proxy](../entities/llm-shield-proxy.md)


## Sources

- [https://github.com/lastreload/mnemonic-proxy](https://github.com/lastreload/mnemonic-proxy)
