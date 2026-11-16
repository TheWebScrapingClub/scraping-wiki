---
type: article_summary
title: How I've built my home made mobile proxy
slug: mobile-proxy-raspberry
canonical_url: https://www.scraping.club/p/mobile-proxy-raspberry
publish_date: '2023-01-15'
visibility: free
topics:
- proxies
- residential-proxies
- proxy-industry
- scraping-infra
description: How I built a home made mobile proxy with a Raspberry Pi, a 4G modem, Squid and a reverse SSH tunnel, and how it compares with commercial mobile proxies.
source_hash: 0b215488f81ae6aa
---

# How I've built my home made mobile proxy

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-01-15 (free to read). **[Read the full article](https://www.scraping.club/p/mobile-proxy-raspberry?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In my early scraping days a small e-commerce site blocked every data center IP. AWS, Azure and GCP all failed. Mobile IPs are almost unbannable, because carriers put many users behind one public IP with CGNAT, and a site can't ban that IP without cutting out hundreds of real visitors. I had a spare SIM and a new Raspberry Pi, and I didn't want to pay a proxy provider for a single target.

I built the proxy in 2019 with a Raspberry Pi 3 and a 4G HAT, then ran Squid on it. The hard part was reaching a proxy that sits behind CGNAT from other machines. In 2020 we added two mini PCs running Ubuntu with a 4G modem, because the Raspberry started freezing under more requests. I also compare this setup with commercial providers and in-house modem products like Proxidize on cost, number of IPs and scalability, and say what I might try next.

## What's inside

- How CGNAT maps many users to one public IP, and why that makes mobile IPs hard for websites to ban.
- The modem instability on the Raspberry Pi and the small check I added to keep the proxy reliable.
- Why the Raspberry was replaced with mini PCs when request volume grew.
- Hardware and data plan costs in Italy compared with per-GB commercial mobile proxies, plus the limit of having very few IPs to rotate.

**In the full article:** The hardware list with photos of the build, the CGNAT diagram, the cost figures for the Raspberry and mini PC setups, and the references for the Squid configuration and the reverse SSH tunnel.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/mobile-proxy-raspberry?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
