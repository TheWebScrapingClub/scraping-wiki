---
name: Kasada
type: entity
category: anti-bot
first_seen: 2022-08-05
last_updated: 2026-04-22
sources:
  - bypassing-kasada-2025-open-source.md
  - undetected-chromedriver-cloudflare-datadome.md
  - scraping-a-kasada-website.md
  - scraping-kasada-protected-websites.md
  - bypassing-kasada-web-scraping.md
  - how-to-by-pass-kasada-bot-mitigation.md
  - octo-browser-bypass-kasada.md
  - anti-detect-anti-bot-matrix.md
  - the-lab-21-bypass-anti-bot-challenges.md
---

## What it is

Kasada is an Australian anti-bot company. Its product uses a zero-trust security philosophy: every request is assumed to be a bot until proven otherwise. It is deployed by a small number of high-profile targets including canadagoose.com (the primary TWSC test target), Twitch, and hyatt.com.

## How it works

Kasada's detection signature at the network level is a distinctive 429 response on the initial request, followed by a correct page load once the client has satisfied the challenge. A blank screen in the browser is a common blocking indicator during this exchange. This is called the "first request detection" approach: automated threats are blocked before reaching the website's infrastructure.

The challenge mechanism is invisible to humans. Kasada runs JavaScript in the browser that collects hundreds of data points, applies them to its detection model, and redirects the request if the client passes. The JavaScript itself is obfuscated using Kasada's own proprietary interpretive language and changes dynamically ("polymorphic obfuscation"), making reverse engineering a moving target.

Kasada generates three tokens used in request authentication: `x-kpsdk-ct`, `x-kpsdk-r`, and `x-kpsdk-c`. These can be reverse-engineered to construct valid requests without a full browser, but the approach is brittle: the token generation logic changes frequently, and any reverse-engineered implementation has a short useful lifespan.

The central detection mechanism is hardware fingerprinting. Kasada collects signals tied to the actual hardware executing the JavaScript, not just browser environment properties. This is why residential proxies alone are insufficient when running from datacenter infrastructure: the IP reputation passes, but the hardware fingerprint of the datacenter machine does not match the claimed client.

Unlike Datadome or PerimeterX, Kasada does not use visible CAPTCHAs. The challenge is always silent.

## How to identify it

Kasada is not detectable via Wappalyzer. The identifying signal is a 429 response on the very first request to the protected domain. The response header from that 429 contains indicators tied to the Kasada platform. After the challenge is solved, the page reloads normally.

## TWSC experience

