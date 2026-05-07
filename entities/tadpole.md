---
name: tadpole
type: entity
category: tool
first_seen: 2026-05-07
last_updated: 2026-05-07
sources:
  - tadpolehq-com.md
---

# Tadpole

## What it is

Tadpole is a language designed for writing declarative, modular scraping code. It abstracts away the complexity of interacting with the browser, making it easier to build scrapers.

## How it works

Tadpole allows you to import modules from local files or remote repositories, enabling composable scraping code. The language simplifies the process of building scrapers by abstracting the browser interaction.

### Example

```sh
tadpole run redfin.kdl --input '{"text": "Seattle, WA"}' --auto --headless --output output.json
```

```kdl
import "modules/redfin/mod.kdl" repo="github.com/tadpolehq/community"

main {
  new_page {
    redfin.search text="=text"
    wait_until
    redfin.extract_from_card extract_to="addresses" {
      address {
        redfin.extract_address_from_card
      }
    }
  }
}

{
  "addresses": [
    {
      "address": "2011 E James St, Seattle, WA 98122"
    },
    {
      "address": "8020 17th Ave NW, Seattle, WA 98117"
    },
    {
      "address": "4015 SW Donovan St, Seattle, WA 98136"
    },
    {
      "address": "116 13th Ave, Seattle, WA 98122"
    }
  ]
}
```

## TWSC Experience

Not yet tested by TWSC.

## Related

- [playwright](../entities/playwright.md)
- [goscrapy](../entities/goscrapy.md)
- [Scrapoxy](../entities/scrapoxy.md)


## Sources

- [https://tadpolehq.com/](https://tadpolehq.com/)
