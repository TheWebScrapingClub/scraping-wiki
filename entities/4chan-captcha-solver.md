---
name: 4chan-captcha-solver
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - breaking-the-4chan-captcha.md
---

# 4Chan CAPTCHA Solver

## What it is

The 4Chan CAPTCHA Solver is a project focused on training a machine learning model to solve both the standard alphanumeric and the slider-based CAPTCHAs found on 4chan. The goal was to achieve a high accuracy rate (over 80%, preferably over 90%) with a model that can run directly in the browser.

## How it works

The project involves scraping CAPTCHA data from 4chan. The standard alphanumeric CAPTCHAs present as an image with 5-6 characters, while the slider CAPTCHAs require aligning fragments of an image by moving a slider. The data acquisition process revealed that 4chan employs throttling mechanisms, increasing the cooldown period between CAPTCHA requests and potentially degrading data quality with excessive requests. Additionally, bypassing the initial Cloudflare Turnstile challenge is necessary to obtain CAPTCHAs, requiring the use of valid cookies.

The project also addresses the challenge of obtaining solutions for the scraped CAPTCHAs. While manual completion is an option, the author explored alternative methods, suggesting that the difficulty humans face with these CAPTCHAs might be an opportunity for automated solutions.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The source document mentions that obtaining CAPTCHAs requires passing a Cloudflare Turnstile challenge, necessitating the use of valid cookies. Simply using numerous proxies without addressing this can be unrealistic. The author also notes that the CAPTCHA data quality can decrease if too many requests are made.

## Related

- [Cloudflare](../entities/cloudflare.md)


## Sources

- [https://nullpt.rs/breaking-the-4chan-captcha](https://nullpt.rs/breaking-the-4chan-captcha)
