---
name: proxy-fundamentals
type: concept
first_seen: 2022-09-11
last_updated: '2026-06-06'
sources:
- everything-about-proxies.md
- choosing-proxy-provider-scraping.md
- five-secrets-of-the-proxy-industry.md
- the-unit-economics-of-proxy-providers.md
- differences-residential-mobile-proxies.md
- evaluating-proxy-providers-ips.md
- how-many-ip-needed-scraping.md
- costs-web-scraping-proxy.md
- optimizing-proxy-costs.md
- proxy-pricing-playbook-september.md
- where-do-proxy-companies-take-ip.md
- x-forwarded-for-header-proxies.md
- reverse-proxies-and-webscraping.md
- managing-proxy-bans-proxy-retries.md
- bypassing-geo-fencing-scraping.md
- scraping-using-tor.md
- optimizing-costs-for-web-scraping.md
- https://harshanu.space/en/tech/dumb-vibe-coders
- https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa
- https://voidmob.com/blog/dns-leak-proxy-killer-carrier-native-dns
- https://voidmob.com/blog/free-vpns-proxies-sell-your-device
- blog-free-vpns-proxies-sell-your-device.md
- blog-how-i-broke-the-anti-bot-behind-nike-kick-and-twitch.md
- clashmac-app.md
- getwick-dev.md
- gh-v6-com.md
- kampala.md
- meshscrape-com.md
- p-use-ipv6-scraping-nyxproxy.md
- posts-what-does-a-vpn-protect-you-from.md
- python-web-scraping-with-scrapingduck.md
- spinov001-art-awesome-web-scraping-2026.md
- dbi-aio-http-library.md
- dbi-common-questions-proxies.md
- dbi-inside-ipidea-residential-proxy-network.md
- dbi-python-requests-library.md
- dbi-authenticate-google-read-aloud.md
- dbi-proxy-db-benchmark-firehol-may-2025.md
- githubv6-com.md
- TimoKats-roxy.md
- apernet-hysteria.md
- michidk-hodor.md
- www-llmcap-io.md
- blacknon-childflow.md
- blog-look-ma-no-proxy.md
- blog-proxy-pool-size-stopped-mattering.md
- news-building-a-peer-to-edge-peer-reverse-proxy.md
- marvinli001-ClashMax.md
- r-RedditEng-comments-1ttwqaj-fromproxytoproxylessremovingenvoyfrom.md
- vnc2go-odinglynn-com.md
---

# Proxy Fundamentals

## Definition

Proxies route outbound HTTP requests through an intermediate IP address, changing the apparent origin of the request. In a scraping context, the proxy's IP reputation, ASN, and network type are often more consequential than any browser-level signal.

## How It Works

There are four proxy types with meaningfully different characteristics.

Datacenter proxies are hosted in cloud infrastructure. They are fast and cheap, but their ASNs (Autonomous System Numbers) are well-known to anti-bot systems. Amazon, Google, and similar ASNs are blacklisted on many targets by default.

ISP proxies use residential IP ranges assigned by real ISPs, but the servers hosting them are in datacenters. They look residential to an IP reputation lookup but are physically co-located with datacenter infrastructure. The categorization is genuinely ambiguous and varies by lookup service.

Residential proxies route through real end-user devices on real ISP connections. The IP addresses are indistinguishable from organic traffic at the network level. The tradeoff is higher latency, lower bandwidth predictability, and significantly higher cost. On Scamalytics, residential proxies score "very risky" because of their high abuse history.

Mobile proxies route through devices on cellular networks. The defining characteristic is CGNAT (Carrier-Grade NAT): multiple physical devices share a single public IP address. Blocking a mobile proxy IP risks blocking thousands of legitimate users sharing the same CGNAT pool, which makes anti-bot systems reluctant to hard-block mobile IPs. This is a structural advantage that has nothing to do with any technical sophistication on the scraper's part. Mobile IPs also score comparatively low on fraud risk tools (Scamalytics labels them "low" in TWSC testing), which is counterintuitive given their use in scraping.

IP reputation is maintained by blacklist services that track abuse history, and by ASN-level classification that reveals the network type. Subnet-level blocking is common: Amazon and Google have been documented blocking entire /24 subnets (256 addresses) when a single IP in the range is abused.

### Forward vs. Reverse Proxies

