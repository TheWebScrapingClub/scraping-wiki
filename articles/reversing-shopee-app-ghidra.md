---
type: article_summary
title: 'THE LAB #107: Reversing Shopee''s native crypto with Ghidra'
slug: reversing-shopee-app-ghidra
canonical_url: https://www.scraping.club/p/reversing-shopee-app-ghidra
publish_date: '2026-06-12'
visibility: premium
topics:
- proxies
- proxy-industry
description: Reversing Shopee's native crypto library libshopeeaegis.so with Ghidra and rebuilding it in Python, part one of two.
source_hash: f2a9af5658c6a103
---

# THE LAB #107: Reversing Shopee's native crypto with Ghidra

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-06-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/reversing-shopee-app-ghidra?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Shopee's mobile API is a better scraping target than its website: plain JSON over HTTPS, stable endpoints, a lighter anti-bot layer. But replay a captured request and the backend answers with HTTP 418 and a security error code. The anti-fraud headers are built in native .so libraries: open the app in JADX and the signing method is there in name only, declared native, its body in ARM machine code.

This is part one of two. We took libshopeeaegis.so, reversed it end to end in Ghidra, with androguard for recon, JADX to find the Java-side door into the Aegis class, and Frida to confirm the static reading on the live app. Every operation is textbook crypto, and we rebuilt it in Python to sign offline, with no app in the loop. Part two takes on libshpssdk.so, the per-request signer, a bytecode VM that gets the oracle approach instead.

## What's inside

- How the integer mode passed to the native fire method dispatches nine operations, and how output sizes and primitive bodies name each one.
- Why the AES modes still need a value from the live process even after full static reversing: the CBC IV sits in .bss and is filled only at runtime.
- libshopeeaegis.so loads only when the app needs it: we watched the process maps over a minute of normal browsing and it never appeared.
- Shopee also ships libjnihook.so and libshook.so, a hooking framework and an anti-hook layer, so the app actively watches for instrumentation.

**In the full article:** The Ghidra headless command, the Java signatures of the native fire method, the full mode-to-operation table, the digest-size breakdown, the primitive-by-primitive reading of the decompiled code, the surviving Aegis and TeslaModel symbols, and the link to the Python reimplementation in the GitHub repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/reversing-shopee-app-ghidra?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
