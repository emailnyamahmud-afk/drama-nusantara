#!/usr/bin/env python3
"""
Deep-dive: periksa empty sections, hierarchy violations, weird chars, HTML comments.
"""
import re
import json
from pathlib import Path

JILID_DIR = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/jilid-3")

with open(JILID_DIR / "_audit" / "structural-audit.json", encoding="utf-8") as f:
    data = json.load(f)

print("="*80)
print("EMPTY SECTIONS DETAIL")
print("="*80)
for r in data:
    if r["empty_sections"]:
        print(f"\n>>> {r['filename']}")
        for es in r["empty_sections"]:
            print(f"  L{es['line']}: '{es['heading']}' ({es['words_between']} words) -> next: '{es['next_heading']}'")

print("\n" + "="*80)
print("HIERARCHY VIOLATIONS DETAIL")
print("="*80)
for r in data:
    if r["hierarchy_violations"]:
        print(f"\n>>> {r['filename']}")
        for v in r["hierarchy_violations"]:
            print(f"  L{v['line']}: ## {v['prev_level']} -> ## {v['jumped_to']}  '{v['text']}'")

print("\n" + "="*80)
print("TRADEMARK (™) WEIRD CHAR DETAIL")
print("="*80)
for r in data:
    if "™" in r.get("weird_chars", {}):
        filepath = JILID_DIR / r["filename"]
        content = filepath.read_text(encoding="utf-8")
        for m in re.finditer(r"(.{0,60})™(.{0,60})", content):
            print(f"  [{r['filename']}] ...{m.group(1)}™{m.group(2)}...")

print("\n" + "="*80)
print("HTML COMMENT DETAIL (14-bab-9.md)")
print("="*80)
fp = JILID_DIR / "14-bab-9.md"
content = fp.read_text(encoding="utf-8")
for m in re.finditer(r"<!--.*?-->", content, re.DOTALL):
    snippet = m.group(0)
    if len(snippet) > 200:
        snippet = snippet[:200] + "..."
    print(f"  {snippet}")

print("\n" + "="*80)
print("PAGE MARKERS SAMPLE (first 5 per file)")
print("="*80)
for r in data:
    if r["page_markers_sample"]:
        print(f"\n>>> {r['filename']}")
        for pm in r["page_markers_sample"]:
            print(f"  L{pm['line']}: '{pm['raw']}' (page {pm['page']})")
