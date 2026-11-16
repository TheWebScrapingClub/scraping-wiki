---
type: article_summary
title: 'THE LAB #9: Scraping OpenSea NFT''s data'
slug: scraping-opensea-bored-ape-nft
canonical_url: https://www.scraping.club/p/scraping-opensea-bored-ape-nft
publish_date: '2023-01-05'
visibility: premium
topics:
- industry-overview
description: Scraping every Bored Ape Yacht Club sale from OpenSea, plus USD values from Etherscan, to see who made or lost money on the collection.
source_hash: bcd142f5b53f39c5
---

# THE LAB #9: Scraping OpenSea NFT's data

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-01-05 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-opensea-bored-ape-nft?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

NFTs were the buzzword of 2021, and the hype is gone. Bored Ape sales on OpenSea have collapsed, and crypto is in a winter. Yet I haven't seen anyone publish who made or lost money on the Bored Ape Yacht Club, the most famous collection. My guess is that the data takes simple but not effortless web scraping, on two different sites.

I tracked every Bored Ape Yacht Club sale on OpenSea from the start, to enrich the stats the marketplace already shows for the collection. Etherscan gave the USD value of each transaction at the time it happened. With that dataset we measured the total money moved, split the accounts into winners and losers, and looked at both ends of the ranking, including a well-known collector. After the numbers I walk through the scrapers I built to get them.

## What's inside

- Why OpenSea alone is not enough: the USD value at the time of each sale needs a second scrape on Etherscan.
- How we treat first movers who got their NFTs in pre-sale when counting winners and losers.
- Two readings of the same data: all traders together, and only accounts that sold more than they bought.
- The extremes of the ranking: accounts that made or lost more than one million USD, and the record of a known collector.

**In the full article:** Volume and profit-and-loss figures with their charts, the account-level results, and the OpenSea and Etherscan scrapers behind the dataset.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-opensea-bored-ape-nft?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
