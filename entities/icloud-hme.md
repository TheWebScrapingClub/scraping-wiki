---
name: icloud-hme
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-using-icloud-subscription-as-its-best.md
---

# icloud-hme

## What it is

A command-line interface (CLI) tool designed to automate the generation of iCloud HideMyEmail aliases. It handles the complexities of iCloud's authentication process, including Secure Remote Password (SRP) protocol, two-factor authentication (2FA), and supports managing multiple iCloud accounts.

## How it works

The tool interacts with iCloud's backend services by first performing a custom SRP authentication flow. This involves several steps, including SRP initialization with account details, handling Apple's specific s2k protocol for password derivation, and completing the authentication with server proofs. If two-factor authentication is enabled, the tool prompts for the security code and then trusts the session for future use.

Once authenticated, icloud-hme accesses the HideMyEmail API to reserve new email aliases, list existing ones, and manage their labels and notes. It also respects iCloud's rate limits for alias generation, which are approximately 5 emails per 30-minute window per family member, with a total account limit of around 700 emails.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The tool is subject to iCloud's rate limits for generating HideMyEmail aliases, which are approximately 5 aliases per 30-minute window per family member, and a total of around 700 aliases per account. Exceeding these limits will result in an error message from Apple.

## Related

None


## Sources

- [https://takionapi.tech/blog/using-icloud-subscription-as-its-best](https://takionapi.tech/blog/using-icloud-subscription-as-its-best)
