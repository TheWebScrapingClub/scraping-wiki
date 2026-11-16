---
type: article_summary
title: 'Interview #5: Veritas - The anti obfuscation master'
slug: interview-veritas-deobfuscation
canonical_url: https://www.scraping.club/p/interview-veritas-deobfuscation
publish_date: '2023-02-05'
visibility: free
topics:
- http-clients
- antibot
- browser-automation
- serp-scraping
description: An interview with Veritas, a NYC reverse engineer, on TikTok's obfuscated fingerprinting, his deobfuscation workflow, and why obfuscation matters for web scrapi
source_hash: e740b550e29eafb1
---

# Interview #5: Veritas - The anti obfuscation master

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-05 (free to read). **[Read the full article](https://www.scraping.club/p/interview-veritas-deobfuscation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Obfuscation and fingerprinting sit between a scraper and the data. Sites hide their collection code and anti-bot logic behind layers of scrambled JavaScript, and some go further with custom binary formats. If you can't read what the script does, you can't work out what the anti-bot expects from you.

For our monthly interview I talked with Veritas, a software engineer and hacker based in New York. His post on how TikTok hides Canvas and device fingerprinting in obfuscated scripts went viral. We talked about what that means for users, how he approaches deobfuscation, and how he sees the link with scraping. We also covered which tools he picks when he scrapes, where he thinks the tooling industry is going, and an anecdote about a browser he rebuilt to get past a retailer's anti-bot.

## What's inside

- Whether TikTok's data collection is really different from what US-based platforms do, and his view on the government device bans
- How combined browser attributes can identify a user without cookies, with FingerprintJS Pro as the example
- His order of attack when he scrapes: exposed APIs first, then libraries such as cheerio.js, Playwright and JSDom
- Why he expects scraping tools to rely more on real browser engines than on lightweight HTTP clients, given TLS and HTTP2 fingerprinting

**In the full article:** Veritas's own answers on his deobfuscation toolchain and the GitHub boilerplate he starts from, plus the full story of the Supreme anti-bot, JScrambler and the Firefox rebuild.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/interview-veritas-deobfuscation?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
