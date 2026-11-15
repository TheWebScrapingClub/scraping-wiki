---
type: article_summary
title: 'THE LAB #105: If LLMs Can Bypass CAPTCHAs, Are CAPTCHA Solver Services Cooked?'
slug: bypassing-hcaptcha-llm
canonical_url: https://www.scraping.club/p/bypassing-hcaptcha-llm
publish_date: '2026-05-29'
visibility: premium
topics:
- captcha
- cloudflare
- browser-as-a-service
- proxies
description: Can an LLM agent solve hCaptcha, or do agentic browsers still rely on solver services? We read the vendor docs and the open-source code.
source_hash: 7684b489cc2dffa3
---

# THE LAB #105: If LLMs Can Bypass CAPTCHAs, Are CAPTCHA Solver Services Cooked?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-05-29 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypassing-hcaptcha-llm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In 2023 the story was that LLMs would make CAPTCHAs irrelevant, and agentic browsers took that promise literally: Browserbase, Hyperbrowser, Skyvern, Browser Use, BrowserOS, Owl Browser. It is 2026 and CAPTCHAs are still in your pipeline. Every one of these products lists CAPTCHA solving on its site, so we asked whether an LLM can solve a production-grade CAPTCHA like hCaptcha, the one where most scrapers break.

We sorted the commercial offers into four strategy families, from stealth-first to in-house solvers, using their public documentation. Then we modeled how the hCaptcha widget works, including the cross-origin iframe and the response token. Finally we read the code of the open-source agents (browser-use, Skyvern OSS, BrowserOS) to see what they do at that boundary. We also kept invisible CAPTCHAs apart from visible image challenges, since the hype hits them unevenly.

## What's inside

- Why reCAPTCHA v3 and Turnstile are a different problem from hCaptcha and reCAPTCHA v2, and where each is covered in earlier posts.
- The four commercial strategies: stealth-first, declared partner agents, proprietary solver plus third-party integration, and in-house solver.
- Why a Playwright or CDP session cannot script the hCaptcha frame while a browser extension can.
- Why browser-use is the cleanest test of a local LLM agent that is supposed to solve the CAPTCHA by reading the page.

**In the full article:** Repo-by-repo code reading with file references, the vendor table with source pages, and the hCaptcha bypass code in the paid GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypassing-hcaptcha-llm?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
