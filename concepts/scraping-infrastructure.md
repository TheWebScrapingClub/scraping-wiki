---
name: Scraping Infrastructure
type: concept
first_seen: 2022-09-11
last_updated: '2026-06-25'
sources:
- the-costs-of-web-scraping.md
- optimizing-costs-for-web-scraping.md
- scraping-aws-lambda-serverless.md
- running-scrapers-on-github-actions.md
- scheduling-scrapers-airflow.md
- scrapyd-manage-schedule-scrapers.md
- scrapeops-managing-scrapers-execution.md
- scrapoxy-proxy-aggregator.md
- the-true-costs-of-a-web-scraping.md
- https://andrewkchan.dev/posts/crawler.html
- https://browser-use.com/posts/firecracker-browser-infra
- SalzDevs-groxy.md
- agudulin-simple-proxy.md
- free-proxy-list.md
- posts-nix-cache-proxy.md
- denoland-clawpatrol.md
- Vaccarini-Lorenzo-ProductivityProxy.md
- skillful-fox-studio-grey-fox-community.md
- blog-smart-tv-apps-residential-proxy-sdks.md
- 50-of-lg-and-samsung-smart-tv-apps-embed-residential-proxies.md
---

# Scraping Infrastructure

## Definition

Scraping infrastructure encompasses the compute, storage, scheduling, monitoring, and proxy management systems that run scrapers reliably at scale. The choice of infrastructure directly determines cost structure, IP rotation capability, and operational overhead. A scraper that works on a laptop fails at 100,000 requests per day without the right infrastructure beneath it.
 
## How It Works

### Compute Options

The four main compute patterns for scraping workloads, ordered by operational simplicity:

**Serverless (AWS Lambda, GitHub Actions)**: Code runs in ephemeral containers triggered by events or schedules. No server management. AWS Lambda has a maximum 15-minute execution limit per invocation; GitHub Actions has a 6-hour job limit. Both are suitable for narrow-scope scrapers (individual product enrichment, small crawls). AWS Lambda provides a different datacenter IP on each invocation, effectively giving free IP rotation at the cost of using AWS ASN ranges (easily detected and blocked). GitHub Actions runners also use datacenter IPs.

**Containers (ECS, Fargate)**: Better resource utilization than VMs for bursty workloads. Fargate costs approximately 2x AWS Lambda for sustained load but removes the execution time constraint. Standard scraping containers: ~2 vCPU + 4GB RAM for HTTP scrapers, more for browser automation.

**Virtual Machines**: Fixed hourly cost regardless of utilization. Correct choice for sustained, predictable workloads where idle time is minimal. Hetzner (bare metal or VMs) is documented as substantially cheaper than AWS/Azure/GCP for compute-heavy sustained jobs, with unlimited bandwidth included in some configurations.

**Bare Metal**: Best cost-per-compute ratio for very high-throughput scenarios. Hetzner dedicated servers are the documented example in TWSC articles.

Cost guidance (September 2022): AWS and Azure beat GCP on micro-sized and medium-sized VM configurations. Google is the most expensive of the three for the scraping-relevant instance sizes. For 10,000 hours of a basic scraping VM, the cost difference between providers is meaningful.

Cost guidance (March 2025): Lambda is good for sporadic invocations. Above sustained load, Fargate becomes cheaper. VMs win for always-on workloads. Bare metal wins for bandwidth-intensive high-concurrency jobs.

### Storage

Scraped data storage costs compound quickly. A site with 500,000 pages at 200KB each, scraped daily and retained for 30 days, generates approximately 750GB/month in compressed HTML storage — roughly $18/month on commodity object storage. For larger datasets or longer retention, storage becomes a meaningful line item in the cost model.

### Scheduling

Four approaches to scheduling scraper executions:

**Cron / OS task scheduler**: Simplest. All executions share the same IP. Works for protected-less targets on a single server. Does not scale to hundreds of scrapers without a database-backed scheduling layer.

**Scrapyd**: Python application (port 6800) that accepts Scrapy spider deployments via `scrapyd-deploy` and exposes an API for scheduling executions. Web interface is basic and becomes cluttered at scale. Executes spiders from a central server, so all runs share that server's IP. Scrapeops provides an improved UI and scheduling layer on top of Scrapyd for teams needing multi-server management.

