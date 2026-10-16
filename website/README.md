# Canonical publication catalogue v3 — 16 October 2026

Authoritative edited data is now **website/data/publications.json** (one file for all published papers). First/last publication dates are stored fields and checked against release history, never inferred. CI generates untracked compatibility views `data/papers.json` and `data/scholarly/part-*.json` before validation and deployment. Existing sections below describe earlier R1/R2 history and must not be followed for manually editing those views. See [PUBLICATIONS_V3_MIGRATION_RU.md](PUBLICATIONS_V3_MIGRATION_RU.md).

---

# Verified PDF cache R2.1 — 16.10.2026

The optional public Zenodo mirror is now resumable across Pages builds:
a previously complete public artifact and GitHub Actions cache may supply
PDF bytes, but every file is revalidated against the currently approved
Zenodo version's MD5, exact byte length, PDF header and filename.
No stale or corrupt file is served. New verified downloads replenish
the cache. See website/PDF_MIRROR_CACHE_R2_1.md for retention limits,
read-only artifact trust boundaries, tests and final deployment QA.

---
# Release automation R2 — 16 October 2026

New publications are driven by three public data sources only:
website/data/papers.json, website/data/scholarly/part-*.json, and
website/data/news.json. Counts, archive pages, sitemap and static bilingual
news fallback cards are generated automatically during Pages deployment.

The scholarly builder discovers any numbered metadata shards and supports
safe release PDF filenames rather than only CF_V6_S8. Verified PDF mirrors
require exact MD5 and bytes and a PDF header, with a 64 MiB limit.
Otherwise the fixed published Zenodo PDF is linked without a false
citation_pdf_url. All math abstracts remain HTML+MathML without JS.

CI simulates a synthetic nineteenth paper (P21) with fake identifiers, a
fourth metadata shard, a different PDF suffix and a new publication event
in temporary directories without network or GitHub/Zenodo writes.

See website/NEW_PAPER_SITE_RUNBOOK_RU.md R2 for instructions. CODEOWNERS
does not enforce owner review until real main branch protection is enabled.

---
# Выпуск новой научной статьи на сайте — актуальная инструкция (16.10.2026)

