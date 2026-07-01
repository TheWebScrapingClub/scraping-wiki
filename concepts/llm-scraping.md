---
name: llm-scraping
type: concept
first_seen: 2024-05-30
last_updated: '2026-07-01'
sources:
- scraping-with-llms-gpt-vision.md
- how-to-use-llms-in-scraping.md
- scraping-with-llms-scrapegraphai.md
- llm-scrapegraphai-costs-web-scraping.md
- writing-scrapers-with-llms.md
- the-lab-84-ai-driven-web-scraping.md
- building-self-healing-scrapers-with-gpt.md
- anycrawl-llm-ready-web-scraping.md
- anycrawl-testing-the-llm-ready-web.md
- when-browsers-think-chatgpt-atlas-cursor-browserbase.md
- https://github.com/vercel-labs/agent-browser
- https://folding-sky.com/blog/ios-26-macos-26-swiftui-headless-browser-webpage-webview
- https://github.com/vifreefly/kimuraframework
- blog-why-i-built-reader.md
- detail-ricci-flow-ai-web-scrap-ngeodkdeahmlnceiomeeidoidhniopam.md
- tadpolehq-com.md
- drmadmeow-up-railway-app.md
- traceaio-org.md
---

# LLM Scraping

## Definition

Using a large language model to extract structured data from web pages, replacing or supplementing traditional CSS selector or XPath-based parsing. The LLM interprets the page content — either raw HTML, cleaned text, or a screenshot — and returns structured output matching a defined schema. A separate but related use case is using LLMs to generate scraper code rather than to parse data at runtime.

## How It Works

Four distinct usage patterns exist, each with different cost and robustness characteristics.

**Schema extraction via prompt**: send page HTML to an LLM with a structured output schema. The model returns JSON matching the schema. Substantially more robust to layout changes than selector-based parsing because the model interprets meaning rather than matching patterns. Cost scales linearly with token count.

**Vision extraction**: send a rendered screenshot to a multimodal model. The most HTML-independent approach — layout, JavaScript rendering, and DOM structure are irrelevant. Highest per-page cost, additional latency from the screenshot step.

**Scraper code generation**: use LLMs to write the initial scraper (CSS selectors, XPaths, BeautifulSoup code), which then executes deterministically at scale. This is the "junior programmer" model — the LLM does the first draft, a human reviews and deploys. Most cost-effective pattern for recurring scraping.

**Self-healing pipelines**: when a scraper breaks (empty fields, changed layout), the broken scraper and current HTML are sent to an LLM that returns a corrected version. The workflow is: QA detects failure, triggers LLM fix request with original scraper + new HTML, the model updates selectors, automated tests run, fixed scraper goes to production.

ScrapeGraphAI implements a node-based pipeline for these approaches: FetchNode (retrieves the URL), ParseNode (parses and chunks HTML), RAGNode (stores in a vector database), GenerateAnswerNode (calls the LLM for final output). The ScriptCreatorGraph variant replaces the last node with a code generator that returns BeautifulSoup Python code.

Token counts are the most immediate practical constraint. A standard Italian e-commerce product page contains over 400,000 tokens of HTML. At current API pricing, that volume makes per-page LLM parsing economically unviable for large-scale extraction.

Previously (2024): three approaches were identified — BeautifulSoup preprocessing, Pydantic schema extraction, and GPT Vision. As of 2025: scraper code generation and self-healing pipelines have become equally significant patterns.

## Where It Matters

The economics of LLM scraping favor horizontal scale over vertical scale. For a project covering many different sites with few URLs each — 33 e-commerce sites, a handful of products per site — the development time saved by not writing 33 custom parsers outweighs the per-request cost. For a project targeting a single site with millions of URLs, the cost and speed disadvantages make it impractical.

LLMs cannot inspect the network tab or retrieve data embedded only in internal APIs. If the target data is not in the rendered HTML, no LLM-powered tool can retrieve it — only custom scrapers that reverse-engineer the API can. This is a hard ceiling on what the approach can do.

Anti-bot bypass is generally absent in open-source LLM scraping tools. Commercial APIs (ScrapeGraphAI API, Firecrawl hosted, Zyte API) include some degree of bot protection bypass, adequate for roughly 90% of targets as of 2025, but not the hardest cases.

Hallucination is a risk with no direct equivalent in traditional scraping. A CSS selector either finds an element or it does not. An LLM can return a plausible but incorrect value — a different product name, a missing price, an invented attribute — with no error signal. This requires validation logic that selector-based scrapers do not need.

