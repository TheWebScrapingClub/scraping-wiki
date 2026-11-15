---
type: article_summary
title: Ensuring data quality in web scraping projects
slug: ensuring-data-quality-in-web-scraping
canonical_url: https://www.scraping.club/p/ensuring-data-quality-in-web-scraping
publish_date: '2023-09-16'
visibility: free
topics:
- industry-overview
description: 'How to keep scraped data reliable as projects grow: monitoring runs, validating at ingestion, completeness and coherence checks, and manual sampling.'
source_hash: 747b843ee76835ab
---

# Ensuring data quality in web scraping projects

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-09-16 (free to read). **[Read the full article](https://www.scraping.club/p/ensuring-data-quality-in-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Data quality is one of the critical pain points in web scraping. How do you know the output fields are mapped to the information you want, that you scraped the whole scope, and that the format is right? As a project grows, these questions get harder to answer, and the quality of the extracted data drops with it.

I walk through the techniques we use, following the data from scraper to publication. We start with talkative scrapers and one place for execution recaps, then move to checks at ingestion into the database. Next come automatic controls on completeness and coherence, with prices across countries as the example. Qualitative fields such as descriptions and reviews come after, where automation runs short and manual sampling takes over. I also describe the Ground Truth method we apply at Databoutique.com, and changedetection.io, a tool I have not tried yet.

## What's inside

- Why a recap of return codes, like the one Scrapy prints, helps you investigate partial results, and why it belongs in one place instead of thousands of log files.
- Why validating formats when loading into the database gives one central point of control instead of the same rules repeated in hundreds of scrapers.
- How the ¥ symbol shared by Japan and China, and similar cases like the dollar sign or the Nordic krona, show up as currency errors when you compare prices across countries.
- Which checks are still possible on emails, URLs, image links and descriptions, and where only sample inspection is left.

**In the full article:** Screenshots of the execution recap and the item count check, the threshold logic behind the Ground Truth alerts, the price coherence examples over places and over time, and my open question on better ways to validate content.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/ensuring-data-quality-in-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
