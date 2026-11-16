---
type: article_summary
title: 'THE LAB #97: My first week with OpenClaw'
slug: my-first-week-with-openclaw
canonical_url: https://www.scraping.club/p/my-first-week-with-openclaw
publish_date: '2026-02-05'
visibility: premium
topics:
- proxies
- proxy-industry
- http-clients
description: 'A first-week report on OpenClaw, the open-source local AI agent: what it does, how I set it up, the security trade-offs, and why it matters for web scraping.'
source_hash: b5468d35d93bd076
---

# THE LAB #97: My first week with OpenClaw

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-02-05 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/my-first-week-with-openclaw?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

OpenClaw appeared on GitHub on November 24, 2025 and has over 160,000 stars two months later. It is an open-source agent that runs on your machine, edits files, executes shell commands and browses the web, and you talk to it from Telegram, WhatsApp, Slack or Signal. Scraping is not its core use. Still, an agent that drives a real browser session and runs background jobs is worth a look, and it also means giving an AI wide access to your computer.

I ran it for about ten days with Claude as the backend, Telegram as the channel and the browser extension on Brave. I go through what it is: integrations, skills, memory, cron jobs and group chats. Then I show what I used it for, from an accounting app to a site with no API. I also spend time on security: what the agent can see, prompt injection, and why I plan to move to a local model.

## What's inside

- The skill system, where the agent can write its own extensions and update its own prompts, and why that is both useful and uncomfortable
- The browser extension only controls tabs you attach, and the docs list Chrome only, so I tried a different Chromium browser
- The trade-off between cloud and local models: privacy on one side, capability on complex reasoning on the other
- Practical precautions I recommend: a dedicated browser profile, no banking tabs, limited directory access and sandbox mode

**In the full article:** Install commands, the Telegram pairing and browser extension steps, my full list of security precautions and the section on why OpenClaw matters for web scraping.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/my-first-week-with-openclaw?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
