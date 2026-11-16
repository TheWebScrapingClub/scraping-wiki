#!/usr/bin/env python3
"""
Turn the wiki repository into the content folder of the public site (Quartz).

    python3 prepare_content.py <repo root> <quartz content dir>

The repository stays as it is for GitHub and Obsidian readers; the site copy gets:
- README.md as the home page, index.md as /catalog;
- a `title` (from the first heading), dates and tags in the frontmatter of every page;
- relative .md links turned into site links;
- campaign parameters on links to www.scraping.club, and a subscribe line on wiki pages;
- search titles and descriptions from .site/seo.json (written by build_wiki_seo.py);
- internal links: the sources of a wiki page point to the article summaries, and every
  summary lists the wiki pages built on that article;
- robots.txt.

postprocess_html.py then finishes the job on the built HTML (canonical, structured data).
"""
import json
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
SITE_URL = "https://wiki.scraping.club"
WIKI_DIRS = ("entities", "concepts", "comparisons", "timelines")
SOURCE_LINE = re.compile(
    r"^- \[https?://(?:www\.scraping\.club|substack\.thewebscraping\.club)/p/([^\]/?#]+)\]\([^)]*\)\s*$",
    re.MULTILINE,
)
ARTICLE_URL = re.compile(r"(?:www\.scraping\.club|substack\.thewebscraping\.club)/p/([A-Za-z0-9_-]+)")
READ_FULL = re.compile(r"^\[Read the full article on The Web Scraping Club\]", re.MULTILINE)
MAX_RELATED = 12
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


def top_heading(body):
    """The page's own H1: the first one, unless it is a `# comment` inside a code block."""
    h1 = H1.search(body)
    return h1 if h1 and "```" not in body[:h1.start()] else None


def split(text):
    m = FM.match(text)
    meta, body = {}, text
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[m.end():]
    return (meta if isinstance(meta, dict) else {}), body


def load_site_data(src: Path):
    """Article titles, the wiki pages built on each article, and the search metadata."""
    articles, related = {}, {}
    for path in sorted((src / "articles").glob("*.md")):
        meta, _ = split(path.read_text(encoding="utf-8"))
        if meta.get("type") == "article_summary":
            articles[path.stem] = str(meta.get("title") or path.stem)
    for folder in WIKI_DIRS:
        for path in sorted((src / folder).glob("*.md")):
            meta, body = split(path.read_text(encoding="utf-8"))
            h1 = top_heading(body)
            name = str(meta.get("name") or (h1.group(1) if h1 else path.stem.replace("-", " ")))
            slugs = {str(x)[:-3] for x in (meta.get("sources") or []) if str(x).endswith(".md")}
            slugs |= set(ARTICLE_URL.findall(body))
            for slug in slugs & articles.keys():
                related.setdefault(slug, []).append((folder, path.stem, name))
    seo_file = src / ".site" / "seo.json"
    seo = json.loads(seo_file.read_text(encoding="utf-8")) if seo_file.exists() else {}
    return {"articles": articles, "related": related, "seo": seo}


def convert(rel: Path, text: str, data: dict) -> str:
    meta, body = split(text)

    h1 = top_heading(body)
    if h1:
        meta.setdefault("title", re.sub(r"[*_`]", "", h1.group(1)))
        body = body[:h1.start()] + body[h1.end():].lstrip("\n")
    if rel == Path("README.md"):
        meta["title"] = "The Web Scraping Wiki"
        body = re.sub(r"^Browse it as a website:.*\n\n?", "", body, flags=re.MULTILINE)
    elif rel == Path("index.md"):
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

    seo = data["seo"].get(rel.as_posix()) or {}
    if seo.get("title"):
        meta["seo_title"] = seo["title"]
    if seo.get("description"):
        meta["description"] = seo["description"]

    if rel.parts[0] in WIKI_DIRS:
        # Sources: the article title as link text, pointing to its summary and to the article.
        def source(m):
            slug = m.group(1)
            if slug not in data["articles"]:
                return m.group(0)
            title = data["articles"][slug].replace("[", "(").replace("]", ")")
            return (f"- [{title}](../articles/{slug}.md) "
                    f"([full article](https://www.scraping.club/p/{slug}))")
        body = SOURCE_LINE.sub(source, body)
    elif rel.parts[0] == "articles" and rel.stem in data["related"]:
        pages = sorted(data["related"][rel.stem], key=lambda p: (WIKI_DIRS.index(p[0]), p[2].lower()))
        block = "## Related pages in the wiki\n\n" + "\n".join(
            f"- [{name}](../{folder}/{stem}.md)" for folder, stem, name in pages[:MAX_RELATED]) + "\n\n"
        m = READ_FULL.search(body)
        body = body[:m.start()] + block + body[m.start():] if m else body.rstrip() + "\n\n" + block

    body = MD_LINK.sub(site_link, body)
    body = TWSC_LINK.sub(lambda x: f"({x.group(1)}?{UTM})", body)
    if rel.parts[0] in CTA_DIRS:
        body = body.rstrip() + CTA

    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n" + body


def main():
    src, dst = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if dst.exists():
        shutil.rmtree(dst)
    data = load_site_data(src)
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
            out.write_text(convert(rel, path.read_text(encoding="utf-8"), data), encoding="utf-8")
            pages += 1
        else:
            shutil.copy2(path, out)
    (dst / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"prepared {pages} pages in {dst} ({len(data['articles'])} summaries, "
          f"{len(data['related'])} with related wiki pages, {len(data['seo'])} search entries)")


if __name__ == "__main__":
    main()
