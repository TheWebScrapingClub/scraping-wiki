---
name: botdeflector
type: entity
category: anti-bot
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-understanding-and-bypassing-botdeflector.md
---

# BotDeflector

## What it is

BotDeflector is a captcha system developed by Martin Pronk, co-founder of Queue-IT, used to protect websites. It is often implemented on websites that use Queue-IT for managing queues, appearing either on the main queue page or a `/softblock/` page.

## How it works

BotDeflector protection consists of two main challenges. The first is an invisible Proof of Work (PoW) challenge, which is obfuscated using JavaScript obfuscation techniques. This challenge involves building a graph based on provided hashes and parameters, then finding a simple cycle within that graph. The difficulty lies in the computational expense of solving the PoW, rather than complex logic.

The second challenge is an icon-based captcha. This part is described as the more difficult aspect, often posing a challenge even for human users. The system also involves a third-party script loaded from `botdeflector.eu` that fingerprints the browser. Notably, the `SiteKey` used by the widget is not bound to a specific domain, allowing it to be served from any location.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The source mentions that BotDeflector lacks rate limits for submitting icon captcha challenges and does not implement rejections after a certain number of tries. This allows for repeated submissions of the same image until it is solved correctly, effectively making the `/icon/verify` endpoint an oracle. Additionally, the `SiteKey` is not domain-bound, which is considered a significant security oversight.

## Related

- [cloudflare](../entities/cloudflare.md)
- [reCAPTCHA](../entities/recaptcha.md)
- [undetected-chromedriver](../entities/undetected-chromedriver.md)


## Sources

- [https://takionapi.tech/blog/understanding-and-bypassing-botdeflector](https://takionapi.tech/blog/understanding-and-bypassing-botdeflector)
