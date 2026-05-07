---
name: nodejs-based-scraper
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-analysis-temporary-phone-numbers.md
---

# NodeJS-based scraper

## What it is

This project is a NodeJS-based scraper created to collect temporary phone numbers and associated messages. The initial implementation successfully collected 5,340 temporary phone numbers and 393,310 messages sent to these numbers for analysis.

## How it works

The scraper was designed to collect message content and sender information for each temporary phone number. The collected data was then analyzed to understand which websites and applications are targeted by temporary phone numbers and the context in which they are used.

## TWSC experience

Not yet tested by TWSC.

## Related

* [device-and-browser-info](../entities/device-and-browser-info.md)
* [proxy-server](../entities/proxy-server.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/analysis-temporary-phone-numbers](https://deviceandbrowserinfo.com/learning_zone/articles/analysis-temporary-phone-numbers)