**2022 (canadagoose.com)**: The first encounter. Playwright with the stealth plugin and a standard Chrome setup produced only a blank page regardless of configuration. A misconfiguration in the robots.txt that allowed Screaming Frog (a headless Chromium-based desktop SEO crawler) provided an alternative entry: changing the User-Agent to match Screaming Frog bypassed the protection. This was a configuration error by the site, not a general Kasada bypass. Covered in [scraping-a-kasada-website](https://substack.thewebscraping.club/p/scraping-a-kasada-website).

**2023 (canadagoose.com, anti-detect matrix)**: Multiple approaches tested. Playwright with Chrome using `ignore_default_args=["--enable-automation"]` and `--disable-blink-features=AutomationControlled` succeeded on the homepage from a local machine, but failed on a datacenter VM even with residential proxies. Playwright with Firefox also worked locally. Undetected-chromedriver worked locally but not from a datacenter with authenticated proxies (UC does not support proxy authentication). The Bright Data Scraping Browser was the reliable commercial solution that bypassed Kasada on canadagoose.com from a server environment. In the broader anti-detect matrix, Kasada was among the harder systems to pass. Covered in [scraping-kasada-protected-websites](https://substack.thewebscraping.club/p/scraping-kasada-protected-websites), [how-to-by-pass-kasada-bot-mitigation](https://substack.thewebscraping.club/p/how-to-by-pass-kasada-bot-mitigation), [bypassing-kasada-web-scraping](https://substack.thewebscraping.club/p/bypassing-kasada-web-scraping), [anti-detect-anti-bot-matrix](https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix).

**2024 (canadagoose.com)**: Undetected-chromedriver and Playwright with Brave Browser both worked locally but failed from a datacenter with residential proxies. Commercial solution (Bright Data Scraping Browser) confirmed working from server. The hardware fingerprint gap between a local machine and a datacenter VM was identified as the blocking factor. Covered in [bypassing-kasada-web-scraping](https://substack.thewebscraping.club/p/bypassing-kasada-web-scraping).

**2024 (hyatt.com)**: Kasada deployment on Hyatt. Standard Chrome and Playwright both blocked. Octo Browser (a commercial anti-detect browser with kernel-level fingerprint spoofing) successfully bypassed the protection. This is the only known successful open-source-adjacent solution documented for hyatt.com at the time. Covered in [octo-browser-bypass-kasada](https://substack.thewebscraping.club/p/octo-browser-bypass-kasada).

**By 2025 (canadagoose.com)**: The picture changed significantly. [Camoufox](camoufox.md), Patchright, and Zendriver all successfully bypassed Kasada on canadagoose.com when combined with a residential proxy. Standard Playwright, including a Brave-based configuration, failed even with a residential proxy. The distinguishing factor is the browser-level fingerprint quality these patched browsers provide versus standard Playwright's detectable automation surface. Covered in [bypassing-kasada-2025-open-source](https://substack.thewebscraping.club/p/bypassing-kasada-2025-open-source).

## Known limitations

Token reverse-engineering (`x-kpsdk-ct`, `x-kpsdk-r`, `x-kpsdk-c`) is technically possible but not a durable strategy. Kasada updates the token generation logic regularly, and any implementation built around a specific version will break without notice. Kasada explicitly advertises this as a design goal.

Standard Playwright fails on Kasada even with Brave. The automation detection surface that Kasada targets is not addressed by switching to a different Chromium binary alone; it requires a patched browser or one with a fundamentally different fingerprint surface.

Hardware fingerprinting means datacenter infrastructure carries a persistent disadvantage. Even with perfect browser and IP configuration, the underlying hardware signals from a cloud provider VM may be detectable. This was the consistent failure mode across multiple testing years.

Undetected-chromedriver does not support proxies with authentication, which limits its usefulness in server environments where whitelisted IPs cannot be guaranteed.

The 429-then-correct-page behavior makes automated detection of Kasada deployments straightforward, but it also means the challenge exchange is visible and potentially inspectable during testing.

SEO impact is a documented side effect of aggressive Kasada deployment. Bing and Baidu indexing of the canadagoose.com website showed degradation consistent with blocking search engine crawlers. This is a legitimate concern for sites using Kasada site-wide on public pages. Covered in [scraping-a-kasada-website](https://substack.thewebscraping.club/p/scraping-a-kasada-website).

## Related

- [Camoufox](camoufox.md)
- [PerimeterX](perimeterx.md)
- [Cloudflare](cloudflare.md)
- [Undetected-chromedriver](undetected-chromedriver.md)
- [Browser Fingerprinting](../concepts/browser-fingerprinting.md)
- [TLS Fingerprinting](../concepts/tls-fingerprinting.md)

## Sources

- [https://substack.thewebscraping.club/p/bypassing-kasada-2025-open-source](https://substack.thewebscraping.club/p/bypassing-kasada-2025-open-source)
- [https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome](https://substack.thewebscraping.club/p/undetected-chromedriver-cloudflare-datadome)
- [https://substack.thewebscraping.club/p/scraping-a-kasada-website](https://substack.thewebscraping.club/p/scraping-a-kasada-website)
- [https://substack.thewebscraping.club/p/scraping-kasada-protected-websites](https://substack.thewebscraping.club/p/scraping-kasada-protected-websites)
- [https://substack.thewebscraping.club/p/bypassing-kasada-web-scraping](https://substack.thewebscraping.club/p/bypassing-kasada-web-scraping)
- [https://substack.thewebscraping.club/p/how-to-by-pass-kasada-bot-mitigation](https://substack.thewebscraping.club/p/how-to-by-pass-kasada-bot-mitigation)
- [https://substack.thewebscraping.club/p/octo-browser-bypass-kasada](https://substack.thewebscraping.club/p/octo-browser-bypass-kasada)
- [https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix](https://substack.thewebscraping.club/p/anti-detect-anti-bot-matrix)
- [https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges](https://substack.thewebscraping.club/p/the-lab-21-bypass-anti-bot-challenges)