A forward proxy sits in front of the client and routes outbound traffic on its behalf. This is what proxy providers sell to scrapers. A reverse proxy sits in front of the server and intercepts incoming traffic. Cloudflare, Fastly, and other CDNs operate as reverse proxies in front of target websites, which is why anti-bot enforcement happens at the reverse proxy layer before a request ever reaches the origin server.

### The X-Forwarded-For Header

Transparent proxies forward the client's real IP via the `X-Forwarded-For` header. A server receiving a request through a transparent proxy can see both the proxy IP and the client's actual IP. Elite (high-anonymity) proxies strip this header and do not disclose the originating IP. Targets that inspect `X-Forwarded-For` can detect transparent proxy use regardless of the proxy's own IP reputation. Test with httpbin.io/anything to see what a proxy actually forwards.

## Where It Matters

The proxy type determines what IP-level signals an anti-bot system sees before any JavaScript or TLS analysis begins. A perfect browser fingerprint sent from a datacenter IP is still a datacenter request. For targets that use IP reputation as a first filter, the proxy type is the highest-leverage variable in the stack.

Residential IP pools rotate significantly — 50 to 70% of IPs change daily due to natural ISP reassignment. This is not a feature of the proxy provider; it is a consequence of how DHCP works in residential networks. Claims of "exclusive IPs" from residential providers are almost universally marketing language, because the provider cannot control what IP a user's router receives from their ISP.

### Geo-targeting and Geo-blocking

Many e-commerce sites serve different prices, inventory, or content based on IP geolocation. Some sites block access from certain regions. The EU Geo-blocking Regulation (2018/302) restricts geo-blocking within the EU for most product categories, but international restrictions remain common. Scraping geo-restricted content typically requires proxies in the target region. Datacenter proxies from cloud providers (via spot instances) are the cheapest way to get specific regional IPs for non-bot-protected targets.

## What We Tested

### IP Pool Quality

Testing 50 requests per provider to US and France destinations revealed significant quality variance. One provider sold datacenter IPs from ipxo.com ranges while marketing them as residential. ASN lookup confirmed the IPs belonged to datacenter infrastructure despite residential pricing. IP type, ASN, and reputation can be checked systematically before committing to a provider.

### Proxy Costs (September 2024)

- Datacenter: ~$0.6/GB (plateaued, commodity pricing)
- Residential: ~$6-8/GB
- ISP: ~$14-15/GB or $0.5-5/IP
- Mobile: ~$8/GB (down from ~$40/GB historically)
- Unblocker services: ~$14/GB or ~$3/1,000 requests

Pay-per-GB billing suits API scraping where response sizes are small and predictable. Pay-per-request suits HTML scraping where page sizes vary. Unblockers bundle in their own bandwidth-intensive rendering costs, making per-request pricing more transparent.

### Proxy Cost Mismanagement

A documented disaster on Stone Island using the Nimble web unblocker: third-party resources (fonts, images, tracking scripts) loaded through the proxy consumed 5x more bandwidth than the target content itself. Lessons: create separate proxy credentials per target site, block non-target domains in Playwright routing (`page.route()`), and set bandwidth usage thresholds with alerts.

### Unit Economics

From a Proxidize analysis: $0.20 bandwidth cost + $0.50 customer acquisition cost + $0.25 infrastructure cost = $0.95 per GB, against a typical $1/GB sale price. The margin at the commodity end of the market is approximately 5%, which explains the industry structure and the pressure toward rebundling and reselling.

Regional pricing differences are substantial: customers in Asian markets pay roughly half of what US and EU customers pay for the same service.

### IP Volume vs. IP Quality

The volume of IPs advertised (70M+) is a marketing metric. Daily active IPs are substantially fewer. For most scraping scenarios, 100 quality IPs outperform thousands of burned or slow ones. A practical formula for estimating required pool size: `(Hourly Volume ÷ Safe Limit Per IP) × Safety Buffer`. Amazon product pages, for example, require roughly 1,000-3,000 IPs for a 10,000-requests/hour enterprise workload.

### Tor as a Free Proxy

Tor operates as a SOCKS5 proxy on port 9050. NewCircuitPeriod controls how frequently the exit node rotates (default is not suitable for scraping; set to 30 seconds). Running 50 concurrent Tor instances provides a form of rotating proxy at zero cost. The critical limitation: Tor exit node IPs are publicly listed and maintained in databases. Most anti-bot systems block them explicitly. Tor is useful for targets without anti-bot protection and for testing whether an IP-based block is the actual cause of failure.

