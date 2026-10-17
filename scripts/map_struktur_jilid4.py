#!/usr/bin/env python3
"""
Mapping struktur lengkap setiap bab sumber primer Jilid 4.
Ekstrak semua heading + sub-bab untuk identifikasi topik.
"""
import re
from pathlib import Path

JILID = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/jilid-4")
RINGKASAN = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/ringkasan-jilid/ringkasan-jilid-4-interaksi-awal-barat.md")

# Baca ringkasan, ekstrak semua judul "Temuan Kunci" (####)
ringkasan_text = RINGKASAN.read_text(encoding="utf-8")
ringkasan_finding_titles = set()
for m in re.finditer(r"####\s+(\d+)\.\s+(.+?)$", ringkasan_text, re.MULTILINE):
    ringkasan_finding_titles.add(m.group(2).strip().lower()[:80])

print(f"Total 'Temuan Kunci' di ringkasan: {len(ringkasan_finding_titles)}")
print("Sample:")
for t in list(ringkasan_finding_titles)[:5]:
    print(f"  - {t}")
print()

# Untuk setiap bab sumber primer, ekstrak struktur
for f in sorted(JILID.glob("[01][0-9]-bab-*.md")):
    text = f.read_text(encoding="utf-8")
    bab_num_match = re.search(r"bab-(\d+)\.md", f.name)
    if not bab_num_match:
        continue
    bab_num = bab_num_match.group(1)
    print(f"\n{'='*80}")
    print(f"BAB {bab_num} — {f.name}")
    print(f"Size: {f.stat().st_size:,} bytes, {len(text.split()):,} kata")
    print(f"{'='*80}")

    # Ekstrak semua heading (## ### #### #####)
    headings = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            # Skip OCR garbage
            if len(title) > 3 and not re.search(r"[<>|]", title):
                headings.append((level, title))

    print(f"\nTotal heading: {len(headings)}")
    print("\nHeading level 2-3 (sub-bab utama):")
    for level, title in headings:
        if level <= 3:
            indent = "  " * (level - 1)
            print(f"{indent}{'#'*level} {title[:120]}")

    # Cek juga heading yang terlihat seperti "1. ...", "2. ...", "A. ...", "B. ..."
    # (seringkali bukan heading markdown, tapi struktur konten)
    print(f"\nStruktur non-heading (paragraf numerik/huruf):")
    structure_markers = []
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        # Pattern: "1. ", "2. ", "A. ", "B. ", "1.1 ", dll
        if re.match(r"^(#{1,2}\s+)?[A-Z][\.\)]\s+[A-Z]", s) or re.match(r"^\d+[\.\)]\s+[A-Z]", s):
            if 5 < len(s) < 200 and not s.startswith("#"):
                structure_markers.append((i, s[:150]))
    if structure_markers:
        for line_no, marker in structure_markers[:15]:
            print(f"  L{line_no}: {marker}")
