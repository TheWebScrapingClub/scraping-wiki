---
name: greyfox-community-edition
type: entity
category: proxy-provider
first_seen: 2026-06-22
last_updated: 2026-06-22
sources:
  - skillful-fox-studio-grey-fox-community.md
---

# GreyFox Community Edition

## What it is

GreyFox Community Edition is a self-hosted AI traffic proxy and local operator console designed for teams seeking to control LLM token usage, enforce per-user limits, reuse exact cached responses, and maintain visibility into AI traffic within their own infrastructure. It runs as a local Docker box, requiring no GreyFox-hosted control plane.

## How it works

GreyFox functions as a proxy layer, requiring that an AI application route its provider requests through GreyFox instead of sending them directly to the upstream provider. It enforces user token quotas, manages an exact response cache for repeated non-streaming requests, and provides traffic logging.

The setup involves configuring the application to use GreyFox as its base URL (e.g., `http://localhost:8080/v1`) and including an `X-App-User-Id` header in every AI request. GreyFox then performs local checks, such as user token quota enforcement and prompt injection guarding, before forwarding the request to the OpenAI-compatible provider.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

*   Up to 5 active managed users are supported.
*   Cost estimates are manual and informational only.
*   There is no hosted GreyFox cloud control plane.
*   There are no automatic update checks or automatic container updates.
*   The Community Edition lacks a request detail drawer, exports, deeper diagnostics, or live traffic metrics.

## Related

*   [proxy-server](../entities/proxy-server.md)
*   [llm-scraping](../concepts/llm-scraping.md)
*   [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://github.com/skillful-fox-studio/grey-fox-community](https://github.com/skillful-fox-studio/grey-fox-community)