### Ban Management

Proxy bans fall into three categories. Soft bans return degraded responses (CAPTCHAs, reduced content) rather than hard errors. Hard bans return 403 or 429 errors for the specific IP. Network-wide bans block entire subnets or ASNs. Status codes indicating proxy bans: 401 (auth), 403 (forbidden), 407 (proxy auth), 429 (rate limit), 502/503 (gateway errors). Exponential backoff is the standard retry strategy. New IP on retry is required for hard bans.

### The Proxy Ladder

A cost-optimization framework for selecting proxy type by target sensitivity:

1. No proxy — direct request from server IP
2. Datacenter proxy — for targets without IP-type filtering
3. Residential proxy — for targets that block datacenter ASNs
4. Mobile proxy — for the most sensitive targets (luxury fashion, ticketing)
5. Web unblocker — when everything else fails or the target requires JavaScript solving

Moving up the ladder multiplies cost by roughly 10x per step. The correct entry point is determined by testing, not assumption. Approximately 15-20% of e-commerce sites require anything beyond datacenter proxies.

### DNS Leak as a Detection Signal

A less-discussed detection vector: platforms compare the ASN of the connection IP against the ASN of the DNS resolver that handled the session's queries. Anti-fraud services (IPQualityScore, IP2Proxy) include this ASN-consistency check as a standard field. When a mobile proxy session uses a T-Mobile IP (ASN 21928) but resolves DNS through Cloudflare (ASN 13335), the mismatch is detectable.

Some detection systems go further by embedding unique subdomains in page resources (e.g., `a3f9x.dnsprobe.platform.com`) and then checking which resolver ASN resolves that subdomain. A resolver ASN that differs from the proxy IP's ASN downgrades the session's trust score.

The architecture matters for how DNS leaks occur:

- **Shared peer-network proxies (Bright Data, Oxylabs, Smartproxy)**: DNS behavior depends on each exit peer's local DNS configuration, making ASN consistency unpredictable across sessions.
- **Provider-resolver proxies (IPRoyal)**: routes DNS through the provider's own resolver infrastructure, not the carrier's. Consistent but still a mismatch versus the exit IP's carrier ASN.
- **Generic SOCKS5/HTTP proxies**: most do not route DNS at all. DNS resolves locally on the client machine, creating a classic DNS leak.
- **Dedicated device proxies**: DNS resolves through the carrier's native infrastructure by design, matching the IP's ASN.

**The `socks5h` vs `socks5` distinction is critical.** Using `socks5://` in curl or Python's requests causes DNS to resolve locally before the connection is made. Using `socks5h://` (the "h" means "host") causes DNS to resolve through the proxy endpoint. This one-character difference determines whether DNS leaks to the client's resolver or flows through the proxy's carrier network.

CLI test method:
```bash
# Check DNS resolver ASN through proxy
curl --proxy socks5h://user:pass@proxy:port https://browserleaks.com/dns -s
# Compare against proxy IP's ASN
curl --proxy socks5h://user:pass@proxy:port https://ipinfo.io/json -s | jq '.org'
```

BrowserLeaks.com/dns resolves 50 randomly generated domains and reveals which DNS server handles them.

Source: voidmob.com/blog/dns-leak-proxy-killer-carrier-native-dns (2026-03-03)

## IP Sourcing: Where Providers Get Their IPs

Market research into the proxy industry revealed approximately seven genuinely independent proxy networks globally. Most providers either resell capacity from these networks or share SDK-sourced pools with competitors under different branding. The practical consequence is that switching providers does not always change the underlying IP pool.

SDK-sourced residential proxies work by embedding a proxy client into consumer apps — often mobile games — which then route traffic through users' connections. The ethical concerns around this sourcing model are well-documented. Providers that do not operate their own SDK are resellers by definition. Botnet-sourced IPs also exist in some pools, though providers do not advertise this.

### IPIDEA Takedown (January 2026)

In January 2026, Google's Threat Intelligence Group disrupted IPIDEA, the largest known SDK-sourced residential proxy botnet. IPIDEA had quietly enrolled 9 million Android devices as proxy exit nodes by embedding SDKs into free VPN apps, casual games, and flashlight tools. Traffic from over 550 threat groups — including state-sponsored actors from China, Russia, Iran, and North Korea — was routed through these devices. The IPIDEA pattern is not unique: Hola VPN was caught doing the same in 2015, PROXYLIB infected 28 Google Play apps in 2023, and Urban VPN was exposed in 2025 for harvesting AI prompts.

