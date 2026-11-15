---
type: article_summary
title: 'Hands On #6: Testing the Infatica web scraper'
slug: hands-on-6-testing-the-infatica-web
canonical_url: https://www.scraping.club/p/hands-on-6-testing-the-infatica-web
publish_date: '2023-10-05'
visibility: free
topics:
- datadome
- proxies
- cloudflare
- antibot
description: Hands-on test of Infatica's Web Scraper super proxy against Datadome, Cloudflare, Kasada, F5 and PerimeterX, with a Scrapy spider and a 0 to 100 score.
source_hash: ceabb4991330e672
---

# Hands On #6: Testing the Infatica web scraper

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-10-05 (free to read). **[Read the full article](https://www.scraping.club/p/hands-on-6-testing-the-infatica-web?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Super proxies promise to get you past the main anti-bot solutions with a single API call. Infatica, a Singapore-based proxy provider born in 2019, has recently launched its own, called Web Scraper. It's a relatively new product with the usual features: JavaScript rendering, IP rotation, country selection and custom headers. Before spending money and time on a trial, you want to know how it behaves on protected sites.

We ran our usual benchmark: a plain Scrapy spider that fetches 10 pages from each of 5 websites, one per anti-bot (Datadome, Cloudflare, Kasada, F5, PerimeterX). Every run is done locally and from a server, and the score goes from 0 to 100. We made three passes: a baseline without the unblocker, the Web Scraper with raw HTML only, and the Web Scraper with JavaScript rendering enabled. We also looked at how the integration fits into Scrapy, how the price compares with Bright Data's Web Unblocker, and what the pros and cons are.

## What's inside

- The baseline spider without any unblocker sets the benchmark at 0, so the final score measures only what the Web Scraper adds.
- Infatica takes an HTTP POST with the target URL in the payload instead of a proxy-style request, which needs care when you want the original URL in your output.
- JavaScript rendering is an option you switch on in the payload, so we tested raw HTML and rendered requests as separate runs.
- The price comparison uses Bright Data's Web Unblocker as the reference, and the cons list covers the plan structure.

**In the full article:** Results tables for each of the three runs, the final score, the pricing figures against Bright Data, the payload screenshots and the link to the test spider on GitHub.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/hands-on-6-testing-the-infatica-web?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
