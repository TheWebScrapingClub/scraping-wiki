---
type: article_summary
title: How to Use LLMs to Enhance Data Extraction From Unstructured Text
slug: how-to-use-llms-data-extraction-unstructured-text
canonical_url: https://www.scraping.club/p/how-to-use-llms-data-extraction-unstructured-text
publish_date: '2026-05-10'
visibility: free
topics:
- nlp-ml
- proxy-industry
description: Turning scraped unstructured text into typed, validated data, with an LLM for meaning and Pydantic with Instructor for structure.
source_hash: 2dbf49fb93309b38
---

# How to Use LLMs to Enhance Data Extraction From Unstructured Text

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-05-10 (free to read). **[Read the full article](https://www.scraping.club/p/how-to-use-llms-data-extraction-unstructured-text?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Scraping the page is only half of the job. From a news site you get a wall of text, with teasers, sponsored lines and comments wrapped around the one fact you need. A newsletter writes "just under two percent" when your column expects 1.8. Job postings give you salary ranges, "competitive compensation" or euros, and "hybrid" means something different at every company. You cannot query, aggregate or load that into a database without preprocessing.

We went through how classical NLP (spaCy, Stanford NLP, NLTK) tried to solve this and where it stops, then through LLMs as extractors and the problems they bring when used alone. The setup I propose splits the work: the LLM reads and normalizes the text, while schema libraries enforce types and reject malformed output. We compare a direct GPT-4o call with a schema-enforced one, using Pydantic and Instructor, on the same news article.

## What's inside

- Three scraping targets show what unstructured text costs you: news with signals buried in noise, financial newsletters with vague wording, and job postings with ambiguous seniority, pay and work arrangements.
- Classical NLP (NER, part-of-speech tagging, dependency parsing, relation extraction) was a real step up from regex, but it breaks on domain shift and needs extra layers to resolve context.
- LLMs used alone have three failure modes: no guaranteed output format, required fields that go missing or get invented, and hallucination. Together they make a 10,000-article pipeline hard to trust.
- The comparison inspects the type of every extracted field, so you can check what a plain prompt returns against what a defined schema enforces.

**In the full article:** Code for the direct GPT-4o call and for the Pydantic and Instructor version, the sample Fed article, the outputs of both runs, and the diagram of the two-step architecture.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/how-to-use-llms-data-extraction-unstructured-text?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
