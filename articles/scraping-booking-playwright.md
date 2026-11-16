---
type: article_summary
title: How to Scrape Booking.com in Python
slug: scraping-booking-playwright
canonical_url: https://www.scraping.club/p/scraping-booking-playwright
publish_date: '2025-08-31'
visibility: free
topics:
- browser-automation
- proxies
- anti-detect-browsers
- residential-proxies
description: 'A Python script that uses Playwright to scrape property listings from Booking.com search results: selectors, headless-mode data loss, and CSV export.'
source_hash: d930b6614e96e732
---

# How to Scrape Booking.com in Python

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-31 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-booking-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Booking.com lists over 28 million properties, and hotel prices keep rising. That makes it a natural source for price monitoring, market analysis and competitor research. The listing pages are dynamic: results load on infinite scroll and filters trigger a spinner. A plain HTTP request is not enough, so you need a browser automation tool such as Playwright, Puppeteer or Selenium.

I build a Python scraper with Playwright that collects property listing data for Rome from a search results page. We start from a URL copied after a manual search, not from the homepage form. We look at why the class names are unreliable and which attributes to select on instead. We also cover what Booking.com does when it detects a headless browser, how to handle cards with missing fields, and how to clean review and price values. The output is a list of properties exported to CSV.

## What's inside

- Why I copy the search URL from the browser instead of simulating the homepage search form, and why that URL expires with its dates.
- Booking.com hides prices and other details from the property cards when it detects headless mode, so the browser runs headful.
- Class names look randomly generated and change at each release, so selection relies on data-testid attributes.
- Not every card has every field, so a helper function avoids Playwright timeout errors on missing elements, while review and price fields need custom cleaning.

**In the full article:** The complete Playwright script, the selector for each of the ten extracted fields, the review and price parsing logic, the CSV export code and the screenshots of the DevTools inspection.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-booking-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
