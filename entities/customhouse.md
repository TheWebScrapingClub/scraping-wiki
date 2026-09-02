---
name: customhouse
type: entity
category: anti-bot
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - vineetpant-customhouse.md
---

# Customhouse

## What it is

Customhouse is a deterministic MCP proxy designed to block money-moving and data-egress tool calls within AI agent sessions that have received untrusted content. It operates by tracking the provenance of every input to determine if a subsequent tool call should be blocked based on that content's trustworthiness.

## How it works

Customhouse tracks the upstream source of every input to determine its provenance. It then deterministically blocks money-moving or data-egress calls in any session that has received untrusted content. The block is based solely on provenance, meaning it cannot be evaded by methods like rewording, summarising, or base64-ing the payload, as no model is involved in the decision path.

The system monitors the entire flow, such as reading untrusted content from one server and attempting to send data out through a different server. It identifies which upstream source tainted the session and which specific call is being made, allowing for precise enforcement of flow policies.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The system has a false-positive rate of 40% over benign workflows that use sinks. Furthermore, it does not suit high-frequency untrusted-to-sink automation, such as support-reply pipelines.

## Related

[agent-vault-proxy](../entities/agent-vault-proxy.md)
[ai-agent-reader-page](../entities/ai-agent-reader-page.md)
[bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://github.com/vineetpant/customhouse](https://github.com/vineetpant/customhouse)
