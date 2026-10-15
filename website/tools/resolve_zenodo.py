#!/usr/bin/env python3
"""Refresh read-only, public Zenodo metadata for the website's published releases.

This tool NEVER changes a Zenodo record and never needs credentials. The checked
catalogue remains the fallback if public Zenodo API requests are unavailable.
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DOI = re.compile(r"^10\.5281/zenodo\.(\d+)$")
RECORD_PATH = re.compile(r"^/(?:api/)?records/(\d+)/?$")
VERSION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$")
MAX_BYTES = 1_500_000
API_ROOT = "https://zenodo.org/api/records/"


def doi_of(record):
    return record.get("doi") or (record.get("pids") or {}).get("doi", {}).get("identifier")


def concept_of(record):
    return record.get("conceptdoi") or (
        ((record.get("parent") or {}).get("pids") or {}).get("doi") or {}
    ).get("identifier")


def latest_record_id(record):
    candidate = (record.get("links") or {}).get("latest")
    if not isinstance(candidate, str):
        return None
    url = urllib.parse.urlsplit(candidate)
    # Do not fetch URLs provided by record metadata unless on the Zenodo host.
    if url.scheme != "https" or url.hostname != "zenodo.org":
        return None
    match = RECORD_PATH.fullmatch(url.path)
    return int(match.group(1)) if match else None


def read_public_record(record_id, timeout=8):
    url = API_ROOT + str(int(record_id))
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "CF-Dependence-Public-Catalogue/1.0 (read-only)"
    })
    with urllib.request.urlopen(req, timeout=timeout) as response:
        content = response.read(MAX_BYTES + 1)
    if len(content) > MAX_BYTES:
        raise ValueError("Oversized Zenodo record")
    obj = json.loads(content)
    if not isinstance(obj, dict):
        raise ValueError("Invalid Zenodo record")
    return obj


def extract_release(paper, base, latest=None):
    """Validate concept lineage and extract only public version metadata."""
    if doi_of(base) != paper["version_doi"] or concept_of(base) != paper["concept_doi"]:
        return None
    record = latest if latest is not None else base
    if concept_of(record) != paper["concept_doi"]:
        return None
    current_doi = doi_of(record)
    if not isinstance(current_doi, str) or not DOI.fullmatch(current_doi):
        return None
    if record.get("is_draft") or record.get("status") in ("draft", "inprogress"):
        return None
    md = record.get("metadata") or {}
    result = {"concept_doi":paper["concept_doi"],"version_doi":current_doi}
    date = md.get("publication_date")
    if isinstance(date, str):
        try:
            if dt.date.fromisoformat(date).isoformat() == date:
                result["published_on"] = date
        except ValueError:
            pass
    version = md.get("version")
    if isinstance(version,str) and VERSION.fullmatch(version):
        result["version_label"] = version
    return result


def check_paper(paper):
    version = DOI.fullmatch(paper.get("version_doi", ""))
    if not version:
        return None
    try:
        base = read_public_record(int(version.group(1)))
        next_id = latest_record_id(base)
        latest = read_public_record(next_id) if next_id and next_id != int(version.group(1)) else None
        return extract_release(paper, base, latest)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError):
        return None


def build(source, output):
    catalog=json.loads(Path(source).read_text(encoding="utf-8"))
    entries=[p for p in catalog.get("papers",[]) if p.get("status")=="published"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        checked=list(pool.map(check_paper,entries))
    records={p["code"]:meta for p,meta in zip(entries,checked) if meta}
    payload={
        "schema":1,
        "checked_on":dt.datetime.now(dt.timezone.utc).date().isoformat(),
        "resolved":len(records),
        "total":len(entries),
        "records":records
    }
    path=Path(output)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Zenodo public metadata: {len(records)}/{len(entries)} records resolved; fallback retained for others.")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("output")
    args=parser.parse_args()
    build(args.source,args.output)
