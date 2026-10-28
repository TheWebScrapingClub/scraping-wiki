---
name: tanuki
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - pigyon-tanuki.md
---

# Tanuki

## What it is

Tanuki is an anonymization proxy built for AI-assisted security testing and bug bounty hunting. Its primary function is to keep real target data, such as domains, IPs, emails, paths, cloud identifiers, and aggressive security terminology, out of LLM API logs during security testing.

## How it works

Tanuki runs as a Docker container and transparently intercepts API traffic between a local agent (like Claude Code) and an upstream provider (like the Anthropic API). Before a prompt leaves the machine, Tanuki swaps real target data for harmless fictional development equivalents.

When the model responds, the proxy rewrites the fictional response back to real values. This allows local tools to execute against the actual targets, while the upstream provider remains blind to the real engagement details.

## TWSC experience

Not yet tested by TWSC.

## Related

* [llm-shield-proxy](../entities/llm-shield-proxy.md)
* [proxy-fundamentals](../concepts/proxy-fundamentals.md)


## Sources

- [https://github.com/pigyon/tanuki](https://github.com/pigyon/tanuki)
