---
name: grith
type: entity
category: anti-bot
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - blog-grith-is-live.md
---

# Grith

## What it is

Grith is a security proxy designed to supervise AI coding agents by enforcing security decisions at the operating system level. It acts as a supervisor, ensuring that AI agents adhere to defined security policies before executing actions, thereby placing a boundary around the agent's operations.

## How it works

Grith operates as an OS-level supervisor, utilizing `ptrace` with a `seccomp-BPF` pre-filter to intercept security-relevant system calls, including file access, process execution, and network operations. These intercepted calls are scored against 18 filters across three phases: static checks, pattern matching (including secret scanning and egress policy), and contextual filters like taint tracking.

The scoring results in three verdicts: ALLOW (score under 3.0), QUEUE (3.0 to 8.0, freezing the process for human review), or DENY (over 8.0, injecting EPERM into the syscall return). The matching layers are deterministic, and the enforcement path contains no Large Language Model.

## Known limitations

The enforcement boundary is the supervised process tree; delegating authority to a pre-existing process outside this tree constitutes a structural escape class. Grith detects known delegation routes but does not claim to replace a VM or container for fully untrusted code.

## Related

- [agent-vault-proxy](../entities/agent-vault-proxy.md)
- [bot-detection-system](../entities/bot-detection-system.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://grith.ai/blog/grith-is-live](https://grith.ai/blog/grith-is-live)
