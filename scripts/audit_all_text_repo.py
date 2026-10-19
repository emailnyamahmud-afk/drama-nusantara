#!/usr/bin/env python3
"""
Audit menyeluruh SEMUA text file di repo drama-nusantara.
Cek: konsistensi path, broken link, encoding error, heading hierarchy,
duplicate content, path referensi yang salah, TODO/placeholder, dll.
"""
import re
import os
import yaml
from pathlib import Path
from collections import defaultdict

REPO = Path("/home/z/my-project")

# Kumpulkan semua file text
text_files = []
for ext in ["*.md", "*.yaml", "*.py", "*.txt"]:
    for f in REPO.rglob(ext):
        rel = f.relative_to(REPO)
        # Skip .git
        if ".git" in str(rel):
            continue
        text_files.append((f, str(rel)))

print(f"Total text files: {len(text_files)}")
print()

issues = []

# ============================================
# 1. CEK BROKEN INTERNAL LINKS
# ============================================
print("=" * 80)
print("1. BROKEN INTERNAL LINKS")
print("=" * 80)

all_files_set = set()
for _, rel in text_files:
    all_files_set.add(rel)

for f, rel in text_files:
    if f.suffix not in [".md", ".yaml"]:
        continue
    content = f.read_text(encoding="utf-8", errors="replace")
    # Cari markdown links [text](path)
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        link = m.group(2)
        # Skip external links
        if link.startswith("http") or link.startswith("#") or link.startswith("mailto:"):
            continue
        # Cek apakah file ada
        target = REPO / link
        if not target.exists():
            # Coba relative to file dir
            target = f.parent / link
            if not target.exists():
                issues.append(("broken_link", rel, f"L{content[:m.start()].count(chr(10))+1}", link))

if not issues:
    print("  ✅ Tidak ada broken links")
else:
    for typ, file, line, link in issues:
        print(f"  ❌ {file} {line}: {link}")

broken_link_issues = len(issues)
issues.clear()

# ============================================
# 2. CEK ENCODING ERRORS
# ============================================
print()
print("=" * 80)
print("2. ENCODING ERRORS (karakter non-UTF8)")
print("=" * 80)

encoding_issues = []
for f, rel in text_files:
    try:
        content = f.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        encoding_issues.append((rel, str(e)))
    else:
        # Cek replacement character
        if "\ufffd" in content:
            count = content.count("\ufffd")
            encoding_issues.append((rel, f"{count} replacement characters"))

if not encoding_issues:
    print("  ✅ Tidak ada encoding errors")
else:
    for rel, err in encoding_issues:
        print(f"  ❌ {rel}: {err}")

# ============================================
# 3. CEK MARKDOWN HEADING HIERARCHY VIOLATIONS
# ============================================
print()
print("=" * 80)
print("3. MARKDOWN HEADING HIERARCHY VIOLATIONS")
print("=" * 80)

hierarchy_issues = []
for f, rel in text_files:
    if f.suffix != ".md":
        continue
    content = f.read_text(encoding="utf-8", errors="replace")
    prev_level = 0
    for i, line in enumerate(content.split("\n"), 1):
        m = re.match(r"^(#{1,6})\s+", line)
        if m:
            level = len(m.group(1))
            if prev_level > 0 and level > prev_level + 1:
                hierarchy_issues.append((rel, i, f"jump {prev_level}→{level}", line.strip()[:80]))
            prev_level = level

if not hierarchy_issues:
    print("  ✅ Tidak ada hierarchy violations")
else:
    for rel, line, desc, text in hierarchy_issues[:20]:
        print(f"  ⚠️ {rel}:L{line} {desc} — {text}")
    if len(hierarchy_issues) > 20:
        print(f"  ... dan {len(hierarchy_issues)-20} lainnya")

# ============================================
# 4. CEK PATH REFERENSI SALAH (referensi path lama)
# ============================================
print()
print("=" * 80)
print("4. PATH REFERENSI SALAH (referensi path lama yang sudah dihapus)")
print("=" * 80)

