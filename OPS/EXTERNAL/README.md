# External scientific discoverability — DOI audit R1

This is a **read-only, manual/on-merge** check against publicly available metadata services.
It does **not** assert Google Search/Google Scholar inclusion, scientific peer review,
priority, citations outside provider-specific numbers, or journal acceptance.

Sources (all are queried by the exact current Version DOI from
`website/data/publications.json`):
- DataCite Registry — the registration agency for Zenodo DOI records;
- OpenAlex — third-party research indexing;
- Semantic Scholar — third-party research indexing and citations when available.

Run: `python OPS/EXTERNAL/doi_visibility.py --self-test` or
`python OPS/EXTERNAL/doi_visibility.py --out _external-discovery/report.json`.
The GitHub Action stores one JSON artifact; it **does not** commit volatile
remote index data to the scientific catalogue.

Classification: `FOUND` only when the provider returns 200 **and** its DOI
matches the requested value; `NOT_FOUND` only on a real HTTP 404.
`RATE_LIMIT`, `HTTP_ERROR`, `NETWORK_ERROR`, and `MISMATCH`
are not evidence of absent research.

We do not scrape Google Scholar or use `site:` queries as precise metrics.
For Google Search, use the owner's Search Console, already configured.
Independent scientific validation requires review by researchers or journal
referees. A third-party mirror or metadata harvest alone is not endorsement.
