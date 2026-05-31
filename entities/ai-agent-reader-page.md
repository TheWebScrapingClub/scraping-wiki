---
name: ai-agent-reader-page
type: entity
category: anti-bot
first_seen: 2026-05-31
last_updated: 2026-05-31
sources:
  - taken-agents.md
---

# AI Agent Reader Page

## What it is

This page is designed to present different content versions of a web page, distinguishing between what a human reader sees and what a software agent reads. It serves as a specimen page to observe how machines process information compared to human consumption.

## How it works

The page displays two distinct views: one for a person, showing a standard developer-tools landing page, and another passage written specifically for software agents. The agent-readable content is delivered inside a `<template data-agent-readable>` tag, which is present in the server HTML but not rendered to humans.

The page tracks interactions, noting whether a visitor is a human or a software reader, and measures metrics such as JS execution and DOM rendering. It also leaves phrases in the markup for the next reader, demonstrating how content can be segmented for different types of consumers.

## TWSC experience

Not yet tested by TWSC.

## Sources

- [https://sinceyouarrived.world/taken/agents](https://sinceyouarrived.world/taken/agents)
