---
name: Algolia
type: entity
category: target
first_seen: 2023-12-10
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/algolia-and-web-scraping-an-introduction
  - https://substack.thewebscraping.club/p/scraping-algolia-endpoints
---

# Algolia

## What It Is

Algolia is a cloud-based search-as-a-service platform. Websites integrate it to power fast, dynamic search and browse experiences. For scraping purposes, Algolia is relevant because a large number of e-commerce sites use it as their product catalog query engine, and the API endpoints Algolia exposes are often easier to scrape than the sites' own HTML.

## How It Works

When a site uses Algolia, the browser does not query the site's own backend for search or browse results. Instead, it queries Algolia's servers directly from the client using credentials embedded in the JavaScript bundle. The request goes to a URL like:

```
https://<app-id>-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=...&x-algolia-api-key=...&x-algolia-application-id=...
```

Three key parameters appear in every Algolia URL:
- `x-algolia-application-id`: Unique ID for the Algolia application. Routes the request to the correct account.
- `x-algolia-api-key`: Authentication key. This is a client-side (search-only) key embedded in the page source and not a secret. It allows querying the indexes but not modifying them.
- `x-algolia-agent`: Identifies the client library and version (e.g., `Algolia for JavaScript (3.35.1); Browser`).

The POST body contains the query in one of two formats:
- **Open text search** (as in Hacker News): `{"query": "scraping", "hitsPerPage": 30, ...}`
- **InstantSearch / browse** (as in Michelin Guide, EndClothing): `{"requests": [{"indexName": "...", "params": "facetFilters=...&page=0&hitsPerPage=120..."}]}`

Pagination changes only the `page` parameter in the params string. All other parameters remain constant between pages.

## TWSC Experience

### EndClothing.com (Lab #54)

The entire product catalog of EndClothing.com was accessible through a single Algolia endpoint:
```
https://search1web.endclothing.com/1/indexes/*/queries?x-algolia-application-id=KO4W2GBINK&x-algolia-api-key=dfa5df098f8d677dd2105ece472a44f8
```

The site itself was protected by Akamai, but the Algolia API endpoint had no anti-bot protection. A curl request with standard browser headers returned the full product catalog. The JSON response per product included: name, description, SKU, prices per country (up to 16 currency variants), stock levels per size, category hierarchy, brand, media gallery URLs, and metadata fields.

To minimize scraper complexity, the original four-request payload was reduced to a single query by removing category filters. This retrieved the entire catalog without iterating over categories.

### Michelin Guide (algolia-and-web-scraping-an-introduction)

All starred restaurants available via Algolia InstantSearch. The only parameter that changed between pages was `page`. The response included GPS coordinates, cuisine types, star counts, Chef names, and regional classifications.

### General Pattern

Algolia endpoints can be identified by:
1. Opening DevTools Network tab on the target site and filtering by `algolia.net` in the URL filter.
2. Looking for POST requests with the `queries` path segment.
3. The three `x-algolia-*` parameters are always present and identify the deployment.

## Known Limitations

- The `x-algolia-api-key` is a client-side search key. It cannot be used to write data. Some keys have query restrictions (e.g., only certain indexes, only certain attributes). If the site restricts what the key can retrieve, those restrictions apply to the scraper as well.
- Algolia's terms of service prohibit using their API for data extraction without authorization from the site owner.
- Algolia endpoints that sit behind the same CDN protection as the main site (rather than using Algolia's own infrastructure at `algolia.net`) may inherit the site's anti-bot protections.

## Related

- [api-scraping](../concepts/api-scraping.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)
- [Akamai](akamai.md)
