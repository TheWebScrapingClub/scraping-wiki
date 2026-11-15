---
type: article_summary
title: 'THE LAB #8: Using Bezier curves for human-like mouse movements'
slug: bezier-curves-web-scraping
canonical_url: https://www.scraping.club/p/bezier-curves-web-scraping
publish_date: '2022-12-09'
visibility: premium
topics:
- human-behavior-emulation
- browser-automation
description: Cubic Bezier curves as a replacement for Playwright's straight-line mouse movement, to look more human to behavior-tracking anti-bot systems.
source_hash: 1ebfad10679cc54b
---

# THE LAB #8: Using Bezier curves for human-like mouse movements

> Summary of an article published on [The Web Scraping Club](https://www.scraping.club/?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary) on 2022-12-09 (for paid subscribers). **[Read the full article](https://www.scraping.club/p/bezier-curves-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)**

Playwright's native move function takes the mouse from A to B in a straight line. Against anti-bot solutions that track user behavior to detect anomalies, that is a weak spot. Reproducing a more human-like movement should trigger fewer red flags, and a curved trajectory is how we get there.

In this episode of THE LAB we build that trajectory with a Bezier curve. I start with what a Bezier curve is and where it comes from, then why it suits mouse movement. We then implement a cubic curve, which needs four control points. I pick the control points, set the density of the interpolation with NumPy, and work through the cubic formula to get the X and Y coordinates of each point on the curve. There is some math along the way, and I warn you before it starts.

## What's inside

- How the interpolation ratio R sets the number of points between the start and the end of the curve.
- How the second and third control points bend the curve, so it is more angled in the first half and smoother in the second.
- A worked calculation of the first point of the curve, for both X and Y.
- Why I want many points on the curve: I want to see it drawn on the monitor.

**In the full article:** The control points and NumPy setup, the formulas for each type of Bezier curve, the worked X and Y calculation and the full set of points that makes up the curve.

[Read the full article on The Web Scraping Club](https://www.scraping.club/p/bezier-curves-web-scraping?utm_source=wiki&utm_medium=referral&utm_campaign=article_summary)
