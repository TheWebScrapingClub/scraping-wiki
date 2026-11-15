---
type: article_summary
title: Building A Scraper Dashboard Using Streamlit
slug: building-a-scraper-dashboard-streamlit
canonical_url: https://www.scraping.club/p/building-a-scraper-dashboard-streamlit
publish_date: '2025-11-09'
visibility: free
topics:
- data-analysis
- proxies
- residential-proxies
description: How to build an interactive Streamlit dashboard from scraped data, using the Scrape This Site hockey teams table, Pandas and Altair.
source_hash: 24d8ba121f6c638f
---

# Building A Scraper Dashboard Using Streamlit

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2025-11-09 (free to read). **[Read the full article](https://www.scraping.club/p/building-a-scraper-dashboard-streamlit?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

A stakeholder asks for a dashboard to get a rough idea of the data before we continue the scraping job. A Jupyter Notebook full of code is the wrong thing to send, and so is a dozen charts with no connection between them. Setting up a database and deploying on the web is too much for a POC. I want something close to a web deployment, but much faster to build.

We build it with Streamlit, an open-source Python library that turns a script into an interactive web app. The project has three files: scraper, charts and main app. The target is the hockey teams table on Scrape This Site, scraped with requests and BeautifulSoup, loaded into Pandas and plotted with Altair. The sidebar lets the user choose how many pages to scrape and set a delay between requests, then start the run.

## What's inside

- Why Streamlit fits this job: widgets created with plain Python calls, automatic script reruns on user input, native DataFrame rendering and caching decorators.
- Where a Pandas and Matplotlib notebook stops being enough, and when a shareable dashboard is the better tool.
- The Raw data section can be filtered and exported as CSV, and the dashboard updates live as the filters change.
- The Deploy button offers several ways to share the dashboard with stakeholders.

**In the full article:** Code for the table detection function, the Altair chart and the sidebar controls, the environment setup commands, the screenshots and GIFs of the running dashboard, and the link to the full repository.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/building-a-scraper-dashboard-streamlit?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