old_paths_to_check = [  # daftar path yang SUDAH DIHAPUS, untuk verifikasi cleanup
    "",
    "phase-1/",
    "download/",
    "scripts/",
    "",
    "skills/",
    "push-to-github.sh",
]

path_issues = []
for f, rel in text_files:
    if f.suffix not in [".md", ".yaml", ".py"]:
        continue
    content = f.read_text(encoding="utf-8", errors="replace")
    for old in old_paths:
        if old in content:
            # Cari baris
            for i, line in enumerate(content.split("\n"), 1):
                if old in line:
                    path_issues.append((rel, i, old, line.strip()[:100]))

if not path_issues:
    print("  ✅ Tidak ada referensi path lama")
else:
    for rel, line, old, text in path_issues[:20]:
        print(f"  ❌ {rel}:L{line} mengandung '{old}' — {text}")
    if len(path_issues) > 20:
        print(f"  ... dan {len(path_issues)-20} lainnya")

# ============================================
# 5. CEK DUPLICATE CONTENT (hash paragraf)
# ============================================
print()
print("=" * 80)
print("5. DUPLICATE CONTENT (paragraf identik lintas file)")
print("=" * 80)

para_map = defaultdict(list)
for f, rel in text_files:
    if f.suffix != ".md":
        continue
    content = f.read_text(encoding="utf-8", errors="replace")
    for para in content.split("\n\n"):
        para = para.strip()
        if len(para) > 200:  # hanya paragraf panjang
            # Hash sederhana
            h = hash(para[:300])  # first 300 chars
            para_map[h].append((rel, para[:80]))

dup_count = 0
for h, locations in para_map.items():
    if len(locations) > 1:
        # Cek apakah cross-file
        files = set(loc[0] for loc in locations)
        if len(files) > 1:
            dup_count += 1
            if dup_count <= 5:
                print(f"  ⚠️ Duplikat di {len(files)} file:")
                for loc in locations[:5]:
                    print(f"    {loc[0]}: {loc[1][:80]}")

if dup_count == 0:
    print("  ✅ Tidak ada duplicate content signifikan")
else:
    print(f"  Total: {dup_count} paragraf duplikat lintas file")

# ============================================
# 6. CEK TODO/PLACEHOLDER/HALUSINASI MARKER
# ============================================
print()
print("=" * 80)
print("6. TODO / PLACEHOLDER / HALUSINASI MARKER")
print("=" * 80)

markers = [
    (r"\bTODO\b", "TODO"),
    (r"\bFIXME\b", "FIXME"),
    (r"\bXXX\b", "XXX"),
    (r"\bTBD\b", "TBD"),
    (r"\[placeholder\]", "placeholder"),
    (r"\[TODO\]", "TODO marker"),
    (r"\[TBD\]", "TBD marker"),
    (r"\bngawur\b", "ngawur (halusinasi marker)"),
    (r"\bhalusinasi\b", "halusinasi"),
    (r"\bfake\b", "fake"),
    (r"\binvented\b", "invented"),
]

todo_issues = []
for f, rel in text_files:
    content = f.read_text(encoding="utf-8", errors="replace")
    for pat, label in markers:
        for m in re.finditer(pat, content, re.IGNORECASE):
            line_start = content.rfind("\n", 0, m.start()) + 1
            line_end = content.find("\n", m.start())
            if line_end == -1:
                line_end = len(content)
            line = content[line_start:line_end].strip()
            line_num = content[:m.start()].count("\n") + 1
            todo_issues.append((rel, line_num, label, line[:100]))

if not todo_issues:
    print("  ✅ Tidak ada TODO/placeholder/halusinasi marker")
else:
    for rel, line, label, text in todo_issues[:20]:
        print(f"  ⚠️ {rel}:L{line} [{label}] — {text}")

# ============================================
# 7. CEK YAML VALIDITY
# ============================================
print()
print("=" * 80)
print("7. YAML VALIDITY CHECK")
print("=" * 80)

