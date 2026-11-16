---
type: article_summary
title: 'The Lab #48: Scraping with AWS Lambda'
slug: scraping-aws-lambda-serverless
canonical_url: https://www.scraping.club/p/scraping-aws-lambda-serverless
publish_date: '2024-04-12'
visibility: premium
topics:
- scraping-infra
- browser-automation
- proxies
description: 'Scraping with AWS Lambda: deploying Selenium in a container through Serverless, what the datacenter IPs mean for blocking, and the pros and limits.'
source_hash: 2e6bf8172c5c40da
---

# The Lab #48: Scraping with AWS Lambda

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2024-04-12 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-aws-lambda-serverless?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

AWS Lambda is serverless, event-driven and billed per use, based on memory allocation and execution time. I had heard of people using it for scraping and the idea intrigued me, so I spent a week working out how it behaves for this job and where it stops being useful. The questions that matter to a practitioner are simple: what IPs you get, how much it costs, and which sites you can still reach.

We deployed Selenium on Lambda using Serverless and a public docker-selenium-lambda repository as a template. The Dockerfile sets up the environment, main.py holds the function, and the built image goes up to Lambda. To check my understanding, I changed the function to call an IP-check API and looked at what came back, including the ASN and the region. From that small test we drew the first pros and cons of the approach. Then I raised the difficulty by passing the URL to scrape as a parameter of the function invocation.

## What's inside

- What Lambda is: triggers from over 200 AWS services or HTTP through API Gateway, supported languages, and the stateless, fully managed model.
- How the Dockerfile and main.py split the work when deploying Selenium on Lambda with Serverless.
- Why AWS datacenter IPs are easy for target sites to detect and block, and when a proxy service becomes necessary.
- How the IP changes between invocations, which works as a cheap IP rotation compared with datacenter proxies.

**In the full article:** The full Dockerfile and main.py from The Lab repository, the deployment steps with Serverless, the IP check output, and the version of the function that takes the URL as a parameter.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-aws-lambda-serverless?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
