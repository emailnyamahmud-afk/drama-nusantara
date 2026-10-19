#!/usr/bin/env python3
"""
Ekstrak semua tokoh (nama orang) dari 10 bab sumber primer Jilid 4.
Bandingkan dengan tokoh yang sudah disebut di ringkasan + suplemen.
Identifikasi tokoh yang BELUM diekstrak.
"""
import re
from pathlib import Path
from collections import Counter, defaultdict

JILID = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/jilid-4")
RINGKASAN_UTAMA = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/ringkasan-jilid/ringkasan-jilid-4-interaksi-awal-barat.md")
SUPLEMEN = Path("/home/z/my-project/riset-backup/phase-1-riset/sumber-primer/kemenbud-2025/ringkasan-jilid/ringkasan-jilid-4-suplemen.md")

# Baca ringkasan + suplemen
ringkasan_text = (RINGKASAN_UTAMA.read_text(encoding="utf-8") + "\n" + SUPLEMEN.read_text(encoding="utf-8")).lower()

# Daftar tokoh yang sudah disebut (manual extraction dari ringkasan)
tokoh_sudah = set()
# Extract all capitalized names from ringkasan
for line in ringkasan_text.split("\n"):
    # Find capitalized words (potential names)
    for m in re.finditer(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,4})\b", line):
        name = m.group(1).lower()
        if len(name) > 4:
            tokoh_sudah.add(name)

print(f"=== Tokoh yang sudah disebut di ringkasan+suplemen: {len(tokoh_sudah)} ===")
print("Sample (20 pertama):")
for n in sorted(tokoh_sudah)[:20]:
    print(f"  - {n}")
print()

# Pola tokoh yang dicari di sumber primer (lebih luas):
# - Sultan X, Pangeran X, Raja X, Sunan X, Kapitan X, Adipati X, Bendahara X
# - Nama Eropa: Cornelis X, Jan X, Henrique X, Antonio X, Jacob X, Pieter X
# - Nama Arab-Islam: Syekh X, Sultan X, Ratu X
# - Gelar lokal: Karaeng X, Daeng X, Arung X, Tuan X

pola_tokoh = [
    # Gelar + nama
    (r"\bSultan\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Sultan"),
    (r"\bPangeran\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Pangeran"),
    (r"\bRaja\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Raja"),
    (r"\bRatu\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Ratu"),
    (r"\bSunan\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Sunan"),
    (r"\bKapitan\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Kapitan"),
    (r"\bAdipati\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Adipati"),
    (r"\bBendahara\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Bendahara"),
    (r"\bKaraeng\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Karaeng"),
    (r"\bDaeng\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Daeng"),
    (r"\bArung\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Arung"),
    (r"\bSyekh\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Syekh"),
    (r"\bPanembahan\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Panembahan"),
    (r"\bTuan\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Tuan"),
    (r"\bPangeran\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Pangeran"),
    (r"\bFrater\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Frater"),
    (r"\bSri\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Sri"),
    (r"\bDatu\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Datu"),
    (r"\bPati\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Pati"),
    (r"\bSangaji\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Sangaji"),
    (r"\bKimelaha\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,5})\b", "Kimelaha"),
    # Nama Belanda/Eropa dengan kapitalisasi
    (r"\b(Cornelis|Jan|Pieter|Jacob|Hendrik|Willem|Johan|Antonio|Afonso|Francisco|Frederick|Joost|Herman|Steven|Anthony|Gerrit|Marten|Leonard|Jochum|Abraham|Wolfert|Dirk|Isaac|Gerard|Reinier|Balthazar|Salvador|Gustaaf|Francois|Sebastiaan|Simon|Abraham)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b", "Belanda/Eropa"),
    # Nama ulama Arab
    (r"\b(Nuruddin|Ibrahim|Ahmad|Yusuf|Abdullah|Muhammad|Hasan|Husain|Ali|Hamzah|Ismail|Ibnu|Abu)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b", "Ulama"),
]

# Ekstrak tokoh per bab
tokoh_per_bab = defaultdict(lambda: defaultdict(int))  # bab -> nama -> count

for f in sorted(JILID.glob("[01][0-9]-bab-*.md")):
    text = f.read_text(encoding="utf-8")
    bab_num_match = re.search(r"bab-(\d+)\.md", f.name)
    if not bab_num_match:
        continue
    bab_num = bab_num_match.group(1)

    for pat, label in pola_tokoh:
        for m in re.finditer(pat, text):
            if m.lastindex:
                full_name = ""
                for i in range(1, m.lastindex + 1):
                    full_name += " " + m.group(i)
                full_name = full_name.strip()
                # Skip noise
                if len(full_name) > 5 and not re.search(r"[<>|]", full_name):
                    tokoh_per_bab[bab_num][full_name] += 1

# Tampilkan tokoh per bab, highlight yang BELUM ada di ringkasan
print("\n" + "="*100)
print("TOKOH PER BAB (urut by frekuensi) — dengan penanda ✗ jika BELUM ada di ringkasan")
print("="*100)

total_belum = 0
total_sudah = 0

for bab in sorted(tokoh_per_bab.keys()):
    print(f"\n### BAB {bab} — {len(tokoh_per_bab[bab])} tokoh unik ###")
    sorted_tokoh = sorted(tokoh_per_bab[bab].items(), key=lambda x: -x[1])
    for name, count in sorted_tokoh[:50]:  # top 50 per bab
        sudah = name.lower() in ringkasan_text or any(part.lower() in ringkasan_text for part in name.split() if len(part) > 4)
        marker = "✓" if sudah else "✗"
        if not sudah:
            total_belum += 1
        else:
            total_sudah += 1
        print(f"  {marker} [{count:3}x] {name}")

print(f"\n{'='*100}")
print(f"TOTAL: sudah={total_sudah}, BELUM diekstrak={total_belum}")
print(f"Persentase terlewat: {total_belum/(total_belum+total_sudah)*100:.1f}%")