yaml_issues = []
for f, rel in text_files:
    if f.suffix != ".yaml":
        continue
    try:
        with open(f, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if data is None:
            yaml_issues.append((rel, "Empty YAML"))
    except yaml.YAMLError as e:
        yaml_issues.append((rel, str(e)[:100]))
    except Exception as e:
        yaml_issues.append((rel, f"Error: {e}"))

if not yaml_issues:
    print("  ✅ Semua YAML valid")
else:
    for rel, err in yaml_issues:
        print(f"  ❌ {rel}: {err}")

# ============================================
# 8. CEK PYTHON SYNTAX
# ============================================
print()
print("=" * 80)
print("8. PYTHON SYNTAX CHECK")
print("=" * 80)

py_issues = []
for f, rel in text_files:
    if f.suffix != ".py":
        continue
    import py_compile
    try:
        py_compile.compile(str(f), doraise=True)
    except py_compile.PyCompileError as e:
        py_issues.append((rel, str(e)[:100]))

if not py_issues:
    print("  ✅ Semua Python script valid")
else:
    for rel, err in py_issues:
        print(f"  ❌ {rel}: {err}")

# ============================================
# 9. CEK KONSISTENSI NAMA FILE
# ============================================
print()
print("=" * 80)
print("9. KONSISTENSI NAMA FILE (slug pattern)")
print("=" * 80)

expected_pattern = re.compile(r"^ringkasan-jilid-\d+-[a-z0-9-]+\.md$")
ringkasan_files = [f for f in REPO.glob("ringkasan/ringkasan-jilid-*.md")]

for f in ringkasan_files:
    if not expected_pattern.match(f.name):
        print(f"  ⚠️ Nama tidak konsisten: {f.name}")

if not any(not expected_pattern.match(f.name) for f in ringkasan_files):
    print("  ✅ Semua nama file ringkasan konsisten")

# ============================================
# 10. STATISTIK AKHIR
# ============================================
print()
print("=" * 80)
print("10. STATISTIK AKHIR")
print("=" * 80)

total_words = 0
total_lines = 0
for f, rel in text_files:
    content = f.read_text(encoding="utf-8", errors="replace")
    total_words += len(content.split())
    total_lines += content.count("\n")

print(f"  Total text files: {len(text_files)}")
print(f"  Total kata: {total_words:,}")
print(f"  Total baris: {total_lines:,}")
print()

# Per kategori
categories = defaultdict(lambda: {"files": 0, "words": 0})
for f, rel in text_files:
    parts = rel.split("/")
    cat = parts[0] if len(parts) > 1 else "root"
    content = f.read_text(encoding="utf-8", errors="replace")
    categories[cat]["files"] += 1
    categories[cat]["words"] += len(content.split())

print("  Per kategori:")
for cat, stats in sorted(categories.items(), key=lambda x: -x[1]["words"]):
    print(f"    {cat}: {stats['files']} file, {stats['words']:,} kata")

# ============================================
# RINGKASAN
# ============================================
print()
print("=" * 80)
print("RINGKASAN AUDIT")
print("=" * 80)
print(f"  Broken links: {broken_link_issues}")
print(f"  Encoding errors: {len(encoding_issues)}")
print(f"  Hierarchy violations: {len(hierarchy_issues)}")
print(f"  Path referensi lama: {len(path_issues)}")
print(f"  Duplicate content: {dup_count}")
print(f"  TODO/placeholder: {len(todo_issues)}")
print(f"  YAML errors: {len(yaml_issues)}")
print(f"  Python syntax errors: {len(py_issues)}")

total_issues = (broken_link_issues + len(encoding_issues) + len(hierarchy_issues) +
                len(path_issues) + dup_count + len(todo_issues) +
                len(yaml_issues) + len(py_issues))
print()
if total_issues == 0:
    print("  ✅ REPO BERSIH — Tidak ada masalah ditemukan!")
else:
    print(f"  ⚠️ Total {total_issues} masalah ditemukan — lihat detail di atas")
