---
name: Scrapoxy
type: entity
category: tool
first_seen: 2024-02-15
last_updated: 2026-04-22
---

# Scrapoxy

## What It Is

Scrapoxy is an open-source proxy aggregator that unifies multiple proxy providers and cloud VM instances behind a single endpoint. A Scrapy spider (or any HTTP client) connects to Scrapoxy as if it were a single proxy, and Scrapoxy distributes requests across the configured backends. This separates proxy management from scraper code and allows the scraping team to switch or combine providers without touching spider logic.

## How It Works

Scrapoxy is configured through a project-based structure. Each project holds one or more proxy pool definitions, organized into three categories:

- **Datacenter**: Cloud VM instances (AWS, GCP, Azure) created on demand and used as egress nodes. Scrapoxy can spin up spot instances, use them as proxies, and terminate them after use. This produces datacenter IPs that rotate as VMs are replaced.
- **Residential**: Connections to residential proxy providers via their APIs. Scrapoxy normalizes the provider API into its own unified interface.
- **Mobile**: Connections to mobile proxy providers.

The Scrapy integration uses `DOWNLOADER_MIDDLEWARES`. Requests pass through Scrapoxy's local endpoint; Scrapoxy selects a backend, forwards the request, and returns the response.

## TWSC Experience

Tested in Lab #premium article (February 2024) as a cost-optimization tool for a mixed Scrapy + Playwright fleet.

Cost comparison documented: 90 Scrapy spiders + 10 Playwright browsers on AWS ≈ $400/month. Same workload on Hetzner + Scrapoxy managing a residential proxy allocation ≈ $289 Hetzner + $46 proxies = ~$335/month. The 20% cost saving comes from moving compute to cheaper bare metal and letting Scrapoxy handle proxy rotation across providers.

Scrapoxy's datacenter pool capability — using cloud VMs as proxy nodes — produces IPs that rotate as instances cycle, at a cost significantly below commercial datacenter proxy providers. This works only for targets that do not filter by datacenter ASN.

## Known Limitations

- Datacenter VMs from AWS, GCP, or Azure still originate from cloud ASNs, which are blacklisted by most anti-bot systems.
- Scrapoxy adds a proxy layer between scraper and target, which increases latency per request.
- Setup complexity is higher than using a single proxy provider directly. The benefit is operational only if the team manages multiple providers or wants to reduce per-GB proxy costs with cloud VM egress.

## Related

- [proxy-fundamentals](../concepts/proxy-fundamentals.md)
- [scraping-infrastructure](../concepts/scraping-infrastructure.md)
- [hybrid-scraping](../concepts/hybrid-scraping.md)

## Sources

- [https://substack.thewebscraping.club/p/scrapoxy-proxy-aggregator](https://substack.thewebscraping.club/p/scrapoxy-proxy-aggregator)
