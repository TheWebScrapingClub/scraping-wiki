---
type: article_summary
title: How CAPTCHAs Are Evolving to Fight AI-Powered Bots
slug: how-captchas-are-evolving
canonical_url: https://www.scraping.club/p/how-captchas-are-evolving
publish_date: '2026-07-12'
visibility: free
topics:
- captcha
- scraping-infra
- browser-automation
- anti-detect-browsers
description: 'How CAPTCHAs are changing against AI bots: hCaptcha puzzles, Microsoft multi-option challenges, Temu''s in-house CAPTCHAs, and why avoiding them still beats solv'
source_hash: b549e137607f57c3
---

# How CAPTCHAs Are Evolving to Fight AI-Powered Bots

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-07-12 (free to read). **[Read the full article](https://www.scraping.club/p/how-captchas-are-evolving?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

CAPTCHAs keep getting stranger. A text-distortion test has become a layered, multi-step, interactive task, and multimodal LLMs are the reason providers keep raising the bar. The old recipe of detect, recognize, simulate worked for years with ML models and browser automation. Now an LLM can read the page and drive the browser like a person. If you scrape, the practical question is whether this ends CAPTCHA solvers and what it changes in your scripts.

I go through why CAPTCHAs got harder and why I don't think they are dead because of AI. Then I look at three newer approaches I've seen trouble popular solving services: hCaptcha's puzzle challenges, Microsoft's multi-option CAPTCHAs and Temu's proprietary ones. I also cover where providers may go next, with Google's hand-gesture reCAPTCHA test, and the cost in user friction. I close with what I'd do as a scraper: avoid the CAPTCHA in the first place.

## What's inside

- Three reasons AI has not killed CAPTCHAs, including why LLM non-determinism and behavioral signals still get in the way of a correct answer.
- How Botright showed the classic ML-plus-automation approach, and why that project is now abandoned.
- The Temu case: AI-generated images used to build challenges meant to stop AI-powered bots.
- Why a CAPTCHA appearing at all means your traffic is already seen as low-trust, and which prevention layers I rely on.

**In the full article:** The screenshots of the hCaptcha, Microsoft, Temu and Google hand-gesture challenges, the links to the research papers, and my full list of prevention practices with the proxy and stealth browser options.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-captchas-are-evolving?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
