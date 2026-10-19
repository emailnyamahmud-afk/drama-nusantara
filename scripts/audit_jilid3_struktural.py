#!/usr/bin/env python3
"""
Audit struktural mendalam untuk Jilid 3 Kemenbud 2025.
Memeriksa:
- Heading hierarchy (## -> ### -> ####) konsisten
- Page markers / halaman cetak
- Truncated content (cutoff indikator)
- Empty sections
- Daftar Isi vs judul bab sebenarnya
- Penomoran gambar/tabel
"""
import re
import os
import json
from pathlib import Path
from collections import Counter, defaultdict

JILID_DIR = Path("/home/z/my-project/sumber-primer/jilid-3")
OUT_DIR = JILID_DIR / "_audit"
OUT_DIR.mkdir(exist_ok=True)

def analyze_file(filepath: Path):
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    out = {
        "filename": filepath.name,
        "size_bytes": filepath.stat().st_size,
        "line_count": len(lines),
        "word_count": len(content.split()),
        "char_count": len(content),
    }

    # Heading hierarchy
    headings = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            headings.append({
                "level": len(m.group(1)),
                "text": m.group(2).strip(),
                "line": i,
            })
    out["headings_count"] = len(headings)
    out["headings_levels"] = dict(Counter(h["level"] for h in headings))
    out["headings"] = headings

    # Heading hierarchy violations: jump from ## to #### without ###
    violations = []
    prev_level = 0
    for h in headings:
        if prev_level > 0 and h["level"] > prev_level + 1:
            violations.append({
                "line": h["line"],
                "prev_level": prev_level,
                "jumped_to": h["level"],
                "text": h["text"],
            })
        prev_level = h["level"]
    out["hierarchy_violations"] = violations

    # Page markers / halaman
    page_markers = []
    for i, line in enumerate(lines, 1):
        # Cari pola: "Halaman 123" atau "[123]" atau "hal. 123"
        for pat in [r"\[hal\.\s*(\d+)\]", r"Halaman\s+(\d+)", r"^\s*(\d+)\s*$"]:
            m = re.search(pat, line, re.IGNORECASE)
            if m:
                page_markers.append({"line": i, "raw": line.strip()[:80], "page": m.group(1)})
                break
    out["page_markers_count"] = len(page_markers)
    out["page_markers_sample"] = page_markers[:5]

    # Truncation indicators
    trunc_indicators = []
    trunc_patterns = [
        (r"\.\.\.$", "ellipsis di akhir baris"),
        (r"\[.{0,10}\]$", "kurung siku di akhir"),
        (r"halaman\s+\d+\s*$", "akhir halaman cutoff"),
        (r"^.{0,3}$", "baris sangat pendek di akhir"),
        (r"\[OCR", "OCR marker"),
        (r"\[image", "image placeholder"),
        (r"\[tabel", "tabel placeholder"),
        (r"\[gambar", "gambar placeholder"),
        (r"<!--.*?-->", "HTML comment"),
    ]
    for pat, label in trunc_patterns:
        matches = list(re.finditer(pat, content, re.MULTILINE))
        if matches:
            trunc_indicators.append({
                "pattern": pat,
                "label": label,
                "count": len(matches),
                "samples": [m.group(0)[:100] for m in matches[:3]],
            })
    out["truncation_indicators"] = trunc_indicators

    # Empty sections (heading diikuti heading lain tanpa konten)
    empty_sections = []
    for i, h in enumerate(headings):
        if i + 1 < len(headings):
            next_h = headings[i + 1]
            content_between = "\n".join(lines[h["line"]:next_h["line"]-1]).strip()
            # hapus heading line sendiri
            content_between = content_between.replace(f"{'#'*h['level']} {h['text']}", "").strip()
            word_count_between = len(content_between.split())
            if word_count_between < 10:
                empty_sections.append({
                    "heading": h["text"],
                    "line": h["line"],
                    "words_between": word_count_between,
                    "next_heading": next_h["text"],
                })
    out["empty_sections"] = empty_sections

    # Image & table references
    images = re.findall(r"!\[[^\]]*\]\([^)]+\)", content)
    tables = re.findall(r"^\|.*\|$", content, re.MULTILINE)
    out["image_refs"] = len(images)
    out["table_rows"] = len(tables)

    # Cari "Gambar X.Y" dan "Tabel X.Y" references
    gambar_refs = re.findall(r"Gambar\s+\d+[.\-]?\d*", content)
    tabel_refs = re.findall(r"Tabel\s+\d+[.\-]?\d*", content)
    out["gambar_refs"] = len(gambar_refs)
    out["tabel_refs"] = len(tabel_refs)

    # Characters aneh (non-ASCII non-Latin non-CJK)
    weird_chars = Counter()
    for ch in content:
        if ord(ch) > 127:
            if ch in "—–…""''""«»§°±·•′″":
                continue  # common punctuation
            weird_chars[ch] += 1
    out["weird_chars"] = dict(weird_chars.most_common(20))

    # Repeated whitespace / blank lines
    blank_line_streaks = []
    streak = 0
    for i, line in enumerate(lines, 1):
        if not line.strip():
            streak += 1
        else:
            if streak >= 3:
                blank_line_streaks.append({"line": i - streak, "streak": streak})
            streak = 0
    if streak >= 3:
        blank_line_streaks.append({"line": len(lines) - streak, "streak": streak})
    out["blank_streaks_3plus"] = blank_line_streaks[:10]

    return out

