---
type: article_summary
title: Rethinking the web browser
slug: rethinking-the-web-browser
canonical_url: https://www.scraping.club/p/rethinking-the-web-browser
publish_date: '2025-01-21'
visibility: free
topics:
- browser-automation
- legal-ethics
- browser-as-a-service
- http-clients
description: Why headless Chrome is a poor fit for scraping and AI crawlers, and what a browser built for machines instead of humans could look like.
source_hash: 000e0fad79e6b93f
---

# Rethinking the web browser

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-21 (free to read). **[Read the full article](https://www.scraping.club/p/rethinking-the-web-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Almost half of internet traffic now comes from machines, and AI crawlers add more every month. The browser they all depend on was built for humans, on rendering code that goes back to KHTML in 1998. Headless Chrome driven by Puppeteer or Playwright works, but at scale it costs memory, startup time, stability and money.

This is a guest post by Katie Hallett, part of the founding team at Lightpanda, who built scraping infrastructure at BlueBoard before that. She walks from cURL to headless browsers, then to browser-as-a-service platforms and natural-language automation libraries, and points out that all of them still sit on Chrome headless. She then sketches what a browser designed for machines would need to do and presents Lightpanda, an open-source headless browser written in Zig.

## What's inside

- How Blink, WebKit and KHTML are related, and why that legacy matters when the user is a script and not a person.
- What Vercel's data says about AI crawlers like GPTBot and Claude: they fetch JavaScript files but do not execute them, and why.
- Four requirements for a machine-first browser, including one that makes the browser part of the agent itself.
- A quote from the BG2Pod discussion on whether agents should click buttons at all or talk to composable APIs.

**In the full article:** Statistics on bot traffic and the Vercel crawler figures, the performance claim from the Lightpanda demo against headless Chrome, and links to the GitHub repository and demo.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/rethinking-the-web-browser?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