**GitHub Actions**: CI/CD platform integrated into GitHub. Free for public repositories; 2,000 free minutes/month for private. YAML-based workflow definition in `.github/workflows/`. Ephemeral runners are datacenter VMs. Suitable for smaller scrapers scheduled via cron syntax. Workaround for 6-hour limit: parameterize the scraper so each workflow run handles one segment (country, category) rather than a full crawl. Inputs passed via `workflow_dispatch` inputs block.

**Apache Airflow**: DAG-based workflow orchestrator. Handles dependencies between tasks, retries with backoff, failure notifications, and multi-step pipelines (scrape → transform → upload to S3). Better fit than cron for multi-stage pipelines. More operational overhead than GitHub Actions. Used when scraping is one step in a larger data engineering workflow.

### Fleet Monitoring

Scrapeops provides a dashboard for Scrapy and `requests`-based scrapers. Integration requires `scrapeops-scrapy` or `scrapeops-python-requests` package plus an API key in the scraper settings. As of the tested version (2023), only Scrapy and requests are supported; Playwright/Selenium/Puppeteer scrapers are not integrated. The monitoring also includes a proxy aggregator API that unifies multiple proxy providers behind a single endpoint.

Scrapy Cloud by Zyte is the other major hosted scheduling and monitoring option for Scrapy-specific projects.

### Proxy Infrastructure

Scrapoxy is an open-source proxy aggregator that presents a unified endpoint across multiple proxy providers and cloud VM instances. It separates the proxy configuration into three project types: datacenter (AWS/GCP/Azure spot VMs), residential, and mobile. The Scrapy integration uses `DOWNLOADER_MIDDLEWARES`. See [Scrapoxy](../entities/scrapoxy.md) for details.

## Where It Matters

Infrastructure choices affect both cost and detection surface. Serverless functions run from datacenter IPs, which limits their use to targets without IP-type filtering. VMs with static IPs require proxy rotation for any protected target. Scraping at scale also requires explicit handling of data persistence: ephemeral runners (Lambda, GitHub Actions) cannot store data locally across invocations without writing to external storage (S3, database) within the function.

## What We Tested

### AWS Lambda Selenium Scraper

A Selenium-based Lambda function was deployed using the `docker-selenium-lambda` template. Each invocation received a fresh AWS EU Central-1 datacenter IP. IP changes between invocations, providing free rotation within the Amazon ASN. The function accepted URL and product code as input parameters and returned scraped product description. Redeploy via `sls deploy` after code changes. Confirmed working for Clarks.com French product pages.

### GitHub Actions Scrapy Integration

A Scrapy spider was scheduled via YAML workflow on GitHub Actions. The workflow: checkout code → install dependencies → run spider → commit output to repository. For a multi-country luxury e-commerce target (Ounass.ae), the 6-hour limit required splitting executions by country/category via `workflow_dispatch` inputs. The `gh` CLI can trigger parameterized workflow runs programmatically.

### Airflow DAG for Scrapy

A two-DAG pipeline: the first DAG runs a Scrapy spider via subprocess and saves output CSV; the second DAG uploads the file to an S3 bucket. The first DAG triggers the second via `TriggerDagRunOperator`. This pattern separates scraping from data movement and makes each step independently retryable. Airflow retries failed tasks 3 times with 5-minute intervals before sending email failure notifications.

### Cost Comparison: AWS vs. Hetzner + Proxies

From the Scrapoxy article: 90 Scrapy spiders + 10 Playwright browsers on AWS ≈ $400/month. Equivalent workload on Hetzner + residential proxy allocation ≈ $289 Hetzner + $46 proxies = ~$335/month. Approximately 20% savings by moving to cheaper compute and treating proxy costs separately.

### True Cost of a Scraping Project

A cost framework documented in TWSC: one-time costs (scraper development, infrastructure setup) vs. recurring costs (hosting, proxies, monitoring, maintenance). Scraper maintenance for a stable target: approximately 2 hours per month per scraper. For three scenarios (small site: 10K pages; medium: 100K pages; large: 1M+ pages), the recurring cost is dominated by proxy spend rather than compute.

### Billion-Page Crawl Benchmark (2025)

A documented single-person crawl of 1.005 billion web pages provides a concrete cost-per-page baseline for large-scale HTTP-only infrastructure. Total cost: $462 over 25.5 hours. That translates to roughly $0.46 per million pages at sustained throughput.

Architecture: a cluster of approximately 12 independent nodes, each node running all crawler functions (fetcher, parser, scheduler). Per-domain URL frontiers managed via Redis. HTML only, no JavaScript rendering. Politeness enforced at 70-second minimum delay per domain, with robots.txt compliance.