The technical mechanics: the app requests standard Android permissions (network access, background execution) that do not trigger Google Play review flags. The SDK runs as a background service, enrolling the device as a proxy exit node. The device owner sees no visible indication.

Detection approaches for users: per-app background data auditing, monitoring outbound connections with PCAPdroid, and checking for excessive permissions in VPN apps.

The takedown confirms that a significant portion of "clean" residential proxy pools sourced from SDK networks carries implicit risk: the underlying devices may have been enrolled without meaningful consent, and the network could be disrupted or classified as malicious at any time by an external authority action.

Source: voidmob.com/blog/free-vpns-proxies-sell-your-device (2026-02-17)

Alternative sourcing methods include router farming (compromised home routers) and SIM card farms, which are the physical basis for many mobile proxy providers (see [mobile-proxy-farming](./mobile-proxy-farming.md)).

### Third-Party Reverse Proxy Trust Model (2026-03)

A documented incident in India illustrates the risk of routing production traffic through third-party reverse proxies. When Indian ISPs began DNS-blocking `*.supabase.co` (February 24, 2026, under Section 69A of the IT Act), a proxy service called JioBase appeared within days, promising a one-line fix. Analysis of the open-source code reveals the security structure:

Indian ISPs applied DNS poisoning: `nslookup yourproject.supabase.co` returned a sinkhole IP (`49.44.79.236`) instead of Supabase's real addresses. Some ISPs additionally performed DPI, inspecting the SNI field in the TLS handshake, which caused failures even when users bypassed DNS poisoning by pointing at `1.1.1.1`. A reverse proxy solves this because the client's TLS connection targets the proxy domain (`yourapp.jiobase.com`); the ISP never sees `supabase.co` in any DNS query or SNI field.

JioBase runs as a Cloudflare Worker that:
1. Receives the incoming request
2. Rewrites the URL to the real Supabase project
3. Forwards all headers verbatim — including `Authorization: Bearer <JWT>`
4. Logs analytics: app ID, HTTP method, URL path, country, response status

The critical problem: TLS is terminated at Cloudflare's edge. Every authenticated request, database query, WebSocket message, and file upload passes through the proxy decrypted before being re-encrypted toward Supabase. JioBase's own privacy policy acknowledges this. The proxy operator (and Cloudflare) have technical access to all in-transit data. Since the code deploying to Cloudflare Workers cannot be verified against the GitHub source (no reproducible build, no deployment attestation), open-sourcing the code does not eliminate the trust problem.

