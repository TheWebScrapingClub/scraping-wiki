---
type: article_summary
title: 'THE LAB #89: Camoufox as a Docker image'
slug: how-to-create-camoufox-docker-image
canonical_url: https://www.scraping.club/p/how-to-create-camoufox-docker-image
publish_date: '2025-07-17'
visibility: premium
topics:
- anti-detect-browsers
- scraping-infra
- browser-automation
- proxies
description: How to package Camoufox in a Docker image and run it behind an AWS Application Load Balancer and an EC2 Auto Scaling group.
source_hash: 8263418a7ac093ab
---

# THE LAB #89: Camoufox as a Docker image

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-07-17 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/how-to-create-camoufox-docker-image?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Camoufox is our go-to stealth Firefox build, but like any automated browser it eats CPU and memory, so a single machine does not scale. Containers are the obvious answer. The catch is that running Camoufox in Docker is harder than with Playwright or other mainstream tools: the requirements chain is long and there are no step-by-step guides. I call it Docker dependency hell.

I spent several weeks building a working Camoufox Docker image and deploying it on AWS. We build the image on Ubuntu 22.04 with a Dockerfile, a Python launcher script for the Camoufox server and an entrypoint script that sets up a virtual display. On the AWS side, scraping clients connect over WebSocket to an Application Load Balancer, which routes them to an EC2 Auto Scaling group where each instance runs one Camoufox container. We also explain why containers pay off for scraping: reproducibility, scalability, portability and isolation.

## What's inside

- Why the same container runs identically in development, testing and production, and what that means for browser behavior
- How the Camoufox server launch options work: headless mode, GeoIP for timezone and locale, WebSocket port and path, optional proxy
- Why main-world JavaScript evaluation is a stealth trade-off on heavily protected sites
- Why the entrypoint starts Xvfb even though Firefox already runs headless

**In the full article:** The complete Dockerfile, the build and push to AWS, the infrastructure setup for the load balancer and Auto Scaling group, and the client connection code are only in the full article.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-create-camoufox-docker-image?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
