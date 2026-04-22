---
name: inventory-tracking
type: concept
first_seen: 2023-09-14
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/scraping-inventory-level
  - https://substack.thewebscraping.club/p/scraping-inventory-data
  - https://substack.thewebscraping.club/p/scraping-inventory-levels
  - https://substack.thewebscraping.club/p/the-lab-28-deep-dive-on-inventory
  - https://substack.thewebscraping.club/p/ikea-scraping-kallax
---

# Inventory Tracking

## Definition

Inventory tracking through web scraping is the practice of monitoring the stock levels of products on e-commerce sites and retail websites by extracting data that those sites expose for operational purposes — usually to power their own availability and pickup features. The extracted data is most valuable as a repeated time series rather than a single snapshot.

## Why It Matters

E-commerce sites must communicate stock availability to customers in real time: which sizes are in stock, whether click-and-collect is available at a given store, how many units are left. To do this, the site queries its own backend inventory systems, and those queries are often observable in network traffic. The data that flows back — typically stock quantities per SKU per location — represents live operational inventory that is not published anywhere else.

The primary use cases are:

- **Revenue estimation for investors**: Monitoring stock levels daily, then applying depletion rules (stock decrease = sale, stock increase above a threshold = restock), yields an approximation of unit sales. For publicly traded companies, this can produce a revenue signal ahead of quarterly earnings. We sold this kind of data to hedge funds through Re Analytics.
- **Competitive intelligence for operators**: Knowing which competitor SKUs are going out of stock, or which sizes sell fastest, informs purchasing, production, and pricing decisions.
- **Out-of-stock analysis**: Tracking when products disappear from availability can indicate supply chain stress, unexpected demand, or deliberate scarcity.

## Where to Find Inventory Data

There is no uniform location. What to check, roughly in order of ease:

**Product list page**: The rarest and most convenient case. Farfetch.com's listing API (`/plpslice/listing-api/products-facets`) includes a `stockTotal` field per product in the JSON response. This allows bulk collection from the list level without visiting individual product pages.

**Product detail page**: The most common case. The HTML of the product detail page often contains a JSON block (sometimes embedded in a `<script>` tag, sometimes in the Next.js `__NEXT_DATA__` block) that includes stock per size and color. Neiman Marcus and Farfetch both expose this. The data may also be in an XHR call triggered when the product page loads.

**Click-and-collect / pick up in store**: When a site offers click-and-collect, it must query inventory at the store level. This is where more granular data appears. Burberry exposes per-store, per-size quantities via an API call made when the customer selects "Find in Store." IKEA directly shows the exact quantity in the HTML with no obfuscation. Stone Island exposes a "book in store" API that returns per-store inventory for any item and size.

**Add to cart**: The most resource-intensive method. Incrementing the requested quantity in an add-to-cart call until the site refuses reveals the maximum available stock. This is a last resort because it generates significant load, may affect cart state on the site, and is explicitly noted in Burberry's and similar sites' terms. We do not recommend including an actual cart-add call in a scraper.

## Reading the Numbers

Stock numbers from internal APIs do not always represent what they appear to represent. Several interpretive problems arise:

**Central warehouse vs. per-store**: Large numbers attached to a "store" API call often indicate a regional warehouse rather than a single store. Lowe's inventory API, when queried per store, returned quantities that were far too large to be a single store's stock. Stone Island's case was different: summing the individual store inventories across Europe for a single product matched the e-commerce-level figure exactly, confirming the e-commerce was fulfilled from the same pool as the stores.

**Cap and discretization**: Some sites display "1 left", "2 left", "only a few left" as categorical labels. Others cap numeric display at 10 (showing "10+" for anything above). The exact number may still appear in the API even if it is not shown to the user.

**Country and regional splits**: When scraping across multiple countries, the same stock may be counted multiple times. Stone Island's inventory showed that Europe was served from one warehouse, the US and Canada from another, Japan from a third, and Korea from a fourth. Scraping all countries independently and summing would have quadruple-counted European inventory. Testing a single product across all regions identifies the warehouse groupings.

## Logistics of Collection

**Frequency**: Grocery industry data can become stale in hours. Fashion and home improvement data is generally stable day-to-day. The scraping frequency must match the industry's restocking and sales velocity. Collecting too infrequently misses intraday movements; too frequently wastes budget and risks detection.

**History requirement**: A single snapshot has limited value. Revenue estimation models require months of data to establish baseline rates and seasonal patterns. Two years of history is a common minimum for hedge fund use cases.

**Request volume**: Full global coverage for a large retailer is expensive. Burberry's global inventory — hundreds of stores, thousands of items, multiple sizes each — requires millions of API calls for a single snapshot. The cost-value tradeoff needs explicit evaluation before starting.

## What We Tested

- **Lululemon**: SKU-level inventory via `https://shop.lululemon.com/api/inventory?country=US&skus=<sku>&storeIDs=<ids>`. Store list from a separate `/api/stores` endpoint (731 stores returned, more than the 655 officially listed). Per-SKU scraping across all stores is the full coverage strategy.
- **On (ONON)**: Product detail page XHR call returns per-SKU quantities in the hundreds, consistent with a central warehouse rather than e-commerce stock.
- **Stone Island**: Per-country scraping revealed 4 warehouse regions. "Book in store" API exposed per-store per-size quantities. Store inventory summed to match the e-commerce total.
- **Lowe's**: Browser geolocation injection to select a store, category pagination for product list, JSON extraction from page HTML. Inventory data was in the HTML (not callable directly from the API in a simple GET request).
- **IKEA**: Exact quantities visible directly in the HTML. No API extraction needed.
- **Farfetch**: `stockTotal` in the product list API response; per-size quantities in the product detail page HTML.

## Current State

Inventory tracking is one of the highest-value web scraping applications and one of the least commoditized. The technical barrier is moderate — finding the right endpoints requires the standard API discovery process — but the analytical barrier is higher: interpreting the numbers requires understanding the retailer's logistics structure, and building a useful derivative dataset (like a sales estimator) requires domain expertise and months of collection history.

## Related

- [api-scraping](./api-scraping.md)
- [location-data-scraping](./location-data-scraping.md)
