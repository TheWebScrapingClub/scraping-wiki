---
name: runo
type: entity
category: tool
first_seen: 2026-07-09
last_updated: 2026-07-09
sources:
  - rhymeswithlimo-runo.md
---

# Runo

## What it is

Runo is an open-source tool designed to extract structured, typed JSON from any URL based on a schema defined by the user. It allows users to specify a field name, its required type, and an example value, and Runo fetches the page, handles necessary JavaScript rendering, extracts the data using an LLM, and coerces every extracted value strictly to the requested type, returning clean, flat JSON.

## How it works

Runo operates by taking a user-defined schema and fetching the target URL. It employs smart rendering, performing a plain HTTP request first and only using a headless browser if the page requires JavaScript to render the content. The extracted data is processed by an LLM, which reads for meaning rather than relying on DOM position, ensuring that the schema remains robust even if the site is redesigned.

The tool supports three modes: extract (single URL), batch (one schema across many URLs), and crawl (following links from a seed URL). It also includes asynchronous variants for all modes, allowing users to run the extraction process inside their own event loop.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Runo requires a Google Gemini API key to function. Additionally, if the LLM cannot find a field defined in the schema, the corresponding value will be returned as `null`.

## Related

* [playwright](../entities/playwright.md)
* [python-requests](../entities/python-requests.md)


## Sources

- [https://github.com/rhymeswithlimo/runo](https://github.com/rhymeswithlimo/runo)
