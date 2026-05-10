# The Web Scraping Wiki

A structured, LLM-maintained knowledge base covering anti-bot systems, scraping tools, browser fingerprinting, proxy infrastructure, and everything else that matters when extracting data from the web.

## What is this

This wiki compiles and organizes the knowledge accumulated across 300+ articles published on [The Web Scraping Club](https://thewebscraping.club/) newsletter since 2022, plus selected research from outside sources (Antoine Vastel's [Device and Browser Info](https://deviceandbrowserinfo.com/), Castle.io research, vendor blogs from DataDome, Cloudflare, Akamai, Bright Data, Oxylabs, and others).

Instead of searching through years of articles to find what we tested on Cloudflare, how Akamai's TLS detection works, or which tool bypassed Kasada last, the wiki keeps it all in one place, cross-referenced and continuously updated.

## Inspirations

The pattern comes from Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): rather than re-deriving knowledge from raw sources on every question, an LLM incrementally builds and maintains a persistent wiki that grows richer over time.

The Obsidian-friendly authoring conventions and the use of `.canvas` (JSON Canvas) and `.base` (Obsidian Bases) files come from Steph Ango (kepano), Obsidian's CEO, and his [obsidian-skills](https://github.com/kepano/obsidian-skills) bundle. The wiki uses `defuddle` for clean source extraction, `obsidian-markdown` conventions for page authoring, `obsidian-bases` for live cross-cutting views, and `json-canvas` for visual landscape maps.

## Sources

The wiki is built from publicly available articles, posts, and READMEs. The main feeds are:

