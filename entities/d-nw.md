---
name: d-nw
type: entity
category: tool
first_seen: 2026-10-28
last_updated: 2026-10-28
sources:
  - carbonmeai-danwo.md
---

# Dánwò

## What it is

Dánwò is the most complete open-source end-to-end testing framework designed for the agentic era, serving as an end-to-end testing framework for both web and mobile applications. It allows users to drive an application through its UI like a user and verify the backend actions that occur behind the interface.

## How it works

The framework provides UI testing capabilities through locators and plain-English agent steps that replay actions without requiring model calls. It also includes screenshot comparison functionality executed within a browser on Android or iOS.

When testing backend interactions, Dánwò includes a backend layer that emulates providers such as Stripe, Clerk, Resend, Google, and Slack, running behind a proxy. Furthermore, it features an invariant system that reads the database and provider state to verify outcomes, and a fault matrix (`danwo matrix`) that reruns tests once per fault to check for issues like 500 errors or lost database commits.

## TWSC experience

Not yet tested by TWSC.

## Related

* [playwright](../entities/playwright.md)
* [proxy-server](../entities/proxy-server.md)
* [nodejs-based-scraper](../entities/nodejs-based-scraper.md)


## Sources

- [https://github.com/carbonmeai/danwo](https://github.com/carbonmeai/danwo)
