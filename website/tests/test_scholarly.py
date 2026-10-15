#!/usr/bin/env python3
"""Regression suite for static scientific indexing; no network is needed."""
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
spec=importlib.util.spec_from_file_location("scholar_build",ROOT/"tools/build_scholarly_pages.py")
scholar=importlib.util.module_from_spec(spec)
spec.loader.exec_module(scholar)


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags=[]
    def handle_starttag(self,tag,attrs):
        self.tags.append((tag,dict(attrs)))


class ScholarlyIndexingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers,cls.metadata=scholar.load_data(ROOT)
        cls.temp=tempfile.TemporaryDirectory()
        cls.dest=Path(cls.temp.name)/"site"
        (cls.dest/"assets").mkdir(parents=True)
        for filename in ("site.css","scholar.js"):
            shutil.copyfile(ROOT/"assets"/filename,cls.dest/"assets"/filename)
        # No public network access and no fallback to older, unverified PDFs.
        scholar.build(ROOT,cls.dest,repo_root=Path(cls.temp.name)/"none",
                      fetch_pdfs=False)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_every_paper_has_unique_crawlable_html(self):
        self.assertEqual(len(self.papers),18)
        codes=set()
        for paper in self.papers:
            code=paper["code"];codes.add(code)
            source=self.metadata[code]
            path=self.dest/"publications"/code/"index.html"
            self.assertTrue(path.is_file(),code)
            text=path.read_text(encoding="utf-8")
            tags=Tags();tags.feed(text)
            metas={v["name"]:v["content"] for k,v in tags.tags
                   if k=="meta" and v.get("name")}
            self.assertEqual(metas["citation_title"],source["title"])
            self.assertEqual(metas["citation_author"],"Alexandr Martinevski")
            self.assertEqual(metas["citation_author_orcid"],
                             "https://orcid.org/0009-0000-4230-4414")
            self.assertEqual(metas["citation_doi"],source["version_doi"])
            self.assertEqual(metas["citation_publication_date"],
                             source["publication_date"].replace("-","/"))
            self.assertEqual(metas["citation_abstract_html_url"],
                             f"https://math.a-martinevski.com/publications/{code}/")
            self.assertNotIn("citation_pdf_url",metas)
            self.assertEqual(metas["robots"],"index,follow")
            self.assertIn('rel="canonical" href="https://math.a-martinevski.com/publications/'+code+'/"',text)
            self.assertIn('<h1 class="scholar-title">'+scholar.esc(source["title"])+"</h1>",text)
            self.assertIn('class="scholar-author citation_author"',text)
            self.assertIn('id="abstract"',text)
            # Native MathML is emitted before crawling, without JS or CDNs.
            if 'class="math inline"' in source["description_html"]:
                self.assertIn("<math",text)
                self.assertNotIn('class="math inline">\\(',text)
            self.assertIn(scholar.sanitized_abstract(source["description_html"])[0],text)
            self.assertEqual(text.count("<h1"),1)
            self.assertIn("https://doi.org/"+source["version_doi"],text)
            self.assertIn("https://doi.org/"+source["concept_doi"],text)
            self.assertIn("https://orcid.org/0009-0000-4230-4414",text)
            self.assertIn('"@type":"ScholarlyArticle"',text)
            self.assertIn('"@id":"https://math.a-martinevski.com/author/#researcher"',text)
            self.assertIn("https://zenodo.org/records/"+str(source["record_id"])+"/files/",text)
            self.assertNotIn('Main contributions, ranked by scientific significance',text)
            self.assertNotIn('<script src="../../assets/site.js',text)
            self.assertIn("scholar.js?v=",text)
            self.assertIn("BibTeX",text)
            self.assertNotIn("journalTitle",text)
        self.assertEqual(len(codes),18)
        self.assertNotIn("P05",codes)
        self.assertNotIn("P10",codes)

    def test_publication_index_and_author_identity_without_js(self):
        directory=(self.dest/"publications/index.html").read_text(encoding="utf-8")
        author=(self.dest/"author/index.html").read_text(encoding="utf-8")
        self.assertEqual(directory.count('class="scholar-list-item"'),18)
        self.assertEqual(author.count("<li><a"),18)
        self.assertIn('<h1 class="scholar-title">',directory)
        self.assertIn("0009-0000-4230-4414",author)
        self.assertIn("Alexandr Martinevski",author)
        self.assertIn('"@type":"Person"',author)
        self.assertNotIn('"worksFor"',author)
        self.assertIn('"sameAs":"https://orcid.org/0009-0000-4230-4414"',author)
        self.assertIn("mailto:math@a-martinevski.com",author)
        self.assertNotIn("citation_title",author)
        self.assertNotIn("citation_title",directory)
        for paper in self.papers:
            self.assertIn(paper["code"]+"/",directory)
            self.assertIn("publications/"+paper["code"]+"/",author)

    def test_sitemap_only_canonical_static_pages(self):
        sitemap=(self.dest/"sitemap.xml").read_text(encoding="utf-8")
        self.assertEqual(sitemap.count("<loc>"),23)
        self.assertNotIn("paper.html?code=",sitemap)
        self.assertIn("<loc>https://math.a-martinevski.com/publications/</loc>",sitemap)
        self.assertIn("<loc>https://math.a-martinevski.com/author/</loc>",sitemap)
        for paper in self.papers:
            self.assertIn("<loc>https://math.a-martinevski.com/publications/"
                          +paper["code"]+"/</loc>",sitemap)

    def test_live_home_links_and_legacy_urls(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        old=(ROOT/"paper.html").read_text(encoding="utf-8")
        script=(ROOT/"assets/site.js").read_text(encoding="utf-8")
        self.assertIn('href="publications/index.html?lang=en"',home)
        self.assertIn('href="author/index.html?lang=en"',home)
        self.assertIn('data-scholarly-index-link',home)
        self.assertIn('data-author-profile-link',home)
        self.assertIn('publications/"+encodeURIComponent(p.code)+"/index.html?lang="+language',script)
        self.assertIn('link.href="publications/index.html?lang="+language',script)
        self.assertIn('link.href="author/index.html?lang="+language',script)
        self.assertIn('<meta name="robots" content="noindex,follow">',old)
        self.assertIn('id="paper-title"',old)

    def test_unsafe_description_markup_is_rejected(self):
        for value in (
            '<p>Hello</p><script>alert(1)</script>',
            '<p onclick="alert(1)">Unsafe</p>',
            '<p><span class="other">Wrong</span></p>',
            '<p><span class="math inline">unclosed</p>',
        ):
            with self.subTest(value=value),self.assertRaises(ValueError):
                scholar.sanitized_abstract(value)

    def test_pdf_byte_check_and_same_directory_scholar_tag(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            local=root/"papers/example"/"paper.pdf"
            local.parent.mkdir(parents=True)
            payload=b"%PDF-"+b"fake-test-bytes"*90
            local.write_bytes(payload)
            base=self.metadata["P01"].copy()
            base.update(pdf_filename="P01_CF_V6_S8.pdf",pdf_size=len(payload),
                        pdf_md5=hashlib.md5(payload).hexdigest())
            p={"code":"P01","source_path":"papers/example"}
            dest=root/"site"/"publications"/"P01"
            self.assertTrue(scholar.mirror_pdf(p,base,root,dest,allow_fetch=False))
            self.assertEqual((dest/base["pdf_filename"]).read_bytes(),payload)
            paper=self.papers[0]
            full=scholar.paper_page(paper,self.metadata[paper["code"]],
                                    {"css":"test","js":"test"},has_pdf=True)
            self.assertIn('<meta name="citation_pdf_url" content="https://math.a-martinevski.com/publications/'
                          +paper["code"]+"/"+self.metadata[paper["code"]]["pdf_filename"]+'">',full)
            base["pdf_md5"]="0"*32
            self.assertFalse(scholar.file_signature(local,base))
            self.assertFalse(scholar.mirror_pdf(p,base,root,dest,allow_fetch=False))

    def test_source_data_rejects_nonpublic_or_swapped_identities(self):
        for code in ("P01","P04","P14","P20"):
            source=self.metadata[code]
            self.assertEqual(source["version_doi"].split(".")[-1],str(source["record_id"]))
            self.assertEqual(source["pdf_filename"],code+"_CF_V6_S8.pdf")
            self.assertRegex(source["pdf_md5"],r"^[0-9a-f]{32}$")
            self.assertLess(source["pdf_size"],5_000_000)
        self.assertEqual(len({p["version_doi"] for p in self.metadata.values()}),18)
        self.assertEqual(len({p["concept_doi"] for p in self.metadata.values()}),18)


if __name__=="__main__":
    unittest.main(verbosity=2)
