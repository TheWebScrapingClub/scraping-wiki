---
name: ag2b
type: entity
category: tool
first_seen: 2026-05-29
last_updated: 2026-05-29
sources:
  - docs.md
---

# AG2B

## What it is

AG2B (Agent to Browser) is a client-side agentic runtime designed to allow an agent to execute its tasks directly within the user's browser. This architecture positions the agent to run where the application resides, allowing it to interact with the DOM and browser environment. The server component can function as a thin LLM proxy or as a layer that extends the client runtime capabilities.

## How it works

The core of AG2B is the Agent, which manages the runtime state and executes "The Loop." This loop involves the LLM interpreting a prompt, selecting an appropriate Tool, and executing that Tool within the browser environment. The result of the tool execution is then fed back into the loop, allowing the model to generate a final response in plain text describing the actions taken.

## TWSC experience

Not yet tested by TWSC.

## Related

* [browser-use](../entities/browser-use.md)


## Sources

- [https://ag2b.ai/docs](https://ag2b.ai/docs)
