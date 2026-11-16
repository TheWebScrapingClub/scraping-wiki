---
type: article_summary
title: What is device fingerprinting? A deep dive
slug: what-is-device-fingerprint
canonical_url: https://www.scraping.club/p/what-is-device-fingerprint
publish_date: '2023-05-21'
visibility: free
topics:
- browser-fingerprinting
- browser-automation
- cloudflare
- tls-fingerprinting
description: 'Device fingerprinting for scrapers: what is collected, active vs passive techniques, privacy rules, and masking the connection and browser layers.'
source_hash: fdb7e12ac54f689c
---

# What is device fingerprinting? A deep dive

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-05-21 (free to read). **[Read the full article](https://www.scraping.club/p/what-is-device-fingerprint?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A device fingerprint is a set of attributes the device and its browser hand over on their own: OS, screen size, user-agent, language, fonts, plugins, IP address, HTTP headers. The more pieces we add, the fewer users share the same configuration, so a site can follow a small niche of users without cookies. That matters now that cookies are refused or wiped, and anti-bot vendors build on the same basics, add Canvas and WebGL results, and look for incompatible data or outliers.

I explain how the data is collected, splitting active from passive techniques, and why marketing and anti-fraud both want it. I also cover the privacy side under European rules. Then we go layer by layer on masking, using deviceinfo.me to see what leaks: the connection layer, with TLS fingerprint, IP and proxy types, and the browser layer, with Playwright, Chrome, and anti-detect browsers like GoLogin.

## What's inside

- Canvas and WebGL work by rendering an image off-screen, which comes out differently on different hardware, while passive techniques only read what the browser and the HTTP layers pass along.
- Why the opinion of the European data protection working party makes the ePrivacy directive apply to fingerprinting, as it does to cookies, and what that means for visitors.
- At the connection layer, IP-derived data like country, state and ISP, and the choice between datacenter, residential and mobile IPs.
- Small machine details that can give away a scraper, such as a server with no microphone or camera, and the computing cost of headful browsers.

**In the full article:** Screenshots from deviceinfo.me comparing Playwright in headless and headful mode and a GoLogin profile, the full list of collected attributes, and the links to our TLS fingerprinting post and the working party opinion.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/what-is-device-fingerprint?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
