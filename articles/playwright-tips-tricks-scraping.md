---
type: article_summary
title: 'Web Scraping from 0 to hero: tips and tricks for Microsoft Playwright'
slug: playwright-tips-tricks-scraping
canonical_url: https://www.scraping.club/p/playwright-tips-tricks-scraping
publish_date: '2024-02-18'
visibility: free
topics:
- browser-automation
- antibot
- anti-detect-browsers
description: 'Playwright features for scraping: persistent contexts, choosing Chromium, Chrome, Edge or Brave, connecting over CDP, and removing automation flags on bot.sanny'
source_hash: b54e745da6f1ed63
---

# Web Scraping from 0 to hero: tips and tricks for Microsoft Playwright

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-02-18 (free to read). **[Read the full article](https://www.scraping.club/p/playwright-tips-tricks-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A plain vanilla Playwright scraper opens a browser, creates a BrowserContext and loads a page in what amounts to an incognito session. For scraping that is not always what you want. Some targets read incognito browsing as a red flag, and the default Chromium setup exposes automation signals that detection pages pick up right away. Knowing what Playwright does under the shortcut commands is the first step to controlling it.

We pick up the scraper from the previous episode and go through the options that matter in practice. We compare a standard BrowserContext with a Persistent Context, and look at which browsers Playwright supports and how to use the installed Chrome, Edge or Brave. We then connect to a browser on a remote machine through the Chrome DevTools Protocol. Finally, we load the Sannysoft test with a standard Chromium setup, look at what it flags, and change Playwright's default launch arguments until the scraper looks like a regular browser.

## What's inside

- What a BrowserContext is, what it isolates (cookies, local storage, session storage) and which settings you can change per context, such as viewport, geolocation, language and permissions
- The difference between the bundled browsers (Chromium, Firefox, WebKit) and the channel values, and why only chrome and msedge matter for scraping
- How to run a Chromium-based browser already installed on your machine, with Brave as the example
- Why the WebDriver property and the "controlled by automated test software" banner give a scraper away, and which launch options relate to them

**In the full article:** The launch code for each browser and context type, the CDP connection snippet, the Sannysoft screenshots before and after each change, and the final spider setup.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/playwright-tips-tricks-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
