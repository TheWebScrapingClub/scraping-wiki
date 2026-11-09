---
name: softpasskey
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - forging-passkeys.md
---

# softpasskey

## What it is

softpasskey is a cross-platform command-line tool designed to register a fake passkey and log users into websites without requiring a physical security key. It achieves this by impersonating a FIDO2 device over USB-Human Interface Device (HID) and forging passkey signatures.

## How it works

The tool operates by intercepting and manipulating the communication between a browser and a FIDO2 authenticator. It first captures the raw communication traffic, typically using tools like Wireshark, to understand the FIDO2 protocol (CTAP2) and its data structures (CBOR/COSE).

softpasskey then reimplements the CTAP2 state machine in Rust. By injecting deterministic cryptographic keys, it can generate reproducible passkey signatures. This allows it to forge credentials and replay signatures, enabling automated headless logins on websites that rely on WebAuthn for authentication. The project also explores hijacking browser-specific virtual authenticators, such as Chrome's hidden Virtual Authenticator via the DevTools Protocol, to facilitate this process.

## TWSC experience

Not yet tested by TWSC.
## Related

The source document mentions the following related technologies and concepts:
* **USB-HID**: The tool uses USB-HID to impersonate a FIDO2 device.
* **CTAP2**: The tool captures and reimplements the CTAP2 protocol.
* **CBOR/COSE**: The tool decodes and manipulates CBOR/COSE data structures.
* **WebAuthn**: The tool aims to automate logins on sites that use WebAuthn.
* **DevTools Protocol**: The tool explores hijacking browser virtual authenticators via this protocol.


## Sources

- [https://nullpt.rs/forging-passkeys](https://nullpt.rs/forging-passkeys)
