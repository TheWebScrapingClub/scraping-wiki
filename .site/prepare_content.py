#!/usr/bin/env python3
"""
Turn the wiki repository into the content folder of the public site (Quartz).

    python3 prepare_content.py <repo root> <quartz content dir>

The repository stays as it is for GitHub and Obsidian readers; the site copy gets:
- README.md as the home page, index.md as /catalog;
- a `title` (from the first heading), dates and tags in the frontmatter of every page;
- relative .md links turned into site links;
- campaign parameters on links to www.scraping.club, and a subscribe line on wiki pages.
"""
import re
import shutil
import sys
from pathlib import Path

import yaml

UTM = "utm_source=wiki&utm_medium=referral&utm_campaign=wiki_page"
SKIP_DIRS = {".git", ".github", ".site", ".obsidian"}
SKIP_FILES = {"log.md", ".last_wiki_update", ".gitignore"}
CTA_DIRS = {"entities", "concepts", "comparisons", "timelines"}
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1 = re.compile(r"^# +(.+?)\s*$", re.MULTILINE)
MD_LINK = re.compile(r"\]\((?!https?:|mailto:|#)([^)\s#]*?)\.md(#[^)\s]*)?\)")
TWSC_LINK = re.compile(r"\((https://www\.scraping\.club(?:/[^)\s?#]*)?)\)")
CTA = (
    "\n\n---\n\n"
    "*The Web Scraping Wiki is compiled from the tests and research published on "
    f"[The Web Scraping Club](https://www.scraping.club/?{UTM}), the newsletter for web scraping "
    f"professionals. [Subscribe](https://www.scraping.club/subscribe?{UTM}) to get the next "
    "article in your inbox.*\n"
)


def site_link(m):
    target, anchor = m.group(1), m.group(2) or ""
    parent, _, base = target.rpartition("/")
    prefix = parent + "/" if parent else ""
    if base == "README":
        return f"]({prefix or './'}{anchor})"
    if base == "index":
        base = "catalog"
    return f"]({prefix}{base}{anchor})"


def convert(rel: Path, text: str) -> str:
    m = FM.match(text)
    meta, body = {}, text
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[m.end():]
    if not isinstance(meta, dict):
        meta = {}

    h1 = H1.search(body)
    if h1:
        meta.setdefault("title", re.sub(r"[*_`]", "", h1.group(1)))
        body = body[:h1.start()] + body[h1.end():].lstrip("\n")
    if rel.name == "README.md":
        meta["title"] = "The Web Scraping Wiki"
    elif rel.name == "index.md":
        meta["title"] = "Index of all pages"
    meta.setdefault("title", str(meta.get("name") or rel.stem.replace("-", " ")))

    created = meta.get("publish_date") or meta.get("first_seen")
    modified = meta.get("last_updated") or meta.get("publish_date")
    if created:
        meta.setdefault("date", str(created))
    if modified:
        meta.setdefault("modified", str(modified))
    if meta.get("topics") and not meta.get("tags"):
        meta["tags"] = list(meta["topics"])

    body = MD_LINK.sub(site_link, body)
    body = TWSC_LINK.sub(lambda x: f"({x.group(1)}?{UTM})", body)
    if rel.parts[0] in CTA_DIRS:
        body = body.rstrip() + CTA

    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n" + body


def main():
    src, dst = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if dst.exists():
        shutil.rmtree(dst)
    pages = 0
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        if not path.is_file() or SKIP_DIRS & set(rel.parts) or rel.name in SKIP_FILES:
            continue
        out = dst / rel
        if rel == Path("README.md"):
            out = dst / "index.md"
        elif rel == Path("index.md"):
            out = dst / "catalog.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".md":
            out.write_text(convert(rel, path.read_text(encoding="utf-8")), encoding="utf-8")
            pages += 1
        else:
            shutil.copy2(path, out)
    print(f"prepared {pages} pages in {dst}")


if __name__ == "__main__":
    main()
