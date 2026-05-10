# The Web Scraping Wiki

A structured, LLM-maintained knowledge base covering anti-bot systems, scraping tools, browser fingerprinting, proxy infrastructure, and everything else that matters when extracting data from the web.

## What is this

This wiki compiles and organizes the knowledge accumulated across 300+ articles published on [The Web Scraping Club](https://thewebscraping.club/) newsletter since 2022, plus selected research from outside sources (Antoine Vastel's [Device and Browser Info](https://deviceandbrowserinfo.com/), Castle.io research, vendor blogs from DataDome, Cloudflare, Akamai, Bright Data, Oxylabs, and others).

Instead of searching through years of articles to find what we tested on Cloudflare, how Akamai's TLS detection works, or which tool bypassed Kasada last, the wiki keeps it all in one place, cross-referenced and continuously updated.

## Inspirations

The pattern comes from Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): rather than re-deriving knowledge from raw sources on every question, an LLM incrementally builds and maintains a persistent wiki that grows richer over time.

The Obsidian-friendly authoring conventions and the use of `.canvas` (JSON Canvas) and `.base` (Obsidian Bases) files come from Steph Ango (kepano), Obsidian's CEO, and his [obsidian-skills](https://github.com/kepano/obsidian-skills) bundle. The wiki uses `defuddle` for clean source extraction, `obsidian-markdown` conventions for page authoring, `obsidian-bases` for live cross-cutting views, and `json-canvas` for visual landscape maps.

## How it works

A daily cron pipeline runs on a Mac mini paired with an [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) (GB10 Blackwell GPU) over an SSH tunnel:

1. **HN ingestion** at 07:00 fetches new web-scraping news from the Hacker News Algolia index.
2. **DBI ingestion** at 07:30 syncs new posts from deviceandbrowserinfo.com.
3. **Wiki update** at 10:30 runs the local LLM pipeline:
   - **Pass 1** — a Gemma 4 E2B classifier (Q8 GGUF, served by `llama.cpp` on the DGX) decides whether each new source belongs in the wiki. The classifier flags both tool/library content AND research-side content (detection techniques, fingerprint signal analysis, browser-platform news).
   - **Pass 2** — for new entities (tools/products/libraries that don't yet have a wiki page), the LLM drafts an entity page following the [schema](schema.md), with frontmatter, sections, and validated cross-links.
   - **Pass 3** — for items whose primary entity already exists, the source filename is appended to the page's `sources:` list. The LLM also picks at most one related concept page that the source enriches and adds the source there too.
   - **Index recompact** — `index.md` is regenerated from the actual wiki tree, grouping entities by category and alphabetizing within each group. Curated blurbs from prior versions are preserved.
   - **Auto-commit and push** — if the wiki tree changed, a daily commit goes to GitHub.

Contradictions between old and new findings are resolved explicitly: the most recent observation wins for behavioral claims, but both versions are preserved with dates so the evolution remains visible. The full ruleset is in [schema.md](schema.md).

We do not write the wiki manually. The LLM does the bookkeeping, cross-referencing, and maintenance. We focus on testing, writing, and asking the right questions.

## What you will find

**120 pages** across these types:

- **Entities** (85 pages): anti-bot systems (Cloudflare, Akamai, DataDome, PerimeterX/HUMAN, Kasada, AWS WAF, reCAPTCHA, F5), scraping tools and libraries (Camoufox, Playwright, Scrapling, curl_cffi, Pydoll, Crawl4AI, GoScrapy, and many more), stealth and anti-detect browsers (Kameleo, GoLogin, Lightpanda, Konform, Owl, Browser Use), proxy networks and tools (NyxProxy, MeshScrape, BlankTrace, ClashMac, IPidea, Firehol), and web unblocker services.

- **Concepts** (27 pages): browser fingerprinting, TLS fingerprinting, CDP detection, ML-based bot detection, the bot detection discipline as a whole, hybrid scraping, cookie reuse patterns, proxy economics, LLM-based scraping, legal landscape, mouse movement emulation, WebSocket detection, IPv6 proxy rotation, and more.

- **Comparisons** (2 pages): Firefox vs Chrome stealth tools, anti-detect browser benchmark 2024.

- **Timelines** (1 page): Cloudflare bypass evolution from 2022 to 2026.

- **Canvases** (1 visual map): the agentic-browsers landscape covering OpenAI Operator/Atlas, Anthropic Computer Use, Perplexity Comet, Browser Use, Browserbase, BrowserOS, Hyperbrowser, and the YC batches that produced them.

- **Views** (4 Obsidian Bases queries): all entities by category, anti-bot vendors, recently-touched pages, tools and browsers.

Every factual claim traces back to a source article filename in the page's `sources:` frontmatter.

## How to navigate

Start from [index.md](index.md) for the full catalog grouped by category. Then click into the specific entity or concept page you care about.

## Use as an Obsidian vault

This repository works directly as an Obsidian vault. Clone it on its own or symlink it under your existing vault, then open the folder in Obsidian:

```bash
# standalone
git clone https://github.com/TheWebScrapingClub/scraping-wiki.git ~/Vaults/scraping-wiki
open -a Obsidian ~/Vaults/scraping-wiki

# or as a sub-vault inside an existing vault
ln -s /path/to/scraping-wiki ~/MyVault/Wiki
```

What you get inside Obsidian:

- Graph view shows connections between entities and concepts via the markdown cross-links in each page.
- The `.base` files under [views/](views/) render as live cross-cutting tables (e.g. all anti-bot vendors grouped by last update) thanks to the built-in Bases plugin.
- The `.canvas` file under [canvases/](canvases/) renders as an interactive visual map.
- YAML frontmatter (`type`, `category`, `last_updated`, `sources`) is queryable from Bases and from Dataview if you use it.

For best results, enable the Bases core plugin (built-in since Obsidian 1.7).

## Contributing

This wiki reflects what The Web Scraping Club has tested and observed, plus what the daily pipeline picks up from outside research. If you find something outdated or wrong, open an issue referencing the specific page and claim. If you have test results that contradict or extend what is documented here, we want to hear about it.

## License

The content of this wiki is derived from articles published on [The Web Scraping Club](https://thewebscraping.club/) and from third-party sources cited in each page. The wiki itself is open for reading and reference. For reuse of substantial portions, please credit the source.
