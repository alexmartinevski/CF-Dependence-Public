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
P01–P03 are the three released records on the site. Current CF V6 draft reservations are
not published entries. `P10` is not currently cleared as a standalone publication.
The September 28 repository release is recorded as repository news, **not** a new
version of any Zenodo paper.

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
