---
type: article_summary
title: Writing a web scraper with ChatGPT. Is it a good idea?
slug: writing-a-web-scraper-with-chatgpt
canonical_url: https://www.scraping.club/p/writing-a-web-scraper-with-chatgpt
publish_date: '2023-04-16'
visibility: free
topics:
- proxy-industry
- industry-overview
description: A test of whether ChatGPT can write, debug and port a Scrapy scraper for a niche fashion e-commerce site, and whether it saves a practitioner any time.
source_hash: 7a7fe4cafc0d31e5
---

# Writing a web scraper with ChatGPT. Is it a good idea?

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2023-04-16 (free to read). **[Read the full article](https://www.scraping.club/p/writing-a-web-scraper-with-chatgpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Five months after ChatGPT launched, and with GPT-4 out, I wanted to check what AI can actually do for web scraping. Asking it for a working scraper on a chosen website does not get far. You get syntactically correct code with generic selectors, useful only if the site is famous enough that the answer already sits on Stack Overflow.

So we picked a niche target, the Gianvito Rossi Italian e-commerce site, and built a Scrapy spider with XPath selectors by prompting ChatGPT step by step. We then looked at two more uses. First, bugfixing: I broke the spider with a quoting error and an uninitialized variable and asked ChatGPT to fix it. Second, porting: I reused the same prompt to get a Node.js scraper, a language I don't know. I measured each use against the time it would take me to do the work by hand, and I draw a conclusion on whether AI is an aid or a threat.

## What's inside

- How we structured the final prompt for the Scrapy spider: the access plan, the selectors we supplied and the four fields to map.
- Why writing the prompt may take as long as writing the spider, and what changes if you reuse an engineered prompt and a spider template.
- Whether ChatGPT explains its fixes when it debugs a broken spider, or only returns corrected code.
- What the Node.js port means for someone learning a new language while writing scrapers.

**In the full article:** The full prompt, the Scrapy spider and Node.js scraper code ChatGPT returned, the broken spider used for the bugfixing test and the complete ChatGPT explanation of its fix.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/writing-a-web-scraper-with-chatgpt?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
