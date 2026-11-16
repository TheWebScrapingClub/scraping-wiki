---
type: article_summary
title: 'THE LAB #18: How to scrape Reddit with Scrapy'
slug: how-to-scrape-reddit-with-scrapy
canonical_url: https://www.scraping.club/p/how-to-scrape-reddit-with-scrapy
publish_date: '2023-05-11'
visibility: premium
topics:
- datadome
- nlp-ml
description: Scraping Reddit with Scrapy now that Datadome is gone from its security tools, either by parsing the HTML or by querying the GraphQL API directly.
source_hash: 8291c29604add95a
---

# THE LAB #18: How to scrape Reddit with Scrapy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-05-11 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-scrape-reddit-with-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Reddit is a good source for sentiment analysis on companies, reactions to the news and retail investor manias like WallStreetBets and Gamestop. In October 2022 I cited it as a Datadome-protected site, a setup that would make scraping it expensive in the long run. When I checked again, Datadome was gone from its security tools. I found no news about it, so it may be temporary, or the contract may have ended.

We built two Scrapy solutions, with no headful browser and without overloading the target. The first is plain vanilla: we read a list of subreddits, parse the JSON in the page to get post URLs and stats, then visit each post page. The second queries the GraphQL API directly, and it's the one I like most because it changes less often than HTML and needs less bandwidth.

## What's inside

- The fields the HTML spider returns for every comment: upvote stats, author, title and the comment content in HTML format.
- Why the listing page is parsed first, since some stats are not available on the page of the single comment.
- How the GraphQL approach cuts the number of requests, because we don't have to enter each comment page.
- A comparison of Reddit's anti-bot measures in October 2022 and today, with the screenshots, and a pointer to our earlier Lab on GraphQL for web scraping.

**In the full article:** Code for both Scrapy spiders from the paid GitHub repository, with the parsing functions for the HTML version and the requests used for the GraphQL version.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-scrape-reddit-with-scrapy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
