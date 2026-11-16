---
type: article_summary
title: 'The LAB #118: Scrape metadata from TikTok videos'
slug: tiktok-scraping-metadata
canonical_url: https://www.scraping.club/p/tiktok-scraping-metadata
publish_date: '2026-10-29'
visibility: premium
topics:
- proxies
- antibot
- captcha
- browser-automation
description: How we reverse engineered TikTok's signed mobile API with GLM, Hermes Agent and the Reverse Engineer Anything repo to collect video metadata with no emulator.
source_hash: 83c33c231469948a
---

# The LAB #118: Scrape metadata from TikTok videos

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-10-29 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/tiktok-scraping-metadata?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A TikTok dataset of 5.6B videos' metadata on Hugging Face made me curious about how it was collected. The write-up said the approach was fully headless, with no emulators, but the details sat behind a 1699 USD paywall. Collecting at that scale with browsers or emulators costs too much, so the method matters.

The obstacle is TikTok's mobile API. Every request carries a signature, and when anything is wrong the server answers HTTP 200 with an empty body, so the status line tells you nothing.

I have limited reverse engineering experience, so we let GLM 5.3, driven by Hermes Agent and the Reverse Engineer Anything repo, do most of the work while I set direction and checked results. We used Jadx, Frida and mitmproxy on a rooted emulator, hit certificate pinning, and then removed the app from the loop with unidbg. I explain what each step showed and where the obvious plan fails.

## What's inside

- Why the HTTP status code is useless here, and the small content-based judge we built before touching anything else.
- The four checks TikTok applies to the same request: device identity, signature, regional endpoint and network fingerprint.
- Why hooking the Java-to-native boundary with Frida does not show the signer, and why the first certificate pinning bypass crashed the app.
- Why signatures cannot be reused for pagination, and the choice between reimplementing the signing math and running the app's own library.

**In the full article:** The classify function, the Hermes and REA setup, the choice of unidbg, the identity handling, the pipeline shape and the split of the GitHub repo between published and withheld code.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/tiktok-scraping-metadata?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