## What We Tested

**ScrapeGraphAI with GPT-3.5-turbo on Net-A-Porter (product listing page, 2024-05)**: zero correct prices returned. The model returned plausible-looking numbers that did not match the page. Running the identical request the following day produced different wrong results using sidebar brand filter names as product names. GPT-4o on the same page improved significantly, returning qualitative fields without hallucinations but still returning only a partial item count.

**ScrapeGraphAI on TripAdvisor (2024-05)**: with a minimal prompt, all data fields were correctly mapped. The only failure was returning 3 of 5 reviews. GPT-4o corrected the count but lost the location field.

**ScrapeGraphAI ScriptCreatorGraph with GPT-4o on GitHub repositories (2024-09)**: generated a working BeautifulSoup scraper on the first attempt. Returned correct data for the first page of repositories. Best-performing pattern in our tests — well-known structured sites where the model's training data is richest.

**ScriptCreatorGraph with Llama 3.1 and Mistral on BBC and e-commerce (2024-09)**: Llama 3.1 produced non-working selectors. Mistral produced correct data extraction but could not reliably generate working scraper code across repeated runs. Running the same prompt ten times produced ten different scrapers with inconsistent behavior.

**Self-healing scraper with GPT-4o on Mrporter.com (2025-02)**: the pipeline (Camoufox HTML retrieval → GPT-4o HTML extraction → XPath generation → scraper fix) worked when product data was embedded in JSON within the HTML. On Balenciaga.com and Gucci.com (pure HTML product data), the HTML extraction step failed to isolate the correct section, making the subsequent XPath generation incorrect.

**ScrapeGraphAI API across multiple e-commerce sites (2025-05)**: described as "quite good on almost every website" with anti-bot bypass included. The commercial API handles the unblocking layer that the open-source version lacks.

**OpenAI Codex (2025-05)**: sandboxed environment with no internet access makes it effectively unusable for scraping tasks. Feeding an HTML page via prompt crashed the environment due to context size limits.

We ran a ScrapeGraphAI experiment across 100 URLs from 33 e-commerce sites. Results: 72% successful extraction, 13% fetch errors, 15% parse errors. Total API cost: $4. Total time: 20 minutes. Extrapolated to 10,000 URLs: $400 cost, roughly 2,800 failed or incorrect extractions requiring handling.

## Current State

As of 2025, the viable uses of LLMs in scraping are:

1. **Scraper code generation** for development acceleration. Fast to prototype, requires human review before production. Cursor + MCP is the current preferred workflow for this pattern (see [ai-scraping-assistants](./ai-scraping-assistants.md)).
2. **Runtime data extraction** for multi-site horizontal projects where diversity of sources makes custom parsers expensive. Commercial APIs handle this better than open-source due to built-in unblocking.
3. **Self-healing** for selector maintenance. Best when product data is embedded in JSON in the HTML. Unreliable when the model must isolate the correct HTML section from a large DOM.

Zyte API uses a composite AI architecture: deterministic ML models for well-defined structured fields (product names, prices, dates), LLMs only for ambiguous or non-standard fields. This hybrid approach reduces per-request LLM cost while preserving flexibility for edge cases.

LLM scraping is not a viable replacement for traditional parsing in high-volume single-site extraction. Token costs, speed penalty, and hallucination risk all scale with volume.

## AI-Driven Browsers and Agents

A separate but converging pattern: AI reasoning engines embedded directly in browser environments. As of November 2025:

**ChatGPT Atlas**: OpenAI's browser integration built on Chromium. Allows ChatGPT to navigate the web, fill forms, and extract data during conversation. Not designed as a scraping tool, but the underlying capability (browser control from LLM reasoning) is functionally equivalent to Browser Use or Stagehand.

**Browserbase Stagehand V3**: An open-source framework that takes natural language instructions and translates them into Playwright browser actions via LLM. The human describes what to do; the LLM generates the Playwright steps. Demonstrated: "find the API endpoint that returns product data on Harrods.com" — Stagehand navigated to the site, inspected network traffic, and identified the Algolia API endpoint automatically.

**Cursor browser integration**: Cursor's IDE browser tool shows network calls to the LLM when performing browser actions. Practical effect for scraping: the model can inspect network traffic during page interaction and surface API endpoints that carry the data, reducing the manual reverse-engineering step.

