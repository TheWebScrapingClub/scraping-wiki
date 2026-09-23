---
name: VM-based JavaScript obfuscation
type: concept
first_seen: 2026-09-22
last_updated: 2026-09-22
sources:
  - https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing
  - https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system
  - https://igorkozlowski.substack.com/p/google-searchguard-reversing-the
---

# VM-based JavaScript obfuscation

## Definition

An anti-bot delivery pattern where the detection logic is not present in the JavaScript shipped to the browser. The page contains an interpreter (a virtual machine written in JavaScript) and an encrypted bytecode program. The checks, the fingerprint collection and the token assembly all happen inside the bytecode. Searching the script text for `navigator.webdriver` finds nothing because the string is built at runtime by the VM.

## How it works

The concrete instance documented in the wiki is [Google SearchGuard](../entities/google-searchguard.md), as taken apart in [google-search-guard-vm-reversing](../entities/google-search-guard-vm-reversing.md). Its structure, established by tooling on the build of 15 September 2026:

- **Interpreter and program are separate.** The interpreter is about 62,000 characters of source; the program is an encrypted field of about 16,800 characters. The interpreter source itself is obfuscated with mixed Boolean-arithmetic expressions that need dozens of verified rewrites before it is readable.
- **The program is encrypted with a runtime key.** An ARX block cipher (add, rotate, xor; 15 rounds on that build) decrypts the image, and a re-key opcode changes the key during execution, so the bitstream cannot be decoded statically end to end. A trace-guided static decode reached 52.1% of the image bits.
- **Opcodes are assigned dynamically.** Part of the handler table is installed at runtime rather than present in the source, and opcode numbers are permuted on every load. A profile of the dispatch table (98 handlers, 93 operand layouts on that build) is valid only for the capture it was built from.
- **Execution has two paths.** The dispatcher serves both an outer instruction fetch loop and a macro queue of deferred handler dispatches (1,780 and 220 respectively in a 2,000-call trace).
- **The VM defends itself.** It borrows pristine prototypes from a hidden iframe realm during bootstrap, checks the integrity of its own interpreter source, and on detected tampering degrades its output to a fixed-length token instead of failing loudly.
- **Builds rotate.** Five interpreter builds were recorded between mid-August and mid-September 2026. Each rebuild changed internal names, opcode numbers, the program-counter slot and the argument order of the store primitives. Constants extracted from one build do not transfer.

This is the same design philosophy described from the defender's side in [client-side-bot-detection](../entities/client-side-bot-detection.md): obfuscation is treated as a cost imposed on the attacker, internal encodings regenerate per build, and tamper signals are folded into key material rather than exposed as a branch.

## Where it matters

Any target whose challenge script shows the interpreter-plus-blob shape. The practical consequence for scraping is that signature-based bypasses (patching one property, hooking one function name) have a lifetime of one build. Two working responses are to run a real browser that passes the checks, or to enumerate what the VM reads without reversing it, see [javascript-proxy-tracing](./javascript-proxy-tracing.md).

## What we tested

Nothing yet. The reference numbers above come from the repository's verified result table and README, not from our own runs.

## Current state

As of 22 September 2026 the SearchGuard tooling can lift a readable interpreter, profile the dispatch table, trace execution and recover the 635-byte plaintext record before encryption, but it does not produce a complete instruction set or an accepted token. Google shipped a new build roughly every two weeks over the observed period.

## Related

- [Google SearchGuard](../entities/google-searchguard.md)
- [google-search-guard-vm-reversing](../entities/google-search-guard-vm-reversing.md)
- [javascript-proxy-tracing](./javascript-proxy-tracing.md)
- [client-side-bot-detection](../entities/client-side-bot-detection.md)
- [bot-detection](./bot-detection.md)

## Sources

- [https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing](https://github.com/Sec-CH-Lemon/google-search-guard-vm-reversing)
- [https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system](https://igorkozlowski.substack.com/p/google-searchguard-anti-bot-system)
- [https://igorkozlowski.substack.com/p/google-searchguard-reversing-the](https://igorkozlowski.substack.com/p/google-searchguard-reversing-the)
