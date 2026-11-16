---
type: article_summary
title: 'The Lab #59: Bypassing certificate pinning with Frida and Fiddler - part 2'
slug: bypass-certificate-pinning
canonical_url: https://www.scraping.club/p/bypass-certificate-pinning
publish_date: '2024-08-15'
visibility: premium
topics:
- industry-overview
description: Bypassing certificate pinning in Android apps with Frida and a rooted virtual device to intercept X's traffic in Fiddler Everywhere.
source_hash: f197810089559582
---

# The Lab #59: Bypassing certificate pinning with Frida and Fiddler - part 2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-08-15 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bypass-certificate-pinning?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

In the previous episode of The Lab we intercepted an app's traffic with Fiddler Everywhere. That setup fails on apps that take security seriously: X uses certificate pinning, binding the app to a specific certificate and refusing anything else, even one from a trusted CA. But when a website is too hard to scrape, or there's no web version, seeing which endpoints the app calls is worth the extra work.

To hijack those checks I used Frida, an instrumentation toolkit that injects JavaScript into a running app and hooks functions like X509TrustManager's checkServerTrusted. Frida needs a rooted device, and I have no spare phone, so we built a virtual device in Android Studio, controlled it with ADB, and rooted it with RootADV and Magisk. Then we adapted a universal SSL pinning bypass script to accept the Fiddler certificate and attached Frida to the X app.

## What's inside

- The two roads for understanding a pinned app: get its source code, or hijack its certificate controls.
- The common hooking targets in Android apps, from network libraries like OkHttp to functions such as SSL_verify_cert_chain and X509TrustManagerImpl.
- Why configuring the virtual device's WiFi proxy for Fiddler is the most annoying part of the process, and the setup that works for now.
- A reproducibility caveat: I ran the whole procedure on a Mac and list the software versions used, since these tools update often and other releases may break the steps.

**In the full article:** The full article includes the step-by-step walkthrough, the ADB and Frida commands, the modified script.js for the certificate bypass, the RootADV rooting procedure, the Fiddler proxy configuration for the virtual device, the software versions I used, and the example of the API traffic captured from the X app.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bypass-certificate-pinning?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
