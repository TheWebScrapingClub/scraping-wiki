---
type: article_summary
title: 'Hands On #5: Testing the Oxylabs Web Unblocker'
slug: oxylabs-web-unblocker-test
canonical_url: https://www.scraping.club/p/oxylabs-web-unblocker-test
publish_date: '2023-08-10'
visibility: free
topics:
- antibot
- cloudflare
- datadome
- proxies
description: Hands-on test of the Oxylabs Web Unblocker with a Scrapy spider against Datadome, Cloudflare, Kasada, F5 and PerimeterX, scored from 0 to 100.
source_hash: bc8e2a9779f8b41b
---

# Hands On #5: Testing the Oxylabs Web Unblocker

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-08-10 (free to read). **[Read the full article](https://www.scraping.club/p/oxylabs-web-unblocker-test?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Almost every month this year a new unblocker shows up, and choosing the right one for your case is getting harder. The feature list is always the same: proxy-style integration, rotating IPs, session handling and Javascript rendering. What matters in practice is price and how well it holds against the anti-bots that block real targets.

We tested the Oxylabs Web Unblocker in this Hands On episode, with the same method we used on other unblockers. A plain Scrapy spider requests 10 pages from each of 5 websites, one per anti-bot: Datadome, Cloudflare, Kasada, F5 and PerimeterX. We score from 0 to 100 on two runs, one local and one from a server, and the base scraper sets the benchmark at 0. We ran it without the unblocker, with raw HTML only, and with Javascript rendering. I also went through account setup and the usage dashboard.

## What's inside

- Each test URL is checked with an XPath-populated field, so a 200 status alone does not count as a success when a challenge page comes back.
- We compare raw HTML requests with Javascript rendering, to see what rendering adds when the target already lets the request through.
- The usage dashboard splits traffic by domain, which helps when one proxy URL serves several sites. I say what I would add to it.
- The closing section lists pros and cons, covers the pricing model per GB and the free trial, and ends with a final rating.

**In the full article:** Result tables for each of the three runs with the per-anti-bot breakdown, the link to the test spider on GitHub, the request setup for rendering, the pricing figures and the final score.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/oxylabs-web-unblocker-test?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
