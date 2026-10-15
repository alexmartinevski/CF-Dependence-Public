#!/usr/bin/env python3
"""Stamp deployed HTML asset URLs with reproducible content hashes.

Runs against the static Pages artifact, not the working tree. Query-string
fingerprints are safe with GitHub Pages and avoid stale mobile browser scripts.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


def stamp_site(root: Path) -> None:
    root = Path(root)
    for page in ("index.html", "paper.html", "achievements.html"):
        html_path = root / page
        html = html_path.read_text(encoding="utf-8")
        for asset in ("assets/site.js", "assets/site.css"):
            fingerprint = hashlib.sha256((root / asset).read_bytes()).hexdigest()[:16]
            # Match exactly one HTML reference, with or without a prior version.
            pattern = r'((?:href|src)="'+ re.escape(asset) +r')(?:\?v=[A-Za-z0-9._-]+)?(")'
            html, count = re.subn(
                pattern,
                lambda m: m.group(1) + "?v=" + fingerprint + m.group(2),
                html,
            )
            if count != 1:
                raise ValueError(f"{page}: expected exactly one reference to {asset}, got {count}")
        html_path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: fingerprint_assets.py PATH_TO_PUBLIC_SITE")
    stamp_site(Path(sys.argv[1]))
