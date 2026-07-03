---
name: hn-attention-cliff
type: entity
category: library
first_seen: 2026-07-03
last_updated: 2026-07-03
sources:
  - posts-your-show-hn-dies-in-7-hours.md
---

# hn-attention-cliff

## What it is

hn-attention-cliff is a repository containing the scraper, analysis, and data used to measure the half-life of Show HN launches on Hacker News. The project analyzes launch outcomes to determine how quickly engagement and visibility decay over time.

## How it works

The project scrapes every Show HN from the last 12 months using the Algolia HN API, collecting 41,301 posts and the full comment tree for launches that received at least ten comments, resulting in about 100,000 comment timestamps. The analysis uses comment timing as a proxy for attention, building a cumulative comment curve for each launch to measure the rate of engagement.

The decay mechanism is attributed to HN's ranking formula, which divides a story's points by its age raised to the power of 1.8. This formula ensures that time sits in the denominator with a larger exponent than votes in the numerator, causing the front page to act as a conveyor belt that limits visibility.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The analysis uses comment timing as a proxy for attention because Hacker News does not publish vote timestamps, which is noted as a real limitation.

## Sources

- [https://jonno.nz/posts/your-show-hn-dies-in-7-hours/](https://jonno.nz/posts/your-show-hn-dies-in-7-hours/)
