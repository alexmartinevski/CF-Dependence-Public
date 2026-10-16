#!/usr/bin/env python3
"""Read-only post-deploy SEO/Scholar crawlability audit, not a Google index check.

Requires only the Python standard library. Inspects the actual HTTPS hostname,
published sitemap, 21 (or N) scholarly pages, and byte-verified PDF mirrors.
Never requests any indexing and never sends authenticated API traffic.
"""
from __future__ import annotations
import argparse
import concurrent.futures
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import socket
import ssl
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

HOST = "math.a-martinevski.com"
BASE = "https://" + HOST
ROOT = Path(__file__).resolve().parents[1]
PDF_LIMIT = 64 * 1024 * 1024
UA = "CF-Dependence-ReadOnly-SEO-Audit/1.0"


def expected_records(root: Path):
    catalog = json.loads((root / "data/publications.json").read_text(encoding="utf-8"))
    if catalog.get("schema") != "cf-publications/v3":
        raise ValueError("Unknown publication schema")
    records = {}
    for code, paper in catalog["papers"].items():
        if not re.fullmatch(r"P[0-9]{2}", code):
            raise ValueError("Invalid paper ID: " + code)
        pub = paper["publication"]
        releases = pub.get("releases") or []
        if pub["status"] != "published" or not releases:
            raise ValueError("Unpublished or missing release: " + code)
        version = releases[-1]
        pdf = version["pdf"]
        records[code] = {
            "title": paper["identity"]["title"],
            "date": pub["last_version_on"],
            "doi": version["version_doi"],
            "pdf": pdf["filename"],
            "md5": pdf["md5"],
            "size": pdf["size_bytes"],
        }
    if len(records) != len(set(records)):
        raise ValueError("Repeated publication IDs")
    return records


def expected_urls(records):
    return [
        BASE + "/", BASE + "/achievements.html", BASE + "/news.html",
        BASE + "/publications/", BASE + "/author/",
    ] + [BASE + "/publications/" + code + "/" for code in records]


class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.metas = {}
        self.canonical = []
        self.h1_count = 0
        self.math_count = 0
        self.duplicate_meta = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "meta" and attrs.get("name"):
            name = attrs["name"]
            if name in self.metas:
                self.duplicate_meta.append(name)
            self.metas[name] = attrs.get("content", "")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href", ""))
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "math":
            self.math_count += 1


def fetch(url: str, *, limit=2_000_000):
    req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urlopen(req, timeout=15, context=ssl.create_default_context()) as response:
        data = response.read(limit + 1)
        if len(data) > limit:
            raise ValueError("Response too large")
        return {"status": response.status, "url": response.geturl(),
                "bytes": data, "content_type": response.headers.get("Content-Type", "")}


def check_html(code, rec):
    url = BASE + "/publications/" + code + "/"
    try:
        r = fetch(url)
        if r["status"] != 200 or r["url"] != url:
            raise ValueError("Unexpected HTTP status or final URL")
        body = r["bytes"].decode("utf-8")
        p = HeadParser()
        p.feed(body)
        expected_pdf_url = url + rec["pdf"]
        expected = {
            "citation_title": rec["title"],
            "citation_author": "Alexandr Martinevski",
            "citation_author_orcid": "https://orcid.org/0009-0000-4230-4414",
            "citation_doi": rec["doi"],
            "citation_publication_date": rec["date"].replace("-", "/"),
            "citation_pdf_url": expected_pdf_url,
            "citation_abstract_html_url": url,
            "robots": "index,follow",
        }
        errors = [name for name, value in expected.items()
                  if p.metas.get(name) != value]
        if p.canonical != [url]:
            errors.append("canonical")
        if p.h1_count != 1:
            errors.append("h1")
        if p.duplicate_meta:
            errors.append("duplicate_meta:" + ",".join(p.duplicate_meta))
        if 'id="abstract"' not in body:
            errors.append("visible_abstract")
        if '"@type":"ScholarlyArticle"' not in body:
            errors.append("ScholarlyArticle_JSONLD")
        return {"code": code, "url": url, "ok": not errors,
                "errors": errors, "mathml_count": p.math_count,
                "bytes": len(r["bytes"])}
    except (OSError, HTTPError, URLError, ValueError, UnicodeError) as e:
        return {"code": code, "url": url, "ok": False,
                "errors": [type(e).__name__ + ": " + str(e)[:180]]}


def check_pdf(code, rec):
    url = BASE + "/publications/" + code + "/" + rec["pdf"]
    try:
        r = fetch(url, limit=PDF_LIMIT)
        content = r["bytes"]
        errors = []
        if r["status"] != 200 or r["url"] != url:
            errors.append("HTTP or final URL")
        if not content.startswith(b"%PDF-"):
            errors.append("PDF header")
        if len(content) != rec["size"]:
            errors.append("PDF byte length")
        if hashlib.md5(content).hexdigest() != rec["md5"]:
            errors.append("PDF MD5")
        return {"code": code, "url": url, "ok": not errors,
                "errors": errors, "bytes": len(content)}
    except (OSError, HTTPError, URLError, ValueError) as e:
        return {"code": code, "url": url, "ok": False,
                "errors": [type(e).__name__ + ": " + str(e)[:180]]}


