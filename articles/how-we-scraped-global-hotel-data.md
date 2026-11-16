---
type: article_summary
title: How We Scraped Global Hotel Data to Track Economic Trends
slug: how-we-scraped-global-hotel-data
canonical_url: https://www.scraping.club/p/how-we-scraped-global-hotel-data
publish_date: '2024-12-17'
visibility: free
topics:
- proxies
- legal-ethics
description: How RE Analytics scraped hotel availability and prices from OTAs in 2017 to build occupancy and RevPAR proxies for tracking global travel flows.
source_hash: 79f27ce4ef078728
---

# How We Scraped Global Hotel Data to Track Economic Trends

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-12-17 (free to read). **[Read the full article](https://www.scraping.club/p/how-we-scraped-global-hotel-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Travel flows are tracked inconsistently around the world, and the official hotel numbers are either private or published late. In 2017, at RE Analytics, we wanted a daily read on how tourism and business travel reacted to events like the Hong Kong protests, the Tokyo Olympics or COVID-19 recovery. Investors and analysts needed that signal, and hotels were the cleanest place to find it.

We scraped hotel websites and OTAs such as Booking.com and Expedia and built proxies for the standard hotel KPIs. Average Published Rate stands in for ADR, an estimate of vacant rooms and total stock gives occupancy, and the two combine into an Online Projected RevPAR. I explain why we chose hotels, how the metrics are defined, and why we standardized collection by time zone. I also cover how we reached global scale by targeting large OTAs and the top cities, and what that choice cost us in coverage.

## What's inside

- Who can see true ADR (owners, benchmarking services, tourism boards) and how APR compares with credit card and email receipt data as an alternative.
- The Next Day Published Rate as a fast indicator, and why time zone calibration matters when collecting it worldwide.
- How simulated reservation requests were used to estimate available rooms, and how searches far into the future were used to estimate total stock.
- The trade-off of covering only the top 1,000 cities: efficient at scale, but with gaps for chains like Hilton, Hyatt or Sheraton.

**In the full article:** The rest of the full article covers how we kept request volume low on the OTAs we targeted and the other scaling choices behind the project.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-we-scraped-global-hotel-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
