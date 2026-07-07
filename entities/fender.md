---
name: fender
type: entity
category: tool
first_seen: 2026-07-07
last_updated: 2026-07-07
sources:
  - marketplace-actions-fender-ci.md
---

# fender

## What it is

fender is a transparent Docker Unix socket proxy designed to eliminate the lock-in to the implicit Docker Hub registry. It operates without requiring changes to Dockerfiles, CI scripts, or standard CLI habits.

## How it works

fender functions by sitting between the Docker CLI and the Docker daemon. Upon startup, it registers itself as a Docker context and activates it, ensuring that all Docker tooling routes through fender automatically. When fender is shut down, it removes its context and restores the previous Docker context.

This mechanism allows Docker commands, such as `docker pull nginx:latest`, to be rewritten to pull from a custom registry mapping, for example, routing `docker.io/library/nginx:latest` to `registry.example.com/library/nginx:latest`.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://github.com/marketplace/actions/fender-ci](https://github.com/marketplace/actions/fender-ci)