- [The Web Scraping Club](https://thewebscraping.club/) — every TWSC article from 2022 onward.
- [Device and Browser Info](https://deviceandbrowserinfo.com/) — Antoine Vastel's research on browser fingerprinting and bot detection.
- [Hacker News](https://news.ycombinator.com/) — front-page submissions matching the wiki domain (web scraping, anti-bot, proxies, browsers, fingerprinting).
- Vendor research blogs (DataDome, Cloudflare, Akamai, Castle.io, Bright Data, Oxylabs, and more).
- Selected GitHub repositories and project sites for tools, libraries, and stealth browsers.

Every page lists its specific sources in YAML frontmatter under `sources:`, and the trail goes back to a URL or a filename inside this repository.

## How it's maintained

We do not maintain this wiki manually. An LLM pipeline reads new articles every day, decides which ones belong in the wiki, drafts new entity or concept pages, links sources to existing pages, and commits the result. Contradictions between old and new findings are resolved explicitly: the newest behavioral observation wins, but the prior version is preserved with a date so the evolution remains visible. The full ruleset is in [schema.md](schema.md).

These are summaries of public articles, restructured for navigation. If you spot an error, an outdated claim, or a misattribution, please open an issue on this repository pointing to the specific page and what is wrong. We will fix it on the next daily run.

## What you will find

The wiki holds **120 pages** across six types. Each type answers a different shape of question.

### Entities (85 pages)

One page per concrete thing in the domain. An entity is a tool, a library, a stealth browser, a commercial anti-bot product, a proxy network, or any other identifiable subject that has its own technical profile. The page describes what it is, how it works, what TWSC observed when testing it, and known limitations.

Examples: [DataDome](entities/datadome.md), [Cloudflare](entities/cloudflare.md), [Camoufox](entities/camoufox.md), [Scrapling](entities/scrapling.md), [Playwright](entities/playwright.md), [curl_cffi](entities/curl-cffi.md), [Lightpanda](entities/lightpanda.md), [Browser Use](entities/browser-use.md).

### Concepts (27 pages)

One page per technique, pattern, or domain idea. Concepts cover the *how* and the *why*: how a detection technique works, what signals it relies on, where it shows up across vendors. They reference the entities that implement or exploit them.

Examples: [Browser Fingerprinting](concepts/browser-fingerprinting.md), [TLS Fingerprinting](concepts/tls-fingerprinting.md), [CDP Detection](concepts/cdp-detection.md), [Bot Detection](concepts/bot-detection.md), [ML-Based Bot Detection](concepts/ml-bot-detection.md), [Hybrid Scraping](concepts/hybrid-scraping.md), [Cookie and Session Reuse](concepts/cookie-session-reuse.md), [Proxy Fundamentals](concepts/proxy-fundamentals.md).

### Comparisons (2 pages)

Side-by-side analyses when two or more entities or approaches occupy the same niche and the question "which one and when?" is itself the topic. Each comparison page has a tabular dimension and a narrative of the differences that actually matter.

Examples: [Firefox vs Chrome Stealth](comparisons/firefox-vs-chrome-stealth.md), [Anti-Detect Browser Benchmark 2024](comparisons/anti-detect-browser-benchmark-2024.md).

### Timelines (1 page)

How something evolved over time, tracked across multiple sources. Used for situations where the *current* state is meaningless without the trajectory that produced it.

Example: [Cloudflare Bypass Evolution](timelines/cloudflare-bypass-evolution.md) from 2022 to 2026.

### Canvases (1 visual map)

[JSON Canvas](https://jsoncanvas.org/) files (`.canvas`) are graph-shaped visualizations Obsidian renders as an interactive whiteboard. Used for landscapes where 5+ entities and the relationships between them are the point. Each node references the matching entity page, so the canvas works as a navigable map.

Example: [Agentic Browsers Landscape 2026](canvases/agentic-browsers-landscape-2026.canvas) covering OpenAI Operator/Atlas, Anthropic Computer Use, Perplexity Comet, Browser Use, Browserbase, BrowserOS, Hyperbrowser, and the proxy companies pivoting to managed browsers.

### Views (4 queries)

[Obsidian Bases](https://help.obsidian.md/bases) files (`.base`) are declarative queries over the rest of the vault. A view does not store knowledge — it surfaces it. As soon as a new entity or concept is added with the matching frontmatter, the view updates automatically. Useful for cross-cutting reads like "every anti-bot vendor sorted by last update" or "every entity touched in the last 90 days".

Files: [all-entities](views/all-entities.base), [anti-bot-vendors](views/anti-bot-vendors.base), [recently-touched](views/recently-touched.base), [tools-and-browsers](views/tools-and-browsers.base).

## How to navigate

Start from [index.md](index.md) for the full catalog grouped by category, then drill into the specific entity, concept, or comparison page you care about. Each page lists its `sources:` in YAML frontmatter and ends with a `## Sources` section linking back to the original URLs.

## Use as an Obsidian vault

[Obsidian](https://obsidian.md/) is a free local-first markdown editor that treats a folder of `.md` files as a personal knowledge base. It builds a graph of cross-links, supports YAML frontmatter as queryable metadata, and ships with a Bases plugin (since 1.7) that turns the queries above into live tables.

This repository works directly as an Obsidian vault. Clone it standalone or symlink it under your existing vault, then open the folder in Obsidian:

```bash
# standalone
git clone https://github.com/TheWebScrapingClub/scraping-wiki.git ~/Vaults/scraping-wiki
open -a Obsidian ~/Vaults/scraping-wiki

# or as a sub-vault inside an existing vault
ln -s /path/to/scraping-wiki ~/MyVault/Wiki
```

Once open, you can:

- Browse the **graph view** — every cross-link between entities and concepts becomes an edge, and the wiki's structure becomes visible as a network.
- Click any `.base` file under [views/](views/) to render a live, sortable table of matching pages.
- Click [agentic-browsers-landscape-2026.canvas](canvases/agentic-browsers-landscape-2026.canvas) to open the interactive landscape map.
- Use any markdown editor or `git diff` to read the wiki — Obsidian is convenient but optional.

## Reporting errors

If you find something outdated, wrong, or misattributed, please open an issue on this repository pointing to the specific page and the claim that is off. Since the wiki is regenerated continuously, a simple GitHub issue is enough — no PR needed unless you also want to attach test results.

## License

The content of this wiki is derived from articles published on [The Web Scraping Club](https://thewebscraping.club/) and from third-party sources cited in each page. The wiki itself is open for reading and reference. For reuse of substantial portions, please credit the source.
