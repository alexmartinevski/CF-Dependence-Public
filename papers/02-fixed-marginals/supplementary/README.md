# Supplementary material for "Two-point extremals for characteristic-function dependence with fixed marginals"

Python 3.12, numpy, scipy, sympy 1.14, mpmath (interval arithmetic `mpmath.iv`). Each script writes the JSON in `outputs/`.

| Claim in the paper | Script | Output |
|---|---|---|
| Proposition "the 9/7 inequality": two-point reduction, Case A minimum 7(b-3)^2(b+6)/(96(b+5)), Case B polynomial N | `ineq97_sym.py` | `ineq97_sym.txt` |
| Thm 3.1: factorizations, formulas vs brute force, random two-point and unimodal laws (min ratio >= 9/7) | `ineq97_check.py` | `ineq97_check.json` |
| Theorem "finite d", d = 3 and 4 <= d <= 60: exact rational mixability, interval lower bounds, kappa_d upper bounds | `cert_small_d.py` | `cert_small_d.json` |
| Theorem "finite d", 61 <= d <= 200; tail constants checked against exact values | `cert_tail.py` (imports `cert_small_d.py`) | `cert_tail.json` |
| Remark 3.3 (projection picture): projection at xi = 1/4 and 1/2, max over xi = 7/9 | `lvx_projection.py` | `lvx_projection.json` |
| Section 5 observations (triangular family, Beta(1,2) large d) | `asym_scan.py` | `asym_scan.json` |
| Exploration behind the 9/7 conjecture (asymmetric families; mixtures with 2-4 atoms) | `price_unimodal.py`, `price_inf.py` | `.json` |
| Finite-d exploration (atom + uniform; d = 3 search) | `atom_uniform_c.py`, `d3_asym.py` | `.json` |

Run `python3 cert_small_d.py` before `python3 cert_tail.py` (the latter reuses functions of the former). Checksums: `SHA256SUMS`.


The files were merged from the former stand-alone symmetry-breaking companion into the fixed-marginal manuscript. Historical script names are retained for reproducibility.
