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
        self.assertGreaterEqual(len(papers),18)
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
                self.assertRegex(p["pdf_filename"],r"^P\d{2}_[A-Za-z0-9][A-Za-z0-9._-]{0,150}\.pdf$")
                self.assertEqual(p["pdf_filename"][:3],p["code"])

    def test_change_log_entries_refer_to_doi(self):
        for p in self.site["papers"]:
            for c in p.get("changes",[]):
                self.assertRegex(c["date"],r"^\d{4}-\d{2}-\d{2}$")
                self.assertTrue(DOI.fullmatch(c["doi"]))
                self.assertTrue(c["summary"]["en"].strip())
                self.assertTrue(c["summary"]["ru"].strip())

    def test_news_sources_link_to_science_not_engineering_changes(self):
        import sys
        sys.path.insert(0,str(ROOT/"tools"))
        import build_news_fallbacks as news_builder
        entries=news_builder.entries(ROOT)
        self.assertGreaterEqual(len(entries),6)
        for event in entries:
            self.assertRegex(event["date"],r"^\d{4}-\d{2}-\d{2}$")
            self.assertTrue(event["title"]["en"].strip())
            self.assertTrue(event["summary"]["ru"].strip())
            self.assertNotIn("github.com",event["source"])
            self.assertNotIn("RELEASE_NOTES",event["source"])
        self.assertTrue(any(e["source"]=="achievements.html#ghz-exact" for e in entries))
        self.assertTrue(any(e["source"]=="achievements.html" for e in entries))
        highlights=[e for e in entries if e["kind"]=="research_highlight"]
        self.assertEqual(len(highlights),1)
        ghz=highlights[0]
        self.assertEqual(ghz["source"],"https://doi.org/10.5281/zenodo.23356092")
        self.assertEqual(ghz["date"],"2026-10-16")
        for language in ("en","ru"):
            self.assertIn("n ≥ 4",ghz["title"][language])
            self.assertIn("v₄ = 34/105",ghz["summary"][language])
            self.assertIn("n = 3",ghz["summary"][language])
        self.assertIn("Independent proof review",ghz["summary"]["en"])
        self.assertNotIn("peer-reviewed",ghz["summary"]["en"].lower())
        # No source is trusted merely because it resembles a Zenodo URL.
        self.assertTrue(all(e["kind"]!="publication_release" or
                            e["source"].startswith("https://doi.org/10.5281/zenodo.")
                            for e in entries))

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
            # Existing 2026-10-14 releases have fixed historical timestamps;
            # future released articles must not inherit those dates.
            if p["code"] in {"P04","P06","P07","P08","P09","P11","P13","P14","P15","P16","P17","P18","P19","P20"}:
                self.assertEqual(p["first_published_on"],"2026-10-14")
                self.assertEqual(p["last_version_on"],"2026-10-14")
            elif p["code"]=="P12":
                self.assertEqual(p["first_published_on"],"2026-10-14")
                self.assertGreaterEqual(p["last_version_on"],"2026-10-15")
            elif p["code"] in {"P01","P02","P03"}:
                self.assertEqual(p["first_published_on"],"2026-09-28")
                self.assertEqual(p["last_version_on"],"2026-10-12" if p["code"]=="P03" else "2026-10-14")
            else:
                self.assertTrue(p.get("first_published_on"))
                self.assertTrue(p.get("last_version_on"))

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

    def test_october_2026_four_public_records_and_p12_lineage(self):
        verified={
            "P12":(23355668,23406562,"2026-10-15","P12_CF_V7_R40.pdf"),
            "P21":(23406540,23406541,"2026-10-16","P21_CF_V7_R40.pdf"),
            "P22":(23406544,23406545,"2026-10-16","P22_CF_V7_R40.pdf"),
            "P27":(23406554,23406555,"2026-10-16","P27_CF_V7_R40.pdf"),
        }
        papers={p["code"]:p for p in self.site["papers"]}
        self.assertGreaterEqual(len(papers),21)
        self.assertTrue(verified.keys()<=papers.keys())
        self.assertFalse({"P05","P10"} & set(papers))
        for code,(concept_id,release_id,first_or_new_date,pdf_name) in verified.items():
            p=papers[code]
            self.assertEqual(p["concept_doi"],f"10.5281/zenodo.{concept_id}")
            self.assertGreaterEqual(p["last_version_on"],first_or_new_date)
            self.assertEqual(p["status"],"published")
            self.assertEqual(len(p["highlights"]),3)
            self.assertTrue(p["highlights_source_doi"].startswith("10.5281/zenodo."))
            if p["version_doi"]==f"10.5281/zenodo.{release_id}":
                self.assertEqual(p["pdf_filename"],pdf_name)
            if code=="P12":
                self.assertEqual(p["first_published_on"],"2026-10-14")
                self.assertGreaterEqual(p["version_index"],2)
            else:
                self.assertEqual(p["first_published_on"],"2026-10-16")
        released={e["source"] for e in self.news["entries"] if e["kind"]=="publication_release"}
        for code,(_,release_id,_,_) in verified.items():
            self.assertIn(f"https://doi.org/10.5281/zenodo.{release_id}",released,code)

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
        for page in ("index.html","paper.html","achievements.html","news.html"):
            html=(ROOT/page).read_text(encoding="utf-8")
            self.assertRegex(html, r'href="assets/site\.css\?v=[A-Za-z0-9._-]+"')
            self.assertRegex(html, r'src="assets/site\.js\?v=[A-Za-z0-9._-]+"')
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            (base/"assets").mkdir()
            for asset in ("assets/site.js","assets/site.css"):
                shutil.copyfile(ROOT/asset,base/asset)
            for page in ("index.html","paper.html","achievements.html","news.html"):
                shutil.copyfile(ROOT/page,base/page)
            stamp_site(base)
            digest=hashlib.sha256((base/"assets/site.js").read_bytes()).hexdigest()[:16]
            first=(base/"index.html").read_text(encoding="utf-8")
            self.assertIn("assets/site.js?v="+digest,first)
            self.assertIn("assets/site.js?v="+digest,(base/"paper.html").read_text(encoding="utf-8"))
            self.assertIn("assets/site.js?v="+digest,(base/"achievements.html").read_text(encoding="utf-8"))
            self.assertIn("assets/site.js?v="+digest,(base/"news.html").read_text(encoding="utf-8"))
            (base/"assets/site.js").write_bytes((base/"assets/site.js").read_bytes()+b"\n/* changed */")
            stamp_site(base)
            self.assertNotIn("assets/site.js?v="+digest,(base/"index.html").read_text(encoding="utf-8"))

    def test_scientific_programme_introduction(self):
        """The research programme follows the subject directory and precedes the author."""
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertLess(html.index('id="area-groups"'),html.index('id="programme-heading"'))
        self.assertLess(html.index('id="programme-heading"'),html.index('id="author"'))
        self.assertIn('id="programme"',html)
        self.assertIn('μ<sub>P</sub>',html)
        self.assertIn('D<sub>d</sub>(P)',html)
        for key in ("programmeLabel","programmeHeading","programmeLead","programmeObject",
                    "programmeObjectHeading","programmeObjectNote","programmeGoalHeading",
                    "programmeGoal","programmeMethodHeading","programmeMethod","programmeBridge"):
            self.assertIn(f'data-i18n="{key}"',html)
            self.assertEqual(script.count(f'{key}:'),2,key)
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
                self.assertGreaterEqual(p["version_index"],2 if p["code"]=="P12" else 1)
            self.assertTrue(DOI.fullmatch(p["highlights_source_doi"]))
            for h in p["highlights"]:
                self.assertTrue(h["en"].strip(),p["code"])
                self.assertTrue(h["ru"].strip(),p["code"])
                self.assertTrue(h["evidence"].strip(),p["code"])
                self.assertNotIn("TODO",h["en"])
                self.assertNotIn("TODO",h["ru"])
        self.assertEqual(sum(len(p["highlights"]) for p in self.site["papers"]),3*len(self.site["papers"]))

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
        self.assertIn("proposed exact value",article)
        self.assertIn("not settled",article)
        self.assertIn("Independent mathematical and historical reviews",article)
        self.assertIn('href="https://doi.org/10.1103/PhysRevA.109.022205"',article)
        self.assertIn('href="https://doi.org/10.1016/0047-259X(85)90025-9"',article)
        concepts={p["code"]:p["concept_doi"] for p in self.site["papers"]}
        for code in ("P01","P04","P13"):
            self.assertIn('href="https://doi.org/'+concepts[code]+'"',article)
        self.assertNotIn("P05 —",article)
        self.assertNotIn("P10 —",article)
        self.assertIn('if(document.body.dataset.page==="achievements")return;',script)
        self.assertIn("data-achievements-link",script)

    def test_p04_leads_with_complete_nge4_result_and_verifiable_sources(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        article=(ROOT/"achievements.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        marker='<article class="achievement-preview-item" data-featured-result="P04">'
        self.assertEqual(home.count(marker),1)
        self.assertEqual(home.index(marker),
                         home.index('<article class="achievement-preview-item"'))
        feature=home.split(marker,1)[1].split("</article>",1)[0]
        self.assertIn("n ≥ 4",feature)
        self.assertIn("v<sub>n</sub><sup>GHZ,XY</sup>",feature)
        self.assertIn("ζ(2n) / ζ(n)",feature)
        self.assertIn("v₄ = 34/105",feature)
        self.assertIn("arbitrary finite settings",feature)
        self.assertIn('href="https://doi.org/10.5281/zenodo.23356092"',feature)
        self.assertIn('href="https://doi.org/10.1103/PhysRevA.109.022205"',feature)
        self.assertIn("n = 3 remains open",feature)
        self.assertIn("External proof and priority review is pending",feature)
        section=article.split('id="ghz-exact"',1)[1].split("</article>",1)[0]
        self.assertIn("v<sub>n</sub><sup>GHZ,XY</sup>",section)
        self.assertIn('href="https://doi.org/10.5281/zenodo.23356092"',section)
        self.assertIn("Designolle–Vértesi–Pokutta (2024)",section)
        self.assertIn("Independent mathematical and historical reviews",section)
        for key in ("achievementGhzExactReadPaper",
                    "achievementGhzExactPrior2024",
                    "achievementGhzExactCaveat"):
            self.assertEqual(script.count('"'+key+'":'),2,key)
        self.assertIn("для всех n ≥ 4",script)
        self.assertIn("n = 3 остаётся открытым",script)

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
        self.assertIn("не решена полностью",script)

    def test_each_achievement_has_plain_language_explanation_and_own_references(self):
        """Every result must explain the problem before its equation and cite 5–7 relevant sources."""
        import re
        from urllib.parse import urlsplit
        article=(ROOT/"achievements.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        blocks=re.findall(
            r'<article class="achievement-feature" id="([^"]+)">([\s\S]*?)</article>',
            article
        )
        self.assertEqual(len(blocks),6)
        expected={
            "ghz-exact":6,"ghz-three":7,"mixing":6,
            "multilinear":6,"cf-profile":7,"stability":7
        }
        total=0
        for anchor,body in blocks:
            self.assertIn(anchor,expected)
            self.assertEqual(body.count('class="achievement-explanation-part"'),4,anchor)
            labels=[
                'achievementProblemTitle','achievementOriginTitle',
                'achievementImportanceTitle','achievementAnswerTitle'
            ]
            positions=[body.index('data-i18n="'+name+'"') for name in labels]
            self.assertEqual(positions,sorted(positions),anchor)
            self.assertLess(positions[-1],body.index('class="achievement-equation"'),anchor)
            self.assertEqual(body.count('class="achievement-sources"'),1,anchor)
            self.assertEqual(body.count('class="achievement-references"'),1,anchor)
            section=re.search(
                r'<ol class="achievement-references"[^>]*>([\s\S]*?)</ol>',
                body
            )
            self.assertIsNotNone(section,anchor)
            links=re.findall(r'<a href="([^"]+)"[^>]*>([^<]+)</a>',section.group(1))
            self.assertEqual(len(links),expected[anchor],anchor)
            self.assertEqual(len({uri for uri,_ in links}),len(links),anchor)
            total+=len(links)
            for uri,title in links:
                parsed=urlsplit(uri)
                self.assertEqual(parsed.scheme,"https",anchor)
                self.assertEqual(parsed.hostname,"doi.org",anchor)
                self.assertTrue(title.strip(),anchor)
                if parsed.hostname=="doi.org":
                    self.assertTrue(parsed.path.startswith("/10."),anchor)
            self.assertIn('data-i18n="achievementSourcesHeading"',body)
            self.assertIn('class="achievement-sources-count">('+str(expected[anchor])+')',body)
            # One original CF publication is a source in every group.
            self.assertRegex(section.group(1),r'href="https://doi\.org/10\.5281/zenodo\.\d+"')
        self.assertEqual(total,39)
        labels=set(re.findall(r'data-i18n="(achievement[A-Za-z0-9]+|sourceRole[A-Za-z0-9]+)"',article))
        for key in labels:
            self.assertEqual(script.count('"'+key+'":'),2,key)
        self.assertIn("Задача",script)
        self.assertIn("доказана",script)

    def test_achievement_mathematical_setups_and_sharpness(self):
        """Every public achievement states the mathematical object before its theorem."""
        import re
        from math import pi, isclose, sqrt
        page=(ROOT/"achievements.html").read_text(encoding="utf-8")
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        articles=re.findall(
            r'<article class="achievement-feature" id="([^"]+)">([\s\S]*?)</article>',
            page
        )
        self.assertEqual(len(articles),6)
        self.assertEqual(home.count('class="achievement-preview-formula"'),4)
        expected={
            "ghz-exact":("κ<sub>n</sub>", "ζ(s)"),
            "ghz-three":("L<sub>3</sub>", "105ζ(3)"),
            "mixing":("α(ℱ,𝒢)", "K<sub>G</sub>(2)"),
            "multilinear":("d<sub>∞</sub>(B)", "‖B‖<sub>ℂ</sub>"),
            "cf-profile":("𝒞<sub>d</sub>(r)", "ℙ(ε=1)"),
            "stability":("Δ(P)", "dist<sub>W<sub>p</sub></sub>")
        }
        for identifier,body in articles:
            self.assertIn(identifier,expected)
            self.assertEqual(body.count('class="achievement-math-context"'),1,identifier)
            self.assertEqual(body.count('achievement-equation-setup"'),1,identifier)
            self.assertEqual(body.count('achievement-equation-extra"'),1,identifier)
            self.assertEqual(body.count('class="math-line"'),3,identifier)
            self.assertIn('data-i18n="achievementMathSetupTitle"',body)
            self.assertIn('data-i18n="achievementMathResultTitle"',body)
            self.assertEqual(body.count('class="achievement-math-notation"'),2,identifier)
            self.assertLess(body.index('class="achievement-explanation"'),
                            body.index('class="achievement-math-context"'),identifier)
            self.assertLess(body.index('achievement-equation-setup"'),
                            body.index('class="achievement-equation" role="math"'),identifier)
            self.assertLess(body.index('achievement-equation-extra"'),
                            body.index('class="achievement-sources"'),identifier)
            for symbol in expected[identifier]:
                self.assertIn(symbol,body,identifier)
        self.assertIn("K<sub>G</sub>(2) = √2",page)
        self.assertIn("π<sup>3</sup>/16",page)
        self.assertIn("b<sub>d</sub>η<sup>2</sup>",page)
        self.assertIn("n≥4",page)
        self.assertIn("S ≤ π",page)
        self.assertIn("sup<sub>m,L≠0</sub>",page)
        self.assertIn("𝔼(XY) − (𝔼X)(𝔼Y)",page)
        self.assertEqual(script.count('"achievementMathSetupTitle":'),2)
        self.assertEqual(script.count('"achievementMathResultTitle":'),2)
        self.assertEqual(script.count('"achievementStabilityMathDetail":'),2)
        # Regression arithmetic, not a proof or a numerical certificate.
        q=(11,13,17,19,23,29,31)
        low=(pi**3/16)*((28/27)*(126/125)*(344/343)+sum(z**-3 for z in q))
        self.assertTrue(isclose(low,2.034968153548,abs_tol=1e-9))
        self.assertTrue(isclose(4*sqrt(2),5.65685424949,abs_tol=1e-8))
        self.assertTrue(isclose(105/34,3.088235294117647,abs_tol=1e-11))
        self.assertNotIn("mathjax",page.lower())
        self.assertNotIn("cdn.jsdelivr.net",page)

    def test_latest_updates_visible_and_aligned_near_top(self):
        import shutil
        import tempfile
        import sys
        sys.path.insert(0,str(ROOT/"tools"))
        import build_news_fallbacks as news_builder
        css=(ROOT/"assets/site.css").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            site=Path(tmp);(site/"data").mkdir()
            for name in ("index.html","news.html"):
                shutil.copyfile(ROOT/name,site/name)
            for name in ("papers.json","news.json"):
                shutil.copyfile(ROOT/"data"/name,site/"data"/name)
            news_builder.build(site)
            html=(site/"index.html").read_text(encoding="utf-8")
            updates=html[html.index('id="updates"'):html.index('id="about"')]
            self.assertLess(html.index('id="achievements"'),html.index('id="updates"'))
            self.assertLess(html.index('id="updates"'),html.index('id="about"'))
            self.assertEqual(updates.count('class="news-item"'),min(4,len(self.news["entries"])))
            for item in news_builder.entries(site)[:4]:
                self.assertIn('datetime="'+item["date"]+'"',updates)
                self.assertIn(item["title"]["en"],updates)
                self.assertIn(item["title"]["ru"].replace("&","&amp;"),updates)
            self.assertIn('href="news.html?lang=en"',updates)
            self.assertNotIn("GitHub PR #",updates)
            self.assertIn('data-news-en=',updates)
            self.assertIn('data-news-ru=',updates)
        self.assertIn('.news-section>.news-items{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))',css)
        self.assertIn('.news-page .news-all-grid{grid-template-columns:1fr',css)
        self.assertIn('const HOME_NEWS_LIMIT=4;',script)
        self.assertIn('events.slice(0,HOME_NEWS_LIMIT)',script)
        self.assertIn('if(newsLoaded)renderUpdates($("news-items"),true)',script)
        self.assertIn('fetch("data/news.json",{cache:"no-store"}).catch(()=>null)',script)

    def test_site_news_references_real_research_content(self):
        events=self.news["entries"]
        updates=[e for e in events if e["kind"]=="site_update"]
        self.assertGreaterEqual(len(events),6)
        self.assertGreaterEqual(len(updates),2)
        self.assertEqual([e["source"] for e in updates[:2]],
                         ["achievements.html#ghz-exact","achievements.html"])
        historic=[e for e in events if e["kind"] in
                 {"collection_update","public_collection_release"}]
        self.assertEqual(len(historic),2)
        self.assertTrue(all(e["source"]=="publications/" for e in historic))
        for entry in updates[:2]:
            self.assertEqual(entry["date"],"2026-10-15")
            self.assertTrue(entry["title"]["ru"])
        html=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('data-news-source="achievements.html#ghz-exact"',html)
        self.assertIn('data-news-source="achievements.html"',html)

    def test_catalogue_is_compact_and_project_nav_follows_section_order(self):
        import re
        page=(ROOT/"index.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        css=(ROOT/"assets/site.css").read_text(encoding="utf-8")
        self.assertEqual(page.count('id="papers"'),1)
        self.assertEqual(page.count('id="about"'),1)
        self.assertEqual(page.count('id="areas"'),1)
        self.assertEqual(page.count('id="programme"'),1)
        self.assertEqual(page.count('id="area-groups"'),1)
        self.assertEqual(page.count('class="science-intro"'),1)
        self.assertIn('class="section areas-section project-catalogue" id="papers"',page)
        self.assertIn('class="project-science-section" id="about"',page)
        self.assertNotIn('id="about-heading"',page)
        self.assertNotIn('data-i18n="aboutHeading"',page)
        self.assertNotIn('data-i18n="aboutText"',page)
        self.assertIn('data-i18n="catalogueLabel"',page)
        self.assertIn('class="section-heading catalogue-heading"',page)
        self.assertIn('class="sr-only" data-i18n="papersHeading"',page)
        self.assertEqual(script.count('catalogueLabel:'),2)
        self.assertEqual(script.count('aboutHeading:'),0)
        self.assertEqual(script.count('aboutText:'),0)
        self.assertIn('НАПРАВЛЕНИЯ И ПУБЛИКАЦИИ',script)
        self.assertIn('RESEARCH AREAS & PUBLICATIONS',script)
        self.assertIn('.project-catalogue>.catalogue-heading{margin:0 0 8px}',css)
        self.assertIn('.project-science-section{position:relative}',css)
        positions=[page.index('id="'+x+'"') for x in
                   ("achievements","updates","papers","about","author")]
        self.assertEqual(positions,sorted(positions))
        main=page[page.index('<div class="nav-actions">'):
                  page.index('<button class="language"')]
        links=re.findall(r'<a href="#([^"]+)" data-i18n="([^"]+)"',main)
        self.assertEqual(links,[
            ("achievements","achievementNav"),
            ("updates","updates"),
            ("papers","papers"),
            ("about","about"),
            ("author","authorNav")
        ])
        self.assertNotIn('href="#areas" data-i18n="areasNav"',page)
        self.assertIn('Расположенные выше публикации',script)
        self.assertLess(page.index('id="papers"'),page.index('id="about"'))
        self.assertLess(page.index('id="about"'),page.index('id="author"'))

    def test_brand_links_preserve_chosen_language(self):
        import re
        for path in ("index.html","paper.html","achievements.html","news.html"):
            html=(ROOT/path).read_text(encoding="utf-8")
            matches=re.findall(r'<a class="brand"[^>]*>',html)
            self.assertEqual(len(matches),1,path)
            link=matches[0]
            self.assertIn('data-home-link',link,path)
            self.assertIn('href="index.html?lang=en"',link,path)
            self.assertNotIn('href="index.html"',link,path)
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('document.querySelectorAll("[data-home-link]")',script)
        self.assertIn('link.href="index.html?lang="+language',script)
        self.assertIn('link.href="index.html?lang="+language+"#papers"',script)

    def test_news_history_page_and_translations(self):
        import shutil
        import tempfile
        import re
        import sys
        sys.path.insert(0,str(ROOT/"tools"))
        import build_news_fallbacks as news_builder
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        css=(ROOT/"assets/site.css").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            site=Path(tmp);(site/"data").mkdir()
            for name in ("index.html","news.html"):
                shutil.copyfile(ROOT/name,site/name)
            for name in ("papers.json","news.json"):
                shutil.copyfile(ROOT/"data"/name,site/"data"/name)
            news_builder.build(site)
            html=(site/"news.html").read_text(encoding="utf-8")
            home=(site/"index.html").read_text(encoding="utf-8")
            events=news_builder.entries(site)
            self.assertIn('data-page="news"',html)
            self.assertIn('id="news-full-list"',html)
            self.assertEqual(html.count('class="news-item"'),len(events))
            self.assertEqual(home.count('class="news-item"'),min(4,len(events)))
            self.assertIn('data-news-en=',html)
            self.assertIn('data-news-ru=',html)
            self.assertNotIn("github.com/alexmartinevski/CF-Dependence-Public",html)
            for event in events:
                self.assertIn('datetime="'+event["date"]+'"',html)
                self.assertIn(event["title"]["en"],html)
                self.assertIn('href="'+event["url"]+'"',html)
                if event["internal"]:
                    self.assertIn('data-news-source="'+event["source"]+'"',html)
            self.assertIn('href="https://math.a-martinevski.com/news.html"',html)
        self.assertIn('function renderNewsPage()',script)
        self.assertIn('news.html?lang=',script)
        self.assertIn('[data-news-en][data-news-ru]',script)
        self.assertIn('.news-page .news-all-grid{grid-template-columns:repeat(2,minmax(0,1fr))',css)
        self.assertIn('.news-page .news-all-grid{grid-template-columns:1fr',css)
        for key in ("newsAllLink","newsPageHeading","newsPageLead",
                    "newsPageListHeading","newsPageIntro","newsPageNote",
                    "newsPageBack","newsPageEyebrow",
                    "newsFormulasLink","newsAchievementsLink","newsPublicationsLink"):
            self.assertEqual(script.count(key+':'),2,key)

    def test_paper_summaries_are_short_priority_focused_and_source_accurate(self):
        """Concise 18-paper bilingual summaries; no extra card length or result count."""
        papers={p["code"]:p for p in self.site["papers"]}
        original_lengths={
            "P01":(140,130),"P02":(156,146),"P03":(152,136),
            "P04":(173,166),"P06":(153,162),"P07":(176,159),
            "P08":(144,136),"P09":(160,139),"P11":(150,148),
            "P12":(184,165),"P13":(150,171),"P14":(153,147),
            "P15":(138,154),"P16":(159,152),"P17":(146,158),
            "P18":(148,164),"P19":(143,161),"P20":(158,173)
        }
        self.assertTrue(set(original_lengths).issubset(set(papers)))
        self.assertGreaterEqual(len(papers),len(original_lengths))
        originals={code:papers[code] for code in original_lengths}
        for code,p in originals.items():
            old_en,old_ru=original_lengths[code]
            self.assertLessEqual(len(p["summary"]["en"]),old_en,code)
            self.assertLessEqual(len(p["summary"]["ru"]),old_ru,code)
            self.assertEqual(len(p["highlights"]),3,code)
            self.assertTrue(all(h.get("en") and h.get("ru") and h.get("evidence")
                                for h in p["highlights"]),code)
        self.assertLessEqual(sum(len(p["summary"]["en"]) for p in originals.values()),2757)
        self.assertLessEqual(sum(len(p["summary"]["ru"]) for p in originals.values()),2750)
        self.assertLessEqual(sum(len(h["en"]) for p in originals.values()
                                 for h in p["highlights"]),7734)
        self.assertLessEqual(sum(len(h["ru"]) for p in originals.values()
                                 for h in p["highlights"]),8298)
        self.assertEqual(sum(len(p["highlights"]) for p in originals.values()),54)
        # The site must use the currently released Zenodo titles, not old branches.
        self.assertEqual(papers["P02"]["title"],
            "The price of prescribed marginals in characteristic-function dependence: phase contact and complete mixability")
        self.assertEqual(papers["P03"]["title"],
            "Local factor profiles and arithmetic resolution of Chebyshev–Lucas critical polynomials")
        # Put the leading results first and retain limits on novelty/attainability.
        self.assertIn("GHZ",papers["P04"]["summary"]["en"])
        self.assertIn("n≥4",papers["P04"]["highlights"][0]["en"])
        self.assertIn("not exactly determined",papers["P04"]["highlights"][1]["en"])
        self.assertIn("full symmetric group",papers["P14"]["highlights"][0]["en"])
        self.assertIn("density one",papers["P14"]["highlights"][1]["en"])
        self.assertIn("1−1/√2",papers["P11"]["highlights"][0]["en"])
        self.assertIn("uniformly consistent",papers["P20"]["highlights"][0]["en"])
        self.assertIn("Uniform marginals",papers["P02"]["highlights"][0]["en"])
        self.assertIn("Gaussian",papers["P02"]["highlights"][1]["en"])
        self.assertIn("remains open",papers["P03"]["highlights"][2]["en"])
        self.assertIn("cycle rank",papers["P07"]["highlights"][0]["en"])
        self.assertIn("already known",papers["P16"]["highlights"][0]["en"])
        self.assertNotIn("Epanechnikov",str(papers["P02"]["highlights"]))
        self.assertNotIn("thm:even",str(papers["P03"]["highlights"]))
        self.assertNotIn("thm:2p1",str(papers["P03"]["highlights"]))

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
        # The checked-in sitemap must exactly match the current canonical
        # published catalogue; no stale 18-paper snapshots, no extra P-IDs.
        expected=[
            hostname,
            hostname+"achievements.html",
            hostname+"news.html",
            hostname+"publications/",
            hostname+"author/",
        ] + [hostname+"publications/"+p["code"]+"/"
             for p in self.site["papers"]]
        self.assertEqual(urls,expected,
                         "Source sitemap differs from verified publication catalogue")
        self.assertEqual(len(urls),len(set(urls)),
                         "Duplicate canonical URLs in sitemap")
        self.assertEqual(len(urls),len(self.site["papers"])+5)
        self.assertNotIn(hostname+"paper.html?code=P01",urls)
        self.assertTrue(all(u.startswith(hostname) for u in urls))
        # Static non-JS fallback must never hard-code the publication count.
        self.assertIn("data-scholarly-index-link",homepage)
        self.assertIn("Browse scholarly abstracts and citations ↗",homepage)
        self.assertNotRegex(homepage,
                            r"Browse scholarly abstracts and citations \(\d+\)")

    def test_static_entrypoints_present(self):
        for rel in ("index.html","paper.html","achievements.html","news.html",
                    "assets/site.css","assets/site.js","assets/scholar.js",
                    "tools/build_scholarly_pages.py","data/scholarly/part-01.json",
                    "data/scholarly/part-02.json","data/scholarly/part-03.json"):
            self.assertTrue((ROOT/rel).is_file(),rel)

if __name__=="__main__":
    unittest.main()
