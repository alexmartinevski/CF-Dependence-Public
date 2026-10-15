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
        papers=self.site["papers"]
        self.assertEqual(len(papers),18)
        codes={p["code"] for p in papers}
        self.assertNotIn("P05",codes)
        self.assertNotIn("P10",codes)
        for p in papers:
            if p.get("source_path"):
                source=p["source_path"]
                self.assertRegex(source,r"^papers/[a-z0-9-]+$")
                self.assertTrue((REPO/source/"paper.pdf").is_file(),source)
                self.assertTrue((REPO/source/"paper.tex").is_file(),source)
            else:
                record_url=p.get("record_url")
                doi=p.get("version_doi")
                self.assertEqual(record_url,"https://zenodo.org/records/"+doi.split(".")[-1])
                self.assertRegex(p["pdf_filename"],r"^P\d{2}_CF_V6_S8\.pdf$")
                self.assertEqual(p["pdf_filename"][:3],p["code"])

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
            source=event["source"]
            if source=="RELEASE_NOTES.md":
                self.assertTrue((REPO/source).is_file())
            else:
                self.assertRegex(source,r"^https://doi.org/10\.5281/zenodo\.\d+$")
                self.assertIn(source.removeprefix("https://doi.org/"),{p["version_doi"] for p in self.site["papers"]})

    def test_subject_directory_and_release_metadata(self):
        from datetime import date
        areas={"extremal","transport","algebra","harmonic","statistics"}
        entries=self.site["papers"]
        self.assertEqual({p["area"] for p in entries},areas)
        self.assertEqual(len([p["code"] for p in entries]),len(set(p["code"] for p in entries)))
        self.assertRegex(self.site["last_curated_on"],r"^\d{4}-\d{2}-\d{2}$")
        for p in entries:
            self.assertTrue(p["area"] in areas)
            if p.get("published_on"):
                self.assertEqual(date.fromisoformat(p["published_on"]).isoformat(),p["published_on"])
            else:
                self.assertIn(p["code"],{"P01","P02","P03"}, "Publication date may not be invented")

    def test_latest_version_links_and_directory_present(self):
        homepage=(ROOT/"index.html").read_text(encoding="utf-8")
        detail=(ROOT/"paper.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('id="areas"',homepage)
        self.assertIn('id="area-groups"',homepage)
        self.assertIn("function renderAreas()",script)
        self.assertIn("doiLink(p.concept_doi,COPY[language].openLatest)",script)
        self.assertIn("paper-latest",detail)
        self.assertIn("paper-version",detail)
        self.assertIn("COPY[language].olderPdf",script)
        self.assertNotIn('id="paper-concept"',detail)

    def test_public_zenodo_metadata_validated_before_display(self):
        import sys
        sys.path.insert(0, str(ROOT/"tools"))
        import resolve_zenodo as sync
        paper=self.site["papers"][0]
        old={"doi":paper["version_doi"],"conceptdoi":paper["concept_doi"],
             "metadata":{"publication_date":"2026-10-01","version":"v0.1"},
             "links":{"latest":"https://zenodo.org/api/records/23355587"}}
        latest={"doi":"10.5281/zenodo.23355587","conceptdoi":paper["concept_doi"],
                "metadata":{"publication_date":"2026-10-15","version":"v0.2"}}
        resolved=sync.extract_release(paper,old,latest)
        self.assertEqual(resolved["version_doi"],"10.5281/zenodo.23355587")
        self.assertEqual(resolved["published_on"],"2026-10-15")
        self.assertEqual(resolved["version_label"],"v0.2")
        self.assertEqual(sync.latest_record_id(old),23355587)
        bad={**latest,"conceptdoi":"10.5281/zenodo.9999"}
        self.assertIsNone(sync.extract_release(paper,old,bad))
        old["links"]["latest"]="https://other.example.org/api/records/23355587"
        self.assertIsNone(sync.latest_record_id(old))

    def test_immutable_asset_urls_and_fingerprint(self):
        import hashlib
        import shutil
        import sys
        import tempfile
        sys.path.insert(0,str(ROOT/"tools"))
        from fingerprint_assets import stamp_site
        for page in ("index.html","paper.html"):
            html=(ROOT/page).read_text(encoding="utf-8")
            self.assertRegex(html, r'href="assets/site\.css\?v=[A-Za-z0-9._-]+"')
            self.assertRegex(html, r'src="assets/site\.js\?v=[A-Za-z0-9._-]+"')
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            (base/"assets").mkdir()
            for asset in ("assets/site.js","assets/site.css"):
                shutil.copyfile(ROOT/asset,base/asset)
            for page in ("index.html","paper.html"):
                shutil.copyfile(ROOT/page,base/page)
            stamp_site(base)
            digest=hashlib.sha256((base/"assets/site.js").read_bytes()).hexdigest()[:16]
            first=(base/"index.html").read_text(encoding="utf-8")
            self.assertIn("assets/site.js?v="+digest,first)
            self.assertIn("assets/site.js?v="+digest,(base/"paper.html").read_text(encoding="utf-8"))
            (base/"assets/site.js").write_bytes((base/"assets/site.js").read_bytes()+b"\n/* changed */")
            stamp_site(base)
            self.assertNotIn("assets/site.js?v="+digest,(base/"index.html").read_text(encoding="utf-8"))

    def test_scientific_programme_introduction(self):
        """The public subject index starts with object, goal and method, in two languages."""
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertLess(html.index('id="programme-heading"'),html.index('id="areas-heading"'))
        self.assertLess(html.index('class="science-intro"'),html.index('id="area-groups"'))
        self.assertIn('μ<sub>P</sub>',html)
        self.assertIn('D<sub>d</sub>(P)',html)
        self.assertIn('programmeGoal',script)
        self.assertIn('programmeMethod',script)
        for key in ("programmeLabel","programmeHeading","programmeLead","programmeObject",
                    "programmeObjectHeading","programmeObjectNote","programmeGoalHeading",
                    "programmeGoal","programmeMethodHeading","programmeMethod","programmeBridge"):
            self.assertIn(f'data-i18n="{key}"',html)
            self.assertEqual(script.count(f'{key}:'),2, f"Both languages must define {key}")
        self.assertIn("Открывать новые математические законы",script)
        self.assertIn("signed interaction measure",script)

    def test_key_results_provenance_and_unique_catalogue(self):
        page=(ROOT/"index.html").read_text(encoding="utf-8")
        detail=(ROOT/"paper.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('id="area-groups"',page)
        self.assertIn('id="search"',page)
        self.assertIn('id="papers"',page)  # Backwards-compatible anchor on the new search
        self.assertNotIn('id="paper-list"',page)  # No duplicate card grid
        self.assertIn('id="paper-results"',detail)
        self.assertIn("function renderAreas(visiblePapers=papers)",script)
        self.assertNotIn("function renderCard(",script)
        self.assertIn("p.highlights",script)
        for p in self.site["papers"]:
            self.assertEqual(len(p.get("highlights", [])), 3, p["code"])
            self.assertEqual(p["highlights_source_doi"],p["version_doi"])
            for h in p["highlights"]:
                self.assertTrue(h["en"].strip(),p["code"])
                self.assertTrue(h["ru"].strip(),p["code"])
                self.assertTrue(h["evidence"].strip(),p["code"])
                self.assertNotIn("TODO",h["en"])
                self.assertNotIn("TODO",h["ru"])
        self.assertEqual(sum(len(p["highlights"]) for p in self.site["papers"]),54)

    def test_custom_domain_assets(self):
        from xml.etree import ElementTree as ET
        hostname = "https://math.a-martinevski.com/"
        homepage = (ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn(f'href="{hostname}"', homepage)
        self.assertIn(f'content="{hostname}"', homepage)
        robot_text = (ROOT/"robots.txt").read_text(encoding="utf-8")
        self.assertIn(hostname+"sitemap.xml", robot_text)
        sitemap = ET.fromstring((ROOT/"sitemap.xml").read_text(encoding="utf-8"))
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        urls = [node.text for node in sitemap.iter(ns+"loc")]
        self.assertIn(hostname, urls)
        self.assertEqual(len(urls), len(self.site["papers"])+1)
        for paper in self.site["papers"]:
            self.assertIn(hostname+"paper.html?code="+paper["code"], urls)
        self.assertTrue(all(u.startswith(hostname) for u in urls))

    def test_static_entrypoints_present(self):
        for rel in ("index.html","paper.html","assets/site.css","assets/site.js"):
            self.assertTrue((ROOT/rel).is_file(),rel)

if __name__=="__main__":
    unittest.main()
