---
name: esp32
type: entity
category: tool
first_seen: 2026-09-23
last_updated: 2026-09-23
sources:
  - hack-tramp-ESP-MQTTunnel.md
---

# ESP32

## What it is

The ESP32 functions as the hardware endpoint in an MQTT TCP proxy setup. It connects to Wi-Fi and is responsible for receiving commands and forwarding the tunneled TCP traffic to the target server.

## How it works

The ESP32 subscribes to an MQTT topic to receive client-to-server bytes. A local Python script acts as an HTTP proxy on the laptop, parsing the `CONNECT` request, publishing an `open` message over MQTT, and streaming the raw TLS bytes. The ESP32 receives these messages, establishes a real TCP socket to the target host, and forwards the data.

Responses from the server are sent back through the MQTT `res` topic, received by the Python proxy, and relayed back to the client.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The ESP32 has limited resources, which restricts its ability to handle a large number of simultaneous connections. It is not suitable for loading pages in multiple tabs concurrently.

## Related

* [python-requests](../entities/python-requests.md)
* [proxy-server](../entities/proxy-server.md)
* [socks5-proxy](../entities/socks5-proxy.md)


## Sources

- [https://github.com/hack-tramp/ESP-MQTTunnel](https://github.com/hack-tramp/ESP-MQTTunnel)