def audit(root: Path):
    records = expected_records(root)
    result = {
        "schema": "cf-seo-live-crawl/v1",
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "domain": BASE,
        "paper_count": len(records),
        "scope": "GitHub runner HTTP/TLS/DNS and crawlability, NOT Google index status",
        "status": "PENDING",
        "errors": [],
        "pages": [],
        "pdfs": [],
    }
    try:
        dns = sorted({addr[4][0] for addr in socket.getaddrinfo(HOST, 443)})
        result["dns_addresses"] = dns
    except OSError as e:
        result["status"] = "BLOCKED_DNS"
        result["errors"].append("DNS resolution failed on GitHub runner: " + str(e))
        return result
    try:
        r = fetch(BASE + "/robots.txt", limit=100000)
        text = r["bytes"].decode("utf-8")
        result["robots"] = {"status": r["status"], "url": r["url"],
                            "sitemap": BASE + "/sitemap.xml" in text}
        if r["status"] != 200 or r["url"] != BASE + "/robots.txt":
            result["errors"].append("robots.txt was not served as HTTP 200")
        if not re.search(r"(?im)^Allow:\s*/\s*$", text):
            result["errors"].append("robots.txt does not explicitly allow /")
        if not result["robots"]["sitemap"]:
            result["errors"].append("robots.txt missing canonical sitemap")
        doc = fetch(BASE + "/sitemap.xml")
        tree = ET.fromstring(doc["bytes"])
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        actual = [el.text for el in tree.iter(ns + "loc")]
        wanted = expected_urls(records)
        result["sitemap"] = {"status": doc["status"], "url": doc["url"],
                             "count": len(actual), "expected_count": len(wanted),
                             "exact_match": actual == wanted}
        if doc["status"] != 200 or doc["url"] != BASE + "/sitemap.xml":
            result["errors"].append("sitemap.xml was not served as HTTP 200")
        if actual != wanted:
            result["errors"].append("Live sitemap differs from published canonical catalogue")
        home = fetch(BASE + "/")
        if home["status"] != 200 or home["url"] != BASE + "/":
            result["errors"].append("Homepage not served at canonical HTTPS URL")
        if "Browse scholarly abstracts and citations (18)" in home["bytes"].decode("utf-8"):
            result["errors"].append("Stale static home page publication count")
        result["homepage"] = {"status": home["status"], "url": home["url"]}
    except (OSError, HTTPError, URLError, ValueError, ET.ParseError, UnicodeError) as e:
        result["status"] = "BLOCKED_HTTP"
        result["errors"].append("Domain/robots/sitemap/home fetch failed: "
                                + type(e).__name__ + ": " + str(e)[:220])
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        result["pages"] = list(executor.map(
            lambda item: check_html(*item), records.items()))
        result["pdfs"] = list(executor.map(
            lambda item: check_pdf(*item), records.items()))
    result["page_pass"] = sum(row["ok"] for row in result["pages"])
    result["pdf_pass"] = sum(row["ok"] for row in result["pdfs"])
    if result["errors"] or result["page_pass"] != len(records) or result["pdf_pass"] != len(records):
        result["status"] = "FAIL"
    else:
        result["status"] = "PASS"
    return result


def self_test(root):
    import io
    records = expected_records(root)
    urls = expected_urls(records)
    assert len(urls) == len(records) + 5
    assert len(set(urls)) == len(urls)
    x = HeadParser()
    x.feed('<html><head><meta name="citation_doi" content="10.5281/zenodo.123">'
           '<link rel="canonical" href="https://example.org/x/"></head>'
           '<body><h1>A</h1><math><mi>x</mi></math></body></html>')
    assert x.metas["citation_doi"] == "10.5281/zenodo.123"
    assert x.canonical == ["https://example.org/x/"]
    assert x.h1_count == 1 and x.math_count == 1
    print(f"SEO crawler self-test passed: {len(records)} papers, {len(urls)} URLs")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default="_seo-live-audit/report.json")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test(ROOT)
    output = Path(args.report)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        report = audit(ROOT)
    except (ValueError, KeyError) as e:
        report = {"schema": "cf-seo-live-crawl/v1", "status": "INVALID_CANONICAL",
                  "errors": [type(e).__name__ + ": " + str(e)]}
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print("CF SEO live check:", report["status"], "report:", output)
    if report.get("page_pass") is not None:
        print("HTML:", report["page_pass"], "/", report["paper_count"],
              "PDF:", report["pdf_pass"], "/", report["paper_count"])
    for error in report.get("errors", []):
        print("Error:", error)
    for group in ("pages", "pdfs"):
        for row in report.get(group, []):
            if not row["ok"]:
                print("Failed " + group + " " + row["code"] + ":", row["errors"])
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
