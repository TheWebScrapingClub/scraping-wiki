---
type: article_summary
title: The Anti-Detect Browser Royal Rumble - updated with notes
slug: anti-detect-browser-royal-rumble-comments
canonical_url: https://www.scraping.club/p/anti-detect-browser-royal-rumble-comments
publish_date: '2024-06-04'
visibility: free
topics:
- anti-detect-browsers
- antibot
- browser-fingerprinting
- proxies
description: 'Updated Anti-Detect Browser Royal Rumble: MultiLogin joins the CreepJS and BrowserScan fingerprint benchmark, and the vendors comment on the methodology.'
source_hash: 39641ec4bbfe04a8
---

# The Anti-Detect Browser Royal Rumble - updated with notes

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-06-04 (free to read). **[Read the full article](https://www.scraping.club/p/anti-detect-browser-royal-rumble-comments?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Every anti-detect browser has its own options and features, so forcing one configuration on all of them can cost some of them points in the benchmark. The first Royal Rumble was well received, and I decided to open it to the companies involved. I wanted them to share their ideas on how the tests were run, and to put that feedback on the record.

This edition adds MultiLogin, which I could not test in time for the first one. We ran it through the same methodology as GoLogin, Incogniton, Kameleo, More Login, NSTBrowser, Octo Browser and Undetectable.io: a Mac OS Chrome profile on a Windows Server VM at AWS, residential proxies, CreepJS and BrowserScan. Then come the vendors' comments, including a mistake I made in the Kameleo setup.

## What's inside

- How the 260 points split between the CreepJS trust score, BrowserScan authenticity, and the browser, OS and WebRTC checks.
- Kameleo's CEO argues that default settings blend in better than noise on every parameter, and that advanced scrapers should benchmark several setups on their own target.
- Octo Browser questions how audio noise is handled and the uneven number of CreepJS visits per browser, and suggests testing on heavily protected sites.
- Incogniton suggests forcing a user agent coherent with the browser, and complains that competitors are not equally open about how their profiles are configured.

**In the full article:** Screenshots of the MultiLogin results on both test pages, the updated ranking, and the complete comments from each vendor.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/anti-detect-browser-royal-rumble-comments?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
