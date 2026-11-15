---
type: article_summary
title: 'Creating a dataset for investors with web scraping: Tesla (TSLA)'
slug: dataset-for-investors-tesla-tsla
canonical_url: https://www.scraping.club/p/dataset-for-investors-tesla-tsla
publish_date: '2023-04-27'
visibility: premium
topics:
- industry-overview
description: Building a Tesla (TSLA) dataset for investors by scraping new and used listings from Tesla's US website to track how models hold their value.
source_hash: 8fac6b9597d8e82b
---

# Creating a dataset for investors with web scraping: Tesla (TSLA)

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-04-27 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/dataset-for-investors-tesla-tsla?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Fundamental investors can work with a meaningful dataset on a single stock, if the data is truly valuable. Tesla is a good candidate: in April 2023 it was the 10th US company by market cap, still below its 2021 peak after the 2022 crash. Investors already have EV market data, order estimates and supply chain data. We wanted something different: how Tesla models keep their value over time, a taste of the brand's appeal, and whether it holds value like a BMW or more like an Opel.

We started from Tesla's US website, which lists new and used cars on sale, filtered by zip code. The data comes from an internal API, so we need a list of zip codes, then iterated calls to that API for each one, and store the results. That way we compare apples with apples, following each model and configuration over time.

## What's inside

- Why a single-stock dataset can be enough for a fundamental investor, while quantitative funds need many stocks and a long history.
- Compliance constraints on financial data: no personal information, and scraping done in an ethical and legal manner.
- Why Tesla: its market cap rank in April 2023 and its position against the 2021 peak.
- The zip code filter on Tesla's inventory page and why it forces us to build a zip code list before scraping.

**In the full article:** Scraper code, the zip code list handling, and the calls to Tesla's internal API that produce the dataset.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/dataset-for-investors-tesla-tsla?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
