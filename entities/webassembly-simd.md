---
name: webassembly-simd
type: entity
category: library
first_seen: 2026-05-20
last_updated: 2026-05-20
sources:
  - writing-wasm-simd-fingerprinting.md
---

# WebAssembly SIMD

## What it is

WebAssembly SIMD refers to Single Instruction, Multiple Data operations introduced to the WebAssembly specification. These operations are designed to introduce a portable subset of vector operations that typically map directly to commonly used hardware instructions on the host CPU. This feature is used to probe hardware execution characteristics for fingerprinting purposes.

## How it works

Browser engines, such as V8 or JavaScriptCore (JSC), are responsible for mapping these SIMD operations to native machine code for the host CPU. The execution latency varies across different CPU models due to physical circuit design, pipeline depth, and the structural efficiency of their execution units.

The fingerprinting opportunity arises when complex operations, such as byte permutations, lack a dedicated hardware path and require software emulation. By placing these SIMD operations in a dependency chain loop, the system forces the CPU to reveal the raw instruction latency, which is the physical time it takes for a signal to propagate through the execution unit.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

Browser vendors implement countermeasures against anti-timing attacks, such as degrading the resolution of timers like `performance.now()` to 0.1ms. To overcome this limitation, the technique involves placing SIMD operations in massive loops of millions of iterations and dividing the measured duration by the iteration count to reduce the impact of timer degradation.

## Related

- [browser-fingerprinting](../concepts/browser-fingerprinting.md)
- [tls-fingerprinting](../concepts/tls-fingerprinting.md)


## Sources

- [https://blog.azerpas.com/writing/wasm-simd-fingerprinting/](https://blog.azerpas.com/writing/wasm-simd-fingerprinting/)
