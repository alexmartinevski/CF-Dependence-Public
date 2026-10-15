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
            for key in ("first_published_on","last_version_on"):
                if p.get(key):
                    self.assertEqual(date.fromisoformat(p[key]).isoformat(),p[key])
            if p.get("first_published_on") and p.get("last_version_on"):
                self.assertLessEqual(p["first_published_on"],p["last_version_on"])
            if p["code"] not in {"P01","P02","P03"}:
                self.assertEqual(p["first_published_on"],"2026-10-14")
                self.assertEqual(p["last_version_on"],"2026-10-14")
            else:
                self.assertEqual(p["first_published_on"],"2026-09-28")
                self.assertEqual(p["last_version_on"],"2026-10-12" if p["code"]=="P03" else "2026-10-14")

    def test_latest_version_links_and_directory_present(self):
        homepage=(ROOT/"index.html").read_text(encoding="utf-8")
        detail=(ROOT/"paper.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('id="areas"',homepage)
        self.assertIn('id="area-groups"',homepage)
        self.assertIn("function renderAreas(visiblePapers=papers)",script)
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
        first={
            "doi":paper["version_doi"],"conceptdoi":paper["concept_doi"],
            "versions":{"index":1},
            "created":"2026-09-21T12:00:00Z",
            "updated":"2026-09-30T12:00:00Z",
            "metadata":{"publication_date":"2026-09-21","version":"0.1"},
            "links":{"latest":"https://zenodo.org/api/records/24444444"}
        }
        newest={
            "doi":"10.5281/zenodo.24444444","conceptdoi":paper["concept_doi"],
            "versions":{"index":2},
            "created":"2026-10-14T12:00:00Z",
            "updated":"2026-10-16T12:00:00Z",
            "metadata":{"publication_date":"2026-10-14","version":"0.2"}
        }
        resolved=sync.extract_release(
            paper,first,latest=newest,versions=[newest,first],history_complete=True
        )
        self.assertEqual(resolved["version_doi"],"10.5281/zenodo.24444444")
        self.assertEqual(resolved["first_published_on"],"2026-09-21")
        self.assertEqual(resolved["last_version_on"],"2026-10-14")
        self.assertEqual(resolved["published_on"],"2026-10-14")
        self.assertEqual(resolved["version_label"],"0.2")
        self.assertEqual(resolved["version_index"],2)
        self.assertEqual(resolved["release_count"],2)
        self.assertEqual(sync.latest_record_id(first),24444444)
        self.assertTrue(sync.is_public_version(first,paper["concept_doi"]))
        wrong={**newest,"conceptdoi":"10.5281/zenodo.9999"}
        self.assertIsNone(sync.extract_release(paper,first,latest=wrong))
        first["links"]["latest"]="https://another-domain.org/api/records/24444444"
        self.assertIsNone(sync.latest_record_id(first))

    def test_zenodo_first_date_and_release_number_not_invented(self):
        import sys
        sys.path.insert(0, str(ROOT/"tools"))
        import resolve_zenodo as sync
        paper=self.site["papers"][0]
        original={
            "doi":paper["version_doi"],"conceptdoi":paper["concept_doi"],
            "metadata":{"publication_date":"2026-09-21"},
            "created":"2026-09-21T12:00:00Z",
            "versions":{"index":2}
        }
        # An old record with index=2 cannot establish the date of first release.
        fallback=sync.extract_release(paper,original)
        self.assertNotIn("first_published_on",fallback)
        self.assertNotIn("version_label",fallback)
        self.assertEqual(fallback["version_index"],2)
        self.assertEqual(fallback["last_version_on"],"2026-09-21")
        self.assertEqual(sync.version_index({"versions":{"index":True}}),None)
        # A complete dated history can establish first publication without index.
        initial={**original,"doi":"10.5281/zenodo.22000000","versions":{},"created":"2026-09-01T12:00:00Z",
                 "metadata":{"publication_date":"2026-09-01"}}
        result=sync.extract_release(paper,original,versions=[initial,original],history_complete=True)
        self.assertEqual(result["first_published_on"],"2026-09-01")
        # Drafts from another lineage must never be shown as public versions.
        draft={**initial,"is_draft":True}
        self.assertFalse(sync.is_public_version(draft,paper["concept_doi"]))

    def test_latest_published_version_doi_curated(self):
        expected={
            "P01":"10.5281/zenodo.23355587",
            "P02":"10.5281/zenodo.23355597",
            "P03":"10.5281/zenodo.23309603"
        }
        for p in self.site["papers"]:
            self.assertTrue(p["version_index_evidence"])
            if p["code"] in expected:
                self.assertEqual(p["version_doi"],expected[p["code"]])
                self.assertTrue(DOI.fullmatch(p["highlights_source_doi"]))
                self.assertNotEqual(p["highlights_source_doi"],p["version_doi"])
            self.assertTrue(p["first_published_on"])
            self.assertTrue(p["last_version_on"])

    def test_public_metadata_display_labels(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        detail=(ROOT/"paper.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        for name in ("firstPublished","lastChanged","latestVersionNumber"):
            self.assertIn(name+":",script)
            self.assertIn('data-i18n="'+name+'"',detail)
        for element in ("paper-first-published","paper-last-updated","paper-version-number"):
            self.assertIn('id="'+element+'"',detail)
        self.assertIn('item.first_published_on',script)
        self.assertIn('item.version_index',script)
        self.assertIn('function versionName(p)',script)
        self.assertIn('lastVersionDate(p)',script)

    def test_immutable_asset_urls_and_fingerprint(self):
        import hashlib
        import shutil
        import sys
        import tempfile
        sys.path.insert(0,str(ROOT/"tools"))
        from fingerprint_assets import stamp_site
        for page in ("index.html","paper.html","achievements.html"):
            html=(ROOT/page).read_text(encoding="utf-8")
            self.assertRegex(html, r'href="assets/site\.css\?v=[A-Za-z0-9._-]+"')
            self.assertRegex(html, r'src="assets/site\.js\?v=[A-Za-z0-9._-]+"')
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            (base/"assets").mkdir()
            for asset in ("assets/site.js","assets/site.css"):
                shutil.copyfile(ROOT/asset,base/asset)
            for page in ("index.html","paper.html","achievements.html"):
                shutil.copyfile(ROOT/page,base/page)
            stamp_site(base)
            digest=hashlib.sha256((base/"assets/site.js").read_bytes()).hexdigest()[:16]
            first=(base/"index.html").read_text(encoding="utf-8")
            self.assertIn("assets/site.js?v="+digest,first)
            self.assertIn("assets/site.js?v="+digest,(base/"paper.html").read_text(encoding="utf-8"))
            self.assertIn("assets/site.js?v="+digest,(base/"achievements.html").read_text(encoding="utf-8"))
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
            if p["code"] in {"P01","P02","P03"}:
                self.assertNotEqual(p["highlights_source_doi"],p["version_doi"])
                self.assertEqual(p["version_index"],2)
                self.assertEqual(p["first_published_on"],"2026-09-28")
            else:
                self.assertEqual(p["highlights_source_doi"],p["version_doi"])
                self.assertEqual(p["version_index"],1)
            self.assertTrue(DOI.fullmatch(p["highlights_source_doi"]))
            for h in p["highlights"]:
                self.assertTrue(h["en"].strip(),p["code"])
                self.assertTrue(h["ru"].strip(),p["code"])
                self.assertTrue(h["evidence"].strip(),p["code"])
                self.assertNotIn("TODO",h["en"])
                self.assertNotIn("TODO",h["ru"])
        self.assertEqual(sum(len(p["highlights"]) for p in self.site["papers"]),54)

    def test_author_profile_contact_and_ai_disclosure(self):
        """The public site has explicit, bilingual researcher identification and AI use."""
        page=(ROOT/"index.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('id="author"',page)
        self.assertIn('id="author-heading"',page)
        self.assertIn('id="ai-disclosure-heading"',page)
        self.assertIn("Alexandr Martinevski",page)
        self.assertIn('href="mailto:math@a-martinevski.com"',page)
        self.assertIn('href="https://orcid.org/0009-0000-4230-4414"',page)
        self.assertNotIn("alex.martinevski@gmail.com",page)
        self.assertLess(page.index('id="about"'),page.index('id="author"'))
        self.assertEqual(page.count('class="author-section"'),1)
        self.assertIn('href="#author" data-i18n="authorNav"',page)
        for key in ("authorNav","authorLabel","authorHeading","authorRole",
                    "aiDisclosureLabel","aiDisclosureHeading","aiDisclosureText"):
            self.assertIn(f'data-i18n="{key}"',page)
            self.assertEqual(script.count(key+":"),2, "Missing EN/RU translation: "+key)
        self.assertIn("Независимый исследователь",script)
        self.assertIn("выполнялись автором совместно с системами",script)
        self.assertIn("AI systems are not listed as co-authors",script)
        self.assertIn("За опубликованные утверждения",script)
        self.assertNotIn("GPT-5.6",page)
        self.assertNotIn("Claude Opus",page)

    def test_research_achievements_page_and_status_boundaries(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        article=(ROOT/"achievements.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('id="achievements"',home)
        self.assertIn('id="achievements-preview-heading"',home)
        self.assertEqual(home.count('class="achievement-preview-item"'),4)
        self.assertIn('href="#achievements" data-i18n="achievementNav"',home)
        self.assertIn('href="achievements.html?lang=en"',home)
        self.assertIn('data-page="achievements"',article)
        self.assertIn('href="https://math.a-martinevski.com/achievements.html"',article)
        self.assertEqual(article.count('class="achievement-feature"'),6)
        for anchor in ("ghz-exact","ghz-three","mixing","multilinear",
                       "cf-profile","stability"):
            self.assertIn('id="'+anchor+'"',article)
        self.assertIn("34/105",article)
        self.assertIn("105ζ(3)/(2π",article)
        self.assertIn("2.034968153548",article)
        self.assertIn("2.035329429153",article)
        self.assertIn("4√2",article)
        self.assertIn("2π",article)
        self.assertIn("Conjecture",article)
        self.assertIn("not solved in its full generality",article)
        self.assertIn("Independent verification",article)
        self.assertIn('href="https://doi.org/10.1103/PhysRevA.109.022205"',article)
        self.assertIn('href="https://doi.org/10.1016/0047-259X(85)90025-9"',article)
        concepts={p["code"]:p["concept_doi"] for p in self.site["papers"]}
        for code in ("P01","P04","P13"):
            self.assertIn('href="https://doi.org/'+concepts[code]+'"',article)
        self.assertNotIn("P05 —",article)
        self.assertNotIn("P10 —",article)
        self.assertIn('if(document.body.dataset.page==="achievements")return;',script)
        self.assertIn("data-achievements-link",script)

    def test_research_achievements_are_fully_bilingual(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        article=(ROOT/"achievements.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        import re
        labels=set(re.findall(r'data-i18n="(achievement[A-Za-z0-9]+)"',home+article))
        self.assertGreaterEqual(len(labels),50)
        for label in labels:
            # Source keys are JSON-quoted so a colon outside quoted text
            # differentiates a declaration from an ordinary string reference.
            self.assertEqual(script.count('"'+label+'":'),2,label)
        for name in ("achievementContextText","achievementGhzThreeZeta",
                     "achievementMultilinearScope","achievementEditorialSecond"):
            self.assertIn(name,labels)
        self.assertIn("гипотезе Римана",script)
        self.assertIn("не объявляется решённой",script)

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
        self.assertEqual(len(urls), len(self.site["papers"])+2)
        self.assertIn(hostname+"achievements.html",urls)
        for paper in self.site["papers"]:
            self.assertIn(hostname+"paper.html?code="+paper["code"], urls)
        self.assertTrue(all(u.startswith(hostname) for u in urls))

    def test_static_entrypoints_present(self):
        for rel in ("index.html","paper.html","achievements.html","assets/site.css","assets/site.js"):
            self.assertTrue((ROOT/rel).is_file(),rel)

if __name__=="__main__":
    unittest.main()
