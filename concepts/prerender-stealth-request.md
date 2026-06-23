---
name: Prerender Stealth Request
type: concept
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
- https://www.brokenbrowser.com/blog/2026-05-09-prerender-stealth-csp-bypass
---

# Prerender Stealth Request

## Definition

A `<link rel="prerender">` element in Chromium-based browsers fires a real HTTP request that bypasses Content Security Policy, does not appear in the DevTools Network tab, and sends the browser's real User-Agent even when DevTools' Network Conditions UA override is active. Discovered by Manuel Garcia (brokenbrowser.com) in May 2026, independently confirmed by soutag (who found it earlier but did not publish).

Chromium only. Firefox and Safari do not implement `rel=prerender`.

## Why It Works

Chrome treats `<link rel="prerender">` as a speculative top-level navigation hint, not a sub-resource fetch. That classification puts it in a separate pipeline with three consequences:

**CSP bypass**: every CSP directive (`default-src`, `connect-src`, `img-src`, etc.) applies to sub-resources of the current document. A speculative navigation is treated as equivalent to the user typing the URL in the address bar, which no CSP governs. CSP evaluation does not run. The `prefetch-src` directive was defined in CSP Level 3 to address exactly this case but was removed before standardization; there is no current CSP directive that constrains the deprecated prerender pipeline.

**DevTools invisibility**: the Network panel is driven by `Network.requestWillBeSent` on the page's main CDP target. Speculative navigations fire on a separate prerendering target. The request is visible under Application → Speculative Loads, but not in the Network tab. Extension-based `webRequest` filters scoped to the page also miss it.

**Real UA leakage**: DevTools' Network Conditions UA override patches `navigator.userAgent` and injects a custom `User-Agent` header via the page's JavaScript and resource loader pipeline. The speculative navigation bypasses that pipeline entirely. The request exits with the real `User-Agent`, real `sec-ch-ua` client hints, and real platform values.

## Wire Signature

```
# <link rel="prerender" href="/x">:
Accept: text/html,application/xhtml+xml,...
Sec-Purpose: prefetch
Upgrade-Insecure-Requests: 1
User-Agent: <real browser UA>
(no Sec-Fetch-Dest)
```

The `Sec-Purpose: prefetch` header combined with `Accept: text/html` and absent `Sec-Fetch-Dest` is the unique server-side signature of Chrome's prerender pipeline. It can be used to detect or block this request type at the edge.

## Trigger

One line of HTML or equivalent JavaScript:

```html
<link rel="prerender" href="https://anywhere/">
```

```javascript
function stealthRequest(url) {
    var lnk = document.createElement("link");
    lnk.rel = "prerender";
    lnk.href = url;
    document.body.appendChild(lnk);
}
```

Adding `prefetch` to `rel` alongside `prerender` breaks the stealth: the prefetch token takes precedence for observability and the request appears in the Network tab. `as=` and `crossorigin=` attributes do not gate the behavior.

## Bot Detection Relevance

This technique exposes a UA spoofing asymmetry: if a user (or scraper) has overridden their UA in DevTools, this primitive can be used to make a server-side request that reveals the true UA while the page-level UA appears spoofed. The detection system receives the real UA; the spoofed UA is only visible to page-level JavaScript and DevTools.

For defenders, the `Sec-Purpose: prefetch` server-side signature allows blocking or flagging these requests. For attackers with an HTML injection vector on a CSP-protected page, it provides a one-way exfiltration channel that CSP cannot stop.

## Limitations

- Chromium-only (Chrome, Edge, Brave, Opera inherit the same pipeline)
- The modern Speculation Rules API (`<script type="speculationrules">`) uses a different path and is blocked normally by CSP
- Only fires a GET request; no request body
- The target receives no cookies from the current page session unless the prerender URL is same-origin

## Related

- [bot-detection](./bot-detection.md)
- [browser-fingerprinting](./browser-fingerprinting.md)
- [cdp-detection](./cdp-detection.md)

## Sources

- Manuel Garcia (brokenbrowser.com) — "Stealth Request That Bypasses CSP, Hides from DevTools, and Leaks the Real User-Agent," [https://www.brokenbrowser.com/blog/2026-05-09-prerender-stealth-csp-bypass](https://www.brokenbrowser.com/blog/2026-05-09-prerender-stealth-csp-bypass) (May 2026)
