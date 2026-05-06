---
name: wxpath
type: entity
category: library
first_seen: 2026-05-06
last_updated: 2026-05-06
sources:
  - rodricios-wxpath.md
---

# wxpath

## What it is

wxpath is a Python library for declarative web crawling using XPath. It allows you to describe traversal and extraction in a single expression, making it easier to perform recursive or paginated web crawling and extraction without writing imperative crawl loops.

## How it works

wxpath introduces the `url(...)` operator and the `///` syntax to enable recursive (or paginated) web crawling and extraction. The library executes the expression concurrently, breadth-first-*ish*, and streams results as they are discovered. For example, you can fetch a page, extract links, and stream them concurrently with a single expression.

```python
import wxpath

expr = "url('https://quotes.toscrape.com')//a/@href"

for link in wxpath.wxpath_async_blocking_iter(expr):
    print(link)
```

By using `///url(...)` syntax, wxpath can perform deep crawling up to a specified `max_depth`:

```python
import wxpath

path_expr = """
url('https://quotes.toscrape.com')
  ///url(//a/@href)
    //a/@href
"""

for item in wxpath.wxpath_async_blocking_iter(path_expr, max_depth=1):
    print(item)
```

## TWSC experience

Not yet tested by TWSC.
## Related

- [playwright](../entities/playwright.md)
- [hRequests](../entities/hrequests.md)
- [Scrapoxy](../entities/scrapoxy.md)


## Sources

- [https://github.com/rodricios/wxpath](https://github.com/rodricios/wxpath)
