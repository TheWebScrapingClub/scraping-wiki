#!/usr/bin/env python3
"""
Finish the search tags of the built site. Quartz writes no canonical link and no
structured data, and uses one title for both the page heading and the search result.

    python3 postprocess_html.py <quartz content dir> <quartz public dir>

For every HTML page: a canonical link. For the pages that come from a Markdown file
(the content dir written by prepare_content.py): the search title (`seo_title`), the
description exactly as written in the frontmatter, and JSON-LD (breadcrumb, plus
Article for the summaries and TechArticle for the wiki pages).
"""
import html
import json
import re
import sys
from pathlib import Path

import yaml

SITE_URL = "https://wiki.scraping.club"
SITE_NAME = "The Web Scraping Wiki"
SUFFIX = " | " + SITE_NAME
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TITLE = re.compile(r"<title>.*?</title>", re.DOTALL)
TITLE_META = re.compile(r'(<meta (?:name|property)="(?:og:title|twitter:title)" content=")[^"]*(")')
DESC_META = re.compile(
    r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(")')
HOME_TITLE = "The Web Scraping Wiki: anti-bot systems, scraping tools, proxies"
NO_DESC = "No description provided"
SECTIONS = {
    "entities": "Entities", "concepts": "Concepts", "comparisons": "Comparisons",
    "timelines": "Timelines", "articles": "Article summaries",
}
PUBLISHER = {"@type": "Organization", "name": "The Web Scraping Club", "url": "https://www.scraping.club"}


def page_url(rel: Path) -> str:
    parts = list(rel.with_suffix("").parts)
    if parts[-1] == "index":
        parts = parts[:-1]
        return SITE_URL + "/" + "".join(p + "/" for p in parts)
    return SITE_URL + "/" + "/".join(parts)


def frontmatter(path: Path) -> dict:
    m = FM.match(path.read_text(encoding="utf-8"))
    try:
        meta = yaml.safe_load(m.group(1)) if m else {}
    except yaml.YAMLError:
        meta = {}
    return meta if isinstance(meta, dict) else {}


def structured_data(rel: Path, meta: dict, url: str) -> list:
    title = str(meta.get("title") or "")
    section = rel.parts[0] if len(rel.parts) > 1 else None
    if rel == Path("index.html"):
        return [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME,
                 "url": SITE_URL + "/", "publisher": PUBLISHER}]
    crumbs = [("Home", SITE_URL + "/")]
    if section in SECTIONS:
        crumbs.append((SECTIONS[section], f"{SITE_URL}/{section}/"))
    if rel.stem != "index":
        crumbs.append((title, url))
    out = [{
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i, "name": name, "item": item}
                            for i, (name, item) in enumerate(crumbs, 1)],
    }]
    if rel.stem == "index" or section not in SECTIONS:
        return out
    page = {
        "@context": "https://schema.org",
        "@type": "Article" if section == "articles" else "TechArticle",
        "headline": title[:110],
        "mainEntityOfPage": url,
        "publisher": PUBLISHER,
    }
    if meta.get("description"):
        page["description"] = str(meta["description"])
    if meta.get("date"):
        page["datePublished"] = str(meta["date"])
    if meta.get("modified"):
        page["dateModified"] = str(meta["modified"])
    if section == "articles":
        page["author"] = {"@type": "Person", "name": "Pierluigi Vinciguerra"}
        if meta.get("canonical_url"):
            page["isBasedOn"] = str(meta["canonical_url"])
    else:
        page["author"] = PUBLISHER
        page["about"] = {"@type": "Thing", "name": str(meta.get("name") or title)}
    return out + [page]


def main():
    content, public = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    metas = {}
    for md in content.rglob("*.md"):
        rel = md.relative_to(content).with_suffix(".html")
        metas[Path(str(rel).replace(" ", "-"))] = frontmatter(md)

    done = with_meta = 0
    for path in sorted(public.rglob("*.html")):
        rel = path.relative_to(public)
        if rel == Path("404.html"):
            continue
        page = path.read_text(encoding="utf-8")
        if "</head>" not in page or 'rel="canonical"' in page:
            continue
        url = page_url(rel)
        extra = f'<link rel="canonical" href="{html.escape(url, quote=True)}"/>'
        meta = metas.get(rel)
        if meta is not None:
            with_meta += 1
            if rel == Path("index.html"):
                meta["seo_title"] = HOME_TITLE
            if meta.get("seo_title"):
                full = str(meta["seo_title"]) + ("" if rel == Path("index.html") else SUFFIX)
                full = html.escape(full, quote=True)
                page = TITLE.sub(lambda _: f"<title>{full}</title>", page, count=1)
                page = TITLE_META.sub(lambda m: m.group(1) + full + m.group(2), page)
            if meta.get("description"):
                desc = html.escape(" ".join(str(meta["description"]).split()), quote=True)
                page = DESC_META.sub(lambda m: m.group(1) + desc + m.group(2), page)
            for block in structured_data(rel, meta, url):
                text = json.dumps(block, ensure_ascii=False).replace("</", "<\\/")
                extra += f'<script type="application/ld+json">{text}</script>'
        if NO_DESC in page:  # tag and folder pages that have no text of their own
            name = TITLE.search(page).group(0)[7:-8].replace(SUFFIX, "").replace("Tag: ", "")
            desc = html.escape(f"Wiki pages and article summaries about {name} on {SITE_NAME}.", quote=True)
            page = DESC_META.sub(lambda m: m.group(1) + desc + m.group(2), page)
        page = page.replace("</head>", extra + "</head>", 1)
        path.write_text(page, encoding="utf-8")
        done += 1
    sitemap = public / "sitemap.xml"  # Quartz leaves out the XML declaration
    if sitemap.exists():
        xml = sitemap.read_text(encoding="utf-8")
        if not xml.startswith("<?xml"):
            sitemap.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + xml, encoding="utf-8")
    print(f"search tags written on {done} pages ({with_meta} with page metadata)")


if __name__ == "__main__":
    main()
