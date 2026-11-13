---
name: telltale-bot
type: entity
category: anti-bot
first_seen: 2026-11-13
last_updated: 2026-11-13
sources:
  - telltale-bot.md
---

# Telltale Bot

## What it is

Telltale Bot is a service designed to detect and classify website visitors as human, AI agent, or bot. It provides these classifications for use in analytics and marketing tools, aiming to offer more accurate insights into website traffic.

## How it works

Telltale Bot operates by deploying a JavaScript tag on a website, which can be integrated directly or via a tag manager. This script analyzes the browser's configuration and behavior, while the Telltale Bot server analyzes connection-level data. This combined analysis uses over 50 signals to determine the visitor's classification. Visitors who do not execute JavaScript, such as many crawlers, are not within its detection scope.

The service provides a verdict for each browser visit, which is delivered within the page's `dataLayer`. This data can then be utilized by analytics platforms like Google Analytics 4 (GA4) and Google Tag Manager, as well as advertising tags. Telltale Bot also offers its own reporting interface to visualize visitor data categorized by verdict, identified agents, and bots.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Telltale Bot's detection capabilities are limited to visitors who execute JavaScript. Visitors that do not run JavaScript, such as most crawlers, are outside of its detection reach.

## Related

- [Bot Detection](../concepts/bot-detection.md)
- [ML-Based Bot Detection](../concepts/ml-bot-detection.md)
- [AI Web API Fingerprinting](../concepts/ai-web-api-fingerprinting.md)


## Sources

- [https://telltale.bot](https://telltale.bot)
