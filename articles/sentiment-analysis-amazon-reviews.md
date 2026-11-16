---
type: article_summary
title: 'THE LAB #91: Performing sentiment analysis on Amazon product reviews - Part #2'
slug: sentiment-analysis-amazon-reviews
canonical_url: https://www.scraping.club/p/sentiment-analysis-amazon-reviews
publish_date: '2025-08-14'
visibility: premium
topics:
- nlp-ml
- proxies
- residential-proxies
- data-analysis
description: 'Part two of a sentiment analysis series: scraping Amazon headphone reviews with Bright Data''s Web Scraper APIs and setting up a Jupyter notebook for the analysi'
source_hash: 88adf3647dbb60c6
---

# THE LAB #91: Performing sentiment analysis on Amazon product reviews - Part #2

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-08-14 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/sentiment-analysis-amazon-reviews?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Sentiment analysis on product reviews only works if you first have clean review data, and Amazon makes that the hard part. In Part #1 I covered the theory. Here we get practical, starting from the data collection step, because everything downstream depends on what you feed the models.

The target is three wired headphones with a microphone from Rorsou, Lorelei and Elecder, all in the same price range. Since the products are simple and comparable, we skipped the full product data and went only for the reviews, using Bright Data's Web Scraper APIs with the "Amazon Reviews - collect by URL" option in Python. Then we set up Jupyter Notebook with pandas, transformers, torch and vaderSentiment, so the analysis phase can start from the scraped JSON. The actual sentiment analysis is the next section of the tutorial.

## What's inside

- Why we chose the reviews-only dataset instead of the full product data, given the three headphones are similar and in the same price range.
- How the API Request builder sample code gets adapted to submit several product URLs in one job.
- How the script separates triggering the job from polling and downloading the snapshot.
- Which fields come back with each review, and which one feeds the sentiment models later.

**In the full article:** The full Python scraper, the structure of the JSON output with a sample review record, the notebook setup steps and the pointer to the paid GitHub repository with the analysis notebook.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/sentiment-analysis-amazon-reviews?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
