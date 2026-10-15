#!/usr/bin/env python3
"""Build crawlable, static scholarly HTML from approved public Zenodo metadata.

The site must remain usable without JavaScript or live Zenodo access.
Optional same-directory PDFs are downloaded exclusively from numeric, pinned
public Zenodo version records, accepted only after PDF + MD5 + size checks.
Never read private manuscript directories or private GitHub credentials.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import urllib.error
import urllib.parse
import urllib.request

from latex2mathml.converter import convert as latex_to_mathml

DOMAIN = "https://math.a-martinevski.com"
ORCID = "0009-0000-4230-4414"
AUTHOR = "Alexandr Martinevski"
EMAIL = "math@a-martinevski.com"
DOI = re.compile(r"^10\.5281/zenodo\.(\d+)$")
CODE = re.compile(r"^P\d{2}$")
PDF = re.compile(r"^P\d{2}_[A-Za-z0-9][A-Za-z0-9._-]{0,150}\.pdf$")
MD5 = re.compile(r"^[a-f0-9]{32}$")
MAX_PDF = 64 * 1024 * 1024
ALLOWED_TAGS = {"p", "strong", "em", "span", "sup", "sub", "br"}


def esc(value):
    return html.escape(str(value), quote=True)


class AbstractHTML(HTMLParser):
    """Pass only a small, known, noninteractive subset of Zenodo markup."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED_TAGS:
            raise ValueError("Unexpected markup in published description: " + tag)
        if tag == "span":
            attributes = dict(attrs)
            if attributes.get("class") != "math inline" or len(attrs) != 1:
                raise ValueError("Unapproved span in abstract")
            self.parts.append('<span class="math inline">')
        else:
            if attrs:
                raise ValueError("Unexpected HTML attributes on " + tag)
            self.parts.append("<" + tag + ">")
        if tag != "br":
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise ValueError("Mismatched abstract markup: " + tag)
        self.parts.append("</" + tag + ">")

    def handle_data(self, data):
        self.parts.append(esc(data))

    def finish(self):
        if self.stack:
            raise ValueError("Unbalanced Zenodo abstract HTML")
        return "".join(self.parts)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)
    def text(self):
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def sanitized_abstract(source):
    parser=AbstractHTML()
    parser.feed(source)
    rendered=parser.finish()
    text_parser=PlainText()
    text_parser.feed(rendered)
    plain=text_parser.text()
    if len(plain)<300 or not rendered.startswith("<p>"):
        raise ValueError("Scholarly abstract is incomplete")
    # Render LaTeX into native, semantic MathML on the server. This avoids
    # exposing raw TeX to readers and requires no browser JavaScript or fonts.
    def inline_math(match):
        source_tex=html.unescape(match.group(1))
        mathml=latex_to_mathml(source_tex)
        if not mathml.startswith("<math"):
            raise ValueError("MathML converter returned unexpected HTML")
        return '<span class="math inline" aria-label="'+esc(source_tex)+'">'+mathml+'</span>'
    rendered,count=re.subn(r'<span class="math inline">\\\((.*?)\\\)</span>',
                           inline_math,rendered,flags=re.DOTALL)
    if '<span class="math inline">\\(' in rendered:
        raise ValueError("Unconverted LaTeX in published abstract")
    return rendered, plain


def load_data(root):
    catalogue=json.loads((root/"data/papers.json").read_text(encoding="utf-8"))
    scholarly={}
    shards=sorted((root/"data/scholarly").glob("part-*.json"))
    if not shards or any(not re.fullmatch(r"part-[0-9]{2}\.json",path.name) for path in shards):
        raise ValueError("Scholarly metadata shards missing or invalid")
    for path in shards:
        blob=json.loads(path.read_text(encoding="utf-8"))
        if blob.get("schema")!=1:
            raise ValueError("Invalid scholarly metadata schema")
        for key,value in blob["papers"].items():
            if key in scholarly:
                raise ValueError("Duplicated scholarly paper: "+key)
            scholarly[key]=value
    papers=catalogue.get("papers") or []
    if not papers or len(papers)!=len(scholarly) or {p["code"] for p in papers}!=set(scholarly):
        raise ValueError("Scholarly metadata must cover exactly all published paper codes")
    if len({p["code"] for p in papers})!=len(papers):
        raise ValueError("Duplicate paper codes in the public catalogue")
    for p in papers:
        s=scholarly[p["code"]]
        if p["status"]!="published" or not CODE.fullmatch(p["code"]):
            raise ValueError("Unpublished catalogue entry")
        if s["version_doi"]!=p["version_doi"] or s["concept_doi"]!=p["concept_doi"]:
            raise ValueError("DOI identity conflict: "+p["code"])
        if DOI.fullmatch(s["version_doi"]) is None or DOI.fullmatch(s["concept_doi"]) is None:
            raise ValueError("Invalid DOI")
        if s["record_id"]!=int(DOI.fullmatch(s["version_doi"]).group(1)):
            raise ValueError("Record ID conflict")
        if not PDF.fullmatch(s["pdf_filename"]) or not s["pdf_filename"].startswith(p["code"]):
            raise ValueError("PDF name mismatch")
        if not MD5.fullmatch(s["pdf_md5"]) or not (1000<s["pdf_size"]<=MAX_PDF):
            raise ValueError("PDF checksum or size missing")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}",s["publication_date"]):
            raise ValueError("Invalid publication date")
        if len(s["keywords"])<4 or len(set(s["keywords"]))!=len(s["keywords"]):
            raise ValueError("Missing or duplicated keywords")
        sanitized_abstract(s["description_html"])
    return papers,scholarly


