#!/usr/bin/env python3
"""
Audit ringkasan-jilid 1, 2, 3 dengan metode yang sama dengan Jilid 4:
- Mapping struktur sub-bab di sumber primer
- Bandingkan dengan struktur ringkasan
- Identifikasi sub-bab terlewat
- Ekstrak tokoh-tokoh yang belum masuk
"""
import re
from pathlib import Path
from collections import defaultdict

BASE = Path("/home/z/my-project/phase-1/sumber-primer/kemenbud-2025")

for jilid in [1, 2, 3]:
    print(f"\n{'#'*100}")
    print(f"# AUDIT JILID {jilid}")
    print(f"{'#'*100}")

    JILID_DIR = BASE / f"jilid-{jilid}"
    RINGKASAN_DIR = BASE / "ringkasan-jilid"

    # Cari file ringkasan jilid ini
    ringkasan_files = list(RINGKASAN_DIR.glob(f"ringkasan-jilid-{jilid}-*.md"))
    if not ringkasan_files:
        print(f"Tidak ada ringkasan jilid {jilid}!")
        continue
    ringkasan_file = ringkasan_files[0]
    ringkasan_text = ringkasan_file.read_text(encoding="utf-8").lower()
    print(f"Ringkasan: {ringkasan_file.name}")
    print(f"Size: {ringkasan_file.stat().st_size:,} bytes, {len(ringkasan_text.split()):,} kata")

    # Hitung heading di ringkasan
    ringkasan_headings = []
    for line in ringkasan_text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            ringkasan_headings.append((len(m.group(1)), m.group(2).strip()))
    print(f"Heading di ringkasan: {len(ringkasan_headings)}")
    print(f"  Bab-level: {sum(1 for h in ringkasan_headings if h[0]==2)}")
    print(f"  Sub-bab (level 3): {sum(1 for h in ringkasan_headings if h[0]==3)}")
    print(f"  Temuan (level 4): {sum(1 for h in ringkasan_headings if h[0]==4)}")

    # Baca semua bab sumber primer
    bab_files = sorted(JILID_DIR.glob("[01][0-9]-bab-*.md"))
    print(f"\nFile bab sumber primer: {len(bab_files)}")
    total_kata_sumber = 0
    total_heading_sumber = 0
    for f in bab_files:
        text = f.read_text(encoding="utf-8")
        total_kata_sumber += len(text.split())
        headings = []
        for line in text.split("\n"):
            m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if m:
                headings.append((len(m.group(1)), m.group(2).strip()))
        total_heading_sumber += len(headings)

    print(f"\nTotal sumber primer: {total_kata_sumber:,} kata, {total_heading_sumber} heading")

    # Mapping struktur per bab
    print(f"\n{'='*80}")
    print(f"STRUKTUR PER BAB — JILID {jilid}")
    print(f"{'='*80}")
    for f in bab_files:
        text = f.read_text(encoding="utf-8")
        bab_num_match = re.search(r"bab-(\d+)\.md", f.name)
        if not bab_num_match:
            continue
        bab_num = bab_num_match.group(1)

        print(f"\n--- BAB {bab_num} — {f.name} ({len(text.split()):,} kata) ---")
        for line in text.split("\n"):
            m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                if 5 < len(title) < 200 and not re.search(r"[<>|]", title):
                    indent = "  " * (level - 1)
                    print(f"{indent}{'#'*level} {title[:120]}")
