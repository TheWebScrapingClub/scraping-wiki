---
name: medium-good-words-solver
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - blog-medium-good-words-solver.md
---

# Medium Good Words Solver

## What it is

Medium Good Words Solver is a Chrome extension designed to automate the process of playing and solving the "Good Words" game on Medium. The game is a multiplayer word game played on a 5x5 grid of letters, where players find words by connecting adjacent letters.

## How it works

The solver operates by first analyzing the game's network requests to identify key resources, including the game's dictionary (`words.txt`), word frequencies (`freq.bin`), and definitions (`vocab.json`). It also notes the use of a WebSocket for multiplayer functionality, which is protected by Cloudflare and can fall back to solo mode if it fails.

The core of the solver's functionality lies in its ability to reconstruct the game's logic. It loads the official dictionary into a trie data structure. Then, it systematically explores all possible letter combinations starting from each tile on the 5x5 grid, checking against the trie to find valid words of four or more letters. For solo play, it leverages the fact that the game board is deterministically generated based on the current round number, allowing it to predict future boards and words. To submit words, it programmatically manipulates the input field's value and triggers the necessary events to submit the word to the game.

## TWSC experience

Not yet tested by TWSC.
## Related

The Medium Good Words Solver interacts with Cloudflare for its WebSocket communication.


## Sources

- [https://takionapi.tech/blog/medium-good-words-solver](https://takionapi.tech/blog/medium-good-words-solver)