Source: [https://harshanu.space/en/tech/dumb-vibe-coders/](https://harshanu.space/en/tech/dumb-vibe-coders/) (2026-03-01)

### Adversarial Reverse Proxy: Starkiller Phishing Kit (2026-02)

Starkiller is a phishing-as-a-service platform by a threat group calling itself Jinkusu. Its architecture is technically distinct from static phishing pages: instead of copying a login page, it reverse-proxies the real login page in real time using a Docker container running a headless Chrome instance.

How it works:
- Customer selects a target brand (Apple, Facebook, Google, Microsoft, etc.)
- Service generates a deceptive URL using the `@` sign trick: `login.microsoft.com@<malicious-url>`. Everything before `@` is treated as URL username data; the actual landing page is what follows the `@`.
- A Docker container running headless Chrome loads the real login page and acts as a man-in-the-middle reverse proxy
- Every keystroke, form submission, and session token from the victim passes through attacker-controlled infrastructure and is logged
- MFA is bypassed because the victim is authenticating with the real site through the proxy in real time; the resulting session cookies and tokens are captured

Platform features: real-time session monitoring (live-screen streaming), keylogger capture, cookie and session token theft, geo-tracking, automated Telegram alerts on new credential capture, campaign analytics (visit counts, conversion rates).

The approach avoids domain blocklisting and static page analysis because the victim sees the genuine login page, served dynamically through the proxy. Source: Abnormal AI analysis via [Krebs on Security](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/) (2026-02-20).

## Current State

As of September 2024, mobile proxy prices have dropped to ~$8/GB from historical highs of ~$40/GB. Residential pricing has stabilized at $6-8/GB with little differentiation between providers. ISP proxies occupy a pricing band between residential and unblockers that is difficult to justify given their characteristics: they cost like residential but carry datacenter infrastructure risk. The proxy market is commoditized at the infrastructure level. Differentiation between providers is largely on network quality, support, and geographic coverage rather than fundamentally different IP pools.

As of 2026-02, adversarial use of reverse proxy patterns (Starkiller) has industrialized real-time MFA bypass into a commercial phishing service. The same proxy-as-man-in-the-middle architecture that makes legitimate reverse proxies useful also makes them effective attack infrastructure when operated with malicious intent.

## Related

- [tls-fingerprinting](./tls-fingerprinting.md)
- [browser-fingerprinting](./browser-fingerprinting.md)
- [mobile-proxy-farming](./mobile-proxy-farming.md)
- [web-unblockers](./web-unblockers.md)
- [scraping-infrastructure](./scraping-infrastructure.md)
- [Cloudflare](../entities/cloudflare.md)
- [Akamai](../entities/akamai.md)
- [Scrapoxy](../entities/scrapoxy.md)

## Sources

- [https://substack.thewebscraping.club/p/everything-about-proxies](https://substack.thewebscraping.club/p/everything-about-proxies)
- [https://substack.thewebscraping.club/p/choosing-proxy-provider-scraping](https://substack.thewebscraping.club/p/choosing-proxy-provider-scraping)
- [https://substack.thewebscraping.club/p/five-secrets-of-the-proxy-industry](https://substack.thewebscraping.club/p/five-secrets-of-the-proxy-industry)
- [https://substack.thewebscraping.club/p/the-unit-economics-of-proxy-providers](https://substack.thewebscraping.club/p/the-unit-economics-of-proxy-providers)
- [https://substack.thewebscraping.club/p/differences-residential-mobile-proxies](https://substack.thewebscraping.club/p/differences-residential-mobile-proxies)
- [https://substack.thewebscraping.club/p/evaluating-proxy-providers-ips](https://substack.thewebscraping.club/p/evaluating-proxy-providers-ips)
- [https://substack.thewebscraping.club/p/how-many-ip-needed-scraping](https://substack.thewebscraping.club/p/how-many-ip-needed-scraping)
- [https://substack.thewebscraping.club/p/costs-web-scraping-proxy](https://substack.thewebscraping.club/p/costs-web-scraping-proxy)
- [https://substack.thewebscraping.club/p/optimizing-proxy-costs](https://substack.thewebscraping.club/p/optimizing-proxy-costs)
- [https://substack.thewebscraping.club/p/proxy-pricing-playbook-september](https://substack.thewebscraping.club/p/proxy-pricing-playbook-september)
- [https://substack.thewebscraping.club/p/where-do-proxy-companies-take-ip](https://substack.thewebscraping.club/p/where-do-proxy-companies-take-ip)
- [https://substack.thewebscraping.club/p/x-forwarded-for-header-proxies](https://substack.thewebscraping.club/p/x-forwarded-for-header-proxies)
- [https://substack.thewebscraping.club/p/reverse-proxies-and-webscraping](https://substack.thewebscraping.club/p/reverse-proxies-and-webscraping)
- [https://substack.thewebscraping.club/p/managing-proxy-bans-proxy-retries](https://substack.thewebscraping.club/p/managing-proxy-bans-proxy-retries)
- [https://substack.thewebscraping.club/p/bypassing-geo-fencing-scraping](https://substack.thewebscraping.club/p/bypassing-geo-fencing-scraping)
- [https://substack.thewebscraping.club/p/scraping-using-tor](https://substack.thewebscraping.club/p/scraping-using-tor)
- [https://substack.thewebscraping.club/p/optimizing-costs-for-web-scraping](https://substack.thewebscraping.club/p/optimizing-costs-for-web-scraping)
- [https://harshanu.space/en/tech/dumb-vibe-coders/](https://harshanu.space/en/tech/dumb-vibe-coders/)
- [https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/](https://krebsonsecurity.com/2026/02/starkiller-phishing-service-proxies-real-login-pages-mfa/)
- [https://voidmob.com/blog/dns-leak-proxy-killer-carrier-native-dns](https://voidmob.com/blog/dns-leak-proxy-killer-carrier-native-dns)
- [https://voidmob.com/blog/free-vpns-proxies-sell-your-device](https://voidmob.com/blog/free-vpns-proxies-sell-your-device)
