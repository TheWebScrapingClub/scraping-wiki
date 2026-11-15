---
type: article_summary
title: On choosing the right proxy provider for scraping
slug: choosing-proxy-provider-scraping
canonical_url: https://www.scraping.club/p/choosing-proxy-provider-scraping
publish_date: '2022-10-02'
visibility: free
topics:
- proxy-industry
- proxies
- residential-proxies
description: 'Two things to check when choosing a proxy provider for scraping: IP diversity across subnets and IP reputation, with notes from Rayobyte''s Neil.'
source_hash: e49cfd58ccb13cbc
---

# On choosing the right proxy provider for scraping

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-10-02 (free to read). **[Read the full article](https://www.scraping.club/p/choosing-proxy-provider-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anyone who scrapes large sites knows that too many requests from one IP get you blocked. That is why we buy proxies. What I did not know is how far the block can reach on targets like Google or Amazon, which are hit hard by bots. Picking a provider on price alone can cost you more than it saves.

I start from the basics of what an IP address is and how ISPs get their ranges from the regional Internet registries. Then I go through the two aspects Neil from Rayobyte, a vendor of data center, residential and mobile proxies, says every proxy user should check: diversity of IPs across subnets, and IP reputation. For each I explain why it matters for a scraping project, using a worked example with Amazon-style request limits for the first. I close with a short fun fact on IPv4 prices.

## What's inside

- How a block on one IP can extend to the other addresses in its subnet, and what the "noisy neighbor problem" means for your request budget.
- Why diversity of sources in the IP rotation matters for scrapers and for the proxy providers themselves.
- How anti-bot software uses blacklists and IP reputation, with the case of the IP addresses stolen from AFRINIC.
- Why proxy prices that look too good to be true often point to poor IP reputation.

**In the full article:** The worked subnet example with request counts, the AFRINIC story, the IPv4 and IPv6 background and the note on IPv4 prices are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/choosing-proxy-provider-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
