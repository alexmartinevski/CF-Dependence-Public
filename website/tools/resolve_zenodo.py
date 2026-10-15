#!/usr/bin/env python3
"""Read-only Zenodo publication lineage metadata for the CF public site.

Dates mean publication dates of version records, not metadata-edit timestamps.
Only published records with the exact expected concept DOI are accepted.
No API token, deposit endpoint, publish action or write permission is used.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

DOI = re.compile(r"^10\.5281/zenodo\.(\d+)$")
VERSION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$")
API_ROOT = "https://zenodo.org/api/records/"
MAX_BYTES = 1_500_000


def doi_of(record):
    return record.get("doi") or ((record.get("pids") or {}).get("doi") or {}).get("identifier")


def concept_of(record):
    return record.get("conceptdoi") or (
        ((record.get("parent") or {}).get("pids") or {}).get("doi") or {}
    ).get("identifier")


def publication_date(record):
    value = (record.get("metadata") or {}).get("publication_date")
    if not isinstance(value, str):
        return None
    try:
        return value if dt.date.fromisoformat(value).isoformat() == value else None
    except ValueError:
        return None


def version_index(record):
    value = (record.get("versions") or {}).get("index")
    # InvenioRDM uses a positive, 1-based index for releases within a lineage.
    return value if isinstance(value, int) and not isinstance(value, bool) and value > 0 else None


def is_public_version(record, concept):
    if not isinstance(record, dict) or record.get("is_draft") is True:
        return False
    if record.get("status") in ("draft", "inprogress", "unpublished"):
        return False
    return concept_of(record) == concept and bool(DOI.fullmatch(str(doi_of(record) or "")))


def latest_record_id(record):
    """Compatibility helper for direct numeric links in older Zenodo responses."""
    from urllib.parse import urlsplit
    candidate = (record.get("links") or {}).get("latest")
    if not isinstance(candidate, str):
        return None
    url = urlsplit(candidate)
    if url.scheme != "https" or url.hostname != "zenodo.org":
        return None
    match = re.fullmatch(r"/(?:api/)?records/(\d+)/?", url.path)
    return int(match.group(1)) if match else None


def read_json(url, timeout=9, attempts=2):
    # URLs are constructed locally from strictly parsed numeric IDs; no remote
    # metadata link is ever used for network requests.
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "CF-Dependence-Public-Catalogue/2.0 (read-only)"
    })
    last_error = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                content = response.read(MAX_BYTES + 1)
            if len(content) > MAX_BYTES:
                raise ValueError("Oversized Zenodo response")
            obj = json.loads(content)
            if not isinstance(obj, dict):
                raise ValueError("Invalid Zenodo JSON payload")
            return obj
        except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(0.5 * (attempt + 1))
    raise last_error


def read_public_record(record_id):
    return read_json(API_ROOT + str(int(record_id)))


def read_versions(record_id):
    """Get the published lineage, fetching every page rather than assuming order."""
    record_id = int(record_id)
    found = []
    page = 1
    while page <= 10:
        payload = read_json(f"{API_ROOT}{record_id}/versions?size=100&page={page}")
        hits = payload.get("hits") or {}
        entries = hits.get("hits") if isinstance(hits, dict) else None
        if not isinstance(entries, list):
            raise ValueError("Zenodo version history not returned")
        found.extend(entries)
        total = hits.get("total") if isinstance(hits, dict) else None
        if isinstance(total, dict):
            total = total.get("value")
        if not isinstance(total, int):
            # A shorter page signals the end of the list even when total omitted.
            if len(entries) < 100:
                return found, True
        elif len(found) >= total:
            return found, True
        if not entries:
            break
        page += 1
    return found, False


def sort_lineage(records):
    """Return chronological versions only when order can be grounded."""
    if not records:
        return None
    if all(version_index(x) is not None for x in records):
        return sorted(records, key=lambda x: version_index(x))
    if all(isinstance(x.get("created"), str) and x["created"] for x in records):
        return sorted(records, key=lambda x: x["created"])
    return None


def extract_release(paper, base, latest=None, versions=None, history_complete=False):
    """Check identity and extract first publication, last release date and version."""
    expected_doi = paper.get("version_doi")
    expected_concept = paper.get("concept_doi")
    if doi_of(base) != expected_doi or not is_public_version(base, expected_concept):
        return None

    family = [base]
    if versions is not None:
        family += list(versions)
    candidates = {}
    for rec in family:
        if is_public_version(rec, expected_concept):
            candidates[doi_of(rec)] = rec

    if latest is not None:
        if not is_public_version(latest, expected_concept):
            return None
        candidates[doi_of(latest)] = latest

    ordered = sort_lineage(list(candidates.values()))
    if latest is not None:
        current = latest
    elif ordered is not None:
        current = ordered[-1]
    else:
        current = base

    # We only identify the first release if its order is verifiable.
    first = None
    if ordered:
        if version_index(ordered[0]) == 1:
            first = ordered[0]
        elif history_complete and versions is not None:
            first = ordered[0]
    elif version_index(base) == 1:
        first = base

    result = {"concept_doi":expected_concept, "version_doi":doi_of(current)}
    date = publication_date(current)
    if date:
        result["last_version_on"] = date
        result["published_on"] = date  # compatibility with older site builds
    if first is not None and (start := publication_date(first)):
        result["first_published_on"] = start
    label = (current.get("metadata") or {}).get("version")
    if isinstance(label, str) and VERSION.fullmatch(label.strip()):
        result["version_label"] = label.strip()
    if (number := version_index(current)) is not None:
        result["version_index"] = number
    if history_complete and ordered:
        result["release_count"] = len(ordered)
    return result


def check_paper(paper):
    match = DOI.fullmatch(str(paper.get("version_doi") or ""))
    if not match:
        return None
    try:
        base_id = int(match.group(1))
        base = read_public_record(base_id)
        if doi_of(base) != paper["version_doi"] or not is_public_version(base, paper["concept_doi"]):
            return None
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError):
        return None

    versions, complete = None, False
    try:
        versions, complete = read_versions(base_id)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError):
        pass

    published_versions = [v for v in (versions or []) if is_public_version(v, paper["concept_doi"])]
    timeline = sort_lineage(published_versions + [base])
    latest = timeline[-1] if timeline else None
    # Fall back to a dedicated published-latest endpoint if the version list is
    # missing or incomplete (or has no reliable chronology).
    if not complete or not timeline:
        try:
            candidate = read_json(f"{API_ROOT}{base_id}/versions/latest")
            if is_public_version(candidate, paper["concept_doi"]):
                latest = candidate
        except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError):
            if not latest and (direct_id := latest_record_id(base)):
                try:
                    candidate = read_public_record(direct_id)
                    if is_public_version(candidate, paper["concept_doi"]):
                        latest = candidate
                except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, json.JSONDecodeError):
                    pass

    return extract_release(
        paper, base, latest=latest, versions=published_versions,
        history_complete=complete
    )


def build(source, output):
    catalog = json.loads(Path(source).read_text(encoding="utf-8"))
    entries = [p for p in catalog.get("papers", []) if p.get("status") == "published"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        checked = list(pool.map(check_paper, entries))
    records = {p["code"]: meta for p, meta in zip(entries, checked) if meta}
    payload = {
        "schema": 2,
        "checked_on": dt.datetime.now(dt.timezone.utc).date().isoformat(),
        "resolved": len(records),
        "first_published_resolved": sum(bool(x.get("first_published_on")) for x in records.values()),
        "version_label_resolved": sum(bool(x.get("version_label") or x.get("version_index")) for x in records.values()),
        "total": len(entries),
        "records": records
    }
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Zenodo publication history: {len(records)}/{len(entries)} records, "
        f"{payload['first_published_resolved']} first dates, "
        f"{payload['version_label_resolved']} release numbers; curated fallback for the rest."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("output")
    args = parser.parse_args()
    build(args.source, args.output)
