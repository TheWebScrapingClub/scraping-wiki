---
name: Datadome
type: entity
category: anti-bot
first_seen: 2022-09-15
last_updated: 2026-04-22
---

## What it is

Datadome is a bot protection service focused heavily on behavioral analysis. Unlike systems that concentrate on TLS or network-level fingerprinting, Datadome's primary detection surface is what a session does: request sequences, timing, mouse movement patterns, and page transition behavior. It uses a trust score assigned to each visitor, updated continuously throughout the session.

## How it works

Datadome evaluates behavioral signals continuously throughout a session. It does not rely on a single challenge-response gate. Instead, it scores session behavior in real time and can trigger a block or CAPTCHA mid-session if the behavior pattern shifts.

The signals it monitors include request sequencing (what pages are visited in what order), event timing (how quickly a session moves between interactions), and mouse movement trajectories. Datadome's CDP (Chrome DevTools Protocol) detection technique, described publicly by Datadome engineer Antoine, means that headless browser sessions using CDP are identifiable regardless of other fingerprint properties.

Fingerprint coherence is a primary check. According to findings from our Browserforge article, Datadome cross-references multiple fingerprint dimensions to detect inconsistencies. A session where navigator properties, rendering output, and hardware signals do not form a coherent profile is flagged even if each individual signal looks plausible in isolation.

Detection is layered across TLS fingerprinting, IP analysis, HTTP header inspection, and behavioral signals including mouse movements, scrolling patterns, typing speed, and form-filling behavior. AI/ML models process these signals in real time. According to Datadome's own claims, they process 3 trillion data signals per day and evaluate every request in under 2 milliseconds.

The challenge type varies by site configuration. Datadome offers a slider CAPTCHA as the standard challenge for suspicious but salvageable sessions.

Cookie behavior is site-specific. The Datadome session cookie can be reused across requests on some targets (leboncoin.fr), fails on others (Allegro), and works with site-specific conditions on others (Idealista). The reusability window and scope are not publicly documented and must be determined empirically per target.

Detection is also entry-point sensitive. The same scraper may be blocked when accessing a site from a desktop browser context but pass when impersonating a mobile browser, as was observed on Hermes.com in 2022. This suggests Datadome configurations can have different thresholds per client type.

## How to identify it

Datadome sets a distinctive session cookie on the first page load. This is visible in the browser's developer tools. Wappalyzer also detects Datadome in its security category for supported sites.

## TWSC experience

**Hermes.com (2022)**: The earliest documented case. A plain Scrapy spider with default headers was immediately blocked. Impersonating a mobile browser (emulated mobile user agent and headers) bypassed the block and returned a Datadome cookie that could be used for subsequent API calls. The site also required an XSRF token from a `syncform` endpoint, refreshed before each API call. Covered in [scraping-datadome-api-hermes](https://substack.thewebscraping.club/p/scraping-datadome-api-hermes).

**Footlocker.co.uk / footlocker.it (2023)**: Tested in early 2023. Playwright with standard Chrome was blocked. Playwright with Firefox passed without proxies, both locally and on a datacenter VM. Playwright with Brave Browser also passed. The distinction appears related to Chrome leaking automation-identifiable signals that Firefox and Brave do not. Ghost Cursor was added in late 2023 testing alongside residential proxies (UK-located) to handle behavioral detection during multi-page navigation. Covered in [how-to-scrape-datadome-2023](https://substack.thewebscraping.club/p/how-to-scrape-datadome-2023) and [bypassing-datadome-2023-scraping](https://substack.thewebscraping.club/p/bypassing-datadome-2023-scraping).

**Anti-Detect Anti-Bot matrix (2023)**: In a structured test across five anti-bots, Datadome was the hardest to consistently bypass. A first load from any tested tool would often succeed, but a second attempt from the same IP would fail. This illustrates the per-session behavioral scoring in practice. Covered in [anti-detect-anti-bot-matrix](https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix).

**Idealista.com**: Confirmed Datadome deployment. Basic Selenium, Puppeteer, and Playwright out-of-the-box all fail. A commercial proxy API (ScraperAPI) was demonstrated to work. Covered in [scraping-idealista-bypass-datadome](https://substack.thewebscraping.club/p/scraping-idealista-bypass-datadome).

The combination of [Camoufox](camoufox.md) with a residential proxy and human-paced navigation worked on Hermes until October 2024, when it broke. A workaround was subsequently identified and documented.

Ghost Cursor, a Bezier curve plus Fitts's Law mouse movement library, was necessary to navigate Hermes's menu structure without triggering blocks. Programmatic clicks on menu items without realistic cursor trajectories were caught. Covered in [bypass-datadome-mouse-movements-in-playwright](https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright).

Cookie and session reuse was explored in [the-lab-94-using-cookies-and-session](https://substack.thewebscraping.club/p/the-lab-94-using-cookies-and-session). The results across leboncoin.fr, Allegro, and Idealista showed that there is no universal answer: each target requires independent testing to determine whether and how cookies can be reused.

## Known limitations

Hermes.com represents a configuration that is near the edge of what open-source tooling can handle. The October 2024 break demonstrated that Datadome updates can invalidate working setups without notice.

Cookie reuse is unreliable as a general strategy. It works on a subset of targets and requires per-site verification. Assuming cookies are reusable across a Datadome deployment is a common mistake.

CDP-based browser automation is detectable by design. Any tool that relies on CDP without patching its detection surface is at a structural disadvantage against Datadome.

Mouse movement simulation (Ghost Cursor or equivalent) addresses one behavioral signal but not all of them. Sessions that simulate realistic mouse trajectories but have unnatural timing in other dimensions are still catchable.

Chrome leaks automation-identifiable information that Firefox and Brave do not, as consistently observed across multiple testing rounds (2023). Firefox was the most reliable free option for Datadome on Footlocker in early 2023.

Mobile impersonation can bypass stricter Datadome configurations on some targets (confirmed on Hermes.com in 2022), but this is configuration-dependent and not universally applicable.

## Related

- [Camoufox](camoufox.md)
- [Cloudflare](cloudflare.md)
- [PerimeterX](perimeterx.md)
- [Ghost Cursor](ghost-cursor.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [TLS Fingerprinting](../concepts/tls-fingerprinting.md)
- [Cookie and Session Reuse](../concepts/cookie-session-reuse.md)

## Sources

- [https://substack.thewebscraping.club/p/scraping-datadome-camoufox](https://substack.thewebscraping.club/p/scraping-datadome-camoufox)
- [https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright](https://substack.thewebscraping.club/p/bypass-datadome-mouse-movements-in-playwright)
- [https://substack.thewebscraping.club/p/the-lab-94-using-cookies-and-session](https://substack.thewebscraping.club/p/the-lab-94-using-cookies-and-session)
- [https://substack.thewebscraping.club/p/fingerprint-injection-playwright](https://substack.thewebscraping.club/p/fingerprint-injection-playwright)
- [https://substack.thewebscraping.club/p/scraping-datadome-api-hermes](https://substack.thewebscraping.club/p/scraping-datadome-api-hermes)
- [https://substack.thewebscraping.club/p/how-to-scrape-datadome-2023](https://substack.thewebscraping.club/p/how-to-scrape-datadome-2023)
- [https://substack.thewebscraping.club/p/bypassing-datadome-2023-scraping](https://substack.thewebscraping.club/p/bypassing-datadome-2023-scraping)
- [https://substack.thewebscraping.club/p/scraping-idealista-bypass-datadome](https://substack.thewebscraping.club/p/scraping-idealista-bypass-datadome)
- [https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix](https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix)
- [https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges](https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges)
