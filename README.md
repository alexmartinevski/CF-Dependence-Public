# CF Dependence

**Research in sharp probability inequalities, Fourier dependence and extremal geometry** by **Alexandr Martinevski**, Independent Researcher, Lithuania.

**[Research website](https://math.a-martinevski.com/)** · **[Published papers](https://math.a-martinevski.com/publications/)** · **[Selected mathematical results](https://math.a-martinevski.com/achievements.html)** · **[Publication updates](https://math.a-martinevski.com/news.html)**

**ORCID:** [0009-0000-4230-4414](https://orcid.org/0009-0000-4230-4414) · **Contact:** math@a-martinevski.com

## Published research

The curated catalogue contains **22 published research preprints as of 17 November 2026**. Each paper has its own Zenodo publication record, permanent Version DOI and, when applicable, Concept DOI for the series of versions. The website provides English/Russian summaries, full scientific abstracts and sources for the selected results.

The work develops several connected research directions: extremal characteristic-function inequalities and dependence profiles; fixed-marginal laws and mixability; polynomial arithmetic and irreducibility; Fourier and Gaussian geometry; and statistical inference for Fourier-based dependence.

Recent publications include:

- **[Sharp constants for Fourier factorization defects](https://doi.org/10.5281/zenodo.24293935)** — sharp mixing and centred-interaction constants, the exact planar GHZ constants for n ≥ 4, and a computer-assisted lower bound for the still-open three-party case. This release contains the main paper, a proof supplement and a reproducibility archive.
- **[The planar GHZ constant for three qubits and the zeros of the Riemann zeta function](https://doi.org/10.5281/zenodo.24293937)** — conditional arithmetic restrictions on globally admissible GHZ Bell functionals. **It does not prove the Riemann hypothesis or determine the exact three-party constant.**
- **[A sharp universal profile for multivariate characteristic-function factorization](https://doi.org/10.5281/zenodo.23355587)** — the latest *published* P01 version verified for this catalogue. Later reserved or draft DOIs are not presented as publications.

For the complete bibliography and stable links, use [CITATION.md](CITATION.md), not internal project numbers as bibliographic titles.

## Earlier published research (2002)

**A. V. Martinevskii; Yu. S. Kharin.** *Estimation of stochastic dependence and testing for the N-dimensional uniformity by sample characteristic functions.* In *Probabilistic Methods in Discrete Mathematics*, 2002, starting p. 227. [German National Library: volume contents](https://d-nb.info/964176513/04).

This earlier co-authored paper is listed in the [author's publication history](https://math.a-martinevski.com/author/) and [research bibliography](https://math.a-martinevski.com/publications/). It is not assigned an internal Pxx code or counted among the 22 later Zenodo preprints. The linked source verifies the volume's contents; it is **not** a chapter full-text download, and a chapter DOI has not been verified.

## How this repository is organized

| Directory or file | Purpose |
| --- | --- |
| [`website/`](website/) | Source for the bilingual [research website](https://math.a-martinevski.com/), search and scholarly pages |
| [`website/data/publications.json`](website/data/publications.json) | **Single curated source** of published article metadata, version histories and selected results |
| [`website/data/news.json`](website/data/news.json) | Verified publication announcements and scientific updates |
| [`papers/`](papers/) | Historical public TeX/PDF snapshots for the initial P01–P03 release, plus navigation to newer publication records |
| [`CITATION.md`](CITATION.md) | Bibliographic entries and current verified Version DOIs |
| [`docs/PUBLICATION_DATA.md`](docs/PUBLICATION_DATA.md) | Metadata, files, reproducibility and publication gate |
| [`RELEASE_NOTES.md`](RELEASE_NOTES.md) | Historical notes for the initial GitHub manuscript release |

**Important:** the PDFs under `papers/01-…` through `papers/03-…` are historical GitHub snapshots and should not be treated as mirrors of each paper's latest Zenodo release. Find the latest verified published file and any supplementary material on the paper's Zenodo record. The root `SHA256SUMS` is the historical checksum list for the 28 September 2026 release, not a checksum manifest for the current GitHub `main` branch.

## Publication, proof and reproducibility

This public repository records **published** Zenodo releases. Draft manuscripts, internal scientific checkpoints, unfinished formalization, registry queues and Zenodo operations remain outside the public research catalogue. Source files and rational verification materials are linked from a released Zenodo record when available. Computation-dependent results are identified as such; numerical exploration is not treated as analytical proof.

The P04 proof supplement is an additional file **of the same publication**, not a separate article or DOI. File roles are visible on the scientific paper page. Different published versions retain separate Version DOIs within their stable Concept DOI lineage.

## Authorship and AI disclosure

AI systems were used in mathematical exploration, proof critique, symbolic and numerical checking, literature search and manuscript preparation, as disclosed in the individual papers. They are not authors. Responsibility for the mathematical content rests with Alexandr Martinevski. The preprints are not represented here as journal peer-reviewed unless their records explicitly establish that status.

Please [cite the individual article](CITATION.md), including its Version DOI, rather than citing the entire repository.
