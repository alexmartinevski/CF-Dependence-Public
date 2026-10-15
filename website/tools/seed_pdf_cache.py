#!/usr/bin/env python3
"""Seed only byte-verified public PDFs from a prior GitHub Pages artifact.

A GitHub Actions downloaded Pages artifact contains artifact.tar with paths
./publications/Pxx/<filename>.pdf. Never extract tar entries onto the
filesystem directly. Each candidate must exactly match a CURRENT, PUBLIC
Zenodo record's code, PDF name, length, header and pinned MD5. Old versions
and malicious archive members are silently discarded.
"""
from __future__ import annotations
import io
from pathlib import Path
import re
import sys
import tarfile

from build_scholarly_pages import load_data,file_signature,MAX_PDF


def seed(source,prior_artifact_dir,cache_dir):
    source=Path(source)
    prior_artifact_dir=Path(prior_artifact_dir)
    cache_dir=Path(cache_dir)
    members=prior_artifact_dir/"artifact.tar"
    if not members.exists():
        print("PDF seed: no older artifact supplied; public Zenodo fetch remains fallback")
        return 0
    papers,approved=load_data(source)
    allowed={p["code"]:approved[p["code"]] for p in papers}
    pattern=re.compile(r"(?:\./)?publications/(P[0-9]{2})/(P[0-9]{2}_[A-Za-z0-9][A-Za-z0-9._-]{0,150}\.pdf)")
    restored=0
    with tarfile.open(members,"r:") as archive:
        for item in archive:
            # Never follow symlinks, redirects or paths other than exact PDF locators.
            if not item.isfile() or not item.name or item.size>MAX_PDF or item.size<=1000:
                continue
            match=pattern.fullmatch(item.name)
            if match is None:
                continue
            code,filename=match.groups()
            record=allowed.get(code)
            if record is None or code!=filename[:3] or record["pdf_filename"]!=filename:
                continue
            if item.size!=record["pdf_size"]:
                continue
            target=cache_dir/code/filename
            if file_signature(target,record):
                restored+=1
                continue
            stream=archive.extractfile(item)
            if stream is None:
                continue
            payload=stream.read(MAX_PDF+1)
            if len(payload)!=record["pdf_size"] or not payload.startswith(b"%PDF-"):
                continue
            import hashlib
            if hashlib.md5(payload).hexdigest()!=record["pdf_md5"]:
                continue
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(payload)
            if not file_signature(target,record):
                target.unlink(missing_ok=True)
                continue
            restored+=1
    print(f"PDF seed: recovered {restored}/{len(papers)} verified release PDFs from prior Pages artifact")
    return restored


if __name__=="__main__":
    if len(sys.argv)!=4:
        raise SystemExit("Usage: seed_pdf_cache.py website_root prior_pages_directory pdf_cache_directory")
    seed(*sys.argv[1:])
