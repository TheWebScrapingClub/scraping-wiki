---
name: bytecode-traversal
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - devirtualizing-nike-vm-2.md
---

# Bytecode Traversal

## What it is

Bytecode Traversal is a method for disassembling virtual machine bytecode. It analyzes the control flow of the bytecode and generates human-readable pseudocode without actually executing the bytecode. This approach aims to provide a static analysis of the code's structure and logic.

## How it works

The process begins by constructing a disassembler. Unlike a linear sweep which can be easily misled by unreachable code or misinterpretations, Bytecode Traversal employs a recursive approach. It starts by disassembling instructions sequentially, but when it encounters jump instructions, it follows them. Conditional jumps are branched and stored for later disassembly.

This recursive method allows for the analysis of control flow, enabling the identification of function definitions and loops. It is more robust against manipulation because it only disassembles reachable code. The method strictly avoids executing the bytecode or evaluating operations, focusing instead on transparency and understanding the origin and destination of values, which is deemed more valuable for analysis than the evaluated results themselves.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The source mentions that static recursive traversal can still be susceptible to bloat, as it cannot identify impossible branches.

## Related

- [vm-based-javascript-obfuscation](../concepts/vm-based-javascript-obfuscation.md)


## Sources

- [https://nullpt.rs/devirtualizing-nike-vm-2](https://nullpt.rs/devirtualizing-nike-vm-2)