def file_signature(path,source):
    if not path.is_file() or path.stat().st_size!=source["pdf_size"]:
        return False
    h=hashlib.md5()
    with path.open("rb") as f:
        start=f.read(5)
        h.update(start)
        if start!=b"%PDF-":
            return False
        for part in iter(lambda:f.read(128_000),b""):
            h.update(part)
    return h.hexdigest()==source["pdf_md5"]


def mirror_pdf(paper,source,repo_root,destination,allow_fetch):
    filename=source["pdf_filename"]
    target=destination/filename
    target.parent.mkdir(parents=True,exist_ok=True)
    # Old local PDFs may be used ONLY if byte-identical with the DOI release.
    path=paper.get("source_path")
    if isinstance(path,str) and re.fullmatch(r"papers/[a-z0-9-]+",path):
        local=repo_root/path/"paper.pdf"
        if file_signature(local,source):
            shutil.copyfile(local,target)
            return True
    if not allow_fetch:
        return False
    name=urllib.parse.quote(filename,safe="")
    url=f"https://zenodo.org/records/{source['record_id']}/files/{name}?download=1"
    req=urllib.request.Request(url,headers={
        "User-Agent":"CF-Dependence-Scholarly-Pages/1.0 (public PDF mirroring)",
        "Accept":"application/pdf"})
    try:
        with urllib.request.urlopen(req,timeout=18) as response:
            data=response.read(MAX_PDF+1)
        if (len(data)!=source["pdf_size"] or not data.startswith(b"%PDF-")
                or hashlib.md5(data).hexdigest()!=source["pdf_md5"]):
            return False
        target.write_bytes(data)
        return True
    except (OSError,urllib.error.URLError,TimeoutError,ValueError):
        return False


def meta(name,value,property=False):
    kind="property" if property else "name"
    return f'<meta {kind}="{esc(name)}" content="{esc(value)}">'


def localized(en,ru,tag="span",class_name=""):
    cls=f' class="{esc(class_name)}"' if class_name else ""
    return f'<{tag}{cls} data-en="{esc(en)}" data-ru="{esc(ru)}">{esc(en)}</{tag}>'


def langlink(href,label,css=""):
    cls=f' class="{css}"' if css else ""
    return f'<a{cls} data-preserve-lang data-base-href="{esc(href)}" href="{esc(href)}">{esc(label)}</a>'


def page_head(title,description,canonical,asset_prefix,assets,scholar=False,record=None,local_pdf=None,kind="WebPage"):
    tags=[
        '<!doctype html><html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        meta("robots","index,follow"),
        meta("description",description[:350]),
        f'<link rel="canonical" href="{esc(canonical)}">',
        f'<link rel="alternate" hreflang="en" href="{esc(canonical)}">',
        meta("og:type","article" if scholar else "website",True),
        meta("og:title",title,True),
        meta("og:url",canonical,True),
        f"<title>{esc(title)} — CF Dependence</title>",
        f'<link rel="stylesheet" href="{asset_prefix}assets/site.css?v={assets["css"]}">',
        f'<script src="{asset_prefix}assets/scholar.js?v={assets["js"]}" defer></script>',
    ]
    if scholar:
        date=record["publication_date"].replace("-","/")
        tags.extend([
            meta("citation_title",record["title"]),
            meta("citation_author",AUTHOR),
            meta("citation_author_orcid","https://orcid.org/"+ORCID),
            meta("citation_publication_date",date),
            meta("citation_doi",record["version_doi"]),
            meta("citation_abstract_html_url",canonical),
            meta("keywords",", ".join(record["keywords"])),
        ])
        if local_pdf:
            tags.append(meta("citation_pdf_url",canonical+urllib.parse.quote(record["pdf_filename"])))
    return "\n".join(tags)


