---
name: Smartproxy Site Unblocker
type: entity
category: tool
first_seen: 2023-07-13
last_updated: 2026-04-22
---

# Smartproxy Site Unblocker

## What It Is

Smartproxy Site Unblocker is the managed anti-bot bypass API offered by Smartproxy. It operates similarly to other unblocker products: the caller sends a target URL, Smartproxy handles bypass and rendering, and returns page content. Price at time of TWSC testing: $12/GB.

## How It Works

Requests are sent to the Smartproxy endpoint formatted as proxy URLs. JavaScript rendering is available. The $12/GB price is lower than Oxylabs ($15/GB) and Zyte, positioning it as the cost-competitive option in the unblocker market.

## TWSC Experience

Tested in Hands-On #4 (July 2023):

- **Score: 80/100** overall.
- 100% success on Cloudflare, DataDome, and PerimeterX.
- Mixed results on F5 (partial pass).
- **0% success on Kasada** — consistent with other providers' difficulty on Kasada in the 2023 testing period.

In the March 2024 multi-provider benchmark:
- Passed Cloudflare (Harrods.com).
- Passed Kasada (Canada Goose) — this is an improvement from the 2023 result. Kasada bypass appears to have been added or improved between 2023 and 2024.

In the June 2024 Kasada-specific benchmark (101 URLs on canadagoose.com):
- **92/100 success rate** — lowest of the passing providers in that test.
- Completed in 413 seconds.
- Cost: $0.13 EUR for 101 URLs.

The improvement from 0% Kasada success in July 2023 to 92% in June 2024 is significant. Previously (2023-07): 0% on Kasada. As of 2024-06: 92% on Kasada.

## Known Limitations

- Overall benchmark score of 80/100 is lower than Oxylabs (96/100) and Zyte (100/100 with rendering).
- Kasada success rate of 92% in June 2024 is the lowest among passing providers (vs. Oxylabs 96%, Bright Data 96%, NetNut 97%).
- F5 performance remains mixed in 2023 testing; no updated F5 data in 2024 benchmarks.

## Related

- [web-unblockers](../concepts/web-unblockers.md)
- [Cloudflare](./cloudflare.md)
- [Kasada](./kasada.md)
- [DataDome](./datadome.md)
- [Zyte API](./zyte-api.md)
- [Oxylabs Unblocker](./oxylabs-unblocker.md)

## Sources

- [https://substack.thewebscraping.club/p/testing-smartproxy-site-unblocker](https://substack.thewebscraping.club/p/testing-smartproxy-site-unblocker)
- [https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024](https://substack.thewebscraping.club/p/web-unblocker-benchmark-march-2024)
- [https://substack.thewebscraping.club/p/web-unblocker-test-kasada](https://substack.thewebscraping.club/p/web-unblocker-test-kasada)
- [https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark](https://substack.thewebscraping.club/p/the-web-unblocker-cost-benchmark)
