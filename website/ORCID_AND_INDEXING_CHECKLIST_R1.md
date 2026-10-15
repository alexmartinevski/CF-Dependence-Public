# CF Dependence: scientific indexing and ORCID verification

## Automatic checks and public pages

- The public site has exactly **18 released papers**, each with its own
  pre-rendered abstract at /publications/Pxx/ (not JavaScript dependent).
- Each page includes citation_title, citation_author, citation_publication_date,
  citation_doi and the creator's ORCID, plus Schema.org ScholarlyArticle data.
- /publications/ is an index reachable from the homepage; /author/ lists all
  18 works under persistent identifier 0009-0000-4230-4414.
- Full PDF links target the exact public Zenodo record. A same-directory PDF
  and citation_pdf_url appear ONLY after matching PDF header, MD5 and byte size.
- The DOI lineage is explicit: citation_doi refers to a fixed version;
  concept DOI links to all versions. No private manuscripts or tokens are used.

## Manual actions after deployment

1. Google Search Console: verify domain ownership if necessary; submit
   https://math.a-martinevski.com/sitemap.xml. Inspect the URL for P01, P04,
   and P14. Request indexing where appropriate. This does not guarantee Scholar.
2. Google Scholar: after recrawling, search exact titles and
   site:math.a-martinevski.com; verify author, date and duplicate clustering
   with the original Zenodo records.
3. ORCID: sign in to https://orcid.org/0009-0000-4230-4414. Confirm that 18
   DOI works are listed. Add math.a-martinevski.com in Websites & social links.
   Use the DataCite Search & Link tool to import any missing Zenodo DOI works
   and grant DataCite update permission if you choose. Public HTML cannot
   change a private ORCID account; owner authentication is required.
4. Zenodo/DataCite: public DOI metadata should include the author ORCID.
   The approved source records contained that ORCID for all 18 versions.
   Recheck after any future Zenodo metadata edits; only read-only comparison
   is performed by this site pipeline.
5. Track 18/18 indexed pages, verified local-PDF count, ORCID works, and
   search-console crawling errors. Do not confuse successful site deployment
   with guaranteed Google Scholar indexing or peer review.

## References

- Google Scholar: https://scholar.google.com/intl/us/scholar/inclusion.html
- ORCID auto-update: https://info.orcid.org/ufaqs/what-is-orcid-auto-update-orcid-auto-update-enables-authors-to-have-their-orcid-records-automatically-updated-it-works-like-this/
- ORCID guidance: https://info.orcid.org/researchers/