def ld_script(graph):
    source=json.dumps(graph,ensure_ascii=False,separators=(",",":"))
    source=source.replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    return f'<script type="application/ld+json">{source}</script>'


def person():
    return {"@type":"Person","@id":DOMAIN+"/author/#researcher",
            "name":AUTHOR,"identifier":"https://orcid.org/"+ORCID,
            "sameAs":"https://orcid.org/"+ORCID,
            "url":DOMAIN+"/author/"}


def licence_url(code):
    accepted={"cc-by-4.0":"https://creativecommons.org/licenses/by/4.0/",
              "cc0-1.0":"https://creativecommons.org/publicdomain/zero/1.0/"}
    return accepted.get(code)


def site_nav(asset_prefix):
    return f"""<header class="scholar-top"><div class="wrap scholar-nav">
      {langlink(asset_prefix+"index.html","CF Dependence","scholar-brand")}
      <nav aria-label="Research navigation">
        {langlink(asset_prefix+"publications/index.html","All papers")}
        {langlink(asset_prefix+"author/index.html","Author & ORCID")}
        <button type="button" class="language" data-lang-toggle aria-label="Переключить интерфейс на русский">Русский</button>
      </nav></div></header>"""


def page_footer(asset_prefix):
    return f"""<footer class="scholar-footer"><div class="wrap">
      <span>© CF Dependence · {esc(AUTHOR)}</span>
      <span>{langlink(asset_prefix+"index.html","Research programme")}</span>
    </div></footer>"""


def paper_page(p,rec,assets,has_pdf):
    code=p["code"]
    canonical=f"{DOMAIN}/publications/{code}/"
    abstract,plain=sanitized_abstract(rec["description_html"])
    filename=rec["pdf_filename"]
    direct=f"https://zenodo.org/records/{rec['record_id']}/files/{urllib.parse.quote(filename)}?download=1"
    download=urllib.parse.quote(filename) if has_pdf else direct
    version=f"https://doi.org/{rec['version_doi']}"
    concept=f"https://doi.org/{rec['concept_doi']}"
    pdf=canonical+urllib.parse.quote(filename) if has_pdf else None
    title=rec["title"]
    data={"@context":"https://schema.org","@type":"ScholarlyArticle","@id":canonical+"#article",
          "headline":title,"name":title,"author":person(),
          "datePublished":rec["publication_date"],
          "identifier":{"@type":"PropertyValue","propertyID":"DOI","value":rec["version_doi"]},
          "url":canonical,"sameAs":version,"publisher":{"@type":"Organization","name":"Zenodo","url":"https://zenodo.org/"},
          "description":plain,"keywords":rec["keywords"],"isAccessibleForFree":True,
          "isPartOf":{"@type":"WebSite","name":"CF Dependence","url":DOMAIN+"/"}}
    if licence_url(rec["license"]):
        data["license"]=licence_url(rec["license"])
    if pdf:
        data["encoding"]={"@type":"MediaObject","encodingFormat":"application/pdf","contentUrl":pdf}
    sources="".join(f'<li>{esc(x)}</li>' for x in rec["keywords"])
    facts="".join(f"<li>{esc(h['en'])}</li>" for h in p["highlights"])
    bib_key="Martinevski"+rec["publication_date"][:4]+code
    bib=f"@misc{{{bib_key},\n  author = {{Martinevski, Alexandr}},\n  title = {{{title}}},\n  year = {{{rec['publication_date'][:4]}}},\n  doi = {{{rec['version_doi']}}},\n  url = {{{version}}}\n}}"
    head=page_head(title,plain,canonical,"../../",assets,scholar=True,record=rec,local_pdf=has_pdf)
    return "\n".join([
        head,ld_script(data),"</head><body class=\"scholar-paper\">",site_nav("../../"),
        '<main class="wrap scholar-layout"><article>',
        f'<div class="overline">{esc(code)} · {localized("RESEARCH PREPRINT","НАУЧНЫЙ ПРЕПРИНТ")}</div>',
        f'<h1 class="scholar-title">{esc(title)}</h1>',
        f'<p class="scholar-author citation_author">{esc(AUTHOR)} · <a href="https://orcid.org/{ORCID}" rel="me noopener noreferrer">ORCID {ORCID}</a></p>',
        f'<p class="scholar-date">{localized("Published version","Опубликованная версия")}: <time datetime="{esc(rec["publication_date"])}">{esc(rec["publication_date"])}</time> · DOI <a href="{esc(version)}">{esc(rec["version_doi"])}</a></p>',
        f'<section id="abstract" class="scholar-abstract"><h2>{localized("Abstract","Аннотация")}</h2>',
        abstract,"</section>",
        '<section class="scholar-keywords"><h2>'+localized("Keywords","Ключевые слова")+'</h2>',
        '<ul class="scholar-keyword-list">'+sources+"</ul></section>",
        '<section class="scholar-results"><h2>'+localized("Selected results","Основные результаты")+'</h2><ol>'+facts+"</ol></section>",
        '<section class="scholar-cite"><h2>'+localized("Citation and full text","Цитирование и полный текст")+'</h2>',
        f'<p><a class="news-all-link" href="{esc(download)}">{localized("Read the full PDF","Открыть полный PDF")} ↗</a></p>',
        f'<p>{localized("Fixed version DOI","DOI фиксированной версии")}: <a href="{esc(version)}">{esc(rec["version_doi"])}</a></p>',
        f'<p>{localized("All versions (concept DOI)","Все версии (Concept DOI)")}: <a href="{esc(concept)}">{esc(rec["concept_doi"])}</a></p>',
        '<h3>BibTeX</h3><pre class="scholar-bibtex"><code>'+esc(bib)+"</code></pre>",
        '</section>',
        '<p class="scholar-caution">'+localized("This page describes a research preprint and does not claim journal peer review.","Это описание научного препринта; журнальное рецензирование здесь не утверждается.")+"</p>",
        '</article></main>',page_footer("../../"),"</body></html>"
    ])


