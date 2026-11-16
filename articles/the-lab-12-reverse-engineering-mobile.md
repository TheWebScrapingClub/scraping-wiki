---
type: article_summary
title: 'THE LAB #12: Reverse-engineering Mobile API '
slug: the-lab-12-reverse-engineering-mobile
canonical_url: https://www.scraping.club/p/the-lab-12-reverse-engineering-mobile
publish_date: '2023-02-16'
visibility: premium
topics:
- proxies
- scraping-infra
description: Setting up Charles Proxy and an Android Studio emulator on Ubuntu 22.04 to intercept HTTPS traffic from a mobile app and find its API for scraping.
source_hash: a2b079bd5aa0cfaa
---

# THE LAB #12: Reverse-engineering Mobile API 

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-02-16 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/the-lab-12-reverse-engineering-mobile?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

When a website fights back, we often forget the mobile app behind it. Mobile is about 59% of internet traffic, according to Tiago Bianchi, and in most cases the app APIs are less protected than the website. That makes the app a reasonable target when the site gets hard to scrape.

This Lab, written by Fabien Vauchelles, the Anti-Ban Expert at Wiremind and creator of Scrapoxy, starts the reverse-engineering of an Android app API. We work on Ubuntu 22.04 with Android Studio and its emulator, and we put Charles proxy in the middle to read HTTP and HTTPS traffic. Charles is an alternative to Fiddler, which Pierluigi used in the first Lab. This part covers the Charles setup: installing it, enabling SSL proxying, preparing its root certificate so Android can use it as a system certificate, and finding the local IP the emulator will connect to. The Android image comes next.

## What's inside

- Why Charles is a useful alternative to Fiddler, which was used in the first Lab on scraping data from an app.
- Why the Charles root certificate cannot be used as is and has to be converted before Android accepts it as a system certificate.
- Which local IP address to give the emulator, and why a stable internal Docker address is a practical choice.
- The Charles free trial is limited in usage time, but it is enough for this work.

**In the full article:** The apt install commands, the SSL proxying settings, the certificate hash and renaming commands, the screenshots of each Charles menu, and the Android Studio image setup in Part B.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/the-lab-12-reverse-engineering-mobile?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
