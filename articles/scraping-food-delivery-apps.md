---
type: article_summary
title: Scraping food delivery data
slug: scraping-food-delivery-apps
canonical_url: https://www.scraping.club/p/scraping-food-delivery-apps
publish_date: '2025-04-03'
visibility: premium
topics:
- scraping-infra
- antibot
- browser-automation
- proxies
description: 'Scraping food delivery data from Deliveroo, Glovo and Uber Eats: what you can extract, the obstacles, and a Glovo case on website and mobile app.'
source_hash: 12665cbc10aeb6be
---

# Scraping food delivery data

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-04-03 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-food-delivery-apps?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Deliveroo, Glovo and Uber Eats hold a lot of data on a city's restaurant market: menus, prices, promotions, ratings, delivery fees. Analysts use it for competitor analysis, pricing and spotting cuisines nobody serves in an area. These platforms are not easy targets. Content depends on the location you set, pages fill through background XHR calls, and anti-bot protection is real. Most also run both a website and a mobile app, and the two can use different API endpoints with different detail.

We first list the data points you can collect and the obstacles. Then we work through a case on Glovo, on both website and mobile app. On the web side we look at the internal JSON endpoints the site calls once a location is chosen. On mobile we intercept the app's traffic with HTTP Toolkit. The aim is structured restaurant lists and menu details.

## What's inside

- Restaurant coordinates, opening hours and contact details can also feed a prospect list if you sell software to restaurants.
- Large cities mean pagination, cuisine segmentation and nested menus, so a single restaurant can take several endpoints or pages.
- Glovo has described shielding its public APIs with AWS CloudFront and AWS WAF, which is why rate limiting, IP blocking and CAPTCHAs matter here.
- Covering several cities means iterating over locations, and in Glovo the location is passed to the API the same way on web and mobile.

**In the full article:** Scripts from the Glovo folder of The Web Scraping Club GitHub repository, the walkthrough of the website endpoints and the HTTP Toolkit capture of the mobile app traffic.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-food-delivery-apps?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