def bibliography_page(papers,records,assets):
    canonical=DOMAIN+"/publications/"
    count=len(papers)
    head=page_head("Research papers and scholarly abstracts",f"{count} research preprints with full abstracts, version DOIs, keywords and public PDFs.",canonical,"../",assets)
    items=[]
    for p in sorted(papers,key=lambda x:int(x["code"][1:])):
        r=records[p["code"]]
        href=f"{p['code']}/"
        items.append(
            f'<li class="scholar-list-item"><span class="code">{p["code"]}</span> '
            +langlink(href,r["title"])
            +f'<div class="scholar-list-meta">{esc(AUTHOR)} · {esc(r["publication_date"])} · '
            +f'<a href="https://doi.org/{esc(r["version_doi"])}">DOI: {esc(r["version_doi"])}</a></div>'
            +f'<p>{esc(p["summary"]["en"])}</p></li>'
        )
    listing="".join(items)
    data={"@context":"https://schema.org","@type":"CollectionPage","name":"CF Dependence research papers",
          "url":canonical,"author":person(),"mainEntity":{"@type":"ItemList",
          "itemListElement":[{"@type":"ListItem","position":i+1,"url":f"{DOMAIN}/publications/{p['code']}/"}
                             for i,p in enumerate(sorted(papers,key=lambda x:int(x["code"][1:])))]}}
    return "\n".join([
        head,ld_script(data),"</head><body class=\"scholar-index\">",site_nav("../"),
        '<main class="wrap scholar-layout"><article>',
        '<div class="overline">CF DEPENDENCE · PUBLICATIONS</div>',
        '<h1 class="scholar-title">'+localized("Research papers","Научные статьи")+"</h1>",
        '<p class="scholar-lead">'+localized(
           f"{count} research preprints. Each paper has a permanent, machine-readable page with its full published description, citation identifiers and links to the original Zenodo version.",
           f"{count} научных препринтов. Для каждой работы доступна отдельная индексируемая страница с полным описанием, DOI и ссылками на Zenodo.",
           tag="span")+'</p>',
        '<ol class="scholar-papers-list">'+listing+'</ol>',
        '</article></main>',page_footer("../"),"</body></html>"
    ])


