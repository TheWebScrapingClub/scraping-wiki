---
name: mycel
type: entity
category: library
first_seen: 2026-07-08
last_updated: 2026-07-08
sources:
  - mycel.md
---

# mycel

## What it is

Mycel is a fast, decentralized web crawler, indexer, and search engine implemented in a Rust binary. It operates on a pipeline that involves seeding, crawling, archiving, indexing, and ranking to provide search capabilities over collected web data.

## How it works

The process begins with seeding an address, which enqueues the root and treats discovered off-host links as candidates. Crawling adheres to `robots.txt` per RFC 9309, enforcing a policy of one request per host via a claim query, which includes mechanisms to handle rate limiting (429 responses). Fetched pages are appended to a WARC file, which serves as the source of truth and advances a durable watermark upon synchronization.

Text is extracted from fetched pages, near-duplicates are composted using SHA256 for exact matches and simhash for near matches, and surviving text is indexed in a tantivy BM25 index. Ranking is computed by folding harmonic centrality over the host webgraph into the BM25 score. Federated results are interleaved round-robin and deduplicated by URL, ensuring that no single peer's score can dominate the final ranking.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://splch.github.io/mycel/](https://splch.github.io/mycel/)
