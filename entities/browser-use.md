---
name: browser-use
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-06-23
sources:
  - posts-bot-detection.md
  - https://browser-use.com/posts/bot-detection
  - https://browser-use.com/posts/firecracker-browser-infra
  - https://browser-use.com/posts/two-ways-to-sandbox-agents
---
 
# Browser Use

## What it is

Browser Use is a cloud-based browser automation platform that aims to create undetectable browsers. It maintains a custom Chromium fork with numerous patches at the C++ and OS level, ensuring that the browser is undetectable by major antibot systems such as Cloudflare, DataDome, Kasada, Akamai, PerimeterX, and Shape Security.

## How it works

Browser Use achieves undetectability by forking Chromium and making fundamental changes to the browser's behavior. When the browser reports `navigator.webdriver === false`, it is because the value was never true in the first place. Every function returns `[native code]` when stringified, and every prototype chain is intact. Nothing is overridden; the browser's actual behavior is changed at the C++ and OS level through dozens of patches.

Their stated thesis (February 2026) frames the strategy: antibot systems (Akamai, Cloudflare, DataDome) can detect far more than they actually block, because false positives hurt conversion, so thresholds are set conservatively. JavaScript patches, stealth plugins, and CDP hacks are already detectable; antibots simply have not flipped the switch from "monitor" to "block." As AI agents flood the web and bot traffic crosses a tipping point, Browser Use expects detection thresholds to tighten, which is why they aim for a browser that is undetectable because there is genuinely nothing to detect rather than because the antibot is lenient.

The full stack addresses the layers JavaScript-only stealth tools miss. Modern antibot systems cross-reference IP reputation (datacenter vs residential), timezone and locale against IP geolocation, hardware consistency (GPU, audio, screen resolution that should agree), API availability for the claimed OS and browser version, and behavioral signals (mouse, scroll, typing cadence). A Windows claim with a SwiftShader GPU, a New York timezone with a Frankfurt IP, or a macOS claim missing APIs every Mac has are all flagged. Browser Use's stack combines the Chromium fork (JS fingerprint consistency), residential proxy infrastructure with proper geolocation, timezone and locale injection matched to the exit IP, and a behavioral layer.

## Real-world fingerprints

Browser Use argues that running everything on Linux (less than 5% of global desktop traffic) and faking Windows or macOS on top is a structural weakness: the mismatch shows up as missing APIs, wrong audio configs, and inconsistent GPU reports. They cite real desktop traffic at roughly Windows 60%, macOS 35%, Linux 5%, and use tens of thousands of real fingerprints across the three platforms. The scaling risk they highlight: antibot AI spots shared fingerprint signatures across requests and applies temporal rules that block entire networks, so a fleet sharing one Linux fingerprint pattern can be flagged wholesale when a single member misbehaves. See [browser-fingerprinting](../concepts/browser-fingerprinting.md).

## Performance and efficiency patches

Not all of the Chromium work is about stealth. To pack more browsers per machine when running thousands concurrently, they apply compositor throttling (agents do not need 60 FPS), feature stripping via flags, V8 memory tuning for JS-heavy sites, CDP message optimization (to avoid leaks from libraries like Playwright), and smart caching. They also patched profile encryption to stay secure while portable across machines, instead of the common `--password-store=basic` flag that disables encryption and stores credentials, cookies, and session data in plaintext.

## In-house CAPTCHA solving

Browser Use built CAPTCHA solving with in-house models, no third-party APIs, currently covering Cloudflare Turnstile, PerimeterX Click & Hold, and reCAPTCHA. Because it is in-house, solving is free for customers with no per-solve fees. Their stated view is that good fingerprinting reduces how often sites challenge in the first place, and that CAPTCHAs will fade as solvers outpace humans and harm legitimate conversion.

## Cloud Infrastructure (Firecracker microVMs)

In June 2026 Browser Use published the architecture of its rebuilt cloud, which runs every session in its own Firecracker microVM. The headline numbers: $0.02 per browser hour (down from $0.06, ~3x cheaper), VM cold start under 400ms, and end-to-end browser creation latency of 825ms at p50 and 1.35s at p99, measured across a 10,000-session stress test with a 100% start success rate.

### Firecracker on regular EC2, not bare metal

The unusual choice is running Firecracker on standard EC2 instances rather than the usual `.metal` bare-metal hosts. Regular EC2 is itself a VM, so every browser ends up as a VM inside a VM (nested virtualization). The tradeoff: regular EC2 provisions faster (a host boots from a pre-built image and serves browsers ~30 seconds after launch) and is cheaper to keep idle, which lowers customer cost. The cost is that any host assistance a browser VM needs crosses two hypervisor layers, adding latency, especially on page faults. They previously ran on Unikraft and moved to Firecracker specifically because they needed horizontal EC2 autoscaling that Unikraft did not yet expose; the move was about the infrastructure layer, not browser lifecycle.

