#!/usr/bin/env python3
"""Read-only bibliographic discovery check for published CF Dependence DOI.

Important: "not found" means not returned by THAT provider at check time.
DataCite is the DOI registry; OpenAlex and Semantic Scholar are downstream
catalogues. This does not query Google Scholar or establish peer review.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
UA = "CF-Dependence-DOI-Discovery/1.0 (scientific metadata audit)"
TIMEOUT = 12
SERVICES = ("datacite", "openalex", "semanticscholar")


def published():
    data = json.loads((ROOT / "website/data/publications.json").read_text("utf-8"))
    assert data["schema"] == "cf-publications/v3"
    rows = []
    for pid, work in data["papers"].items():
        latest = work["publication"]["releases"][-1]
        doi = latest["version_doi"]
        if work["publication"]["status"] != "published" or not re.fullmatch(
                r"10\.5281/zenodo\.[0-9]+", doi):
            raise ValueError("Invalid canonical published DOI for " + pid)
        rows.append({"id": pid, "title": work["identity"]["title"], "doi": doi,
                     "publication_date": latest["published_on"],
                     "record_id": latest["record_id"]})
    return rows


def url_for(service, doi):
    if service == "datacite":
        return "https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe="/")
    if service == "openalex":
        return "https://api.openalex.org/works/" + urllib.parse.quote(
            "https://doi.org/" + doi, safe="/:")
    if service == "semanticscholar":
        return ("https://api.semanticscholar.org/graph/v1/paper/" +
                urllib.parse.quote("DOI:" + doi, safe=":/") +
                "?fields=title,year,url,citationCount,externalIds,authors")
    raise ValueError("Unknown service")


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
            data = res.read(600_000 + 1)
            if len(data) > 600_000:
                return "BAD_RESPONSE", None, "Body too large"
            return "HTTP_200", json.loads(data), None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "NOT_FOUND", None, None
        return ("RATE_LIMIT" if e.code == 429 else "HTTP_ERROR"), None, "HTTP_" + str(e.code)
    except (ValueError, OSError, urllib.error.URLError, json.JSONDecodeError) as e:
        return "NETWORK_ERROR", None, type(e).__name__ + ": " + str(e)[:120]


def doi_match(found, expected):
    if not found or not isinstance(found, str):
        return False
    found = found.strip().lower().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return found == expected.lower()


def classify(service, doi, payload, http_status, error):
    out = {"status": http_status}
    if error:
        out["error"] = error
    if http_status != "HTTP_200":
        return out
    try:
        if service == "datacite":
            a = payload["data"]["attributes"]
            stated_doi = payload["data"].get("id") or a.get("doi")
            result_title = (a.get("titles") or [{}])[0].get("title")
            out.update(registry_state=a.get("state"), type=a.get("types", {}).get("resourceTypeGeneral"))
        elif service == "openalex":
            stated_doi = payload.get("doi") or (payload.get("ids") or {}).get("doi")
            result_title = payload.get("title")
            out.update(url=payload.get("id"), citations=payload.get("cited_by_count"))
        else:
            stated_doi = (payload.get("externalIds") or {}).get("DOI")
            result_title = payload.get("title")
            out.update(url=payload.get("url"), citations=payload.get("citationCount"))
        if not doi_match(stated_doi, doi):
            out.update(status="MISMATCH", stated_doi=stated_doi)
        else:
            out.update(status="FOUND", title=result_title)
    except (KeyError, AttributeError, IndexError, TypeError) as e:
        out.update(status="BAD_RESPONSE", error=type(e).__name__)
    return out


def scan(rows, services=SERVICES):
    result = {"schema": "cf-external-discovery/v1",
              "checked_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "DOI metadata presence, not Google/Google Scholar coverage or peer review",
              "records": [], "counts": {}, "caveats": [
                  "A 404 at a downstream provider is time-local, not permanent exclusion.",
                  "403/429/network errors are unknown, not absent records.",
                  "Citations counted here are provider-specific and may lag or be duplicates.",
                  "Zenodo assigns DataCite DOI; successful registration is not peer review."
              ]}
    disabled = set()
    for row in rows:
        record = dict(row, checks={})
        for service in services:
            if service in disabled:
                record["checks"][service] = {"status": "NOT_CHECKED_AFTER_RATE_LIMIT"}
                continue
            status, data, error = get_json(url_for(service, row["doi"]))
            answer = classify(service, row["doi"], data, status, error)
            record["checks"][service] = answer
            if status in ("RATE_LIMIT",):
                disabled.add(service)
            # Be polite to remote public endpoints without service credentials.
            time.sleep(0.4 if service != "semanticscholar" else 1.05)
        result["records"].append(record)
        print(row["id"], row["doi"], " ".join(
            s + "=" + record["checks"][s]["status"] for s in services), flush=True)
    for service in services:
        cnt = Counter(row["checks"][service]["status"] for row in result["records"])
        result["counts"][service] = dict(sorted(cnt.items()))
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--out", default="_external-discovery/report.json")
    args = ap.parse_args()
    items = published()
    if args.self_test:
        assert len(items) >= 21 and len(set(x["doi"] for x in items)) == len(items)
        assert doi_match("https://doi.org/" + items[0]["doi"], items[0]["doi"])
        assert not doi_match("10.5281/zenodo.1", "10.5281/zenodo.2")
        assert classify("openalex",items[0]["doi"],{"doi":items[0]["doi"],"title":"sample"},
                        "HTTP_200", None)["status"] == "FOUND"
        assert classify("semanticscholar",items[0]["doi"],
                        {"externalIds":{"DOI":items[0]["doi"]}},
                        "HTTP_200", None)["status"] == "FOUND"
        assert classify("datacite",items[0]["doi"],
                        {"data":{"id":items[0]["doi"],"attributes":{"titles":[{"title":"sample"}]}}},
                        "HTTP_200", None)["status"] == "FOUND"
        print("External DOI audit offline checks passed:",len(items),"works")
        return 0
    report = scan(items)
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print("SUMMARY", json.dumps(report["counts"], sort_keys=True), flush=True)
    print("Report saved:", path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
