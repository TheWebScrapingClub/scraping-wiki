---
type: article_summary
title: 'The LAB #114: Manus at Work - Kasada on Nike.com'
slug: deobfuscating-kasada-with-manus-ai
canonical_url: https://www.scraping.club/p/deobfuscating-kasada-with-manus-ai
publish_date: '2026-08-27'
visibility: premium
topics:
- proxies
- akamai
- browser-automation
description: Using Manus AI to inventory the browser values Kasada's client-side VM reads on nike.com, and how to back each claim with an evidence level.
source_hash: 42a0187b57714ee3
---

# The LAB #114: Manus at Work - Kasada on Nike.com

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-08-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/deobfuscating-kasada-with-manus-ai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Kasada no longer ships obfuscated JavaScript a beautifier can help with. It ships a custom virtual machine and a blob of bytecode, so you read an interpreter loop, not logic. Sending the right token gets you the page, but it doesn't tell you how the system decides you're a real user. On nike.com I wanted to know what opening one of these costs and what you can claim afterwards.

We pointed Manus AI at the client side of Kasada on nike.com, read-only, without executing anything Kasada served. The goal was an inventory of the values it reads to build your fingerprint, not a bypass or a token generator. We cover how p.js and ips.js are laid out, how their decoders and string tables work, how the two VMs differ, and how we gave every claim an evidence level.

## What's inside

- Four layers separate the loader, the fingerprinting program, the transport and the server-side decision, and I say which one I'm after and which one nobody outside Kasada can see.
- Why "N signals collected and transmitted" claims usually come from the weakest evidence level, and what separates a string in a table from a value actually read and sent.
- The ips.js decoder is tied to the wall clock, which limits how long a captured file stays readable and changes when you have to analyze it.
- Substring search on the string table produces false matches, so we reconstruct structural references the bytecode can actually address.

**In the full article:** The full fingerprint inventory with category, reference count and byte positions per entry, the decoder logic, the seed window script, the synthetic clock test output and the opcode breakdown of both VMs.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/deobfuscating-kasada-with-manus-ai?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
