---
name: google-search-guard-vm-reversing
type: entity
category: tool
first_seen: 2026-09-22
last_updated: 2026-09-22
sources:
  - https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing
  - https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system
  - https://igorkozlowski.substack.com/p/google-searchguard-reversing-the
---

# google-search-guard-vm-reversing

## What it is

A GitHub repository by Ihar Kazlouski (Sec-CH-Lemon, MIT licensed, created 17 August 2026) that takes apart [Google SearchGuard](google-searchguard.md), the challenge Google serves on a cookieless search request. It answers three questions: which browser data the challenge reads, how its virtual machine is built, and what goes into the `SG_SS` token. Everything runs offline against a capture you make yourself. No Google code is redistributed and none of the tools solve the challenge or produce a token. Two Node.js bundles ship, one per article, each with its own README and pinned dependencies.

## How it works

### Part 1: proxy probe (`part-1-proxy-probe/`)

Three scripts, Node 18+, single dependency jsdom.

- `fetch-challenge.js` requests the search page with no cookies and saves the response as `challenge.html`, after checking that what came back is actually the challenge and not results, a consent page or `/sorry/`. Supports `--query`, `--attempts`, `--delay`, `--force`.
- `probe-proxy.js` runs the captured interpreter under jsdom with a JavaScript Proxy in place of `window` and prints every property read, `in` check and call, grouped by surface, marking names that do not exist as `ABSENT`. It runs the challenge twice, tapped and untapped, and compares the tokens byte for byte; the `invisible: YES` header line is the precondition for trusting the report. The technique is described in [javascript-proxy-tracing](../concepts/javascript-proxy-tracing.md).
- `verify-claims.js` re-derives the numbers stated in the first article from your own capture and prints which still hold. `--slow` adds an integrity probe that edits the interpreter source and confirms the challenge notices. This is the script to run first if the challenge looks changed.

### Part 2: VM reversing tools (`part-2-reverse-vm/tools/`)

Node 20.19+, 22.13+ or 24+, dependencies acorn, jsdom and prettier. The pipeline starts from `captures/response.html` and runs in a fixed order: `build-id`, `readable`, `equivalence`, `pristine`, `cipher`, `profile`, then the trace, disassembly and record recovery.

- `lib/challenge.js` parses minified and formatted challenge pages, extracting the interpreter, the encrypted `p` field, loader constants, response mode and the build-dependent VM global name.
- `lib/builds.js` holds reviewed per-build facts (store primitives, register file, program-counter slot, alphabet and re-key opcodes, output key slot) for five builds. Profile-dependent tools reject an unknown build instead of borrowing constants.
- `build-compare.cjs` identifies a response by interpreter length and SHA, `p` size and loader values.
- `vm-deobfuscate.cjs` parses the interpreter as an AST, simplifies supported mixed Boolean-arithmetic expressions, verifies each rewrite on sampled 32-bit inputs, and writes a readable interpreter. `run-readable-vm.cjs` proves the readable version produces a byte-identical token.
- `pristine-tap.cjs` observes `String.prototype.replace` calls in the hidden iframe realm while runtime opcode handlers are created, accepting the result only if tapped and untapped tokens match.
- `cipher-params.cjs` locates the ARX block function by dataflow shape and verifies round count, constant and rotation against the predictable first plaintext opcode.
- `dump-handlers.cjs`, `opcode-table.cjs`, `opcode-roles.cjs` and `build-profile.cjs` capture the runtime-installed handlers, derive operand layouts, classify control-flow, alphabet, string and re-key families, and write a capture-specific JSON profile.
- `opcode-trace.cjs` instruments the dispatcher and records executed instruction starts, cipher state, queue bursts and the separate output key. `static-disasm.cjs` decodes the program image without executing it, optionally guided by a verified trace. `sgss-token.js` is the configurable ARX keystream helper the disassembler uses, not a token generator.
- `record-recover.cjs` hooks the output writer at a verified invisible point and recovers the plaintext record before encryption, finding the eight-byte keystream sibling by shape rather than by name.

### Verified reference result

Checked against the clean capture of 15 September 2026, build `f6ad334abefc`: interpreter 62,751 characters, `p` field 16,831 characters, 39 MBA rewrites, cipher 15 rounds / constant 1819 / rotation 3, 98 handlers with 93 operand layouts, 2,000-call trace, 1,220 instruction starts covering 52.1% of the image bits, 635-byte plaintext record. The README states these identify that capture and are not protocol constants.

## TWSC experience

Not run by TWSC yet. It is a candidate instrument for a Lab article on Google's first-visit gate, and the part 1 probe is cheap to reproduce: one capture, one `npm install`, one script. The design pattern worth borrowing is the tapped-versus-untapped byte comparison that every instrumented run performs before its output is trusted.

## Known limitations

- Offline only: a capture must be supplied, and a trusted IP gets results instead of a challenge.
- Part 1 runs under jsdom, which lacks `window.chrome`, `trustedTypes` and similar Chrome names, so `ABSENT` needs interpretation.
- Part 2 only regenerates profiles for the builds listed in `lib/builds.js`; an unknown interpreter SHA needs primitive-discovery tools that are not in the bundle and a manual review.
- Scope explicitly excludes a complete ISA, an independent interpreter and token generation.
- The MIT license covers the tooling only; a captured interstitial and anything lifted from it remain Google's copyrighted code.
- The full derivation for part 2 sits behind the author's paid Substack post; the README documents what each file does but not the reasoning.
- Early-stage project: 4 stars and a last push on 22 September 2026 at the time of ingest.

## Related

- [Google SearchGuard](google-searchguard.md)
- [javascript-proxy-tracing](../concepts/javascript-proxy-tracing.md)
- [vm-based-javascript-obfuscation](../concepts/vm-based-javascript-obfuscation.md)
- [camoufox-reverse](camoufox-reverse.md)
- [client-side-bot-detection](client-side-bot-detection.md)

## Sources

- [https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing](https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing)
- [https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system](https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system)
- [https://igorkozlowski.substack.com/p/google-searchguard-reversing-the](https://igorkozlowski.substack.com/p/google-searchguard-reversing-the)
