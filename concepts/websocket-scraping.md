---
name: websocket-scraping
type: concept
first_seen: 2024-04-04
last_updated: 2026-04-22
sources:
  - https://substack.thewebscraping.club/p/scraping-real-time-data-bitstamp
  - https://substack.thewebscraping.club/p/how-to-get-data-from-polymarket-fast
  - https://substack.thewebscraping.club/p/how-fast-can-you-call-polymarket-apis
---

# WebSocket Scraping

## Definition

WebSocket scraping is the practice of connecting to a site's WebSocket endpoint directly, subscribing to the same channels the browser subscribes to, and receiving the same real-time data stream. Unlike HTTP scraping, which is request-response, WebSocket connections are persistent and bidirectional. The server pushes updates without the client polling.

## How It Works

A WebSocket connection starts as a plain HTTP request with an `Upgrade: websocket` header. The server acknowledges with `101 Switching Protocols`, and from that point the connection is held open. Data flows in frames rather than HTTP requests.

Identifying a WebSocket endpoint in DevTools requires filtering by the WS type (not Fetch/XHR). Once the connection is selected, the Messages tab shows all frames sent and received. The first frames from the client are typically subscription messages — the client tells the server which channels or topics it wants to follow.

To replicate this in Python, the `websocket-python` library provides a callback-based API:

```python
ws = websocket.WebSocketApp(
    url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    header=HEADERS
)
ws.run_forever()
```

The `on_open` callback fires when the handshake completes. The subscription message (copied from the DevTools Messages tab) is sent there. The `on_message` callback receives each incoming frame. `run_forever()` blocks and keeps the connection alive until closed.

## Protocols Inside WebSocket

Not all WebSocket traffic is JSON. Some platforms use different messaging protocols transmitted over the WebSocket transport layer.

Bitstamp uses straightforward JSON subscriptions and responses. A subscription to `live_trades_btcusd` looks like `{"event":"bts:subscribe","data":{"channel":"live_trades_btcusd"}}`.

Sofascore uses NATS messaging over WebSocket. The initial connection message is a NATS-format string (`CONNECT {...}`), and subscriptions use NATS syntax (`SUB sport.football 1`). NATS requires periodic PING/PONG frames to keep the connection alive — a scraper that does not implement this will have the connection dropped after a short idle period.

Polymarket exposes a WebSocket at `wss://ws-subscriptions-clob.polymarket.com/ws/` for real-time order book updates and price changes. For high-frequency monitoring, this feed eliminates the need for HTTP polling entirely: "the fastest request is the one you never have to make."

## When to Use WebSockets vs HTTP Polling

WebSocket connections are appropriate when:
- The target data updates faster than once per second
- The platform explicitly uses WebSocket for real-time feeds (visible in DevTools)
- Polling would require a request rate that triggers rate limiting

For Polymarket's prediction market data, we benchmarked HTTP polling vs WebSocket alternatives. The HTTP polling approach with aiohttp from an AWS eu-west-2 instance (co-located with Polymarket's origin in London) reached 3,012 requests per second with 50 concurrent connections. The WebSocket feed is still preferable for this use case because it eliminates the server-side processing overhead entirely and reduces latency to the time between state changes.

For Bitstamp's trade feed, HTTP polling is not a viable alternative — the data updates multiple times per second and is inherently push-based. WebSocket is the only practical approach.

## What We Tested

We connected to Bitstamp's `wss://ws.bitstamp.net/` endpoint and subscribed to `live_trades_btcusd`. The subscription message was copied directly from the DevTools Messages tab and sent in the `on_open` callback. The connection received a stream of live Bitcoin-USD trade events with no authentication required.

We also attempted the same approach on Sofascore and encountered the NATS protocol requirement. Without implementing the NATS PING/PONG keepalive, the connection dropped after a few minutes.

## Current State

WebSocket scraping is straightforward when the protocol is JSON. The main complications are alternative messaging protocols (NATS, STOMP, custom binary) that require protocol-specific handling, and keepalive requirements that vary by platform. For most financial and betting targets where real-time data matters, the WebSocket endpoint will be more reliable and efficient than polling internal REST APIs.

## Related

- [api-scraping](./api-scraping.md)
- [http-performance](./http-performance.md)
