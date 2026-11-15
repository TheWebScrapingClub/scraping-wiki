---
type: article_summary
title: 'Buy cheaper plane tickets using a VPN: truth or myth?'
slug: cheaper-plane-tickets-vpn
canonical_url: https://www.scraping.club/p/cheaper-plane-tickets-vpn
publish_date: '2023-07-20'
visibility: premium
topics:
- proxies
- browser-automation
- residential-proxies
- akamai
description: We tested whether a VPN or proxy cuts flight prices on British Airways (Akamai) using Playwright and Smartproxy residential proxies.
source_hash: 7290dd8537929928
---

# Buy cheaper plane tickets using a VPN: truth or myth?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-07-20 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/cheaper-plane-tickets-vpn?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Every summer a travel guru on TikTok or YouTube says a VPN and cleared cookies will get you a cheaper plane ticket. An affiliate link for the VPN usually follows. I've heard this trick for years. Maybe it worked once, as a glitch fixed as soon as it was exploited, but it makes a good excuse to practice Playwright with proxies.

We checked British Airways, which is protected by Akamai, looking at London to New York flights on the 12th of August. Picking airports and dates means real interaction with the page, so a simple Scrapy spider is not enough. We drove the booking form with Playwright and Brave, first from Italy without a proxy and then through Smartproxy residential proxies, changing the exit country per run. We only looked at prices, we did not download data.

## What's inside

- How the script picks a different Smartproxy residential endpoint depending on the country it receives as input
- How the form is filled: page.type for airports and dates, page.click with XPath selectors for navigation
- What happens on the first run from Italy, including the redirect to the Italian site and the cookie consent step
- Real use cases where choosing the country of the IP matters, such as social media scraping and online advertising monitoring

**In the full article:** The Playwright code, the proxy configuration per country, the XPath selectors for the booking form and the price screenshots from each run.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/cheaper-plane-tickets-vpn?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