**Основной регламент:** [NEW_PAPER_SITE_RUNBOOK_RU.md](NEW_PAPER_SITE_RUNBOOK_RU.md). Zenodo и ручной Publish: [private OPS/API/NEW_ARTICLE_PUBLICATION_RUNBOOK_RU.md](https://github.com/alexmartinevski/CF-Dependence/blob/main/OPS/API/NEW_ARTICLE_PUBLICATION_RUNBOOK_RU.md) (ссылка доступна только с доступом к закрытому репозиторию). ZIP передачи и новый чат: private OPS/API/START_NEW_CHAT_NEW_ARTICLE_RU.md.

Новая запись на сайте появляется **только после фактической публичной публикации Zenodo**, а не резервирования DOI/draft. Сейчас сайт и часть тестов строго рассчитаны на **18** статей и суффикс PDF **_CF_V6_S8.pdf**; прежде чем добавлять P-ID, исправить перечисленные в регламенте счетчики/проверки, scholarly cache и статические карточки новостей. Публикацию Zenodo GitHub Pages не выполняет.

---

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

### Public-lineage chronology reconciliation, 2026-10-15
GitHub Pages deployment artifacts for the verified earlier public catalogue
(2026-10-15 run 38709797834, which retained the September Zenodo baseline
versions) and the current Zenodo-history resolver (run 38713365579) establish:
- P01: first 2026-09-28 (10.5281/zenodo.23021780), latest 2026-10-14
  (10.5281/zenodo.23355587).
- P02: first 2026-09-28 (10.5281/zenodo.23022043), latest 2026-10-14
  (10.5281/zenodo.23355597).
- P03: first 2026-09-28 (10.5281/zenodo.23022245), latest 2026-10-12
  (10.5281/zenodo.23309603).
- The other 15 papers were first issued in their newly created Zenodo
  lineages on 2026-10-14 and have no other published version yet recorded.

The site now carries a curated 1-based **Zenodo publication-release ordinal**
(2 for P01–P03, 1 for the 15 initial new lineages), distinctly labeled from a
semantic `metadata.version` value. The Zenodo version-list endpoint did not
return a verifiable semantic label or numerical index in the current automated
snapshot, so none is claimed. A later independently verified version label or
ordinal from Zenodo overrides this dated curated snapshot.
For P01–P03 the scientific `highlights_source_doi` continues to reference
the earlier **actually reviewed** TeX version, despite the current published
Version DOI being updated. A future scientific review should reconcile the
results to the new files before their provenance is updated.

## Author profile and AI research disclosure (15 October 2026)
The public homepage now has a separate, bilingual **About the author** section
at `#author`, following the project description. It identifies the publication
author **Alexandr Martinevski**, the affiliation **Independent Researcher**,
the current public research contact `math@a-martinevski.com`, and
ORCID `0009-0000-4230-4414`.

The accompanying AI collaboration disclosure states that research work involved
AI-assisted mathematical exploration, the development and critique of
arguments and manuscript preparation. AI systems are not listed as co-authors,
and the author accepts responsibility for the scientific content.

This **website-level statement does not amend the existing AI disclosures
in publication manuscripts** and deliberately does not enumerate or speculate
about individual AI systems or specific contributions to individual theorems.
Both English and Russian wording are covered by public-site CI tests.

## Research achievements landing page (15 October 2026)
The home page now displays a prominent **Major research achievements** feature
at `#achievements`, with four short representative items and a link to
`website/achievements.html`. The standalone page explains six selected
scientific claims in both languages and includes formulae, source Concept DOIs,
historical journal links and explicit statements of scope.

Editorial distinctions are intentional:
- P04: analytic exact planar XY GHZ threshold for `n>=4` within the
  full-correlator setting, *not* every Bell scenario.
- P04: `n=3` finite-certificate lower bound + analytic upper bound,
  improving the 2024 published interval; the exact zeta formula remains
  conjectural. Zeta zeros explain a difficulty in one dual approach, not
  equivalence to the Riemann hypothesis.
- P04: sharp complex alpha-mixing covariance `4 sqrt(2)` versus the
  classical `2*pi` bound, with a clearly stated independent novelty-review gate.
- P04: the general Bradley–Bryc 1985 complex multilinear problem remains
  unsolved by a result restricted to forms real on real arguments.
- P01: exact universal characteristic-function factorization profile.
- P13: optimal Wasserstein stability exponent with the theorem hypotheses.

No broader historical open problem is advertised as entirely solved without
proof review and prior-art verification. These are statements about the claims
in published papers, not external referee certification. The article-level
AI disclosure and scientific text are unchanged.

The page is included in GitHub Pages, content-fingerprint asset cache busting,
the sitemap and the standalone bilingual regression tests. The language toggle
preserves the selected language in links between the home page and the
achievements landing page. Zenodo links use permanent Concept DOIs.

## Reader-facing achievements / separate bibliographies (15 October 2026)
The home-page highlights and the detailed `achievements.html` have been
edited for non-specialists. **Each** of the six achievement sections now follows
a consistent narrative:

1. What question was being asked?
2. Where and how did it emerge historically?
3. Why is its answer mathematically or experimentally important?
4. What was actually established, with formulas and clear scope.

Every achievement has its **own visible list of 6 or 7 source links**, 39
bibliographic appearances in total (sources can recur where relevant).
References are labeled as the CF research publication, history of the problem,
previous results, scientific background, or a related public article. One section's sources are not inherited
from a global bibliography: each claim is tied to directly visible references
in its own section.

The source roles are editorial classifications, **not external proof-review or
priority certificates**. The historic literature includes Mermin (1990),
Żukowski (1993), Sen–Sen–Żukowski (2002), Designolle et al. (2023), and
Designolle–Vértesi–Pokutta (2024) for GHZ, as well as Dvoretzky (1972),
Bradley–Bryc (1985), Bradley–Bryc–Janson (1987), Bradley (2005), and Pisier
(2012) for mixing and multilinear estimates. The CF-profile and stability
sections also cite their own literature and adjacent CF papers.
Public-source DOI links were checked during the edit. The home page and
`achievements.html` each retain English and Russian versions of all narrative
copy, and mobile styles preserve readable paragraphs and citation lists.

The detailed page continues to distinguish exact theorems from bounds and
conjectures: the GHZ case `n=3` is not claimed solved; the broad 1985 complex
multilinear question is not claimed solved; historical priority and proof remain
awaiting external review.

Public citation hygiene: never link a private CF-Dependence repository path from this public site. The GHZ three-party section cites Werner–Wolf (2001) as a public seventh reference instead of the private internal K7 supplement; the public P04 Zenodo DOI remains its main result source. The computer-assisted nature of the K7 proof is clearly disclosed in text.

## Graduate-level mathematical formulation on the achievements page (15 October 2026)
Each of the six research-achievement sections now provides an explicit
mathematical formulation **after the readable problem/history/motivation**
and **before the theorem**. Notation and hypotheses are bilingual; equations
are local, accessible HTML with subscripts/superscripts, so no MathJax
runtime, external CDN, scripts, or third-party tracking is required.

The new mathematical objects were checked against the actual published
P01/P04/P13 TeX texts:

- P04 GHZ: planar full correlation `E_n(angles)=cos(sum angles)`,
  multilinear complexification ratio `kappa_n`, visibility `v_n=1/kappa_n`,
  and zeta-series notation for the exact `n>=4` result.
- P04 `n=3`: the **exact** K7 harmonic lower-bound expression
  using the seven specified primes, and the proven zeta upper bound.
- P04 strong mixing: the event-based `alpha(F,G)`, the complex
  covariance convention, and the sharp Grothendieck factor
  `4 K_G(2) = 4 sqrt(2)`.
- P04 multilinear: indicator norm `d_infty(B)`, the n-factor
  interaction defect, and both sharp norm inequalities on the stated
  real-on-real class. The full 1985 complex problem is not claimed solved.
- P01: the law-space supremum and exact extremal fair-sign construction
  (when the total angle does not exceed pi).
- P13: extremal deficit `Delta(P)`, distance to the whole equality
  orbit in `W_p`, and the two-point family that proves the
  exponent `1/(2p)` is optimal.

All four teaser cards on the home page now also include a concise,
substantive mathematical formula. Scientific proof and historical
priority review caveats remain unchanged. Tests assert the correct
placement, notation, bilingual keys, external-dependency prohibition,
and numerical regression of published exact expressions.

## Home-page update section: location, layout and resilience (2026-10-15)
The `#updates` section ("What's new" / "Что изменилось") used to appear
**after** the full annotated 18-paper catalogue. It now appears immediately
after the featured scientific achievements and before the research directory,
all within the same centred `wrap` container.

The former asymmetric two-column title/sidebar layout has been replaced with
a full-width section title and a consistent two-column grid of news cards,
collapsing to one column on mobile. Dates, category tags and citation links
share the same spacing and alignment.

Two verified site updates dated 15 October 2026 (GitHub PR #12 and #11)
were added to the pre-existing four public paper-release notes. Website
updates are marked as such, not misrepresented as newly published research.
Only allowlisted public GitHub PR URLs and validated Zenodo DOI URLs are
rendered as external news links; the public `RELEASE_NOTES.md` has its own link.

Two dated **static bilingual fallback cards** now exist directly in HTML:
an unavailable optional `news.json` must not leave a permanent loading
placeholder or block the main catalogue. CI tests check the page section
order, the responsive CSS, the six actual news items, the public links and
the missing-feed fallback.

## About section and standalone news history — 2026-10-15

**Research field directory and About are consolidated.** The canonical
`#about` section now contains the five thematic areas with all 18 published
papers. The old `#areas` anchor remains as a backwards-compatible locator
at the start of the same catalogue; there is no duplicate About card or
By-field menu entry. The Scientific Programme block moved immediately above
the author/ORCID/AI disclosure section.

The home page has exactly **four latest news cards** in a responsive 2×2 grid.
A visible, bilingual **All news and updates / Все новости и изменения** link
opens `news.html`. The news page includes **every** verified update in
reverse chronological order (currently six) with dates and source links.
The earlier expandable home-page archive is removed to keep the homepage
compact. Both pages use the same `website/data/news.json` catalogue.
Static fallback HTML supplies four recent items and the full history,
respectively, even when the optional feed fails.

The standalone page is included in the public GitHub Pages workflow,
sitemap and SHA256 asset fingerprinting. Regression tests verify the new
information architecture, permanent legacy section anchors, layout,
exact recent vs historical counts, source citations and bilingual rendering.

## Catalogue header, navigation and language retention (2026-10-15)

Following direct editorial feedback, the research catalogue **retains**
the bilingual small overline `RESEARCH AREAS & PUBLICATIONS /
НАПРАВЛЕНИЯ И ПУБЛИКАЦИИ` but removes the redundant large About title
and the descriptive paragraph above search. The catalogue still has
an accessible hidden `h2`, intact search, publication count and
last-verified Zenodo metadata.

The five main navigation links follow the actual visual section order:
**Achievements → What's new → Publications → About → Author** (also in
Russian). The `#papers` section anchors the catalogue at its beginning,
while `#about` now points to the scientific programme immediately
above the author; older `#areas` and `#programme` deep links remain
as compatible anchors.

On **all four pages** (`index.html`, `paper.html`,
`achievements.html`, `news.html`), the CF Dependence brand link has
`data-home-link` and is rewritten to `index.html?lang=<locale>`
by the shared language controller. This fixes Russian visitors being
sent back to the English homepage by the top-left brand. A static
English fallback is retained for visitors without JavaScript.
Public-source data, mathematical manuscripts, versions and disclosures
are unchanged.

## Shorter, priority-aligned paper descriptions (2026-10-15)

Following the approved Zenodo metadata updates, the annotated site catalogue
now leads with each paper's strongest proved claim rather than a list of topics.
All 18 bilingual short summaries were updated (including the already revised
P04). **Every individual summary is no longer than its former wording**:
English summary characters 2757 -> 2111, Russian 2750 -> 2102.

The three result bullets per paper remain **exactly 54 in total**, and their
aggregate text also decreased (English 7734 -> 6837, Russian 8298 -> 7189).
Seven entries received focused, source-checked result rewrites and six papers
have their highlights re-ordered by scientific significance without changing
the mathematical claims. P02 no longer advertises an Epanechnikov result absent
from the final abstract; P03 no longer points its highlights at older theorem
labels, and instead foregrounds its proven infinite irreducible families.
P11 emphasizes the Huber nonidentifiability threshold; P14 the generic
symmetric Galois group and density-one irreducibility. P16 explicitly states
that the five-bit endpoint 160 is classical.

P02 and P03 catalogue titles have also been synchronized with the **existing**
released Zenodo titles. Version DOIs, Concept DOIs, publication dates,
provenance labels, HTML layouts, mathematical papers and source PDFs were not
modified. This website-only change does not create any Zenodo release.

## Reader-facing links in news (2026-10-15)

The main page's "What's new" section and `news.html` now link to
**scientific content**, not GitHub implementation PRs. The two website
enhancements open the achievements page (including a direct link to the
analytical GHZ result with mathematical formulas). Both collection-level
announcements open the complete public scientific bibliography rather than
a generic GitHub release note or the unrelated single-paper P04 DOI.
The two article-release cards still link to their fixed Zenodo version DOIs.

Each internal target is a literal allowlisted site path with the selected
`lang=en/ru`, including static HTML fallbacks when `news.json` fails.
The source-link resolver refuses GitHub PRs and any unknown external URLs.
News history and chronology remain unchanged; this is a navigation and
reader-facing source correction, not a claim of new publication.
Regression tests cover both languages, internal/external URLs, all six
cards and the 2×2 homepage layout.
