---
type: article_summary
title: How Airproxy built its 2000 mobile proxies infrastructure from scratch
slug: how-build-mobile-proxy-farm-airproxy
canonical_url: https://www.scraping.club/p/how-build-mobile-proxy-farm-airproxy
publish_date: '2025-09-16'
visibility: free
topics:
- proxies
- residential-proxies
- proxy-industry
- legal-ethics
description: 'How Airproxy built a mobile proxy farm of over 2,000 USB modems and SIMs in Italy from scratch: hardware, power, connectivity and monitoring.'
source_hash: 17ab3dc942b8fe48
---

# How Airproxy built its 2000 mobile proxies infrastructure from scratch

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-09-16 (free to read). **[Read the full article](https://www.scraping.club/p/how-build-mobile-proxy-farm-airproxy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In 2018 Instagram started blacklisting datacenter IPs, and tools like MassPlanner and Jarvee needed mobile proxies to keep working. Only 3 to 5 providers existed worldwide, none had a proper website or infrastructure, and Italy had none. I saw the gap and we decided to build Airproxy.io from scratch, with no documentation and nobody to learn from.

This is the story of how we got from there to over 2,000 modems with dedicated SIMs across 6 server rooms in Italy. I start with the differences between datacenter, residential and mobile proxies, then go through the questions we had to answer ourselves, from hardware and power to bandwidth, carriers and software. I explain how the racks, the USB hubs, the fiber lines and the power backup are set up today. On the software side, we run 3proxy on Linux, Django for the site and dashboard, and Zabbix for monitoring and automatic recovery.

## What's inside

- Why I hired freelancers first, why that failed, and how meeting Mikhail, the developer, got the project moving.
- Why we needed a small office in a northern Italian city with early fiber, and what its line of sight to a cell tower meant for us.
- Why per-port power switching on custom 10-port USB hubs matters compared with off-the-shelf hubs when a modem crashes.
- How redundancy works in each server room: two fiber lines from separate ISPs, an online UPS, portable generators and an auto-reset circuit breaker.

**In the full article:** The full list of open questions we faced in 2018 on hardware, SIMs, carriers and regulation, the photos of the in-house racks and the full setup, and the detailed description of the power and failover design.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-build-mobile-proxy-farm-airproxy?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
