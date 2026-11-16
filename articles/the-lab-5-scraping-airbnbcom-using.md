---
type: article_summary
title: 'The Lab #5 - Scraping Airbnb.com using GraphQL'
slug: the-lab-5-scraping-airbnbcom-using
canonical_url: https://www.scraping.club/p/the-lab-5-scraping-airbnbcom-using
publish_date: '2022-10-27'
visibility: premium
topics:
- cloudflare
description: How GraphQL works and how Airbnb uses it to serve search results, with a Scrapy scraper for Airbnb listings built on that endpoint.
source_hash: 28d82ed129e30dbb
---

# The Lab #5 - Scraping Airbnb.com using GraphQL

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-10-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-5-scraping-airbnbcom-using?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Booking.com, Edreams and Airbnb have something in common besides traffic: they all use GraphQL to feed data to the front end. For anyone scraping them, that matters. A GraphQL endpoint returns exactly the fields requested, as JSON, maintained by the site for its own use, so we don't have to download and parse HTML pages or overload the target with requests.

We start with what GraphQL is, how a single endpoint replaces several separate APIs, and how the schema definition language maps objects and relationships, much like an entity-relationship diagram. Then we look at Airbnb. We simulate a search for a place in Manhattan for two adults over one week in November 2022 and inspect the payload the site sends to the GraphQL engine. We compare the filters set in the search bar with the data that comes back, which is more than the page shows. From there we set up the Scrapy project and the output data model for the Airbnb scraper.

## What's inside

- How a single GraphQL request replaces calls to several APIs and returns only the fields you ask for
- Why the schema definition language works like a database entity-relationship diagram
- Where the search bar filters show up in the Airbnb request, and how the response compares with what the page displays
- The Scrapy project setup and the data model defined for the Airbnb output

**In the full article:** The full payload structure, the Scrapy project code, the output data model and the working Airbnb scraper are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-5-scraping-airbnbcom-using?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
