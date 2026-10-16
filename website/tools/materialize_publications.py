#!/usr/bin/env python3
"""Generate legacy site views from the one authoritative publications.json v3.

Source of truth: website/data/publications.json.
Generated (untracked): website/data/papers.json and data/scholarly/part-NN.json.
Only already published Zenodo versions belong in the public source.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

DOI = re.compile(r"10\.5281/zenodo\.([1-9][0-9]*)\Z")
CODE = re.compile(r"P[0-9]{2}\Z")
MD5 = re.compile(r"[0-9a-f]{32}\Z")
PDF = re.compile(r"P[0-9]{2}_[A-Za-z0-9][A-Za-z0-9._-]*\.pdf\Z")
AREA = {"extremal", "transport", "algebra", "harmonic", "statistics"}
MAX_PDF = 64 * 1024 * 1024
BATCH = 6
SITE = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def checked_date(value, description):
    require(nonempty(value), description + ": missing stored date")
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(description + ": invalid stored ISO date") from exc
    require(parsed.isoformat() == value, description + ": noncanonical date")
    return parsed


def checked_doi(value, description, record_id=None):
    require(isinstance(value, str), description + ": DOI missing")
    match = DOI.fullmatch(value)
    require(match is not None, description + ": DOI format invalid")
    if record_id is not None:
        require(type(record_id) is int and record_id > 0,
                description + ": record_id must be positive integer")
        require(int(match.group(1)) == record_id,
                description + ": DOI and record_id disagree")


def bilingual(value, description):
    require(isinstance(value, dict) and set(value) == {"en", "ru"},
            description + ": expected exact en/ru pair")
    for language in ("en", "ru"):
        require(nonempty(value[language]),
                description + ": " + language + " text must be nonempty")


def unique_strings(value, description):
    require(isinstance(value, list) and bool(value),
            description + ": nonempty list expected")
    require(all(nonempty(item) for item in value),
            description + ": empty or nonstring item")
    require(len(value) == len(set(value)),
            description + ": duplicate item")


def checked_pdf(pdf, code):
    """Validate optional historical or mandatory latest PDF metadata."""
    require(isinstance(pdf, dict), code + ": PDF metadata missing")
    name = pdf.get("filename")
    require(isinstance(name, str) and PDF.fullmatch(name) and
            name.startswith(code + "_"),
            code + ": invalid PDF basename")
    require(isinstance(pdf.get("md5"), str) and MD5.fullmatch(pdf["md5"]),
            code + ": PDF MD5 required")
    require(type(pdf.get("size_bytes")) is int and
            1000 < pdf["size_bytes"] <= MAX_PDF,
            code + ": PDF size invalid")
    return pdf


def project(publications):
    """Return the exact legacy shapes as deterministic derived views.

    Dates first_published_on/last_version_on are author-curated STORED values,
    never synthesized from a release list. Release dates only validate them.
    """
    require(isinstance(publications, dict) and
            publications.get("schema") == "cf-publications/v3",
            "Expected publications schema v3")
    require(nonempty(publications.get("source_repo")), "source_repo missing")
    checked_date(publications.get("curated_on"), "curated_on")
    require(isinstance(publications.get("editorial_policy"), dict),
            "editorial_policy missing")
    require(nonempty(publications.get("scholarly_verified_scope")),
            "scholarly_verified_scope missing")
    all_papers = publications.get("papers")
    require(isinstance(all_papers, dict) and bool(all_papers),
            "No canonical papers")

    rows, detailed = [], {}
    all_concepts, all_versions, all_record_ids = set(), set(), set()
    for code, paper in all_papers.items():
        require(isinstance(code, str) and CODE.fullmatch(code),
                "Invalid P-ID: " + str(code))
        require(isinstance(paper, dict), code + ": invalid record")
        identity = paper.get("identity")
        science = paper.get("science")
        pub = paper.get("publication")
        require(all(isinstance(v, dict) for v in (identity, science, pub)),
                code + ": identity/science/publication blocks required")

        title = identity.get("title")
        require(nonempty(title), code + ": published title missing")
        display_title = identity.get("catalogue_title", title)
        require(nonempty(display_title), code + ": catalogue title invalid")
        require(identity.get("area") in AREA, code + ": unknown science area")
        unique_strings(identity.get("topics"), code + ": topics")
        unique_strings(identity.get("keywords"), code + ": keywords")
        bilingual(science.get("summary"), code + ": summary")
        require(nonempty(science.get("abstract_html")),
                code + ": approved abstract missing")
        results = science.get("results")
        require(isinstance(results, list) and len(results) == 3,
                code + ": exactly three checked scientific results required")
        for i, item in enumerate(results):
            require(isinstance(item, dict) and nonempty(item.get("evidence")),
                    code + ": evidence label missing for result " + str(i+1))
            bilingual({"en": item.get("en"), "ru": item.get("ru")},
                      code + ": result " + str(i+1))
        source_id = science.get("results_source_record_id")
        require(type(source_id) is int and source_id > 0,
                code + ": results source must reference a published version")

        require(pub.get("status") == "published",
                code + ": drafts must never enter public catalogue")
        concept = pub.get("concept_doi")
        checked_doi(concept, code + ": concept DOI")
        require(concept not in all_concepts, code + ": duplicate concept DOI")
        all_concepts.add(concept)

        first = checked_date(pub.get("first_published_on"),
                             code + ": stored first_published_on")
        last = checked_date(pub.get("last_version_on"),
                            code + ": stored last_version_on")
        require(first <= last, code + ": stored dates reversed")
        releases = pub.get("releases")
        require(isinstance(releases, list) and bool(releases),
                code + ": published release history missing")
        index = pub.get("version_index")
        require(type(index) is int and index == len(releases),
                code + ": release history must match verified version_index")
        require(nonempty(pub.get("version_index_evidence")),
                code + ": version_index_evidence missing")
        require(isinstance(pub.get("changes"), list),
                code + ": changes must be a list")
        source_path = pub.get("source_path")
        if source_path is not None:
            require(isinstance(source_path, str) and
                    re.fullmatch(r"papers/[A-Za-z0-9][A-Za-z0-9/_-]*", source_path) and
                    ".." not in source_path,
                    code + ": invalid public source path")

        dates, release_ids = [], set()
        for i, version in enumerate(releases):
            require(isinstance(version, dict),
                    code + ": malformed release")
            rec_id = version.get("record_id")
            checked_doi(version.get("version_doi"),
                        code + ": version DOI", rec_id)
            when = checked_date(version.get("published_on"),
                                code + ": release date")
            dates.append(when)
            require(rec_id not in release_ids and rec_id not in all_record_ids,
                    code + ": repeated published record ID")
            require(version["version_doi"] not in all_versions,
                    code + ": repeated Version DOI")
            release_ids.add(rec_id)
            all_record_ids.add(rec_id)
            all_versions.add(version["version_doi"])
            if "pdf" in version:
                checked_pdf(version["pdf"], code)
        require(dates == sorted(dates),
                code + ": releases must be ordered by publication date")
        require(dates[0] == first and dates[-1] == last,
                code + ": stored first/last dates differ from verified history")
        require(source_id in release_ids,
                code + ": results must cite a published record in this lineage")

        latest = releases[-1]
        pdf = checked_pdf(latest.get("pdf"), code)
        name = pdf["filename"]
        require(nonempty(latest.get("license")),
                code + ": latest license missing")

        # Front-end fields are generated, never independently edited.
        row = {
            "code": code,
            "title": display_title,
            "summary": science["summary"],
            "topics": identity["topics"],
            "status": pub["status"],
            "version_doi": latest["version_doi"],
            "concept_doi": concept,
            "changes": pub["changes"],
            "area": identity["area"],
            "highlights": results,
            "highlights_source_doi": "10.5281/zenodo." + str(source_id),
            # Explicitly copied from stored fields, not derived.
            "first_published_on": pub["first_published_on"],
            "last_version_on": pub["last_version_on"],
            "published_on": pub["last_version_on"],
            "version_index": index,
            "version_index_evidence": pub["version_index_evidence"],
        }
        if source_path:
            row["source_path"] = source_path
        else:
            row["record_url"] = "https://zenodo.org/records/" + str(latest["record_id"])
            row["pdf_filename"] = name
        rows.append(row)
        detailed[code] = {
            "title": title,
            "description_html": science["abstract_html"],
            "keywords": identity["keywords"],
            "publication_date": pub["last_version_on"],
            "version_doi": latest["version_doi"],
            "concept_doi": concept,
            "pdf_filename": name,
            "pdf_md5": pdf["md5"],
            "pdf_size": pdf["size_bytes"],
            "license": latest["license"],
            "record_id": latest["record_id"],
        }

    catalog = {
        "schema": "cf-publications-public/v1",
        "source_repo": publications["source_repo"],
        "last_curated_on": publications["curated_on"],
        "papers": rows,
        "highlights_editorial_policy": publications["editorial_policy"],
    }
    parts = [
        {
            "schema": 1,
            "verified_scope": publications["scholarly_verified_scope"],
            "papers": dict(list(detailed.items())[i:i + BATCH]),
        }
        for i in range(0, len(detailed), BATCH)
    ]
    return catalog, parts


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def materialize(source, root):
    publications = json.loads(source.read_text(encoding="utf-8"))
    catalog, parts = project(publications)  # validate all before touching files
    data = root / "data"
    target = data / "scholarly"
    target.mkdir(parents=True, exist_ok=True)
    (data / "papers.json").write_bytes(encode(catalog))
    filenames = set()
    for i, part in enumerate(parts, start=1):
        name = f"part-{i:02d}.json"
        filenames.add(name)
        (target / name).write_bytes(encode(part))
    for stale in target.glob("part-*.json"):
        if stale.name not in filenames:
            stale.unlink()
    return len(catalog["papers"]), len(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
                        default=SITE / "data/publications.json")
    parser.add_argument("--destination", type=Path, default=SITE)
    parser.add_argument("--check-only", action="store_true",
                        help="Validate the canonical source without writing views")
    args = parser.parse_args()
    if args.check_only:
        n, parts = project(json.loads(args.source.read_text(encoding="utf-8")))
        print(f"Canonical v3 valid: {len(n['papers'])} published papers; {len(parts)} derived shards")
    else:
        count, shards = materialize(args.source, args.destination)
        print(f"Materialized {count} published papers and {shards} transient scholarly shards")


if __name__ == "__main__":
    main()
