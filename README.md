# CF Dependence

Research manuscripts by **Alexandr Martinevski** (Independent Researcher, Lithuania).

ORCID: https://orcid.org/0009-0000-4230-4414  
Email: alex.martinevski@gmail.com

This repository contains the public manuscript set for the **CF Dependence** project. The three papers are ordered by logical and intended publication sequence.

## Papers

### 1. A sharp universal profile for multivariate characteristic-function factorization

Primary source for the sharp profile
\[
C_d(\mathbf r)=\prod_j r_j-\cos\!\left(\min\left\{\sum_j\arccos r_j,\pi\right\}\right)
\]
and the universal constant
\[
C_d=\max_{0\le x\le\pi}\{\cos^d(x/d)-\cos x\}=\|T_d-x^d\|_{\infty,[-1,1]}.
\]

Files: [`papers/01-sharp-universal-profile/`](papers/01-sharp-universal-profile/)

### 2. Two-point extremals for characteristic-function dependence with fixed marginals

Develops the fixed-marginal theory: two-point extremals, convex-order certificates, complete/joint mixability, exact symmetric-unimodal regimes, the price of fixing marginals, and the non-symmetric unimodal extension.

Files: [`papers/02-fixed-marginals/`](papers/02-fixed-marginals/)  
Reproducibility scripts and recorded outputs: [`papers/02-fixed-marginals/supplementary/`](papers/02-fixed-marginals/supplementary/)

### 3. Chebyshev--Lucas critical polynomials: local blocks, irreducibility and Galois groups

Studies the critical polynomial family arising from the extremal equation for \(C_d\), including local Newton polygons, irreducibility, Galois groups, and the algebraic degree of \(C_d\).

Files: [`papers/03-chebyshev-lucas-critical-polynomials/`](papers/03-chebyshev-lucas-critical-polynomials/)

## Relation between the papers

The intended reading order is

1. universal profile and \(C_d\);
2. fixed marginals and two-point extremals;
3. arithmetic of the critical Chebyshev--Lucas polynomial family.

The separate expository synthesis *One constant, five extremal problems* is intentionally **not included in this public release** and is being held for a later overview publication.

## Reproducibility

The fixed-marginal paper includes its current certification scripts and machine-readable outputs. Each manuscript directory contains the TeX source and compiled PDF used for this release.

Repository-level hashes are recorded in [`SHA256SUMS`](SHA256SUMS).

## AI assistance disclosure

The manuscripts disclose AI assistance on their first pages. AI systems used in the research and manuscript workflow included **OpenAI GPT-5.6 Sol** and **Anthropic Claude Opus 5.5**. They were used for mathematical exploration, proof development and critique, symbolic and numerical verification, literature search, and manuscript drafting and editing. AI systems are not authors. The author reviewed the mathematical statements and proofs and takes full responsibility for the content.

## Citation

Please cite the specific paper used. Bibliographic records can be updated with arXiv identifiers and DOIs after they are assigned. See [`CITATION.md`](CITATION.md).

## Status

Public manuscript release prepared 28 September 2026. These are research manuscripts/preprints; publication or peer-review status should be checked from the corresponding paper record.
