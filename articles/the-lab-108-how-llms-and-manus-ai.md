---
type: article_summary
title: 'THE LAB #108: How LLMs and Manus AI are transforming bot detection'
slug: the-lab-108-how-llms-and-manus-ai
canonical_url: https://www.scraping.club/p/the-lab-108-how-llms-and-manus-ai
publish_date: '2026-06-26'
visibility: premium
topics:
- akamai
- tls-fingerprinting
- browser-automation
- antibot
description: How Manus AI, an agent with a sandboxed VM, reverse-engineered Akamai Bot Manager on net-a-porter.com, and why chat assistants like Claude refuse that task.
source_hash: fd0ba98d19fc6fb2
---

# THE LAB #108: How LLMs and Manus AI are transforming bot detection

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-06-26 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-108-how-llms-and-manus-ai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Reverse-engineering an anti-bot sensor is expensive because it takes days or weeks of human work on minified JavaScript. That cost is what keeps most protections standing. A capable model that automates deobfuscation and code analysis changes the economics of the arms race between scrapers and vendors. The June 2026 order that cut public access to Anthropic's strongest models shows how tightly the guardrails on Claude and ChatGPT are enforced.

We gave Manus AI a cold task: study Akamai Bot Manager on net-a-porter.com, deobfuscate the client script and explain which parameters feed the sensor. We gave it none of our notes or prior Lab articles. We wanted a map of the layers, not a bypass, and we kept our own review of the output in view. I reproduce Manus's anti-hooking and TLS fingerprinting summary in full. I also cover its deeper analysis of the sensor, with the operational specifics redacted. The full version sits in the paying-users GitHub repository.

## What's inside

- Why Manus fits this task: it pairs a language model with a sandboxed VM, so it runs the script and checks instead of only describing it.
- The four Akamai layers on net-a-porter.com, from the TLS check at the edge to the client-side anti-hook layer, and how each one fails differently.
- Why we picked net-a-porter.com: a live, current Akamai deployment, an observable sensor, and in-house Akamai knowledge to judge whether the output was accurate.
- The caveat on the output: we did not re-verify every claim, the sensor version dates from May 2025, and anything amounting to a turnkey recipe is redacted.

**In the full article:** The Manus AI schema of Akamai's protection, the redacted deep technical analysis of the sensor, and a pointer to the unredacted files in the paying-users GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-108-how-llms-and-manus-ai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
