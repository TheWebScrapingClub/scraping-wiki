---
type: article_summary
title: Mouse movements in Playwright with Ghost Cursor
slug: bypass-datadome-mouse-movements-in-playwright
canonical_url: https://www.scraping.club/p/bypass-datadome-mouse-movements-in-playwright
publish_date: '2024-02-01'
visibility: premium
topics:
- browser-automation
- human-behavior-emulation
- datadome
- antibot
description: Why Playwright's default mouse movement is easy to flag, and how python_ghost_cursor uses Bezier curves for human-like movement against behavioral anti-bots lik
source_hash: 371ab112399f4a99
---

# Mouse movements in Playwright with Ghost Cursor

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-01 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypass-datadome-mouse-movements-in-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

On about 20% of the 200+ fashion e-commerce sites I scrape, there is some kind of bot protection. Often a plausible device fingerprint is enough and nobody checks the mouse. Datadome set to a high level is different: it looks at behavior, including how you move from page to page and how the pointer moves once you are there. Hermes.com is the example I use, and you can get blocked on it even as a human if you browse too fast.

We look at when mouse movement starts to matter in a scraping project and why Playwright's default is a problem. Playwright is built for testing web apps, so it has no human-like movement. It moves fast and in a straight line, and it produces very few mousemove events compared with a person. We then move to python_ghost_cursor, which draws Bezier curves and adjusts the speed of the pointer to mimic a real user in a Playwright browser.

## What's inside

- Rough share of protected sites in my fashion e-commerce scraping, and why large players are more likely to have anti-bot protection.
- Why a Scrapy spider or a good fingerprint is often enough and mouse movement can be ignored.
- What the W3C UI Events spec says about mousemove frequency, and how that differs from a scraper jumping from selector to selector.
- How Bezier curves tie into the human-like movement used by Python packages.

**In the full article:** The python_ghost_cursor implementation with Playwright, the draw_play.py script that plots the default movement, and the code from the paid subscribers' repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypass-datadome-mouse-movements-in-playwright?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
