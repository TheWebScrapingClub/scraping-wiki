---
type: article_summary
title: 'The Lab #58: Intercepting traffic from an App - part 1'
slug: intercepting-api-traffic-for-scraping
canonical_url: https://www.scraping.club/p/intercepting-api-traffic-for-scraping
publish_date: '2024-08-09'
visibility: premium
topics:
- tls-fingerprinting
description: How to intercept mobile app traffic with a man-in-the-middle proxy like Fiddler Everywhere to find hidden endpoints, tested on the Saks Fifth Avenue iPhone app.
source_hash: fe918ae911e71937
---

# The Lab #58: Intercepting traffic from an App - part 1

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-08-09 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/intercepting-api-traffic-for-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Sometimes a website is so hard to scrape that we want to see how its app works and emulate it, hoping the underlying endpoints are less protected. Other times there is no web version to scrape at all. In both cases, seeing what the app sends and receives is the first step.

We cover the man-in-the-middle approach: a proxy sits between the app and the target server, and a root certificate installed on the device lets it decrypt HTTPS. I refresh how HTTPS and root certificates work, then use Fiddler Everywhere on my own iPhone against the Saks Fifth Avenue app. We look at the requests it makes, the third-party services in the traffic, and how the mobile headers differ from the website's. I also mention open-source alternatives and show where the technique stops working. Part two moves to that limit with a different tool.

## What's inside

- How Fiddler generates its own root certificate and signs certificates on the fly for each domain it intercepts.
- What shows up in the Saks app traffic besides the backend: third-party services such as Facebook, Airship and Forter.
- Why the app's requests hit the same endpoint as the website but with very different headers, starting from the user agent, and why that matters against anti-bot systems.
- Why the technique fails on apps like Twitter and WhatsApp because of certificate pinning.

**In the full article:** The step-by-step iPhone setup for Fiddler Everywhere, the screenshots of the Saks app traffic and mobile request headers, and the Twitter and WhatsApp failure examples.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/intercepting-api-traffic-for-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
