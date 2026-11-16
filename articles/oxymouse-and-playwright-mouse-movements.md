---
type: article_summary
title: 'THE LAB #63: Oxymouse and Playwright'
slug: oxymouse-and-playwright-mouse-movements
canonical_url: https://www.scraping.club/p/oxymouse-and-playwright-mouse-movements
publish_date: '2024-10-04'
visibility: premium
topics:
- browser-automation
- human-behavior-emulation
- datadome
- cloudflare
description: How websites track mouse events with JavaScript listeners, and how Oxylabs' OxyMouse adds human-like mouse movement to Playwright and Selenium scrapers.
source_hash: 5524030d66369333
---

# THE LAB #63: Oxymouse and Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-10-04 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/oxymouse-and-playwright-mouse-movements?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Anti-bot vendors can watch how a user moves the mouse. Websites do it with JavaScript event listeners, which were built for developers and ended up used for advertising, behavior tracking and bot detection. If your scraper drives a browser with Playwright or Selenium, a straight-line jump from A to B may be a signal, so it matters to know when a target actually listens.

We look at OxyMouse, a new open-source package from Oxylabs that generates human-like mouse paths for browser automation tools. First we check the listeners on a few pages with the browser Developer Tools, including sites protected by Datadome, Cloudflare and Kasada, to see what each one seems to track. Then we go through the algorithms OxyMouse offers on top of ghost-cursor, which we covered in an earlier Lab. Finally we put it in a real Playwright scraper, combined with ghost-cursor for the part OxyMouse can't do yet.

## What's inside

- How to read the event listeners active on a page from the Elements tab in Developer Tools, and why the code behind them is usually obfuscated.
- What the listeners look like on Datadome, Cloudflare and Kasada, and my own reading of what each vendor probably collects.
- How the Gaussian and Perlin algorithms differ from Bezier-based movement, and which parameters control smoothness and randomness.
- Why the working example needs ghost-cursor alongside OxyMouse for clicking on a selector.

**In the full article:** The test_oxymouse.py script from the paying subscribers' repository, showing OxyMouse random movements on a page followed by a ghost-cursor click on a selector.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/oxymouse-and-playwright-mouse-movements?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
