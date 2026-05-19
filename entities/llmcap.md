---
name: llmcap
type: entity
category: tool
first_seen: 2026-05-19
last_updated: 2026-05-19
sources:
  - www-llmcap-io.md
---

# LLMCap

## What it is

LLMCap is a service designed to enforce hard dollar caps on LLM API calls across various providers. It prevents unexpected billing by stopping calls once a defined dollar limit is reached, ensuring users are never surprised by charges.

## How it works

To use LLMCap, users change their API client's `base_url` to point to `proxy.llmcap.io/[provider]`, which works with every SDK. Users can then define daily, monthly, or per-key dollar limits via the dashboard, supporting per-model granularity.

When a cap is hit, LLMCap returns an HTTP 429 response before the token is consumed, meaning the token is never charged. This mechanism ensures that existing error handling works as-is, as the application receives the standard rate-limiting response.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Self-hosting is currently on the roadmap. The managed service at proxy.llmcap.io is the recommended path for deployment.

## Related

* [proxy-server](../entities/proxy-server.md)
* [go-http-client](../entities/go-http-client.md)


## Sources

- [https://www.llmcap.io/](https://www.llmcap.io/)
