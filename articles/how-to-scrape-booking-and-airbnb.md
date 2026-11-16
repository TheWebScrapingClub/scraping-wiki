---
type: article_summary
title: 'THE LAB #66: How to properly scrape a booking website'
slug: how-to-scrape-booking-and-airbnb
canonical_url: https://www.scraping.club/p/how-to-scrape-booking-and-airbnb
publish_date: '2024-11-07'
visibility: premium
topics:
- industry-overview
description: 'How to structure requests when scraping booking sites like Booking.com: stay parameters, room type, advance time, and map-based grids, with Genova hotels as the'
source_hash: fbca1a23e6e18b86
---

# THE LAB #66: How to properly scrape a booking website

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-11-07 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-scrape-booking-and-airbnb?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Booking.com and Airbnb data feeds revenue management in hospitality: competitor pricing, availability, fill rates, amenities, and long-term tourism trends. At that scale, the number of calls matters, and so does knowing which parameters you put in each request. Price depends on length of stay, number of rooms, room type, how far ahead you book, and the amenities of the structure. What you ask for should follow the business need, whether that is market statistics or a revenue management system.

We look at how these platforms work behind the map view. Moving or zooming the map triggers API calls built on coordinates and a bounding box, so covering a whole city means simulating a user who looks at the entire territory. We link this to the world grid approach from THE LAB #31, with layered grids that keep completeness high and requests low. As a real case, we plan the requests to collect the hotels in Genova, Italy, from Booking.com. I focus on the logic of building the requests, not on a full GraphQL wrapper.

## What's inside

- How we used room and date parameters at Re Analytics to estimate fill rates in hundreds of cities, and what an event-driven spike looked like
- Why fill-rate checks work better on medium-sized structures than on hotels with over one hundred rooms
- Why Airbnb needs trimmed request parameters compared with hotels
- How to handle coordinates in API calls when you can't know beforehand whether they fall inside your target area

**In the full article:** The request-building logic for the Genova example on Booking.com, the grid setup passed to the scrapers, and the details of the underlying API payload.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-scrape-booking-and-airbnb?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
