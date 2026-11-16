---
type: article_summary
title: 'The Lab #47: Scraping real time data with Python'
slug: scraping-real-time-data-bitstamp
canonical_url: https://www.scraping.club/p/scraping-real-time-data-bitstamp
publish_date: '2024-04-04'
visibility: premium
topics:
- industry-overview
description: How WebSockets work and how to spot one on Bitstamp's tradeview page, as the first step to scraping data that updates several times per second.
source_hash: b5020ccfe5d74604
---

# The Lab #47: Scraping real time data with Python

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-04-04 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-real-time-data-bitstamp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Most of the scraping we have covered in The Lab targets sites where data changes often, but not every second. Bitstamp's tradeview is a different case: the Bitcoin price, the order book and the trades update several times per second, and sports bets work the same way. Before writing any scraper, we need to understand how these pages receive their data.

In most cases the answer is a WebSocket. I explain what it is, how the handshake starts over HTTP and upgrades to a persistent, full-duplex connection, and why that suits live data. Then we use Bitstamp as the target. We locate the WebSocket in the browser's developer tools and read the messages between browser and server to see how the live feed is set up. I'm not an expert in real-time scraping, so the examples that follow are basic, and I say so upfront.

## What's inside

- Why WebSockets sidestep HTTP limits such as connection throttling and proxy filtering, and how they carry discrete text or binary messages.
- Where to find the connection in the Network tab of the developer tools, using the WS filter.
- What the browser sends first on Bitstamp: five channel subscriptions covering live BTC/USD trades, the order book and the ticker.
- An open request: if you have more real-time scraping experience than I do, I'd like to hear from you.

**In the full article:** Python code that collects the stream, stored in the 47.REAL-TIME-SCRAPING folder of The Lab GitHub repository for paying subscribers, plus the basic examples that follow the Bitstamp analysis.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-real-time-data-bitstamp?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
