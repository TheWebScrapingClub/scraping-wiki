# The Web Scraping Wiki

A structured, LLM-maintained knowledge base covering anti-bot systems, scraping tools, browser fingerprinting, proxy infrastructure, and everything else that matters when extracting data from the web.

## What is this

This wiki compiles and organizes the knowledge accumulated across 300+ articles published on [The Web Scraping Club](https://thewebscraping.club/) newsletter since 2022. Instead of searching through years of articles to find what we tested on Cloudflare, how Akamai's TLS detection works, or which tool bypassed Kasada last, the wiki keeps it all in one place, cross-referenced and up to date.

The idea is inspired by Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: rather than re-deriving knowledge from raw sources on every question, an LLM incrementally builds and maintains a persistent wiki that grows richer with every article published.

## How it works

Every time a new article is published on The Web Scraping Club, the relevant wiki pages are updated with new findings, test results, and observations. The LLM reads the article, identifies which entities and concepts are affected, and integrates the new information following a set of rules defined in [schema.md](schema.md). Contradictions between old and new findings are resolved explicitly: the most recent observation wins for behavioral claims, but both versions are preserved with dates so the evolution remains visible.

We do not write the wiki manually. The LLM does all the bookkeeping, cross-referencing, and maintenance. We focus on testing, writing, and asking the right questions.

## What you will find

**64 pages** organized in four categories:

- **Entities** (31 pages): anti-bot systems (Cloudflare, Akamai, DataDome, PerimeterX/HUMAN, Kasada, AWS WAF, reCAPTCHA, F5), scraping tools and libraries (Camoufox, Playwright, Scrapling, curl_cffi, Pydoll, and more), anti-detect browsers (Kameleo, GoLogin, Dolphin Anty), and web unblocker services.

- **Concepts** (26 pages): browser fingerprinting, TLS fingerprinting, CDP detection, hybrid scraping, cookie reuse patterns, proxy economics, LLM-based scraping, legal landscape, mouse movement emulation, WebSocket detection, and more.

- **Comparisons** (2 pages): Firefox vs Chrome stealth tools, anti-detect browser benchmark 2024.

- **Timelines** (1 page): Cloudflare bypass evolution from 2022 to 2026.

Every factual claim traces back to a source article via URL in the page frontmatter.

## How to navigate

Start from [index.md](index.md) for a full catalog of all pages with one-line descriptions.

Each page uses YAML frontmatter with metadata (type, category, sources, last updated) and markdown links to related pages. If you use Obsidian, the wiki works as a vault with the graph view showing connections between entities and concepts.

## Contributing

This wiki reflects what The Web Scraping Club has tested and observed. If you find something outdated or wrong, open an issue referencing the specific page and claim. If you have test results that contradict or extend what is documented here, we want to hear about it.

## License

The content of this wiki is derived from articles published on [The Web Scraping Club](https://thewebscraping.club/). The wiki itself is open for reading and reference. For reuse of substantial portions, please credit the source.
