# CF Dependence — Public site editorial policy

This `website/` directory hosts a public catalogue of **released** research papers.
The scientific research workspace remains private at `alexmartinevski/CF-Dependence`.

## Publication vs DOI reservation
- List a paper only after an actual public release has been verified (Zenodo published record, not just a draft).
- `version_doi` is the DOI of the latest **published** version; `concept_doi` is the lineage DOI.
- A new reserved DOI is not evidence that a record has been published.
- Do not copy draft descriptions, review reports, internal statuses, project archives, tokens, or GitHub Actions credentials into this public repo.
- A positive review of a draft does not itself mean publication.

## Updating a paper
1. Confirm that the new record has been published, and record its version DOI and concept DOI.
2. Verify that it is the correct continuation/new publication and that the public title matches.
3. Update `website/data/papers.json` in a PR; retain old DOI in a dated `changes` entry if the actual public record supports that comparison.
4. Add a concise bilingual description of the **verified** mathematical/editorial changes. Do not invent changes.
5. Keep the public manuscript files under the existing `papers/` directories consistent with the linked published release, if updating them is approved.
6. Review the PR and merge to main to deploy via GitHub Pages; Zenodo Publish is a separate **manual action**.

## Current publication scope
The public catalogue contains **18 released works**: the previously published P01–P03 versions
and fifteen further CF V6 articles (P04, P06–P09, P11–P20) verified as published in Zenodo
on 2026-10-14. The P19/P20 PDF and DOIs were checked against their Zenodo public records.

**P05 and P10 remain excluded** because their drafts were not published.
The *new-version drafts* of P01–P03 are not yet independently confirmed as public records;
the site therefore retains the earlier published version DOIs and public PDF/TeX links.
Newer published papers link to their Zenodo records with PDF downloads instead of to
private research files. Individual version-change notes are not fabricated from
a change of title or an unpublished draft.

The September 28 repository release remains repository news, not a new Zenodo version.

## Site structure
- `website/index.html`: bilingual catalogue/search, public updates and project overview.
- `website/paper.html`: each paper detail by `?code=P01`.
- `website/data/papers.json`: manually curated released papers.
- `website/data/news.json`: verified public site/release notes.
- `website/assets/`: responsive CSS and JavaScript; no third-party tracking.
- `website/tests/test_public.py`: checks all entries are published and linked to local public materials.

Run locally:
```bash
python -m http.server 8000 --directory website
# open http://localhost:8000/
```

GitHub Pages: merge approved PR, then Settings → Pages → Source: GitHub Actions.
The public site will use the custom domain **`math.a-martinevski.com`**.
See [DOMAIN_SETUP_RU.md](DOMAIN_SETUP_RU.md) for the DNS and GitHub Settings steps.
Target URL after successful deploy and domain verification:
`https://math.a-martinevski.com/`.
This URL is not confirmed live until GitHub Pages is enabled and DNS/HTTPS checks pass.
For GitHub Actions deployments, no `CNAME` file is required or read by GitHub Pages.

## Research-area directory and current-version links (October 2026)
The home page now has a bilingual subject directory with exactly one primary area per
published paper, and shows each paper's existing verified summary, the date of its
last verified public release (if available), and the specific Version DOI from this
curated snapshot. As of 2026-10-14, P01–P03 do not have independently verified Zenodo
publication dates in the catalogue, so the interface explicitly says so instead of
reusing a repository release date.

**Primary links always use `concept_doi`**, which Zenodo resolves to the latest
published release. **The displayed `version_doi` is a fixed, independently
verifiable citation reference** and is only refreshed after the newer Zenodo
release is confirmed public. The Zenodo PDF action opens the concept landing page
so readers can select the current PDF. Older GitHub snapshots are clearly marked
"Archived PDF / Archived TeX"; they are not advertised as the newest release.
The site intentionally does not invent semantic version labels (v1, v0.19, etc.)
when Zenodo version metadata has not been independently checked.

To curate a new published version, update the specific DOI, the checked date and
the appropriate summary/change notes in a reviewed PR. The subject classification
(`area`) uses one of: `extremal`, `transport`, `algebra`, `harmonic`, `statistics`.
P05/P10 remain excluded.

