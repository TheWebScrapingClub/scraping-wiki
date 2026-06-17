---
name: nakshguard
type: entity
category: proxy-provider
first_seen: 2026-06-17
last_updated: 2026-06-17
sources:
  - PujanMirani-NakshGuard.md
---

# NakshGuard

## What it is

NakshGuard is an on-premises reverse proxy designed to detect and block runaway loops in AI agent traffic before they consume excessive API tokens. It operates by sitting between AI agents and LLM APIs, inspecting each request to identify looping behavior.

## How it works

The proxy inspects every request, tracks per-agent session state, and applies a set of detection layers to identify looping behavior, such as rapid repetition, unbounded context growth, and rate spikes. It blocks or logs traffic based on the configuration.

The detection layers include rate limit, hard token limit, repetition, and context velocity. Context velocity specifically detects error-append loops where an agent appends its last error to the context and retries, causing the request to grow with each turn.

## TWSC experience

Not yet tested by TWSC.

## Related

- [proxy-server](../entities/proxy-server.md)
- [bot-detection-system](../entities/bot-detection-system.md)
- [ai-agent-reader-page](../entities/ai-agent-reader-page.md)


## Sources

- [https://github.com/PujanMirani/NakshGuard](https://github.com/PujanMirani/NakshGuard)
