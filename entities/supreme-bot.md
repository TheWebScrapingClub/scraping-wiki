---
name: supreme-bot
type: entity
category: tool
first_seen: 2026-11-09
last_updated: 2026-11-09
sources:
  - anatomy-of-a-supreme-bot-part-1.md
---

# Supreme bot

## What it is

A Supreme bot is a tool designed to automate the process of purchasing items from the Supreme website. This particular type of bot focuses on utilizing the mobile endpoints of the Supreme site to fetch and post data, rather than directly parsing the Document Object Model (DOM) of the web pages.

## How it works

Supreme bots operate in a series of steps to secure items. Initially, they identify a desired item by searching for keywords or attributes and storing its unique ID. This ID is then used to access the item's specific endpoint, from which style and sizing information is retrieved. The bot proceeds to add the selected item to the cart, initiate the checkout process, and finally, verify if the purchase was successful.

The process of finding items involves querying the `mobile_stock.json` endpoint, which Supreme uses to display items on its mobile site. This endpoint is updated frequently and provides a JSON object containing details for all items in the shop, including their names, IDs, images, and prices. Bots can parse this JSON to extract the necessary information, such as the item's ID, by iterating through categories or focusing on newly added items.

## TWSC experience

Not yet tested by TWSC.
## Related

The Supreme bot interacts with web endpoints and fetches data, which is a common task in web scraping. While not explicitly mentioned in the provided text, the process of interacting with web services and handling data is fundamental to many scraping tools.

- [API Scraping](../concepts/api-scraping.md)
- [HTTP Performance in Scraping](../concepts/http-performance.md)


## Sources

- [https://nullpt.rs/anatomy-of-a-supreme-bot-part-1](https://nullpt.rs/anatomy-of-a-supreme-bot-part-1)