def author_page(papers,records,assets):
    canonical=DOMAIN+"/author/"
    head=page_head(f"{AUTHOR} — ORCID and research works",
        "Independent researcher Alexandr Martinevski; ORCID identifier and bibliographic list of published CF Dependence research preprints.",
        canonical,"../",assets)
    data={"@context":"https://schema.org",**person(),
          "email":"mailto:"+EMAIL,
          "subjectOf":[{"@type":"ScholarlyArticle","@id":f"{DOMAIN}/publications/{p['code']}/#article"}
                       for p in papers]}
    rows=[]
    for p in sorted(papers,key=lambda x:int(x["code"][1:])):
        rec=records[p["code"]]
        rows.append(f'<li>{langlink("../publications/"+p["code"]+"/",rec["title"])}'
                    +f' · <a href="https://doi.org/{esc(rec["version_doi"])}">{esc(rec["version_doi"])}</a></li>')
    return "\n".join([
        head,ld_script(data),"</head><body class=\"scholar-author-page\">",site_nav("../"),
        '<main class="wrap scholar-layout"><article>',
        '<div class="overline">RESEARCHER · ORCID</div>',
        f'<h1 class="scholar-title">{AUTHOR}</h1>',
        '<p class="scholar-lead">'+localized("Independent researcher","Независимый исследователь")+'</p>',
        f'<p><strong>ORCID:</strong> <a rel="me noopener noreferrer" href="https://orcid.org/{ORCID}">{ORCID}</a></p>',
        f'<p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>',
        '<p>'+localized("Research areas: extremal probability, characteristic functions, prescribed marginals, optimal transport, harmonic analysis, algebra and mathematical statistics.",
                         "Области исследований: экстремальная вероятность, характеристические функции, заданные маргинали, оптимальный транспорт, гармонический анализ, алгебра и математическая статистика.")+'</p>',
        '<section><h2>'+localized("Published research works","Опубликованные научные работы")+'</h2>',
        '<ol class="scholar-author-works">'+"".join(rows)+'</ol></section>',
        f'<p>{localized("Author's scientific programme and research transparency statement:",
                        "Научная программа и информация об участии ИИ:")} '
        +langlink("../index.html#about","CF Dependence")+"</p>",
        '</article></main>',page_footer("../"),"</body></html>"
    ])


def build(source,dest,repo_root=None,fetch_pdfs=False):
    source=Path(source)
    dest=Path(dest)
    repo_root=Path(repo_root) if repo_root else source.parent
    papers,records=load_data(source)
    styles=(dest/"assets/site.css").read_bytes()
    scholar_js=(dest/"assets/scholar.js").read_bytes()
    hashes={"css":hashlib.sha256(styles).hexdigest()[:16],"js":hashlib.sha256(scholar_js).hexdigest()[:16]}
    pdf_status={}
    def get_pdf(p):
        s=records[p["code"]]
        output=dest/"publications"/p["code"]
        present=mirror_pdf(p,s,repo_root,output,allow_fetch=fetch_pdfs)
        return p["code"],present
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        pdf_status=dict(pool.map(get_pdf,papers))
    for p in papers:
        code=p["code"]
        folder=dest/"publications"/code
        folder.mkdir(parents=True,exist_ok=True)
        (folder/"index.html").write_text(
            paper_page(p,records[code],hashes,pdf_status[code]),encoding="utf-8")
    (dest/"publications"/"index.html").write_text(
        bibliography_page(papers,records,hashes),encoding="utf-8")
    (dest/"author").mkdir(parents=True,exist_ok=True)
    (dest/"author"/"index.html").write_text(
        author_page(papers,records,hashes),encoding="utf-8")
    # Sitemap is generated from the same verified catalogue; omit the
    # query-string legacy detail pages to avoid duplicate scholarly records.
    base=["/","/achievements.html","/news.html","/publications/","/author/"]
    urls=base+[f"/publications/{p['code']}/" for p in papers]
    sitemap='<?xml version="1.0" encoding="utf-8"?>\n'
    sitemap+='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for uri in urls:
        sitemap+=f"  <url><loc>{esc(DOMAIN+uri)}</loc></url>\n"
    sitemap+='</urlset>\n'
    (dest/"sitemap.xml").write_text(sitemap,encoding="utf-8")
    print(f"Scholar pages: {len(papers)} papers, bibliography + author, "
          f"verified same-directory PDFs: {sum(pdf_status.values())}/{len(papers)}; "
          "all abstracts and DOI metadata are always statically visible.")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("source",help="The checked-in website directory")
    ap.add_argument("destination",help="Public Pages artifact root")
    ap.add_argument("--repo-root",default=None)
    ap.add_argument("--fetch-pdfs",action="store_true",
                    help="Read-only public Zenodo downloads, verified against MD5 and size")
    args=ap.parse_args()
    build(args.source,args.destination,args.repo_root,args.fetch_pdfs)
