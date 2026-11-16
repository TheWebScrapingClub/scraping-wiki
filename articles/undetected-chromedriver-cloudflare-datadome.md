---
type: article_summary
title: Can Undetected Chromedriver bypass Cloudflare or Datadome?
slug: undetected-chromedriver-cloudflare-datadome
canonical_url: https://www.scraping.club/p/undetected-chromedriver-cloudflare-datadome
publish_date: '2023-07-23'
visibility: free
topics:
- cloudflare
- datadome
- proxies
- residential-proxies
description: A stress test of Undetected Chromedriver 3.5 against Cloudflare, Datadome, Kasada, PerimeterX and F5, run locally, from an AWS datacenter and with residential p
source_hash: 5c365ce3dd9b3e3b
---

# Can Undetected Chromedriver bypass Cloudflare or Datadome?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-07-23 (free to read). **[Read the full article](https://www.scraping.club/p/undetected-chromedriver-cloudflare-datadome?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A scraper that works on your laptop is not a scraper that works in production. Choosing the tool is only the first piece of what I call the web scraping triad. The other two are the hardware the scraper runs on and the type of proxy in front of it. The idea came from the undetected-chromedriver readme, where the main contributor complains about issues opened by people who only thought about the tool.

So we ran Undetected Chromedriver 3.5 against our usual five anti-bots: Cloudflare, Datadome, Kasada, PerimeterX and F5. Each one was tested on a real e-commerce site, with the scraper browsing category pages to see whether it gets flagged after a few requests. We repeated the test in three setups: a local machine, a VM on AWS with no proxy, and the same VM with Smartproxy residential proxies. Chrome and Brave were both used where Chrome got stuck. The scripts are on our GitHub repository.

## What's inside

- Which e-commerce site stands in for each anti-bot, and how far the scraper had to browse on each: category pages, scrolling to the end, or the last page.
- Why Brave replaced Chrome on some targets, and what happened to the IP on the PerimeterX site after repeated attempts.
- Why the datacenter run behaves differently from the local one, and what AWS publishing its IP ranges means for anti-bots.
- Why authenticated proxies are painful with undetected-chromedriver, and the IP whitelisting workaround I used.

**In the full article:** The per-anti-bot results for each of the three runs, the recap table, the screenshots of the blocks, the test scripts on GitHub and my closing view on what to use in production.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/undetected-chromedriver-cloudflare-datadome?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