### Automatic latest-version metadata (public Zenodo API)
During every Pages deploy and a daily read-only scheduled workflow, the standard-library
script `website/tools/resolve_zenodo.py` retrieves **published** Zenodo REST records,
follows only same-origin `links.latest` pointers, verifies the exact Concept DOI
lineage and emits `_site/data/zenodo_latest.json`. The browser merges that
same-origin metadata into the grouped directory and article pages. This enables
public release dates, semantic version labels (when present in Zenodo), and current
specific version DOIs without storing an API token. If the API cannot confirm a
record, the hand-curated metadata remains and the latest link still uses the
Zenodo Concept DOI. The read-only process cannot publish or change any Zenodo record.

## Asset caching: GitHub Pages + mobile browsers
The HTML references a versioned `assets/site.js` and `assets/site.css`.
At every Pages deployment `website/tools/fingerprint_assets.py` replaces
those query parameters with SHA-256 content fingerprints. This prevents an
updated page from running an old cached JavaScript, which caused a blank subject
index on Android Chrome after the subject directory was first deployed.
Catalogue/news requests use `cache: "no-store"` so the JavaScript and its
data cannot silently drift apart. If the subject map cannot be rendered the
user sees a localized fallback message; the complete article list still works.
CI tests both the renderer and fingerprinting.

## Research-programme introduction (October 2026)
The home-page research map starts with a bilingual, reader-facing account of the
scientific object, project objective and research method. The scientific formulation
distinguishes the fundamental signed interaction measure
`mu_P = P - (P_1 ⊗ ... ⊗ P_d)` from its original Fourier-factorization
observation, rather than claiming that the entire programme is one scalar metric.
The stated goal is to discover mathematically explanatory and transferable laws;
the research cycle moves from exploratory examples and invariants to rigorous
proofs and tests across heterogeneous problems. The introduction describes
scope, not a claim of novelty for the bare measure. The publication listing and
DOI/publication status policy are unchanged.

## Annotated publication catalogue (15 October 2026)
The grouped subject map is now the **single primary list**, replacing the redundant
18-card grid. Its integrated search filters article codes, titles, bilingual summaries,
subject names and bilingual result statements. The old `#papers` navigation anchor
is preserved at the search controls; individual `paper.html?code=Pxx` pages continue
to work and now show the same key results.

Every published record has **three bilingual scientific results**, kept in
`website/data/papers.json` under `highlights`. Each result includes an editorial
`evidence` key naming a matching LaTeX theorem/corollary/proposition/lemma label,
or `abstract` for a result expressly stated in the release abstract.
The `highlights_source_doi` is fixed to the **specific public version whose
manuscript was read**; an automatically discovered newer version DOI is never
silently substituted as the source of an unchecked result. A provenance link
appears automatically if the article's current version and highlight source
differ. The source manuscripts used were the published public P01–P03 TeX files
and the V6 S8 article sources for the other 15 public Zenodo releases.

Results distinguish proved from conditional bounds, do not advertise conjectures
as theorems, and explicitly retain important gaps (e.g. exact κ₃).
Future revisions should only change these claims following a fresh textual check.
Search, publication-count display, dated news and immutable Zenodo concept links
continue without a second bibliography grid.

## Publication chronology (15 October 2026)
Every grouped item and individual article page distinguishes three different
metadata fields: **first public release date**, **date of the latest public
revision**, and **latest published version**. The primary DOI still uses the
Zenodo Concept DOI, and a specific Version DOI remains visible for citation.

- Publication dates are **per-version `metadata.publication_date` values** from
  Zenodo's published version history; they do not refer to edits of the website,
  reserved drafts, or repository commits. Version dates in Zenodo are supplied
  as publication metadata, not proven to be the exact clock time of a Publish
  action.
- The version label is taken from Zenodo `metadata.version`. If that optional
  text is absent but a verified 1-based `versions.index` exists, the catalogue
  explicitly says "Zenodo release №N". The ordinal is not a guessed semantic
  version number.
- `website/tools/resolve_zenodo.py` consults the public versions endpoint
  (pagination enabled), validates every version's Concept DOI, rejects drafts,
  and orders releases by the authoritative version index or record creation time.
  A direct latest-public-version endpoint is used when the lineage API cannot
  supply a complete and ordered history.
- The static, independently curated first-publication snapshot for the 15 new
  release lineages P04, P06–P09, P11–P20 is 2026-10-14. P01–P03 remain
  explicitly unverified until their first release metadata can be resolved;
  published dates and version names are never extrapolated from reserved DOIs.
- The nightly/automatic build runs only public read-only GET requests and
  publishes a JSON snapshot used by the site; failures preserve the dated,
  verified catalogue metadata.
- The highlights' `highlights_source_doi` is not changed when live Zenodo
  metadata points to a newer version: scientific claims still cite their
  actual reviewed source version.
