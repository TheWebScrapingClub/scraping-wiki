---
type: article_summary
title: 'The LAB #117: Scraping club data and results from Fussball.de'
slug: scraping-club-data-fussball-de
canonical_url: https://www.scraping.club/p/scraping-club-data-fussball-de
publish_date: '2026-10-22'
visibility: premium
topics:
- proxies
- antibot
- captcha
- browser-automation
description: Scraping the fussball.de club directory, plus how to decode the custom web font that hides match dates and scores on the German football portal.
source_hash: d1c10dcedacca808
---

# The LAB #117: Scraping club data and results from Fussball.de

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2026-10-22 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/scraping-club-data-fussball-de?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Google Search Console showed hundreds of searches for how to scrape club data from fussball.de, the DFB portal covering German amateur football from the Bundesliga down to the last Kreisliga team. With that much demand I expected a hard target. The club directory isn't one: I found no anti-bot, and the data comes as plain HTML from endpoints anyone can call. The real obstacle is on fixtures, where dates, kick-off times, scores and referee names sit behind a custom web font. The HTML contains characters that mean nothing until the browser draws them.

We split the work in two parts. First we map how the site is built, from the Varnish cache and Azure Front Door to the AngularJS front end, and scrape the club directory from search to profiles. Then we move to the results and decode the font, first the easy way, then in a way that keeps working if the site removes the shortcut we use today.

## What's inside

- How the site's own search form turns fields into path segments, and why the query string version is not the one to rely on.
- Where the "Mehr laden" button points and which parameters control page size and offset.
- How the postal code search matches, and what that means for covering every club without an "all clubs" query.
- Caveats on the profile data: clubs registered in two regional associations, and pages that answer 200 without a profile.

**In the full article:** The code for the club scraper, the request rates and coverage figures from the full run, and the font decoding in both versions.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/scraping-club-data-fussball-de?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
