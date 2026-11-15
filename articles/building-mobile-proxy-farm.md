---
type: article_summary
title: Building an in-house mobile proxy farm
slug: building-mobile-proxy-farm
canonical_url: https://www.scraping.club/p/building-mobile-proxy-farm
publish_date: '2025-02-23'
visibility: free
topics:
- proxies
- browser-automation
- residential-proxies
- proxy-industry
description: 'Brainstorm for an in-house mobile proxy farm: phones versus dongles, USB hubs, the central server and management software, and the use cases for scraping or res'
source_hash: dd7814ef2719a200
---

# Building an in-house mobile proxy farm

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-02-23 (free to read). **[Read the full article](https://www.scraping.club/p/building-mobile-proxy-farm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Our first homemade mobile proxies, built on a Raspberry Pi and later mini PCs, saved us thousands of dollars at Re-Analytics when providers charged 40 USD per GB. At today's 6-8 USD per GB and our usage, keeping them made no sense, because they were unreliable and needed too much attention. Still, I got pulled back into the idea of an in-house mobile farm, and there is little written about it online beyond the BlackHatWorld forum.

This is an initial brainstorm, not a finished build. I start with the economics, using Italian unlimited mobile plans and a handful of SIMs against buying traffic by the GB. Then I go through the components: smartphones versus dongles, why you need a powered USB hub, and the central server that routes traffic to the SIMs. I list the tools that can manage the devices and compare two use cases: selling IPs and scraping internally. The project is one I plan to document on the newsletter and on YouTube.

## What's inside

- Why a real phone farm gives a better scraping fingerprint than dongles, and where dongles still win on cost and size.
- Why you cannot connect directly to the devices once they are running, and how a server port maps to a device through a reverse SSH tunnel.
- Which management tools we looked at: localtonet, Iproxy, ProxySmart and Proxidize.
- Reselling IPs raises three questions: whether your country is attractive, how to find buyers, and what legal exposure you take on as the IP owner.

**In the full article:** The cost comparison for the SIM plans, the component-by-component description of the farm architecture and the notes on running Playwright on Android phones for internal scraping.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-mobile-proxy-farm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
