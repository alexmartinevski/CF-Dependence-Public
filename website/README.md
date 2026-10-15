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