These tools do not replace specialized scrapers but they do reduce the discovery phase. Finding hidden API endpoints — which previously required opening browser dev tools and reading network logs — can be partially automated by describing the goal to an AI agent.

[AnyCrawl](../entities/anycrawl.md) is the most directly scraping-focused of the LLM-adjacent tools: a structured scraping API with JSON extraction mode and MCP server support, comparable to FireCrawl. It does not handle anti-bot bypass and is not suitable for protected targets.

## Additional AI Browser Tools (2026)

**Vercel agent-browser** (github.com/vercel-labs/agent-browser, 14.7k stars, Apache-2.0): browser automation CLI built for AI agents. The Vercel Labs project provides a headless browser environment designed specifically for agentic workloads — navigating, clicking, and extracting information in response to natural-language instructions. Positioned as an open-source alternative to commercial browser-as-a-service platforms for AI agent use cases.

**iOS 26 / macOS 26 WebPage API**: Apple shipped a native headless browser capability in iOS 26 and macOS 26 as part of SwiftUI WebKit. The `WebPage` class loads a URL, runs JavaScript, and returns rendered HTML with no visible on-screen view required. The practical relevance: an AI app using `WebPage` fetches content from the user's device using a real Safari engine and the device's residential IP address. Server-side scraping blocks (Cloudflare challenges, 403s, cookie walls) that would stop a cloud-based fetch tend not to apply — the request looks identical to a Safari user navigating normally. Demonstrated in production via the Cumbersome app's `openWebPageLocally` tool. `socks5h://` syntax applies here as it does to CLI proxies: load with `WebPage`, run `await webPage.callJavaScript("...")` to extract rendered HTML. Availability: `#available(iOS 26.0, macOS 26.0, *)`.

**Kimurai** (github.com/vifreefly/kimuraframework, 1.1k stars): Ruby scraping framework with an AI-assisted DSL. Uses LLM inference to identify where data lives on a page, then caches the discovered selectors for subsequent requests. Positioned as getting "the intelligence of an LLM without the per-request latency or token costs" for each request after the initial discovery pass.

## Related

- [browser-fingerprinting](./browser-fingerprinting.md)
- [hybrid-scraping](./hybrid-scraping.md)
- [ai-scraping-assistants](./ai-scraping-assistants.md)
- [AnyCrawl](../entities/anycrawl.md)

## Sources

- [https://substack.thewebscraping.club/p/scraping-with-llms-gpt-vision](https://substack.thewebscraping.club/p/scraping-with-llms-gpt-vision)
- [https://substack.thewebscraping.club/p/how-to-use-llms-in-scraping](https://substack.thewebscraping.club/p/how-to-use-llms-in-scraping)
- [https://substack.thewebscraping.club/p/scraping-with-llms-scrapegraphai](https://substack.thewebscraping.club/p/scraping-with-llms-scrapegraphai)
- [https://substack.thewebscraping.club/p/llm-scrapegraphai-costs-web-scraping](https://substack.thewebscraping.club/p/llm-scrapegraphai-costs-web-scraping)
- [https://substack.thewebscraping.club/p/writing-scrapers-with-llms](https://substack.thewebscraping.club/p/writing-scrapers-with-llms)
- [https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping](https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping)
- [https://substack.thewebscraping.club/p/building-self-healing-scrapers-with-gpt](https://substack.thewebscraping.club/p/building-self-healing-scrapers-with-gpt)
- [https://substack.thewebscraping.club/p/anycrawl-llm-ready-web-scraping](https://substack.thewebscraping.club/p/anycrawl-llm-ready-web-scraping)
- [https://substack.thewebscraping.club/p/anycrawl-testing-the-llm-ready-web](https://substack.thewebscraping.club/p/anycrawl-testing-the-llm-ready-web)
- [https://substack.thewebscraping.club/p/when-browsers-think-chatgpt-atlas-cursor-browserbase](https://substack.thewebscraping.club/p/when-browsers-think-chatgpt-atlas-cursor-browserbase)
- [https://github.com/vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- [https://folding-sky.com/blog/ios-26-macos-26-swiftui-headless-browser-webpage-webview](https://folding-sky.com/blog/ios-26-macos-26-swiftui-headless-browser-webpage-webview)
- [https://github.com/vifreefly/kimuraframework](https://github.com/vifreefly/kimuraframework)