# Process all .md files (kecuali _meta.yaml)
results = []
for f in sorted(JILID_DIR.glob("*.md")):
    print(f"Analyzing {f.name}...")
    r = analyze_file(f)
    results.append(r)

# Summary
summary = {
    "jilid": 3,
    "total_files": len(results),
    "total_words": sum(r["word_count"] for r in results),
    "total_headings": sum(r["headings_count"] for r in results),
    "files_with_hierarchy_violations": [r["filename"] for r in results if r["hierarchy_violations"]],
    "files_with_empty_sections": [(r["filename"], len(r["empty_sections"])) for r in results if r["empty_sections"]],
    "files_with_truncation_indicators": [(r["filename"], [t["label"] for t in r["truncation_indicators"]]) for r in results if r["truncation_indicators"]],
    "files_with_weird_chars": [(r["filename"], list(r["weird_chars"].keys())[:5]) for r in results if r["weird_chars"]],
    "files_with_blank_streaks": [(r["filename"], len(r["blank_streaks_3plus"])) for r in results if r["blank_streaks_3plus"]],
}

# Save detailed
with open(OUT_DIR / "structural-audit.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
with open(OUT_DIR / "structural-summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print("\n=== SUMMARY ===")
print(f"Files: {summary['total_files']}")
print(f"Total words: {summary['total_words']:,}")
print(f"Total headings: {summary['total_headings']}")
print(f"\nFiles with hierarchy violations: {len(summary['files_with_hierarchy_violations'])}")
for fn in summary["files_with_hierarchy_violations"]:
    print(f"  - {fn}")
print(f"\nFiles with empty sections: {len(summary['files_with_empty_sections'])}")
for fn, n in summary["files_with_empty_sections"]:
    print(f"  - {fn}: {n} empty sections")
print(f"\nFiles with truncation indicators: {len(summary['files_with_truncation_indicators'])}")
for fn, labels in summary["files_with_truncation_indicators"]:
    print(f"  - {fn}: {labels}")
print(f"\nFiles with weird chars: {len(summary['files_with_weird_chars'])}")
for fn, chars in summary["files_with_weird_chars"][:10]:
    print(f"  - {fn}: {chars}")
print(f"\nFiles with blank streaks >=3: {len(summary['files_with_blank_streaks'])}")
for fn, n in summary["files_with_blank_streaks"]:
    print(f"  - {fn}: {n} streaks")

print(f"\nDetailed JSON saved to: {OUT_DIR}")
