---
type: article_summary
title: 'THE LAB #74: Running scrapers on GitHub Actions'
slug: running-scrapers-on-github-actions
canonical_url: https://www.scraping.club/p/running-scrapers-on-github-actions
publish_date: '2025-01-30'
visibility: premium
topics:
- scraping-infra
- proxies
description: How to schedule a Python price scraper on GitHub Actions, compared with cron jobs, cloud platforms and third-party tools, with its pros and limits.
source_hash: fa1a379e1f6d947b
---

# THE LAB #74: Running scrapers on GitHub Actions

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-01-30 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/running-scrapers-on-github-actions?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Once a scraper works from start to finish, the next question is how to run it on a schedule without launching it by hand. The options are many: cron jobs on a server you control, cloud platforms like AWS, Azure and GCP, third-party automation tools, and GitHub Actions. Each fits a different project size and execution time, and each has a different IP address profile. That matters when the target has some protection.

Here we focus on GitHub Actions. We cover what it is, how workflows, triggers, jobs and runners fit together, and where it helps or gets in the way for scraping. For the test, I picked a working price scraper for Ounass, a luxury e-commerce site popular in the Middle East, and put it in a new repository. We then get to the YAML workflow file that tells GitHub what to run and when.

## What's inside

- How GitHub Actions compares with cron on your own server, cloud VMs, containers and Lambda, and third-party tools like Zapier, especially on IP addresses and execution limits.
- The limits that matter for scrapers: the 6-hour job cap, limited CPU and memory, and runner minutes on private repositories.
- Runners are ephemeral, so data persistence has to be handled explicitly with artifacts or external storage.
- The difference between GitHub-hosted and self-hosted runners.

**In the full article:** The YAML workflow file, the Ounass scraper code in the paid-access GitHub repository, and the step-by-step setup and scheduling of the run.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/running-scrapers-on-github-actions?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
