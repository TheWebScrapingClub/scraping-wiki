---
name: Agent Sandboxing
type: concept
first_seen: 2026-06-23
last_updated: 2026-06-23
sources:
- https://browser-use.com/posts/two-ways-to-sandbox-agents
---

# Agent Sandboxing

## Definition

When an AI agent can execute arbitrary code (run Python, shell commands, write files), it can read anything on the machine it runs on: environment variables, API keys, database credentials, internal services. Agent sandboxing is the architecture that isolates that code execution from the infrastructure and secrets it must never reach. There are two structural patterns, documented by Browser Use in February 2026 from running millions of web agents.

## The Two Patterns

**Pattern 1 — isolate the tool.** The agent loop runs on your infrastructure. Only the dangerous operations (code execution, terminal access) run in a separate sandbox, which the agent calls over HTTP. The code runs somewhere with nothing to leak, but the agent itself still sits next to your secrets and shares resources with your backend.

**Pattern 2 — isolate the agent.** The entire agent runs inside a sandbox that holds zero secrets. It reaches the outside world only through a control plane that owns all credentials. The agent becomes disposable: nothing to steal, no state to preserve, killable and restartable, scalable independently. The control plane holds the truth.

Browser Use started with Pattern 1 and moved to Pattern 2. The motivation was not only security but operational: with the agent loop sharing the same backend process as the REST API, a redeploy killed all running agents and a memory-hungry agent slowed the API. The two workloads are fundamentally different and belong in separate processes.

## How Pattern 2 Works

### One image, two runtimes

The same container image runs everywhere. In production it runs as a Unikraft micro-VM (boots in under a second, scale-to-zero suspend/resume, distributed across multiple metros); in local development and evals it runs as a Docker container. A single config switch (`sandbox_mode: 'docker' | 'ukc'`) selects the provisioning path. This guarantees the agent that runs on a dev laptop, the hundreds spun up in parallel for evals, and the production deployment are byte-for-byte the same.

### Minimal trust surface

The sandbox receives only three environment variables: `SESSION_TOKEN`, `CONTROL_PLANE_URL`, and `SESSION_ID`. No cloud keys, database credentials, or API tokens. The VM sits in a private VPC whose only permitted egress is the control plane, so the session token is useless outside the sandbox's network even if extracted.

### Hardening before agent code runs

Three steps execute before any agent code:

1. **Bytecode-only execution.** During the Docker build, all Python source is compiled to `.pyc` bytecode and every `.py` file is deleted. The framework code is loaded into memory as root, after which the source no longer exists on disk.
2. **Privilege drop.** The entrypoint starts as root (needed to read the root-owned bytecode), then immediately drops to an unprivileged `sandbox` user via `setuid`/`setgid`.
3. **Environment stripping.** After reading the three env variables into Python variables, they are deleted from `os.environ`. An agent that inspects its environment finds nothing.

### The control plane as a credentialed proxy

The control plane is a stateless FastAPI service that acts as the only path between the sandbox and the outside world. Every request carries a `Bearer: {session_token}` header; the control plane looks up the session, validates it is active, and executes the operation with the real credentials. Concrete responsibilities:

- **LLM proxying.** The sandbox sends only the new messages. The control plane owns the full conversation history in the database, reconstructs it on each call, forwards the complete context to the provider, and enforces cost caps and billing. This keeps the sandbox stateless: kill it, spin up a new one, and the conversation resumes.
- **File sync via presigned URLs.** The sandbox writes to a `/workspace` directory. To persist, it asks the control plane for presigned S3 URLs scoped to the session, then uploads directly to S3 without ever holding an AWS credential. Downloads work in reverse.
- **Gateway protocol.** Inside the sandbox, the agent talks to the control plane through an `AgentGateway` protocol (`invoke_llm`, `persist_messages`). `ControlPlaneGateway` sends HTTP in production; `DirectGateway` calls the LLM directly and keeps history in memory for local dev. The agent code does not know which backend it is using.

### Independent scaling

Because the control plane is stateless, each layer scales on its own bottleneck: more sandboxes for more agents (scheduled by Unikraft across metros), more control plane instances behind a load balancer for more throughput. The backend runs on ECS Fargate in private subnets behind an ALB, auto-scaling on CPU.

## Tradeoffs

Pattern 2 adds an extra network hop on every operation and three services to deploy instead of one. In practice the latency is noise next to LLM response times, and the operational shape is familiar to ops teams. The governing principle: the agent should have nothing worth stealing and nothing worth preserving.

## Where It Matters

For anyone running code-executing scraping or automation agents at scale, this is the security-versus-operability decision. The same control-plane-holds-credentials model appears in adjacent tools: just-in-time credential brokering ([agent-vault-proxy](../entities/agent-vault-proxy.md)), agent-to-production firewalls ([claw-patrol](../entities/claw-patrol.md)), runaway-loop limiters ([nakshguard](../entities/nakshguard.md)), and AI traffic proxies ([greyfox-community-edition](../entities/greyfox-community-edition.md)). Browser Use's own cloud browser layer uses a structurally similar control plane for placement and credential handling (see [browser-use](../entities/browser-use.md)).

## Related

- [browser-use](../entities/browser-use.md)
- [agent-vault-proxy](../entities/agent-vault-proxy.md)
- [claw-patrol](../entities/claw-patrol.md)
- [nakshguard](../entities/nakshguard.md)
- [greyfox-community-edition](../entities/greyfox-community-edition.md)
- [scraping-infrastructure](./scraping-infrastructure.md)

## Sources

- Larsen Cundric (Browser Use) — "How We Built Secure, Scalable Agent Sandbox Infrastructure," [https://browser-use.com/posts/two-ways-to-sandbox-agents](https://browser-use.com/posts/two-ways-to-sandbox-agents) (February 2026)
