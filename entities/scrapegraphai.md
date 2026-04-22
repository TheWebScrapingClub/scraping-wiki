---
name: ScrapeGraphAI
type: entity
category: tool
first_seen: 2024-05-30
last_updated: 2026-04-22
---

# ScrapeGraphAI

## What It Is

ScrapeGraphAI is an open-source Python library and commercial API for LLM-powered web scraping. The open-source project (GitHub: ScrapeGraphAI/Scrapegraph-ai) allows scraping any webpage by providing a prompt and a URL — the tool handles fetching, parsing, and calling an LLM to extract the requested data. The commercial API variant (scrapegraphai.com) wraps the same idea with managed infrastructure including anti-bot bypass. The project was developed by Italian researchers and reached 9,000+ GitHub stars within months of release (as of mid-2024).

## How It Works

ScrapeGraphAI is built around the concept of "Graphs" — directed pipelines of nodes, each handling a step in the scraping process.

The core pipeline nodes are:
- **FetchNode**: fetches the URL (using Playwright for dynamic pages).
- **ParseNode**: parses and chunks the HTML into manageable segments.
- **RAGNode**: stores the chunks in a vector store for retrieval.
- **GenerateAnswerNode**: calls the configured LLM with the relevant chunks and the user's prompt, returning structured output.

The main graph types available:
- **SmartScraperGraph**: single-page scraper. Takes a URL and a prompt, returns structured JSON.
- **SmartScraperMultiGraph**: parallel multi-page scraper. Runs multiple SmartScraperGraph instances simultaneously.
- **SearchGraph**: uses a search engine as the starting point rather than a direct URL.
- **ScriptCreatorGraph**: instead of returning data, returns a BeautifulSoup Python scraper. Uses a `GenerateScraperNode` in place of the answer node.
- **SpeechGraph**: text-to-speech output.

The library supports any LLM that can be configured via LangChain: OpenAI models (GPT-3.5-turbo, GPT-4o, GPT-4-turbo), local models via Ollama (Mistral, Llama), Gemini, and others. The model is swapped by changing the configuration dict.

The commercial API simplifies the interface to: provide a URL and a desired output schema, receive structured data. Anti-bot bypass is handled on the server side.

## TWSC Experience

**Net-A-Porter product listing page with GPT-3.5-turbo (2024-05)**: prices were entirely wrong — the model returned fabricated numbers, not the ones on the page. Running the same prompt the next day returned different wrong results, pulling brand filter names from the sidebar and treating them as product names. The non-determinism across identical runs is the core reliability problem.

**Net-A-Porter single product page with GPT-3.5-turbo (2024-05)**: qualitative fields (category, subcategory, brand) extracted correctly. Sizes showed hallucinations. A minor prompt change (adding a period after one sentence) caused the model to describe a completely different product.

**Net-A-Porter single product page with GPT-4o (2024-05)**: significantly better. No hallucinations observed on qualitative fields.

**TripAdvisor hotel page with GPT-3.5-turbo (2024-05)**: with a minimal prompt, all data fields correctly mapped. 3 of 5 reviews returned. GPT-4o corrected the count but lost the location field.

**GitHub repositories with GPT-4o via ScriptCreatorGraph (2024-09)**: generated a working BeautifulSoup scraper on the first attempt. Best result across all tested sites. Likely because GitHub's HTML structure was heavily represented in the model's training data.

**BBC article with GPT-4o and Mistral (2024-09)**: Mistral read the page correctly and returned the right data when asked for direct extraction, but could not reliably generate a working scraper from the HTML. Repeated runs produced inconsistent results.

**Multiple e-commerce sites via the commercial API (2025-05)**: described as "quite good on almost every website" in a conference presentation context. The API's built-in anti-bot bypass makes it more practical than the open-source version for sites with bot protection.

A cost experiment across 100 URLs from 33 e-commerce sites produced: 72% successful extraction, 13% fetch errors, 15% parse errors, at a total API cost of $4. Extrapolated to 10,000 URLs: $400 and roughly 2,800 failed extractions.

## Known Limitations

- **Non-determinism**: the same prompt and URL can return different results on different runs. This makes the tool fundamentally difficult to test and impossible to trust without per-run validation.
- **Price/numeric hallucination**: GPT-3.5-turbo (and to a lesser extent GPT-4o) can fabricate numeric values that look plausible but don't match the page. This is a known failure mode for numeric fields specifically.
- **Prompt sensitivity**: small changes to the prompt wording can produce radically different outputs or cause the model to describe a different page entirely.
- **No anti-bot bypass in open-source**: the open-source library runs a standard browser automation tool. Sites with active bot protection will block it. The commercial API addresses this.
- **Cannot access data in internal APIs**: if the target data is only available via an XHR or internal API call (not in the rendered HTML), ScrapeGraphAI cannot retrieve it.
- **Token costs at scale**: at $4 per 100 URLs (2024 pricing), extracting from a single large site with millions of URLs is cost-prohibitive compared to a traditional scraper.
- **Prompt engineering overhead**: getting reliable extraction on a new site often requires significant trial and error. The process has been described as "playing slot machines" — iterating without a clear debugging path.

## Related

- [llm-scraping](../concepts/llm-scraping.md)
- [ai-scraping-assistants](../concepts/ai-scraping-assistants.md)
- [hybrid-scraping](../concepts/hybrid-scraping.md)

## Sources

- [https://substack.thewebscraping.club/p/scraping-with-llms-scrapegraphai](https://substack.thewebscraping.club/p/scraping-with-llms-scrapegraphai)
- [https://substack.thewebscraping.club/p/llm-scrapegraphai-costs-web-scraping](https://substack.thewebscraping.club/p/llm-scrapegraphai-costs-web-scraping)
- [https://substack.thewebscraping.club/p/writing-scrapers-with-llms](https://substack.thewebscraping.club/p/writing-scrapers-with-llms)
- [https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping](https://substack.thewebscraping.club/p/the-lab-84-ai-driven-web-scraping)
