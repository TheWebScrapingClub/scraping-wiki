---
type: article_summary
title: Google has exclusive access to a browser API
slug: google-browser-api-cpu
canonical_url: https://www.scraping.club/p/google-browser-api-cpu
publish_date: '2024-07-14'
visibility: free
topics:
- datadome
- browser-fingerprinting
description: Google's hidden Chrome extension exposes a CPU info API that only Google-domain pages can call, and what that means for browser fingerprinting and the open web.
source_hash: ca86134c8fb6c79b
---

# Google has exclusive access to a browser API

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-07-14 (free to read). **[Read the full article](https://www.scraping.club/p/google-browser-api-cpu?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Last week Luca Casonato reported a case that looks minor and isn't. In 2023 Google shipped a hidden extension in Chrome that exposes CPU usage through browser APIs. APIs like this are normal. What isn't normal is that only pages loaded on Google domains can call this one.

We looked at the case from two sides. First, we ran the snippet Simon Willison shared in the console, once on a Google page and once on another site, and compared what came back. Then we read Google's stated reasons for the API: video and audio optimization, and crash reporting. I don't think Google is fingerprinting users with it, but I still find it unfair, since Zoom or Teams get no access. From there I widen the view to the 8k+ APIs in Chrome, the data points anti-bot vendors collect from them, and why users can't opt out of fingerprinting.

## What's inside

- The API is open to any extension developer, but a regular web page can reach it only from a Google domain.
- The fairness question: Meet gets CPU data for call quality, while Zoom, Teams and other browser-based tools do not.
- I compare the case with the browser choice screen Microsoft was forced to show and with Google's search default deals, and explain why I doubt regulators will act on something this technical.
- Cookies can be deleted, but the only way to block fingerprinting is to disable JavaScript, which breaks most sites.

**In the full article:** The console snippet, the screenshots of the output on Google and non-Google pages, Google's full statement and the links to my earlier post on browser fingerprinting papers.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/google-browser-api-cpu?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
