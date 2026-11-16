---
type: article_summary
title: 'THE LAB #26: From internal API to insights.'
slug: the-lab-26-from-internal-api-to-insights
canonical_url: https://www.scraping.club/p/the-lab-26-from-internal-api-to-insights
publish_date: '2023-08-31'
visibility: premium
topics:
- industry-overview
description: 'How to find a website''s internal APIs with browser developer tools, and what to fall back on when none exist: embedded JSON, then plain HTML selectors.'
source_hash: 3b7dd8f9dd7396ff
---

# THE LAB #26: From internal API to insights.

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-31 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-26-from-internal-api-to-insights?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Before writing a scraper for a new project, I want to know how the site gets its data. On dynamic pages, like products on an e-commerce site, the content usually comes from a request to an internal API endpoint, and the front-end just renders the result. When that API returns everything the scraper needs, it is the best source. It is usually more stable than HTML, it is made to be queried with proper throttling, and it has no overhead, so it costs less in server load and bandwidth.

We go through the three options in order of preference. First the internal API, then JSON embedded in the HTML, which is common on Next.js sites, and finally selectors on plain HTML when nothing else is there. We then look at how I spot internal APIs in practice, using the Network tab of the browser's developer tools to watch background requests and see what each click on the page triggers.

## What's inside

- Why an internal API beats HTML parsing: stability, intended use, and lighter responses
- What to look for in the page source on Next.js sites when no API is exposed
- Why embedded JSON is only the second-best option: no bandwidth gain, but more stable than HTML selectors
- How to tell tracking requests from the ones that load the data you need

**In the full article:** The walkthrough of the Network tab on a real target, the requests we identified and the way we turned the API calls into a working scraper.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-26-from-internal-api-to-insights?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
