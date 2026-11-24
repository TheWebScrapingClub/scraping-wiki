---
name: castle
type: entity
category: anti-bot
first_seen: 2026-11-24
last_updated: 2026-11-24
sources:
  - blog-how-to-bypass-x-twitter-login.md
---

# Castle

## What it is

Castle is an anti-bot system used by X (formerly Twitter) that scores tokens at each step of the login process to detect automation. It analyzes various signals from the user's device and interaction to determine if the login attempt is from a human or a bot.

## How it works

Castle's JavaScript SDK runs on the X login page, collecting signals about the user's environment and interactions. This data is used to mint a unique token for each step of the login process, such as submitting a username, password, or security code. These tokens are sent in the request body and are encrypted.

On the server side, Castle decrypts these tokens and scores them based on device and browser information, environment settings (like timezone and language), interaction data (mouse movements, keystroke timing), timing information, and a device ID. If the collected signals indicate automation, the token is scored negatively, leading to login restrictions.

## TWSC experience

Not yet tested by TWSC.

## Known limitations

The source document implies that standard automation tools like Selenium, even with stealth plugins, may still be detected by Castle due to their inherent differences in interaction patterns (e.g., machine-speed typing, lack of natural mouse movement) compared to human behavior.

## Related

- [x-twitter-ui-metrics](../entities/x-twitter-ui-metrics.md)
- [twitter-generator](../entities/twitter-generator.md)
- [client-side-bot-detection](../entities/client-side-bot-detection.md)


## Sources

- [https://takionapi.tech/blog/how-to-bypass-x-twitter-login](https://takionapi.tech/blog/how-to-bypass-x-twitter-login)
