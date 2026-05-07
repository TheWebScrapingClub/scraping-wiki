---
name: facebookexternalhit
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - dbi-facebookexternalhit.md
---

# facebookexternalhit

## What it is

`Facebookexternalhit` is the Facebook crawler used to retrieve information about websites or applications that have been shared on Facebook. This crawler is utilized when content is shared via platforms like Messenger or Facebook, often triggering a request to gather details such as the title, a short description, and the favicon of the site.

## How it works

The Facebook crawler makes requests using specific user agents, such as `facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)`. These requests originate from Facebook's IP addresses belonging to AS32934 (Facebook, Inc.) when retrieving shared content information.

Requests that appear to use the `facebookexternalhit` substring may also originate from end-user IP addresses, particularly when linked with `Twitterbot/1.0`, which is associated with the Apple iMessage link preview feature.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Relying solely on the user agent to authenticate a bot is not recommended, as this HTTP header can be easily spoofed by an attacker. Verification requires confirming both the user agent pattern and that the request originates from the AS32934 IP range. Furthermore, spikes in traffic from Facebook's autonomous systems, while not malicious, can still cause infrastructure issues such as high CPU load and increased latency.

## Related

* [is-antibot](../entities/is-antibot.md)


## Sources

- [https://deviceandbrowserinfo.com/learning_zone/articles/facebookexternalhit](https://deviceandbrowserinfo.com/learning_zone/articles/facebookexternalhit)
