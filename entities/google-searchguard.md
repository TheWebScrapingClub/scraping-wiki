---
name: Google SearchGuard
type: entity
category: anti-bot
first_seen: 2026-09-22
last_updated: 2026-09-22
sources:
  - https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing
  - https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system
  - https://igorkozlowski.substack.com/p/google-searchguard-reversing-the
  - google-removed-the-urls-serp.md
---

# Google SearchGuard

## What it is

SearchGuard is the anti-bot challenge Google serves instead of search results when a client hits `google.com/search` without cookies. The response is an HTML page carrying an obfuscated script instead of the results list. That script is a JavaScript virtual machine plus an encrypted program for it. When the program runs it collects browser signals, assembles a token and sets it client-side as the `SG_SS` cookie. The next request carries `SG_SS` and, if Google accepts it, gets the results. Without JavaScript execution the cookie is never generated and the client fails.

The name and the whole description below come from the teardown published by Ihar Kazlouski (writing as Igor Kozlowski) in the [google-search-guard-vm-reversing](google-search-guard-vm-reversing.md) repository and its two companion articles (August and September 2026).

## How it works

### Request side

Before any JavaScript runs, Chrome already sends Client Hints (`sec-ch-ua-platform`, `sec-ch-ua-arch`, `sec-ch-ua-mobile`) plus two product headers, `x-browser-channel` and `x-browser-validation`. The second is a 20-byte value that looks like a hash of an embedded API key and the User-Agent string. The author could not reproduce it from public Chromium keys, so the formula stays unconfirmed, but the practical consequence holds: a value captured under one User-Agent will not match a spoofed one.

The challenge page embeds a `sei` parameter, which appears to be a session identifier derived from the initial request, and the server sets HttpOnly cookies alongside it. Whether the challenge is served at all depends on the IP: the repository's capture helper notes that if every attempt returns results instead of the challenge, the fix is a different IP, not more attempts. A request can also land on a consent page or on the `/sorry/` page instead.

### The `SG_SS` cookie

`SG_SS` has a 30-second TTL. It is never returned by the server, so it is generated on the client. Its length and value change on every attempt even in the same browser, which means dynamic data is mixed in. A normal run produces a token of roughly 1,660 characters. When the challenge detects tampering it falls into a degraded path and emits a token of exactly 871 characters, which is the only reliable tamper indicator the author found: the length collapses, not the format.

### What the challenge reads

Measured with the [JavaScript Proxy tracing](../concepts/javascript-proxy-tracing.md) technique on a capture run under jsdom, one execution makes 84 accesses to 72 distinct names, 32 of them to names that do not exist, plus 14 function calls. The surfaces are `window`, `document`, `navigator`, `screen`, `history`, `performance` and `Math`.

The reads fall into three groups:

- **Automation markers**, names that exist in no browser and whose only purpose is detection: `document.$cdc_asdjflasutopfhvcZLmcfl_` and `document.$wdc_` (ChromeDriver), `document.__webdriver_script_fn`, `window.webdriver`, `__nightmare`, `callPhantom`, `Cypress`, `domAutomationController`, `awesomium`, `cefsharp_CreatePromise`, `windmill`, `knitsail`, `ubot`, `boundObject`, `____LocationIntercept`, `PerfTestReturnValue`. `navigator.webdriver` is read too.
- **Chrome-presence probes**, names that exist in real Chrome and whose absence is an inverted signal ("this is not Chrome"): `window.chrome`, `trustedTypes` (read four times), `navigator.deviceMemory`, `navigator.connection`, `isSecureContext`, `requestIdleCallback`, `setImmediate`, `performance.memory`, `performance.getEntriesByType`.
- **Environment values** that feed the fingerprint: `navigator.hardwareConcurrency`, `navigator.languages` (walked element by element), `navigator.maxTouchPoints`, `screen.width/height/availWidth/availHeight/availLeft`, `innerWidth/innerHeight/outerWidth/outerHeight`, `devicePixelRatio`, `history.length`, `document.URL`, `window.opener`, `Date` and `Math.random`.

It also calls `document.createElement("iframe")` twice and `createElement("a")` once, and registers then removes a test event listener. The iframe gives the VM a hidden clean realm whose pristine prototypes it borrows during its own bootstrap (part 2 of the teardown taps `String.prototype.replace` in that realm).

