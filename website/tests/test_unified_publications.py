#!/usr/bin/env python3
"""Regression and adversarial checks for the single publication source."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import materialize_publications as publications


class CanonicalCatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = ROOT / "data/publications.json"
        cls.doc = json.loads(cls.source.read_text(encoding="utf-8"))
        cls.catalog, cls.parts = publications.project(cls.doc)
        cls.scholar = {}
        for part in cls.parts:
            cls.scholar.update(part["papers"])

    def test_only_one_source_has_all_published_data(self):
        self.assertEqual(self.doc["schema"], "cf-publications/v3")
        self.assertGreaterEqual(len(self.doc["papers"]), 18)
        self.assertEqual(len(self.catalog["papers"]), len(self.doc["papers"]))
        self.assertEqual(len(self.parts), (len(self.doc["papers"]) + 5) // 6)
        self.assertEqual(set(self.doc["papers"]), set(self.scholar))
        self.assertEqual(sum(len(x["science"]["results"]) for x in
                             self.doc["papers"].values()), 3 * len(self.doc["papers"]))
        self.assertEqual({p["status"] for p in self.catalog["papers"]},
                         {"published"})
        self.assertEqual(len({p["concept_doi"] for p in
                              self.catalog["papers"]}), len(self.doc["papers"]))
        self.assertEqual(len({p["version_doi"] for p in
                              self.catalog["papers"]}), len(self.doc["papers"]))
        self.assertNotEqual(self.doc["papers"]["P01"]["identity"]["title"],
                            self.doc["papers"]["P01"]["identity"]["catalogue_title"])

    def test_stored_dates_are_not_synthesized(self):
        for code, p in self.doc["papers"].items():
            pub = p["publication"]
            self.assertEqual(pub["first_published_on"],
                             pub["releases"][0]["published_on"], code)
            self.assertEqual(pub["last_version_on"],
                             pub["releases"][-1]["published_on"], code)
            legacy = next(x for x in self.catalog["papers"]
                          if x["code"] == code)
            self.assertEqual(legacy["first_published_on"],
                             pub["first_published_on"])
            self.assertEqual(legacy["last_version_on"],
                             pub["last_version_on"])
        for field in ("first_published_on", "last_version_on"):
            bad = copy.deepcopy(self.doc)
            bad["papers"]["P01"]["publication"][field] = "2026-09-29"
            with self.subTest(field=field), self.assertRaises(ValueError):
                publications.project(bad)

    def test_release_lineage_and_results_provenance(self):
        for code in ("P01", "P02", "P03"):
            paper = self.doc["papers"][code]
            self.assertGreaterEqual(paper["publication"]["version_index"], 2)
            self.assertGreaterEqual(len(paper["publication"]["releases"]), 2)
            self.assertEqual(paper["publication"]["releases"][0]["record_id"],
                             {"P01": 23021780, "P02": 23022043,
                              "P03": 23022245}[code])
        for code, paper in self.doc["papers"].items():
            self.assertIn(paper["science"]["results_source_record_id"],
                          {r["record_id"] for r in
                           paper["publication"]["releases"]}, code)

    def test_rejects_draft_swapped_doi_and_corrupt_pdf(self):
        for mutation in ("draft", "doi", "pdf", "results", "source"):
            bad = copy.deepcopy(self.doc)
            paper = bad["papers"]["P12"]
            if mutation == "draft":
                paper["publication"]["status"] = "draft"
            elif mutation == "doi":
                paper["publication"]["releases"][-1]["version_doi"] = (
                    "10.5281/zenodo.99999999")
            elif mutation == "pdf":
                paper["publication"]["releases"][-1]["pdf"]["md5"] = "bad"
            elif mutation == "results":
                paper["science"]["results"] = []
            else:
                paper["science"]["results_source_record_id"] = 99999999
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                publications.project(bad)

    def test_generated_views_match_canonical_source(self):
        path = ROOT / "data/papers.json"
        self.assertTrue(path.is_file(), "Run materialize_publications.py first")
        site = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(site, self.catalog)
        for n, part in enumerate(self.parts, 1):
            out = ROOT / f"data/scholarly/part-{n:02d}.json"
            self.assertEqual(json.loads(out.read_text(encoding="utf-8")), part)
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            count, shards = publications.materialize(self.source, dest)
            self.assertEqual((count, shards),
                             (len(self.doc["papers"]), len(self.parts)))
            self.assertEqual(json.loads(
                (dest / "data/papers.json").read_text(encoding="utf-8")),
                self.catalog)
            stale = dest / "data/scholarly/part-99.json"
            stale.write_text("{}", encoding="utf-8")
            publications.materialize(self.source, dest)
            self.assertFalse(stale.exists())

    def test_p12_public_version_and_files_remain_unchanged(self):
        history = self.doc["papers"]["P12"]["publication"]["releases"]
        old = next(r for r in history if r["record_id"] == 23355669)
        self.assertEqual(old["pdf"]["filename"], "P12_CF_V6_S8.pdf")
        self.assertEqual(old["pdf"]["size_bytes"], 485042)
        self.assertEqual(old["pdf"]["md5"],
                         "1590c32efb3165b4dabfe9daf856aede")
        self.assertEqual(self.doc["papers"]["P12"]["publication"]
                         ["first_published_on"], "2026-10-14")

    def test_json_schema_documents_stored_date_contract(self):
        schema = json.loads((ROOT / "data/publications.schema.json")
                            .read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema"]["const"],
                         "cf-publications/v3")
        pub = schema["$defs"]["publication"]
        self.assertIn("first_published_on", pub["required"])
        self.assertIn("last_version_on", pub["required"])
        for name in ("first_published_on", "last_version_on"):
            self.assertIn("Stored", pub["properties"][name]["description"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
