#!/usr/bin/env python3
"""Offline synthetic +1 paper release: NO Zenodo, GitHub writes or real DOI.

Verifies that the site grows from its approved catalogue to N+1 from JSON
alone, including a fourth metadata shard, arbitrary safe release PDF suffix,
crawler-visible abstracts/MathML, checksum-based local PDF mirror, and
latest-four/full-history static EN/RU news fallbacks.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import build_scholarly_pages as scholar
import build_news_fallbacks as news_builder


class SyntheticNextPaperTests(unittest.TestCase):
    def setUp(self):
        self.work=tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        tmp=Path(self.work.name)
        self.site=tmp/"site"
        self.dist=tmp/"dist"
        self.repo=tmp/"repo"
        for path in ("data/scholarly","assets"):
            (self.site/path).mkdir(parents=True,exist_ok=True)
        for file in ("index.html","news.html","data/papers.json","data/news.json",
                     "assets/site.css","assets/scholar.js"):
            shutil.copyfile(ROOT/file,self.site/file)
        for path in (ROOT/"data/scholarly").glob("part-*.json"):
            shutil.copyfile(path,self.site/"data/scholarly"/path.name)
        (self.dist/"assets").mkdir(parents=True)
        for file in ("site.css","scholar.js"):
            shutil.copyfile(self.site/"assets"/file,self.dist/"assets"/file)
        original=json.loads((self.site/"data/papers.json").read_text(encoding="utf-8"))
        source=list(original["papers"])
        baseline={p["code"] for p in source}
        self.assertNotIn("P21",baseline)
        ref=next(p for p in source if p["code"]=="P20")
        fake=copy.deepcopy(ref)
        self.code="P21"
        self.version="10.5281/zenodo.999999921"
        self.concept="10.5281/zenodo.999999920"
        fake.update(code=self.code,title="OFFLINE SYNTHETIC paper for release infrastructure TEST ONLY",
                    status="published",version_doi=self.version,concept_doi=self.concept,
                    first_published_on="2026-10-16",last_version_on="2026-10-16",
                    published_on="2026-10-16",version_index=1,
                    version_index_evidence="OFFLINE UNIT TEST ONLY, NEVER PUBLISHED",
                    highlights_source_doi=self.version,
                    source_path="papers/21-synthetic-offline",changes=[])
        fake.pop("pdf_filename",None)
        fake.pop("record_url",None)
        source.append(fake)
        original["papers"]=source
        original["last_curated_on"]="2026-10-16"
        (self.site/"data/papers.json").write_text(
            json.dumps(original,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        latest=next(
            json.loads(path.read_text(encoding="utf-8"))["papers"]["P20"]
            for path in sorted((ROOT/"data/scholarly").glob("part-*.json"))
            if "P20" in json.loads(path.read_text(encoding="utf-8"))["papers"]
        )
        fake_meta=copy.deepcopy(latest)
        # Fake PDF bytes are deliberately not a real Zenodo file.
        self.pdf=b"%PDF-"+b"offline-test-not-a-publication"*90
        name="P21_CF_V8_RELEASE.pdf"
        fake_meta.update(title=fake["title"],version_doi=self.version,concept_doi=self.concept,
                         publication_date="2026-10-16",record_id=999999921,pdf_filename=name,
                         pdf_size=len(self.pdf),pdf_md5=hashlib.md5(self.pdf).hexdigest())
        (self.site/"data/scholarly/part-04.json").write_text(
            json.dumps({"schema":1,"papers":{"P21":fake_meta}},ensure_ascii=False,indent=2),
            encoding="utf-8")
        folder=self.repo/"papers/21-synthetic-offline"
        folder.mkdir(parents=True)
        (folder/"paper.pdf").write_bytes(self.pdf)
        (folder/"paper.tex").write_text("% OFFLINE TEST ONLY\n",encoding="utf-8")
        updates=json.loads((self.site/"data/news.json").read_text(encoding="utf-8"))
        updates["entries"].append({
            "date":"2026-10-16","kind":"publication_release",
            "source":"https://doi.org/"+self.version,
            "title":{"en":"OFFLINE P21 synthetic test only","ru":"ТЕСТ P21 — не публикация"},
            "summary":{"en":"Synthetic release exercise with no Zenodo writes.",
                       "ru":"Проверка инфраструктуры без обращения к Zenodo."}
        })
        (self.site/"data/news.json").write_text(
            json.dumps(updates,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    def test_19th_synthetic_release_builds_without_touching_network(self):
        originals,meta=scholar.load_data(self.site)
        self.assertEqual(len(originals),len({p["code"] for p in originals}))
        self.assertEqual(len(originals),19)
        self.assertEqual(len(meta),19)
        self.assertEqual(meta["P21"]["pdf_filename"],"P21_CF_V8_RELEASE.pdf")
        scholar.build(self.site,self.dist,repo_root=self.repo,fetch_pdfs=False)
        target=self.dist/"publications/P21"
        page=(target/"index.html").read_text(encoding="utf-8")
        self.assertIn("999999921",page)
        self.assertIn('name="citation_pdf_url"',page)
        self.assertIn('<math',page)
        self.assertIn("0009-0000-4230-4414",page)
        self.assertEqual((target/"P21_CF_V8_RELEASE.pdf").read_bytes(),self.pdf)
        self.assertEqual((self.dist/"publications/index.html").read_text(encoding="utf-8").count(
            'class="scholar-list-item"'),19)
        self.assertIn("19 research preprints",(self.dist/"publications/index.html").read_text(encoding="utf-8"))
        self.assertEqual((self.dist/"author/index.html").read_text(encoding="utf-8").count("<li><a"),19)
        sitemap=(self.dist/"sitemap.xml").read_text(encoding="utf-8")
        self.assertEqual(sitemap.count("<loc>"),24)
        self.assertIn("publications/P21/",sitemap)

    def test_new_news_automatically_enters_four_latest_and_full_archive(self):
        e=news_builder.entries(self.site)
        self.assertEqual(len(e),7)
        self.assertEqual(e[0]["source"],"https://doi.org/"+self.version)
        news_builder.build(self.site)
        home=(self.site/"index.html").read_text(encoding="utf-8")
        full=(self.site/"news.html").read_text(encoding="utf-8")
        first=home.split('id="news-items" aria-live="polite">')[1].split('class="news-all-link-wrap"')[0]
        self.assertEqual(first.count('class="news-item"'),4)
        self.assertIn("OFFLINE P21 synthetic test only",first)
        self.assertIn("ТЕСТ P21 — не публикация",first)
        self.assertEqual(full.count('class="news-item"'),7)
        self.assertIn("2026-09-28",full)
        self.assertIn('href="https://doi.org/'+self.version+'"',home)
        self.assertNotIn("github.com/alexmartinevski/CF-Dependence-Public/pull",full)

    def test_unpublished_or_unverified_19th_record_fails_closed(self):
        doc=json.loads((self.site/"data/papers.json").read_text(encoding="utf-8"))
        doc["papers"][-1]["status"]="draft"
        (self.site/"data/papers.json").write_text(json.dumps(doc),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"Unpublished"):
            scholar.load_data(self.site)

    def test_unlisted_news_doi_or_engineering_pr_rejected(self):
        doc=json.loads((self.site/"data/news.json").read_text(encoding="utf-8"))
        for source in ("https://doi.org/10.5281/zenodo.888880001",
                       "https://github.com/alexmartinevski/CF-Dependence-Public/pull/20"):
            with self.subTest(source=source):
                doc["entries"][-1]["source"]=source
                (self.site/"data/news.json").write_text(json.dumps(doc),encoding="utf-8")
                with self.assertRaises(ValueError):
                    news_builder.entries(self.site)


if __name__=="__main__":
    unittest.main(verbosity=2)