A custom control plane (not CloudWatch, which reacts on one-minute windows) monitors the fleet in real time, places new sessions on hosts with room, and drains hosts being removed. Stateless edge routers forward raw CDP-over-WebSocket bytes to the right VM; the control plane owns placement.

### Memory: 2MB pages and userfaultfd

Browsers resume from a snapshot paused just before Chromium launches. The first bottleneck was page faults when a restored VM first touches memory, expensive under nesting because each fault can cross both VM layers. During an early cold start, page faults were 72% of all VM exits and resume-to-CDP-ready took 9.8s. Two fixes: mapping memory in 2MB pages instead of 4KB (each page covers 512x more memory), and a custom `userfaultfd` handler that preloads the hot pages Chromium accesses first. Result: resume-to-ready dropped to 3.1s and missing-memory pauses fell from ~100,000 to ~1,100 per resume (~91x). They also dropped a 500ms PS/2 keyboard probe and switched the readiness signal from HTTP polling to a `vsock` log read (host sees ready in <1ms).

### CPU: two-phase vCPU pinning

Chromium's startup burst (renderers, compositors, V8 isolates) is CPU-heavy; automation afterward is quiet, so many browsers pack onto one host. They leave vCPUs unpinned during launch so Linux spreads the burst across cores, then pin to stable cores once the browser reports ready. Pinning from the start piled launches onto hot cores and failed. Each browser also gets both sibling hyperthreads of its physical core to avoid sibling contention, and pinned vCPU threads get real-time priority. Together these took a 1,000-browser test from 17% lost sessions to zero.

### Fully headless stealth

Browser Use runs fully headless, unlike most providers who run headful (paying for a display server, GPU, and compositor) because plain headless Chromium avoids blocks only 2% of the time on their stealth benchmark versus 50% for the same Chromium headful. Headless works for them only because they changed the browser itself: the Chromium fork patches automation signals at the lowest level so values like `navigator.webdriver` are never exposed (no JS injection that detection can catch), plus tens of thousands of real fingerprints across macOS, Windows, and Linux. They report 81% block avoidance on their own stealth benchmark and 84.8% on Halluminate BrowserBench, the highest of any provider tested. See [browser-fingerprinting](../concepts/browser-fingerprinting.md).

### Remaining bottleneck

Chromium startup after resume is still ~545ms at p50, now the largest cost. The next step is snapshotting after Chromium is already running so sessions wake with a live browser, which requires safely freezing open devices, timers, graphics, network, and fingerprint state and then restoring each browser as a distinct instance rather than a clone.

## Agent Sandbox Architecture

For agents that execute arbitrary code (Python, shell, file writes), Browser Use isolates the entire agent rather than just the dangerous tool (the "isolate the agent" pattern, see [agent-sandboxing](../concepts/agent-sandboxing.md)). The agent runs in a sandbox holding zero secrets and reaches the outside world only through a stateless control plane that owns all credentials. The sandbox is one container image: a Unikraft micro-VM in production (boots under a second, scale-to-zero, distributed across metros), a Docker container in dev and evals, selected by a `sandbox_mode: 'docker' | 'ukc'` switch. It receives only three env variables (`SESSION_TOKEN`, `CONTROL_PLANE_URL`, `SESSION_ID`) and sits in a private VPC whose only egress is the control plane. Hardening before any agent code runs: Python compiled to `.pyc` with all `.py` deleted, privilege drop from root to a `sandbox` user, and stripping the three env vars from `os.environ` after reading them. The control plane proxies LLM calls (reconstructing full conversation history so the sandbox stays stateless), file sync via session-scoped presigned S3 URLs, plus cost caps and billing.

Note this Unikraft-based agent sandbox (Feb 2026) predates and is separate from the Firecracker cloud browser layer (Jun 2026); Browser Use runs both, for different workloads.

## TWSC experience

Not yet tested by TWSC. Architecture details above are from Browser Use's own engineering posts (February and June 2026).

## Known limitations

OMIT

## Related

- [Cloudflare](../entities/cloudflare.md)
- [DataDome](../entities/datadome.md)
- [Kasada](../entities/kasada.md)
- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [bot-detection](../concepts/bot-detection.md)
- [agent-sandboxing](../concepts/agent-sandboxing.md)
- [scraping-infrastructure](../concepts/scraping-infrastructure.md)
- [cdp-detection](../concepts/cdp-detection.md)


## Sources

- [https://browser-use.com/posts/bot-detection](https://browser-use.com/posts/bot-detection)
- [https://browser-use.com/posts/firecracker-browser-infra](https://browser-use.com/posts/firecracker-browser-infra)
- [https://browser-use.com/posts/two-ways-to-sandbox-agents](https://browser-use.com/posts/two-ways-to-sandbox-agents)
