---
name: ai-scraping-assistants
type: concept
first_seen: 2025-03-21
last_updated: 2026-04-22
---

# AI Scraping Assistants

## Definition

AI scraping assistants are setups where a large language model is embedded into the development workflow to generate, modify, or repair scrapers — rather than to extract data at runtime. The LLM acts as an accelerator for the developer, not as a replacement for the scraper itself. The canonical current form is an AI-powered IDE (Cursor) connected to custom tooling via the Model Context Protocol (MCP).

## How It Works

The core components of the current best-practice setup are:

**Cursor IDE**: an AI-first code editor built on VS Code. The AI assistant has full visibility into the local codebase, can edit files, generate new code from natural language prompts, and learns the codebase's conventions over time. The autocomplete in a standardized scraper codebase is significantly more accurate than with a generic codebase because the pattern space is narrow.

**Model Context Protocol (MCP)**: an open standard developed by Anthropic that standardizes how AI models connect to external tools and data sources. In practice it is a client-server architecture: the AI (client, running inside Cursor) connects to one or more MCP servers that expose specific capabilities. Each server is a programmed function — given a defined input, it produces a defined output — so there is no LLM fuzziness inside the server itself. MCP was open-sourced by Anthropic in early 2024.

An MCP server for scraping assistance typically exposes tools like:
- `fetch_page_content`: opens a browser (typically Camoufox for stealth), navigates to the URL from the prompt, saves the HTML to a file.
- `generate_xpaths`: reads the HTML file and, given a template identifier (PLP/PDP), returns field definitions for XPath generation.
- `write_camoufox_scraper`: reads a scraper template and the selectors file, generates a new scraper.

Each tool is a deterministic function. The LLM's role is to parse the natural language prompt, determine which tool to invoke and with which arguments, confirm with the user, and then process the tool's output. Intermediate results are saved to files between steps rather than passed through the context window — this avoids context size limits and makes each step independently inspectable.

**Cursor rules**: structured instructions stored in `.cursor/rules/` that encode the developer's conventions and procedures. Rules define things like: which XPath patterns to prefer, what the scraper template looks like, what data model to use for PLP vs PDP scrapers, how to detect anti-bot cookies and respond. The more specific and prescriptive the rules, the more consistent the LLM output.

**LLM selection**: Claude Sonnet 3.7 has been the model of choice in TWSC experiments for this use case. It was found more reliable and predictable than GPT-4o when operating with MCPs and rules. Cursor CEO has noted Claude handles real-world coding tasks well enough that it became the default model for all Cursor users.

## Where It Matters

This pattern is most valuable when:
- A team runs many scrapers with a standardized structure (the LLM learns and applies the pattern).
- The same data model recurs across many sites (PLP e-commerce, PDP e-commerce, etc.).
- Anti-bot protection on the target is light to moderate — heavy protection (Kasada, DataDome) still requires manual intervention to select and configure the right tools.

The setup is less useful for:
- One-off scraping tasks where setup time exceeds direct coding time.
- Sites that require reverse-engineering internal APIs (the assistant cannot inspect the network tab or reason about API endpoints it has not seen).
- Sites with strong anti-bot protection — the assistant can detect cookies from known providers but cannot bypass Kasada or DataDome automatically.

## What We Tested

**MCP + Camoufox + Cursor + Claude 3.7 Sonnet on Gucci.com (2025-03)**: given the prompt "Fetch the URL, write XPath selectors using PLP template, write a Camoufox scraper", the assistant opened Camoufox, browsed to the URL, saved HTML, generated XPath selectors in a text file, and generated a working scraper on the first run. The scraper correctly populated all product fields. Issues noted: prompt did not always produce the same outcome across runs; output data structure defaulted to what the template defined rather than what was explicitly requested.

**AI Scrapy assistant with Cursor rules (2025-04)**: a rule set was defined that instructed the assistant to:
1. Understand the scraper type from the prompt (PLP vs PDP).
2. Create the Scrapy project structure.
3. Use the MCP to browse the starting URL and download HTML and cookies.
4. Analyze HTML for JSON first, then fall back to CSS/XPath selectors.
5. Read cookies to detect anti-bot providers — stop if Kasada or DataDome detected; implement `scrapy_impersonate` if Akamai detected.
6. Optimize `settings.py` with headers and user agent.
7. Write and launch the scraper.

Results after extensive rule tuning: the process is not yet reliable enough to run unsupervised. The main failure mode is the LLM going off-script when edge cases arise. The mitigation is making rules as specific and constrained as possible.

**OpenAI Codex for scraping (2025-05)**: no internet access in the sandboxed environment; feeding HTML via prompt crashes due to context size. Verdict: not suitable for this use case at current capability level.

**Cursor + MCP cost**: approximately $20/month for Cursor Pro, plus LLM API costs (OpenAI or Anthropic). Total is a fraction of the time saved on routine spider creation.

## Current State

As of 2025, Cursor + MCP + Claude is a working productivity tool for scraper development. It is not autonomous — human supervision is required at each step, and reliability across repeated runs of the same prompt is not yet consistent. The practical value is compressing the time to write a first-draft scraper from hours to minutes, with a human doing final review and launch.

The pattern improves with investment: the more specific the Cursor rules, the more scraper templates are defined, and the more MCP tools are added, the more capable the assistant becomes. It is a system that compounds over time.

Alternative hosted MCP servers exist (BrowserBase, Hyperbrowser) with pre-built tools for page interaction and data extraction, reducing the need to build a custom server from scratch.

## Related

- [llm-scraping](./llm-scraping.md)
- [camoufox](../entities/camoufox.md)
- [hybrid-scraping](./hybrid-scraping.md)

## Sources

- [https://substack.thewebscraping.club/p/cursor-mcp-web-scraping-assistant](https://substack.thewebscraping.club/p/cursor-mcp-web-scraping-assistant)
- [https://substack.thewebscraping.club/p/claude-cursor-ai-scraping-assistant](https://substack.thewebscraping.club/p/claude-cursor-ai-scraping-assistant)
- [https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping](https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping)
- [https://substack.thewebscraping.club/p/building-self-healing-scrapers-with-gpt](https://substack.thewebscraping.club/p/building-self-healing-scrapers-with-gpt)
- [https://substack.thewebscraping.club/p/writing-scrapers-with-llms](https://substack.thewebscraping.club/p/writing-scrapers-with-llms)
