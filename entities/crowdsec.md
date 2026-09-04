---
name: crowdsec
type: entity
category: anti-bot
first_seen: 2026-09-04
last_updated: 2026-09-04
sources:
  - blog-crowdsec-1-8-waf-bot-detection-kubernetes.md
---

# CrowdSec

## What it is

CrowdSec is a Web Application Firewall (WAF) solution that has incorporated bot detection capabilities. This feature allows the WAF to react not only to user actions but also to the identity of the user, distinguishing between legitimate human users and automated bots. It is designed to efficiently deal with distributed attacks, scraping, scalping, and other forms of aggressive automation.

## How it works

The bot detection approach combines several techniques, most notably fingerprinting and proof of work. This combination forces attackers to engage with anti-detection measures while simultaneously increasing the computational cost of botting, thereby raising the economics of automated attacks.

CrowdSec also features a dedicated Kubernetes datasource that interacts directly with the Kubernetes API using `pods/logs`. This allows users to deploy a single CrowdSec instance to monitor multiple pods, simplifying the build, run, and architecture of Kubernetes deployments.

## TWSC experience

Not yet tested by TWSC.

## Related

- [bot-detection-system](../entities/bot-detection-system.md)


## Sources

- [https://www.crowdsec.net/blog/crowdsec-1-8-waf-bot-detection-kubernetes](https://www.crowdsec.net/blog/crowdsec-1-8-waf-bot-detection-kubernetes)
