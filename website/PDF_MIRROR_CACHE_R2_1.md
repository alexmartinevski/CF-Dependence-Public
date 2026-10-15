# PDF mirror resilience R2.1 — 16 October 2026

## Why this exists
The first R2 GitHub Pages deployment produced 18 indexable HTML articles
but only 8 of 18 local PDF mirrors when public Zenodo downloads timed out.
Exact source DOI and public fallback PDF links remained valid, however
same-directory PDF availability for Google Scholar had regressed.

## Verified, nonpublishing repair
- The deploy workflow restores previously verified public PDF bytes from
  Actions cache and optionally bootstraps from the last 18/18 Pages artifact
  (GitHub Actions run 38812459965, an historical record that may expire).
- The tar archive is NEVER extracted wholesale. website/tools/seed_pdf_cache.py
  reads candidate PDF entries only under publications/Pxx/<filename>.pdf.
  The candidate is reused only when code, exact current PDF name, byte
  length, %PDF- prefix and MD5 all match the CURRENT approved public
  website/data/scholarly/part-*.json metadata. Symlinks, traversal paths,
  stale PDF versions and invalid checksums are ignored.
- website/tools/build_scholarly_pages.py can read/write --cache-dir.
  A valid cached PDF is copied to the same-directory article. If absent,
  it tries verified local source bytes then fetches the public Zenodo
  file and caches only bytes passing the exact checksum/size gate.
- Cache storage is advisory, not an authority about any published record.
  The Version DOI and public Zenodo metadata remain the source of truth.
  If no mirror can be verified, the article still links to the public
  Zenodo PDF and omits citation_pdf_url for nonexistent local files.
- The restore/save Actions cache key includes a unique run ID to allow
  incremental replenishment, with only public PDFs and no Zenodo token.

## Offline verification and manual follow-up
website/tests/test_dynamic_release.py simulates a corrupted cached PDF,
a malicious archive path, and a correct synthetic P21 PDF restored from
an artifact.tar. It also verifies offline Google Scholar citation_pdf_url
is emitted only for a byte-verified existing same-directory file.

After deployment, inspect the actual Pages artifact: count the deployed
PDFs and verify their MD5 against the pinned scholarly metadata; inspect
the corresponding HTML citation_pdf_url. Do not claim 18/18 mirrors solely
because the deployment job reports SUCCESS. If the prior artifact expires
and the cache is absent, re-download safely from live public Zenodo and
accept a partial mirror count only as a documented degraded condition.

Google Scholar indexing remains an external crawler outcome.
