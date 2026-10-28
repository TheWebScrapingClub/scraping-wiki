---
name: circuit-breaker-sage
type: entity
category: anti-bot
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - circuit-breaker-sage-vercel-app.md
---

# Circuit Breaker Sage

## What it is

Circuit Breaker Sage is a drop-in reverse proxy designed to prevent autonomous agents from draining API budgets by catching infinite tool loops and enforcing hard spend caps within volatile RAM. It is engineered to operate with sub-35ms overhead and maintains zero payload retention.

## How it works

The architecture involves an agent sending a request through the Circuit Breaker, which utilizes a RAM hash and a spend-cap engine before forwarding the request to the upstream OpenAI API. This system performs loop detection by recognizing repeated tool calls or prompt fingerprints, halting the cycle before further requests are sent.

Requests are checked against rolling spend ceilings, including hourly and daily account caps, before they are allowed to proceed upstream. This mechanism ensures that requests are blocked if they breach configured budget limits.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Performance figures are engineering targets and depend on deployment, network conditions, and request profile. Furthermore, the spend figures illustrated in failure analysis are modeled scenarios, not measured customer spend.

## Related

* [llm-shield-proxy](../entities/llm-shield-proxy.md)
* [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://circuit-breaker-sage.vercel.app/](https://circuit-breaker-sage.vercel.app/)
