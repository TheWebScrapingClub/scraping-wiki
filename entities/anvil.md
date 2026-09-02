---
name: anvil
type: entity
category: proxy-provider
first_seen: 2026-09-02
last_updated: 2026-09-02
sources:
  - ThatXliner-anvil.md
---

# Anvil

## What it is

Anvil is a proxy designed to allow GitHub-compatible tools to interact seamlessly with a Forgejo instance, making it appear as if the instance were GitHub. It enables tools like `gh repo list`, Renovate, and CI status reporting to function correctly against a Forgejo backend without requiring rewrites.

## How it works

Under the hood, Anvil utilizes Shotgun, which functions as an OpenAPI-to-OpenAPI translation proxy. This translation is powered by a curated configuration file, `mappings.toml`, which defines the specific mapping between GitHub and Forgejo endpoints.

The system is tested live against Codeberg to ensure accuracy. The process involves trimming and editing OpenAPI specifications (`specs/trim_github.py`, `specs/trim_forgejo.py`) and synchronizing the mappings before deployment.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Anvil requires HTTPS for the `gh` command. Since Anvil speaks plain HTTP, a reverse proxy (such as Caddy, nginx, or Cloudflare Tunnel) must be placed in front of it for `gh` usage. Certain features are not supported, including git ref creation/updates, Actions variable creation, reading a single secret back, Dependabot, Codespaces, GitHub Apps, GraphQL, Packages, and code scanning, which result in a 501 error.

## Related

- [3rd-party-proxy](../entities/3rd-party-proxy.md)
- [proxy-server](../entities/proxy-server.md)


## Sources

- [https://github.com/ThatXliner/anvil](https://github.com/ThatXliner/anvil)
