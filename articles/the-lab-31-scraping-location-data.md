---
type: article_summary
title: 'THE LAB #31: Scraping location data using a world grid'
slug: the-lab-31-scraping-location-data
canonical_url: https://www.scraping.club/p/the-lab-31-scraping-location-data
publish_date: '2023-11-09'
visibility: premium
topics:
- industry-overview
description: 'Scraping location data when APIs need coordinates: radius-based store locators, Airbnb''s rectangle queries, and a world grid that covers both cases.'
source_hash: 32dd28a3a857c74b
---

# THE LAB #31: Scraping location data using a world grid

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-11-09 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-31-scraping-location-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Location data is one of the most popular datasets built with web scraping: store locators, place reviews, accommodation prices and occupancy. It gets tricky when the website API wants coordinates as input. Others, like Dolce & Gabbana, take a point and a radius, and the radius can be much smaller than the 65 km seen there. Airbnb takes the corners of a rectangle plus a zoom level. The practical question is how to be sure you scraped every location.

I walk through the two families, radius-based and square-based APIs, using Alexander McQueen, Dolce & Gabbana and Airbnb as examples. The answer is a grid of the world made of small squares: the center of each square feeds radius APIs, and its corners feed APIs that expect a rectangle. I also cover how big the squares should be and how to build them without reinventing the wheel each time.

## What's inside

- The easiest store locator case: an API with a countryCode parameter, where you iterate over the countries of the world.
- In Airbnb's internal POST request, the zoom level plays the same role as the radius, and the North-East and South-West points define the rectangle.
- Why zooming in on a map shows locations that were hidden at the wider view, and what that means for coverage.
- The right square size changes from site to site, so the grid has to be built as a reusable tool.

**In the full article:** Code for the grid-generation tools in The Lab GitHub repository, plus the full API calls and request parameters for the three example targets.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-31-scraping-location-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
