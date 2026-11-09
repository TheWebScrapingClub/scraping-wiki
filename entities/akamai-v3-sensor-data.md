---
name: akamai-v3-sensor-data
type: entity
category: anti-bot
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-akamai-v3-sensor-data-deep-dive-into-encryption-decryption-and-bypass-tools.md
---

# Akamai v3 Sensor Data

## What it is

Akamai v3 Sensor Data is a component of Akamai's bot protection system. It involves a two-step encryption process for data transmitted to detect and mitigate bots. This system relies on JavaScript file hashes and cookie hashes to seed its encryption algorithms.

## How it works

The encryption process begins with shuffling the JSON payload data after converting it into a colon-delimited string. This shuffling is performed using a pseudo-random number generator (PRNG) seeded with a hash derived from Akamai's JavaScript files. Following the shuffling, a second PRNG, seeded with a hash from a cookie (typically the `bm_sz` cookie), is used to substitute characters within the shuffled string.

Decryption requires reversing these steps. First, the character substitutions are undone using the cookie-derived hash to reinitialize the PRNG. Subsequently, the elements are shuffled back into their original order using the script-derived file hash to reinitialize the PRNG for the shuffling phase. The dependency on both the script content and the cookie hash makes bypassing this system complex.

## TWSC experience

Not yet tested by TWSC.
## Related

- [Akamai Bot Manager](../entities/akamai.md)


## Sources

- [https://takionapi.tech/blog/akamai-v3-sensor-data-deep-dive-into-encryption-decryption-and-bypass-tools](https://takionapi.tech/blog/akamai-v3-sensor-data-deep-dive-into-encryption-decryption-and-bypass-tools)
