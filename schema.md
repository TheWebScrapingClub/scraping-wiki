# TWSC Wiki Schema

This document defines the structure, conventions, and rules for the TWSC knowledge wiki. The wiki is a persistent, LLM-maintained knowledge base that sits between the raw source archive and the article writing process. The LLM writes and maintains it. The human curates, directs, and reads.

## Purpose

Accumulate and organize everything TWSC learns about web scraping, anti-bot systems, tools, and techniques across articles, research, and news. Eliminate the need to re-derive knowledge from scratch for each new article.

## Directory structure

```
wiki/
  schema.md          # This file. Rules and conventions.
  index.md           # Content catalog. Updated on every ingest.
  log.md             # Chronological record of all wiki operations.
  entities/          # Pages for specific things: tools, anti-bot systems, providers, sites.
  concepts/          # Pages for techniques, patterns, and ideas.
  comparisons/       # Side-by-side analyses between entities or approaches.
  timelines/         # How something evolved over time.
  canvases/          # JSON Canvas visual maps of landscapes and ecosystems.
  views/             # Obsidian Bases queries (.base) for live cross-cutting views.
```

## Page types

### Entity pages (`entities/`)

One page per distinct tool, anti-bot system, proxy provider, or scraping target.

Filename: `kebab-case.md` matching the entity name.

Required frontmatter:

```yaml
---
name: Entity Name
type: entity
category: tool | anti-bot | proxy-provider | browser | target | library
first_seen: YYYY-MM-DD        # When TWSC first covered this
last_updated: YYYY-MM-DD      # When this page was last modified
sources: []                    # List of article/news filenames that informed this page
---
```

Page structure:

1. **What it is** - one paragraph, no fluff
2. **How it works** - technical explanation based on what TWSC has observed or tested
3. **TWSC experience** - what we found when we used/tested/analyzed it, with references to specific articles
4. **Known limitations** - what does not work, what breaks, what changed
5. **Related** - wiki links to related entities and concepts

### Concept pages (`concepts/`)

One page per technique, pattern, or domain concept.

Filename: `kebab-case.md`.

Required frontmatter:

```yaml
---
name: Concept Name
type: concept
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
sources: []
---
```

Page structure:

1. **Definition** - what it is, in TWSC's domain context
2. **How it works** - mechanics, based on observation and testing
3. **Where it matters** - which anti-bot systems or scraping scenarios rely on this
4. **What we tested** - specific experiments and findings from TWSC articles
5. **Current state** - what is the latest known behavior (with date)
6. **Related** - wiki links

### Comparison pages (`comparisons/`)

Side-by-side analysis of two or more entities or approaches.

Filename: `entity-a-vs-entity-b.md` or descriptive kebab-case.

Required frontmatter:

```yaml
---
name: Comparison Title
type: comparison
subjects: []                   # List of compared entities
last_updated: YYYY-MM-DD
sources: []
---
```

Page structure:

1. **What is being compared** - and why the comparison matters
2. **Comparison table** - dimensions relevant to the use case
3. **Key differences** - narrative explanation of what actually matters
4. **When to use which** - practical guidance based on TWSC findings
5. **Related** - wiki links

### Timeline pages (`timelines/`)

How something evolved over time, tracked across multiple sources.

Filename: `kebab-case-timeline.md`.

Required frontmatter:

```yaml
---
name: Timeline Title
type: timeline
subject: entity-name           # What this tracks
last_updated: YYYY-MM-DD
sources: []
---
```

Page structure:

1. **Subject** - what is being tracked and why it matters
2. **Timeline** - chronological entries, each with date, what changed, and source reference
3. **Current state** - latest known status
4. **Related** - wiki links

### Canvas pages (`canvases/`)

JSON Canvas (`.canvas`) visual maps of a landscape, ecosystem, or set of relationships. Used for things that are inherently graph-shaped and where a list or table flattens too much information: vendor ecosystems, competitor maps, evolution flows, "who-acquired-whom" diagrams.

A canvas is a companion to entity pages, not a replacement for them. Each node should reference an existing entity or concept page when one exists.

