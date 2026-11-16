---
type: article_summary
title: 'THE LAB #7: Scraping PerimeterX protected websites'
slug: scraping-perimeterx-websites
canonical_url: https://www.scraping.club/p/scraping-perimeterx-websites
publish_date: '2022-11-24'
visibility: premium
topics:
- captcha
- cloudflare
description: How to detect PerimeterX, what its Human Challenge does, and why simulating a real user beats reverse engineering when scraping neimanmarcus.com.
source_hash: 98acf662307f946e
---

# THE LAB #7: Scraping PerimeterX protected websites

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-11-24 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-perimeterx-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

PerimeterX, now merged with Human Security, protects some top-tier websites. Its Human Challenge is easy to recognize: instead of a captcha, a big button you must keep pressed. Behind it, a real-time score built from behavior, path and fingerprints decides whether you are a human or a bot. So a scraper has to look like a human and also act like one.

For the test I used neimanmarcus.com. Finding a target was not easy, because most sites I knew on PerimeterX now stack Cloudflare bot management on top, which would have muddied the results. We cover how to spot PerimeterX with Wappalyzer and the network tab, and why I would not reverse engineer its algorithm, as the Zenrows write-up describes. I prefer simulating a real user with as few resources as possible.

## What's inside

- How PerimeterX shows up in Wappalyzer and in the cookie it sets on the first page load.
- What a 2020 interview with a PerimeterX product manager says about the Human Challenge, including its claims against reCAPTCHA.
- Why reverse engineering is fragile: the algorithm changes often and the work starts over each time.
- Why a PerimeterX-only test target was hard to find once Cloudflare bot management was added on the same sites.

**In the full article:** The scraper code, the methodology for the neimanmarcus.com test and the setup used to simulate a real user are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-perimeterx-websites?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
