---
type: article_summary
title: Predictive Analytics Using Scraped Data
slug: predictive-analytics-web-scraped-data
canonical_url: https://www.scraping.club/p/predictive-analytics-web-scraped-data
publish_date: '2025-06-29'
visibility: free
topics:
- nlp-ml
- browser-automation
- data-analysis
- proxies
description: 'Predictive analytics on scraped data: Yahoo Finance AAPL history collected with Selenium, then an LSTM model in Jupyter to predict Adj Close.'
source_hash: 1332ba4cf0332e6f
---

# Predictive Analytics Using Scraped Data

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-06-29 (free to read). **[Read the full article](https://www.scraping.club/p/predictive-analytics-web-scraped-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Data is only worth something once you turn it into forecasts, and most of us don't have large proprietary datasets to train on. For a lot of teams, web scraping is the only realistic way to get enough data for a predictive model. I wanted to put the two fields side by side and strip out the hype: predictive analytics is applied mathematics, a model that learns patterns from historical data and then predicts values it has never seen.

We start with the theory: what predictive analytics is, how machine learning relates to deep learning, and why scraping matters for training data, fresh data and market sentiment. Then we build a full tutorial. We scrape one year of Apple stock history from Yahoo Finance with Selenium and save it with pandas. In a Jupyter Notebook we clean and scale the data, split it into training and test sets, train a deep learning model with TensorFlow, and check how well it predicts.

## What's inside

- How deep learning relates to machine learning, and why supervised learning needs historical data with known outcomes
- Concrete use cases for scraped data: competitor pricing for e-commerce and news and social sentiment for a hedge fund
- Why the tutorial predicts Adj Close, and why the choice of target price is arbitrary
- Preparation steps before training: type conversion, handling missing values, feature scaling and the train/test split

**In the full article:** The Selenium scraper code, the notebook cells for cleaning, splitting and training, the model architecture, and the numerical evaluation of the predictions.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/predictive-analytics-web-scraped-data?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