Filename: `kebab-case.canvas`.

Authoring rules:

- Use the `json-canvas` skill to create or edit `.canvas` files. Do not hand-write JSON Canvas syntax.
- Each node that represents a wiki entity must include the entity's wikilink in the node label or text (e.g., `[[Bright Data]]`) so Obsidian renders the connection.
- Group related nodes (same category) into a JSON Canvas group with a label.
- Edges should carry a label when the relationship type is non-obvious (e.g., "acquired", "spun off from", "competitor in").
- Maintain a one-line description at the top-left text node explaining what the canvas tracks and the date it was last refreshed.

When to create a canvas vs. a comparison page:

- Comparison page when you have 2-4 entities and a stable set of dimensions. Reads as a table.
- Canvas when you have 5+ entities or the relationships between them are the point. Reads as a graph.

### View pages (`views/`)

Obsidian Bases (`.base`) files: declarative queries over the rest of the vault. A view does not store knowledge, it surfaces it. Use views for cross-cutting reads that change as the underlying entity/concept pages change.

Examples of useful views:
- All entities in the `anti-bot` category, ordered by `last_updated`
- All entity pages with no inbound wikilinks (orphan check)
- All comparison pages mentioning a given entity
- All entities first seen in the last 90 days

Authoring rules:

- Use the `obsidian-bases` skill to create or edit `.base` files. Do not hand-write base syntax.
- Each view file must have a one-line comment header explaining what the view shows.
- Views must filter on properties already present in the page schemas above (e.g., `type`, `category`, `last_updated`). If a view requires a property not yet in the schema, add the property to the schema first.

## Cross-referencing

- Use standard markdown links to reference other wiki pages: `[Cloudflare](../entities/cloudflare.md)`
- Always use relative paths from the current file
- When an entity or concept is mentioned in a page, link it on first mention
- Do not link the same page more than once per section

## Source references

- Sources are listed at the bottom of each page in a `## Sources` section as a bulleted list of markdown links
- Use the full URL: `- [https://substack.thewebscraping.club/p/<slug>](https://substack.thewebscraping.club/p/<slug>)`
- For news and research sources, use the `url_canonical` from the article's frontmatter
- For inline text references, use markdown links with the URL
- Always add the source URL to the page's Sources section when adding information from a new article

## Contradiction resolution policy

When a newer source contradicts an older one, apply these rules in order:

1. **Behavioral/technical claims (what works, what is blocked, success rates):** the most recent observation wins. Anti-bot systems and tools change constantly. Replace the old claim with the new one, but add a dated note: `Previously (YYYY-MM): [old claim]. As of (YYYY-MM): [new claim].`

2. **Different configurations of the same system:** both claims survive. Cloudflare on Harrods behaves differently than Cloudflare on Indeed. Label each claim with its specific target and date.

3. **Structural/architectural claims (how a system works internally):** newer wins only if the source demonstrates the change through testing. If the newer article just describes behavior differently without evidence of a change, keep both perspectives.

4. **Economics and pricing:** newest data always wins. Mark the date explicitly.

5. **Tool capabilities:** newest version documentation wins. Note which version was tested.

In all cases, preserve enough context that a reader can understand what changed and when. The wiki should reflect the current state while making the evolution visible.

## Updating rules

1. **Never delete information without replacement.** If a fact becomes outdated, mark it with the date it was superseded and add the new information.
2. **Always update `last_updated`** in frontmatter when modifying a page.
3. **Always update `sources`** when adding information from a new source.
4. **Always update `index.md`** after creating or significantly modifying a page.
5. **Always append to `log.md`** after any wiki operation.
6. **Contradictions must be explicit.** If a new source contradicts existing wiki content, note both claims with their sources and dates. Do not silently overwrite.
7. **Claims require sources.** Every factual claim on a wiki page must trace back to at least one source in the archive. If it cannot, mark it as unverified.

## What does NOT go in the wiki

- Raw article text (that stays in the archive)
- Opinion or speculation not grounded in testing
- Marketing claims from tool vendors unless verified
- Duplicate information already covered in another wiki page (link instead)
