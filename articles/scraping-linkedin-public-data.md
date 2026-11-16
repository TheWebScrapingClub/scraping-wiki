---
type: article_summary
title: Automating LinkedIn Scraping Using Its Hidden APIs
slug: scraping-linkedin-public-data
canonical_url: https://www.scraping.club/p/scraping-linkedin-public-data
publish_date: '2025-06-22'
visibility: free
topics:
- api-scraping
- browser-automation
- proxies
- http-clients
description: How to scrape LinkedIn job listings from its hidden guest API endpoints with Python, without logging in or hitting the login wall.
source_hash: 27c1b7fd87d82521
---

# Automating LinkedIn Scraping Using Its Hidden APIs

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-06-22 (free to read). **[Read the full article](https://www.scraping.club/p/scraping-linkedin-public-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

LinkedIn has plenty of useful data, but scraping it the traditional way is a pain. An HTTP client with an HTML parser, or Playwright and Selenium, runs into the login wall, page structures that change from one listing to the next, and infinite scroll with client-side rendering. Automating the login also raises legal concerns, so we stay on public data. Hidden API endpoints are a better target: public, and more stable than page markup.

Taking job listings as the target, I show why a Google search lands on a Jobs URL that returns only the login wall, and which URL shows the real page. We then find the endpoint in the DevTools Network tab, using a Wayback Machine snapshot because LinkedIn removed dynamic loading from the public page. I then build a Python script with Requests and Beautiful Soup that calls the endpoint and parses the returned HTML into job data.

## What's inside

- Why two Jobs URLs that look almost the same behave differently, and the query parameter that seems to bring back the login wall.
- The endpoint has no official documentation, so the parameters for keyword, location and pagination come from testing, and some in the original URL can be ignored.
- The endpoint returns raw HTML instead of JSON, with a limited number of listings per page.
- Job cards carry different or missing fields, so the parsing checks every element before reading it.

**In the full article:** Python code for the request and parsing functions, the full endpoint with its parameters, the Wayback Machine snapshot to inspect, and the complete working script.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-linkedin-public-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