There are no canvas, WebGL or audio reads in this first-visit probe. The author's reading is that this is a lightweight check meant to catch plain automation tools quickly, not a heavy fingerprint.

### The virtual machine

Searching the script for `navigator.webdriver` returns zero matches because the checks are not in the JavaScript text: they live in an encrypted program executed by an interpreter. For the build captured on 15 September 2026 (`f6ad334abefc`) the interpreter is 62,751 characters and the encrypted program field `p` is 16,831 characters. Loader constants in the page include `ce`, `challenge_version`, `ss_cgi` and `r`.

Facts established by the part 2 tooling on that build:

- The interpreter source uses mixed Boolean-arithmetic obfuscation; 39 rewrites were needed to make it readable, and the readable version still executes byte-identically to the original.
- The program image is decrypted with an ARX cipher (15 rounds, constant 1819, rotation 3 on this build), with a runtime re-key opcode. The key is issued at runtime.
- The dispatch table holds 98 handlers with 93 distinct operand layouts. Part of the opcode set is installed at runtime rather than present in the source.
- A 2,000-call dispatcher trace covered 1,780 outer fetches and 220 queued dispatches, decoding 1,220 instruction starts, which is 52.1% of the image bits.
- The output record written before `SG_SS` encryption is 635 bytes on this capture. The writer emits it one byte at a time XORed with an eight-byte keystream sibling.
- The interpreter checks its own integrity: editing its source is noticed and the challenge degrades the token.

Every one of these numbers is capture-specific, not a protocol constant. See [VM-based JavaScript obfuscation](../concepts/vm-based-javascript-obfuscation.md) for the per-build rotation.

### Build churn

The repository's build table records five interpreter builds between mid-August and 15 September 2026 (`885c049eda50`, `c348580f3670`, `d4a6b4f0a2a5` on 2026-08-27, `80056f9da7b2` on 2026-09-11, `f6ad334abefc` on 2026-09-15). Across builds the internal names, opcode numbers, program-counter slot, alphabet opcode and re-key opcode all changed, and the argument order of the three store primitives was permuted per build. Anything hardcoded against one build breaks on the next.

## TWSC experience

We have not run the repository's tools ourselves yet. Our own contact with this layer is the [Google SERP link experiment](https://www.scraping.club/p/google-removed-the-urls-serp) from August 2026: Google serves different search results depending on whether it classifies the client as a human or a script, the decisive check happens when the query is submitted, and a session Google has already accepted keeps working even when it is then driven over CDP. That matches the first-visit gate described here: the challenge sits at the entry, and the 30-second `SG_SS` is the pass. Playwright triggers the challenge immediately on launch according to the teardown, which is consistent with what we saw from automation stacks landing on `/sorry/` at query submission.

## Known limitations

- The part 1 probe runs in jsdom, so `ABSENT` conflates "exists nowhere" with "exists in Chrome but not in jsdom". The article separates the two groups by hand.
- Google rotates builds every couple of weeks and the repository refuses to apply one build's constants to another. Bootstrapping an unknown build needs manual review.
- The published tools do not generate an accepted `SG_SS` token, do not provide a complete instruction set, and do not implement an independent interpreter.
- The IP decides whether the challenge appears at all. A trusted IP gets results and no capture.

## Related

- [google-search-guard-vm-reversing](google-search-guard-vm-reversing.md)
- [javascript-proxy-tracing](../concepts/javascript-proxy-tracing.md)
- [vm-based-javascript-obfuscation](../concepts/vm-based-javascript-obfuscation.md)
- [client-side-bot-detection](client-side-bot-detection.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [cdp-detection](../concepts/cdp-detection.md)
- [reCAPTCHA](recaptcha.md)

## Sources

- [https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing](https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing)
- [https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system](https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system)
- [https://igorkozlowski.substack.com/p/google-searchguard-reversing-the](https://igorkozlowski.substack.com/p/google-searchguard-reversing-the)
- [https://www.scraping.club/p/google-removed-the-urls-serp](https://www.scraping.club/p/google-removed-the-urls-serp)
