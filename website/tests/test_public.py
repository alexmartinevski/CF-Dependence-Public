#!/usr/bin/env python3
"""Public-site checks: fail closed if nonpublic entries appear in the public catalogue."""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
DOI=re.compile(r"^10\.5281/zenodo\.\d+$")
CODE=re.compile(r"^P\d{2,}$")

class PublicSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.site=json.loads((ROOT/"data/papers.json").read_text(encoding="utf-8"))
        cls.news=json.loads((ROOT/"data/news.json").read_text(encoding="utf-8"))

    def test_catalogue_only_published_items(self):
        papers=self.site["papers"]
        self.assertGreater(len(papers),0)
        self.assertEqual(len({p["code"] for p in papers}),len(papers))
        for p in papers:
            self.assertTrue(CODE.fullmatch(p["code"]))
            self.assertEqual(p["status"],"published", f"{p['code']} is not a public publication")
            self.assertTrue(DOI.fullmatch(p["version_doi"]))
            self.assertTrue(DOI.fullmatch(p["concept_doi"]))
            self.assertNotEqual(p["version_doi"],p["concept_doi"])
            self.assertTrue(p["summary"]["en"].strip())
            self.assertTrue(p["summary"]["ru"].strip())

    def test_sources_are_already_public(self):
        for p in self.site["papers"]:
            source=p["source_path"]
            self.assertRegex(source,r"^papers/[a-z0-9-]+$")
            self.assertTrue((REPO/source/"paper.pdf").is_file(),source)
            self.assertTrue((REPO/source/"paper.tex").is_file(),source)

    def test_change_log_entries_refer_to_doi(self):
        for p in self.site["papers"]:
            for c in p.get("changes",[]):
                self.assertRegex(c["date"],r"^\d{4}-\d{2}-\d{2}$")
                self.assertTrue(DOI.fullmatch(c["doi"]))
                self.assertTrue(c["summary"]["en"].strip())
                self.assertTrue(c["summary"]["ru"].strip())

    def test_news_comes_from_public_sources(self):
        for event in self.news["entries"]:
            self.assertRegex(event["date"],r"^\d{4}-\d{2}-\d{2}$")
            self.assertTrue(event["title"]["en"].strip())
            self.assertTrue(event["summary"]["ru"].strip())
            self.assertEqual(event["source"],"RELEASE_NOTES.md")
            self.assertTrue((REPO/event["source"]).is_file())

    def test_static_entrypoints_present(self):
        for rel in ("index.html","paper.html","assets/site.css","assets/site.js"):
            self.assertTrue((ROOT/rel).is_file(),rel)

if __name__=="__main__":
    unittest.main()
