---
name: obscrd
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - www-obscrd-dev.md
---

# obscrd

## What it is

obscrd is an open-source content protection system for React that scrambles HTML and blocks AI crawlers. It renders content normally for real users through the browser but transforms the underlying DOM so that scrapers, bots, and automated tools only see scrambled, meaningless data. The visual output remains identical, but the source code is altered.

## How it works

obscrd uses CSS ordering and decoy character injection to protect content. When a user views the page, they see normal text. However, scrapers and AI bots reading `textContent` only see garbled nonsense. The system includes client-side and server-side components to provide comprehensive protection.

- **Client-side protection**:
  - Text obfuscation using CSS flex ordering and character shuffling.
  - Email and phone protection through RTL reversal and decoys.
  - Image protection via canvas rendering, without using `<img>` URLs.
  - Clipboard interception to ensure shuffled text when copied.
  - AI honeypots and forensic breadcrumbs to detect and block scrapers.

- **Server-side crawler blocking**:
  - Automation of `robots.txt` to block 20+ AI crawlers.
  - Middleware support for Express, Fastify, and Node.js.
  - Meta tag generation for crawler control.
  - Standalone functionality without a React dependency.

## TWSC experience

Not yet tested by TWSC.

## Related

- [@obscrd/react](../entities/obscura.md)
- [@obscrd/robots](../entities/obscura.md)
- [obsrd CLI](../entities/obscura.md)


## Sources

- [https://www.obscrd.dev/](https://www.obscrd.dev/)
