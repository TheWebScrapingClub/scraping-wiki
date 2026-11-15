---
type: article_summary
title: Build or buy, now that writing code is almost free
slug: build-or-buy-scrapers-in-llm-era
canonical_url: https://www.scraping.club/p/build-or-buy-scrapers-in-llm-era
publish_date: '2026-09-21'
visibility: free
topics:
- proxies
- antibot
- captcha
- anti-detect-browsers
description: 'Build or buy a scraper in 2026, when LLMs have cut code costs: a redo of the 2023 cost analysis across code, infrastructure and execution layers.'
source_hash: d52768cf2a72fcb5
---

# Build or buy, now that writing code is almost free

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-09-21 (free to read). **[Read the full article](https://www.scraping.club/p/build-or-buy-scrapers-in-llm-era?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In November 2023 I concluded that you buy a scraper if you need it once and build it if you need a feed running for years, because a developer's hourly rate was the biggest cost. Three years later, with a properly set up coding environment, the cost of writing and even maintaining a scraper is close to zero. That pushes toward building everything in-house again, and I wanted to check whether the numbers back it up.

We split the question into three decisions: code production, infrastructure (proxies, stealth browsers, anti-bot bypass, captcha solving) and execution. I describe the skills library I built for my own scraping agents. Then I redid the 2023 exercise at the same $20 an hour, adding LLM token costs and a traffic column. For traffic, I measured page weight on four ecommerce sites: ikea.it, mediaworld.it, etsy.com and asos.com. The comparison covers three tiers of anti-bot protection, plus maintenance, hidden costs and the sites no vendor sells.

## What's inside

- Why the code layer is only near zero for teams that already built a harness of skills for their scraping agents, and what keeping those skills current takes.
- How the pricing models differ: proxies billed per GB, unblockers and scraping browsers billed per request, and why that makes the total project price hard to predict.
- What changes in maintenance, and why it does not change on the hardest targets, where the work is working out the bypass again.
- Why building is cheap to start and expensive to leave, and the rule I suggest for deciding in advance how long an internal attempt gets before you buy.

**In the full article:** The cost table with break-even points for the three anti-bot tiers, the token and traffic assumptions behind it, the skills library details, and my verdict on which layer to build and which to buy.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/build-or-buy-scrapers-in-llm-era?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
