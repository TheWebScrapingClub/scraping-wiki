---
name: location-data-scraping
type: concept
first_seen: 2023-11-09
last_updated: 2026-04-22
---

# Location Data Scraping

## Definition

Location data scraping covers the techniques for extracting data that is spatially indexed — store locators, accommodation listings, restaurant maps, delivery zones — where the API requires geographic inputs (coordinates, radius, or bounding box) and returns data for the area specified. The central challenge is ensuring complete geographic coverage without issuing redundant or missing queries.

## How It Works

### Two API Patterns

Most location-based APIs fall into one of two patterns:

**Radius-based**: The API accepts a latitude/longitude center point and a radius parameter. Results are all items within that circle. Alexander McQueen's store locator uses country code as input. Dolce & Gabbana's store locator accepts coordinates and a radius of 65km: `https://boutique.dolcegabbana.com/index.html?q=<lat>,<lon>&r=65`.

**Bounding box**: The API accepts two corner coordinates (NE and SW) that define a rectangle. Results are all items within that rectangle. Airbnb's listing API accepts the zoom level and the two corner coordinates of the current map view. Zooming in changes the zoom level parameter and brings the corner coordinates closer together.

For Glovo's food delivery API, location is passed via request headers: `glovo-delivery-location-latitude`, `glovo-delivery-location-longitude`, `glovo-location-city-code`, and `glovo-location-country-code`. Setting these headers, rather than a URL parameter, is what locates the request.

### The World Grid Approach

When an API uses a small radius or bounding box, a single query cannot cover an entire country or city. The solution is to divide the target area into a grid of non-overlapping squares and query each one.

Building the grid requires accounting for the curvature of the Earth. A naive grid that adds fixed degree increments produces squares that are very different in physical size at different latitudes. The correct formula uses the Earth's radius (6,378,137 meters) to compute the offset in meters, then converts back to degrees:

```python
R = 6378137
off_lat = radius / R
off_lon = radius / (R * math.cos(math.pi * nw_lat / 180))
next_lat = current_lat + off_lat * 180 / math.pi
next_lon = current_lon + off_lon * 180 / math.pi
```

Starting from (-90, -180) and stepping through the world at 100km intervals produces around 10,000 squares. This is the outer grid. Squares covering ocean, desert, or unpopulated areas can be discarded — for example by querying the Google Places API `nearby-search` endpoint with an `includedTypes` filter and treating squares with zero results as empty.

The remaining populated squares can be recursively split into 50km, 25km, or smaller squares as needed. Each subdivision multiplies the square count by 4. This recursive approach avoids the combinatorial explosion of generating the full fine-grained grid for the entire world upfront. Once a grid is built and filtered, it is reusable across different scraping projects.

### Browser Geolocation Injection

For sites that store-localize content based on IP geolocation and do not expose the location via URL parameters or headers, Playwright's geolocation context can be used to override the browser's reported location:

```python
context = browser.new_context(
    geolocation={"longitude": float(lon), "latitude": float(lat)},
    permissions=["geolocation"],
)
context.set_geolocation({"longitude": float(lon), "latitude": float(lat)})
```

We used this approach on Lowe's, where the "pick up in store" feature changed based on geolocation. The browser was initialized with the coordinates of the target store, which caused the site to select the nearest store automatically, allowing inventory scraping for that specific location.

## Known Complications

**Inventory ambiguity**: When a site's API returns a stock number tied to a store or pickup location, the number may represent the inventory of a regional warehouse rather than the individual store. Lowe's returned stock numbers that were implausibly large for a single store — consistent with a central warehouse that serves a geographic area. Interpreting these numbers requires domain knowledge about the company's logistics.

**Pagination limits**: Some APIs cap the number of results per bounding box regardless of zoom level. Autoscout24 returns a maximum of 20 pages (400 items) per query — to get full coverage, the query must be filtered more specifically (by model, brand, etc.) until each sub-query fits within the 400-item limit.

**API result inconsistency**: When iterating programmatically (rather than through normal user interaction), some sites return stale results. On Lowe's, fetching category pages via Playwright required a page reload after every pagination click — without reloading, the JSON embedded in the HTML was not refreshed and the same page-one data was returned repeatedly.

## What We Tested

- **Alexander McQueen store locator**: Iterated by country code parameter. Simplest case — one query per country.
- **Airbnb**: Bounding box API documented. Grid approach recommended for full coverage. Effective radius for dense cities was approximately 100 meters.
- **Lowe's**: Browser geolocation injection to select a specific store, then category-level pagination to extract inventory data embedded in page HTML.
- **Glovo**: Location set via request headers. Restaurant list for Rome (700+ results) fetched by incrementing the offset parameter. Mobile app API uses different headers but the same endpoint for menu and contact data.

## Current State

The world grid pattern is reusable infrastructure. A filtered, populated grid at multiple resolutions (100km, 50km, 25km) can be built once and applied to any project that needs geographic coverage. The choice of resolution depends on the API's radius or bounding box size. The main technical cost is the initial Google Places API queries (or equivalent) to filter out empty squares.

## Related

- [api-scraping](./api-scraping.md)
- [inventory-tracking](./inventory-tracking.md)

## Sources

- [https://substack.thewebscraping.club/p/the-lab-31-scraping-location-data](https://substack.thewebscraping.club/p/the-lab-31-scraping-location-data)
- [https://substack.thewebscraping.club/p/scraping-food-delivery-apps](https://substack.thewebscraping.club/p/scraping-food-delivery-apps)
- [https://substack.thewebscraping.club/p/the-lab-28-deep-dive-on-inventory](https://substack.thewebscraping.club/p/the-lab-28-deep-dive-on-inventory)
