#!/usr/bin/env python3
"""Build the static fallback news cards from ONE vetted public news.json.

Runs only against a build artifact, never Zenodo. Every announcement keeps an
exact source locator, with no links to GitHub implementation pull requests.
Four newest cards appear on the homepage; full history on news.html.
All links and bilingual text remain visible even without JavaScript.
"""
from __future__ import annotations
from datetime import date
import html
import json
from pathlib import Path
import re
import sys

DOI=re.compile(r"^https://doi\.org/10\.5281/zenodo\.[1-9][0-9]*$")
TITLE_SOURCE={
    "achievements.html#ghz-exact":(
        "View the formulas ↗","Смотреть формулы ↗","achievements.html?lang=en#ghz-exact"),
    "achievements.html":(
        "Explore research achievements ↗","Открыть достижения ↗","achievements.html?lang=en"),
    "publications/":(
        "Browse publications ↗","Перейти к публикациям ↗","publications/index.html?lang=en"),
}
KIND={
    "site_update":("Website update","Обновление сайта"),
    "publication_release":("Publication","Публикация"),
    "collection_update":("Publication collection","Коллекция публикаций"),
    "public_collection_release":("Publication collection","Коллекция публикаций"),
}


def e(v):
    return html.escape(str(v),quote=True)


def entries(root:Path):
    data=json.loads((root/"data/news.json").read_text(encoding="utf-8"))
    catalog=json.loads((root/"data/papers.json").read_text(encoding="utf-8"))
    if data.get("schema")!="cf-publication-updates/v1" or not isinstance(data.get("entries"),list):
        raise ValueError("Unsupported news schema")
    paper_dois={p["version_doi"] for p in catalog.get("papers",[]) if p.get("status")=="published"}
    out=[]
    for idx,item in enumerate(data["entries"]):
        if not isinstance(item,dict) or item.get("kind") not in KIND:
            raise ValueError("Unknown news type")
        stamp=item.get("date","")
        if not isinstance(stamp,str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}",stamp):
            raise ValueError("Invalid date")
        if date.fromisoformat(stamp).isoformat()!=stamp:
            raise ValueError("Invalid calendar date")
        for key in ("title","summary"):
            field=item.get(key)
            if not isinstance(field,dict) or set(field)!={"en","ru"}:
                raise ValueError("Incomplete EN/RU news copy")
            for value in field.values():
                if not isinstance(value,str) or not value.strip() or len(value)>3000:
                    raise ValueError("Empty/oversized news field")
        source=item.get("source")
        if source in TITLE_SOURCE:
            en,ru,url=TITLE_SOURCE[source]
            internal=True
        elif isinstance(source,str) and DOI.fullmatch(source):
            doi=source.removeprefix("https://doi.org/")
            if doi not in paper_dois:
                raise ValueError("News DOI not present in published catalogue: "+doi)
            en=ru=doi+" ↗"
            url=source
            internal=False
        else:
            raise ValueError("Unapproved news link source: "+str(source))
        # Distinguish real article releases and site / collection announcements.
        if item["kind"]=="publication_release" and internal:
            raise ValueError("Published paper announcement must cite a fixed DOI")
        if item["kind"]=="site_update" and not internal:
            raise ValueError("Website update must link to reader-facing site content")
        out.append({**item,"label_en":en,"label_ru":ru,"url":url,
                    "internal":internal,"order":idx})
    # Stable among equal dates: editorial order in the JSON is maintained.
    return sorted(out,key=lambda x:x["date"],reverse=True)


def localized_attrs(en,ru):
    return f'data-news-en="{e(en)}" data-news-ru="{e(ru)}"'


def card(event):
    en,ru=KIND[event["kind"]]
    source=e(event["source"])
    href=e(event["url"])
    ext='' if event["internal"] else ' target="_blank" rel="noopener noreferrer"'
    internal=f' data-news-source="{source}"' if event["internal"] else ""
    date_str=e(event["date"])
    return (
        '        <article class="news-item">\n'
        '          <div class="news-meta">'
        f'<time datetime="{date_str}">{date_str}</time>'
        f'<span class="news-type" {localized_attrs(en,ru)}>{e(en)}</span></div>\n'
        f'          <h3 {localized_attrs(event["title"]["en"],event["title"]["ru"])}>{e(event["title"]["en"])}</h3>\n'
        f'          <p {localized_attrs(event["summary"]["en"],event["summary"]["ru"])}>{e(event["summary"]["en"])}</p>\n'
        f'          <a class="news-source" href="{href}"{internal}{ext} '
        f'{localized_attrs(event["label_en"],event["label_ru"])}>{e(event["label_en"])}</a>\n'
        '        </article>'
    )


def splice(source,beg,end,replacement):
    i=source.find(beg)
    if i<0 or source.find(beg,i+1)>=0:
        raise ValueError("Expected unique news opening marker")
    j=source.find(end,i+len(beg))
    if j<0 or source.find(end,j+1)>=0:
        raise ValueError("Expected unique news closing marker")
    return source[:i+len(beg)]+"\n"+replacement+"\n      "+source[j:]


def build(root):
    root=Path(root)
    events=entries(root)
    index=root/"index.html"
    news=root/"news.html"
    home=index.read_text(encoding="utf-8")
    full=news.read_text(encoding="utf-8")
    home=splice(home,
        '<div class="news-items" id="news-items" aria-live="polite">',
        '<div class="news-all-link-wrap">',
        "\n".join(map(card,events[:4])))
    full=splice(full,
        '<div class="news-items news-all-grid" id="news-full-list" aria-live="polite">',
        '<p class="news-page-note"',
        "\n".join(map(card,events)))
    index.write_text(home,encoding="utf-8")
    news.write_text(full,encoding="utf-8")
    print(f"Static news generated: homepage={min(4,len(events))} / all={len(events)}; EN+RU accessible without JSON")


if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("Usage: python build_news_fallbacks.py PUBLIC_SITE_ROOT")
    build(Path(sys.argv[1]))