Key operational findings: parsing was the primary bottleneck, not network I/O. NVMe SSDs were critical for the Redis frontier operations. Using independent nodes (no shared state coordinator) rather than a centralized architecture eliminated a coordination bottleneck that would have become the limiting factor at scale.

The benchmark confirms that commodity cloud compute at this scale costs less than most proxy budgets for the same request volume. The infrastructure cost itself is not the binding constraint for large crawls; bandwidth, politeness throttling, and parsing throughput are.

Source: andrewkchan.dev/posts/crawler.html

### Cloud Browser Infrastructure (microVM-per-session)

Managed cloud-browser providers face a different infrastructure problem than HTTP crawlers: each browser session needs to start fast, stay isolated from other sessions (shared cookies, cache, or logged-in state across tenants is a security failure), and be cheap enough to create and discard thousands at a time. [Browser Use](../entities/browser-use.md) documented one production approach in June 2026: one Firecracker microVM per browser session, resumed from a snapshot, running on regular EC2 rather than `.metal` bare metal. Running Firecracker on regular EC2 means nested virtualization (a VM inside AWS's own VM), which they accept because regular EC2 provisions faster and costs less, trading latency on host-assisted operations like page faults.

Concrete figures from that build: $0.02 per browser hour, VM cold start under 400ms, end-to-end create latency 825ms p50 / 1.35s p99 over a 10,000-session test. The optimizations that mattered under nesting were 2MB memory pages plus a `userfaultfd` handler preloading hot pages (resume-to-ready 9.8s → 3.1s, page faults ~91x fewer), two-phase vCPU pinning (unpinned during Chromium's launch burst, pinned to stable cores after ready), and giving each browser both sibling hyperthreads to avoid core contention. The takeaway for anyone sizing browser infrastructure: browsers are quiet after startup, so many pack onto one host, but the launch burst is the hard part to schedule. See [Browser Use](../entities/browser-use.md) for the full breakdown.

## Current State

As of 2025, the infrastructure decision tree is: sporadic invocation → Lambda/GitHub Actions; sustained medium volume → containers (Fargate/ECS); sustained high volume → VMs or bare metal; multi-step pipeline → Airflow or equivalent orchestrator. Hetzner is the documented cost leader for EU-region compute. AWS Lambda provides free IP rotation but from detectable ASN ranges.

## Related

- [proxy-fundamentals](./proxy-fundamentals.md)
- [hybrid-scraping](./hybrid-scraping.md)
- [Scrapoxy](../entities/scrapoxy.md)
- [Playwright](../entities/playwright.md)
- [Camoufox](../entities/camoufox.md)
- [browser-use](../entities/browser-use.md)

## Sources

- [https://substack.thewebscraping.club/p/the-costs-of-web-scraping](https://substack.thewebscraping.club/p/the-costs-of-web-scraping)
- [https://substack.thewebscraping.club/p/optimizing-costs-for-web-scraping](https://substack.thewebscraping.club/p/optimizing-costs-for-web-scraping)
- [https://substack.thewebscraping.club/p/scraping-aws-lambda-serverless](https://substack.thewebscraping.club/p/scraping-aws-lambda-serverless)
- [https://substack.thewebscraping.club/p/running-scrapers-on-github-actions](https://substack.thewebscraping.club/p/running-scrapers-on-github-actions)
- [https://substack.thewebscraping.club/p/scheduling-scrapers-airflow](https://substack.thewebscraping.club/p/scheduling-scrapers-airflow)
- [https://substack.thewebscraping.club/p/scrapyd-manage-schedule-scrapers](https://substack.thewebscraping.club/p/scrapyd-manage-schedule-scrapers)
- [https://substack.thewebscraping.club/p/scrapeops-managing-scrapers-execution](https://substack.thewebscraping.club/p/scrapeops-managing-scrapers-execution)
- [https://substack.thewebscraping.club/p/scrapoxy-proxy-aggregator](https://substack.thewebscraping.club/p/scrapoxy-proxy-aggregator)
- [https://substack.thewebscraping.club/p/the-true-costs-of-a-web-scraping](https://substack.thewebscraping.club/p/the-true-costs-of-a-web-scraping)
- [https://andrewkchan.dev/posts/crawler.html](https://andrewkchan.dev/posts/crawler.html)
