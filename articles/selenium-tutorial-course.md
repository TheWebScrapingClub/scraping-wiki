---
type: article_summary
title: 'Web Scraping from 0 to hero: Selenium'
slug: selenium-tutorial-course
canonical_url: https://www.scraping.club/p/selenium-tutorial-course
publish_date: '2024-03-03'
visibility: free
topics:
- browser-automation
description: 'An introduction to Selenium for web scraping: how it compares to Playwright, what a WebDriver does, and how to wire one into a Python scraper.'
source_hash: 95a4da4c83bd7963
---

# Web Scraping from 0 to hero: Selenium

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-03-03 (free to read). **[Read the full article](https://www.scraping.club/p/selenium-tutorial-course?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Selenium is the other big browser automation framework used for scraping, and it was built for testing first. After Scrapy and Playwright, this episode of Web Scraping from 0 to Hero covers it before we write any scraper. If you already use Playwright, the question is what Selenium does differently and whether it is worth your time. The answer starts with how it talks to the browser.

We compare Selenium and Playwright on architecture, language support, browser coverage, speed and API, and I say which one I prefer for scraping. Then we look at the WebDriver: the browser-specific component that sits between your script and the browser, and the JSON Wire Protocol and HTTP requests behind it. We go through the setup of ChromeDriver, GeckoDriver and EdgeDriver in a Python scraper, and the connection to a remote WebDriver session, which parallels Playwright's remote connection over CDP. The first actual scraper comes in the next episode.

## What's inside

- Why Selenium's round trip between script, WebDriver and browser makes it slower than Playwright's direct communication
- Which browsers each tool covers, and why that matters when you need a different browser to spoof your fingerprint
- How the JSON Wire Protocol serializes commands as REST calls, independent of the language binding you use
- Why the driver version has to match the browser version, and why you should close the session when the job is done

**In the full article:** The Python snippets for ChromeDriver setup, session closing and the remote WebDriver connection, plus the full side-by-side comparison with Playwright and the WebDriver architecture diagram.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/selenium-tutorial-course?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
