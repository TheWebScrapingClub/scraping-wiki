---
name: keyfence
type: entity
category: proxy-provider
first_seen: 2026-09-09
last_updated: 2026-09-09
sources:
  - aminueza-Keyfence.md
---

# Keyfence

## What it is

Keyfence is a local proxy designed to prevent API keys and other secrets from being exposed when making requests to Large Language Model (LLM) APIs. It functions by intercepting every request to an AI provider before it leaves the local machine to inspect and modify sensitive information.

## How it works

Keyfence operates by sitting between the user's tools and the LLM provider. It checks every request to an AI provider and applies one of three modes: `block`, which results in a 403 error and stops the request; `redact` (the default), which replaces the secret with a placeholder like `[REDACTED:<kind>]`; or `placeholder`, which replaces the secret with `<<SECRET_id>>` and restores the real value in the response stream.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/aminueza/Keyfence](https://github.com/aminueza/Keyfence)
