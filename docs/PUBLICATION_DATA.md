# Published catalogue and reproducibility contract

This repository is the **public scholarly presentation** of the CF Dependence project, not the operational research workspace.

## Source of truth

- `website/data/publications.json` is the sole manually curated publication source.
- Every entry must have **publicly confirmed Zenodo publication** (published Version DOI, matching Concept DOI, date, author, license and the exact files).
- `website/data/news.json` holds separately curated public publication/news events. Historical events may cite any confirmed published Version DOI; unpublished draft DOIs are prohibited.
- The generator `website/tools/materialize_publications.py` validates the canonical catalogue and derives temporary site views. Do not edit generated `papers.json` and `data/scholarly/part-*.json` by hand.

## Versions and published files

A paper retains its stable P-number as a catalogue key, but **titles and scientific citations use the published title and DOI**, not the internal key. One Zenodo Concept DOI corresponds to a lineage of Version DOIs. Each published release is immutable in the catalogue; earlier releases remain in `releases`.

The current publication schema retains `pdf` for the **primary** PDF. An optional `files` list records its complete published set, with one `main` PDF and any `supplement` PDF or `reproducibility` ZIP. Each has its published exact filename, MD5 and byte size; the primary file metadata must match the `pdf` entry. The public article page exposes additional files as links to the published Zenodo record. Historical releases and their files are preserved.

The public scholarly PDF mirror is **optional** and allowed only if the downloaded bytes agree with the published Version DOI's PDF name, length, MD5 and %PDF signature. If the mirror cannot be confirmed, use the original Zenodo download URL.

## Scientific scope and claims

The catalogue gives three sourced mathematical results per paper (English and Russian) and its full approved description. Conditional claims must remain conditional. The P04 three-party bound is computer-assisted and its exact constant is not claimed known. P52 does **not** establish RH. Neither numerical experimentation nor incomplete Lean drafts constitute verified proofs.

New scientific results, historical claims and public catalogue changes require research approval and record verification, not just an API response or editor draft.

## Publishing and CI

Scientific publication is a **manual author action in Zenodo**; GitHub Actions in this public repository only build/read/validate the site. Updates should arrive in a PR with data and tests, then pass the site workflow before deployment. The private source-of-truth research and Zenodo transport machinery are not replicated in the public repository.

The initial GitHub release notes and `SHA256SUMS` describe the 28 September 2026 snapshot. They must not be interpreted as a checksum manifest of current `main`; current Zenodo filenames and MD5 are pinned per published version in the canonical catalogue.
