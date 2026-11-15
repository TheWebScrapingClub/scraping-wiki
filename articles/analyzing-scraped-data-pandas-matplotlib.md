---
type: article_summary
title: Analyzing Scraped Data With Pandas And Matplotlib
slug: analyzing-scraped-data-pandas-matplotlib
canonical_url: https://www.scraping.club/p/analyzing-scraped-data-pandas-matplotlib
publish_date: '2025-10-19'
visibility: free
topics:
- data-analysis
- proxies
- nlp-ml
- residential-proxies
description: 'Tutorial on analyzing scraped data with Pandas and Matplotlib: scrape a GDP table, clean it in a dataframe, then plot it in a Jupyter Notebook.'
source_hash: 7c98e9b386dce6da
---

# Analyzing Scraped Data With Pandas And Matplotlib

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-10-19 (free to read). **[Read the full article](https://www.scraping.club/p/analyzing-scraped-data-pandas-matplotlib?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scraping is only half of the job. Once the data is in a file, you still have to clean it, check it and look at it before it is useful. Pandas and Matplotlib are the two Python libraries most of us reach for here, and they work well together because Matplotlib plots dataframes directly. The catch is that Pandas needs tabular data, so you either scrape a table or reshape messy data into one.

I wrote this as a step-by-step tutorial. The target is the Worldometers page with US GDP per year, which already has a table. We scrape it with requests and BeautifulSoup and save it to CSV. Then we load it into a dataframe in a Jupyter Notebook and look at what went wrong in the scrape: unrecognized characters, and currency and percent symbols that leave columns as text. We fix those, rename the columns, and build a line chart and a bar chart with Matplotlib.

## What's inside

- Two ways to get tabular data for Pandas: scrape a table that already exists, or scrape unordered data and reshape it.
- Using describe() to find out which columns Pandas does not see as numeric.
- Why deleting the rows with unrecognized characters is a bad idea when the character is a minus sign and you would lose the negative values.
- Choices for the charts: readable axis units, rotated year labels, and colors that separate positive from negative GDP change.

**In the full article:** The full scraper.py code, the notebook cells for cleaning and renaming, the Matplotlib plotting code and the resulting charts with the project setup steps.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/analyzing-scraped-data-pandas-matplotlib?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
