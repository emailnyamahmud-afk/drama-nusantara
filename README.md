# Drama Nusantara — Riset Sejarah

> Riset sejarah untuk produksi drama Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## Struktur Repo (150 file)

```
drama-nusantara/
├── README.md                  ← file ini
├── worklog.md                 ← log 25 task IDs
├── .gitignore
│
├── ringkasan/                 ← 10 file, 106.680 kata
│   ├── INDEX.md               ← panduan navigasi 5 jilid
│   ├── master-tokoh.yaml      ← 250 tokoh, 77 lintas-jilid, 4.033 baris
│   ├── ringkasan-jilid-1-akar-peradaban-nusantara.md        (9.438 kata)
│   ├── ringkasan-jilid-2-perjumpaan-india-tiongkok-persia.md (9.592 kata)
│   ├── ringkasan-jilid-3-timur-tengah.md                     (12.979 kata)
│   ├── ringkasan-jilid-4-interaksi-awal-barat.md             (40.861 kata)
│   ├── ringkasan-jilid-5-negara-kolonial-1800-1900.md        (16.382 kata)
│   ├── ringkasan-jilid-4-suplemen.md                         (4.612 kata, sub-bab terlewat)
│   ├── ringkasan-jilid-4-suplemen-2-tokoh.md                 (6.864 kata, 420 tokoh)
│   └── ringkasan-jilid-1-2-3-suplemen.md                     (5.952 kata, 150 tokoh + 80 sub-bab)
│
├── audit/                     ← 3 laporan, 10.656 kata
│   ├── audit-jilid3-kemenbud-2025.md     (3.322 kata, struktural OCR artifacts)
│   ├── audit-ringkasan-jilid4.md         (6.071 kata, 228 klaim cross-check, 98,7% akurat)
│   └── audit-ringkasan-jilid5.md         (1.263 kata, 75+ klaim cross-check, ≥98% akurat)
│
├── sumber-primer/             ← 123 file, 1.257.120 kata
│   ├── jilid-1/               ← 13 file MD (300.940 kata) — Akar Peradaban Nusantara
│   ├── jilid-2/               ← 15 file MD (297.374 kata) — Perjumpaan India-Tiongkok-Persia
│   ├── jilid-3/               ← 17 file MD (230.624 kata) — Timur Tengah / Islamisasi
│   ├── jilid-4/               ← 18 file MD (221.902 kata) — Interaksi Awal dengan Barat
│   ├── jilid-5/               ← 15 file MD (206.280 kata) — Negara Kolonial 1800-1900
│   └── enhanced-chapters/     ← 38 YAML ontology per bab + 5 _meta.yaml
│
├── phase-1/                   ← riset drama awal (sebelum Kemenbud 2025)
│   ├── riset-drama-nusantara.md           (10 era, 14.277 kata)
│   ├── phase-1-mataram-kuno-master.yaml   (Mataram Kuno, 79 KB)
│   └── phase-2-singasari-master.yaml      (Singasari, 64 KB)
│
└── scripts/                   ← 8 script Python
    ├── audit_all_text_repo.py             (audit menyeluruh semua file repo)
    ├── audit_jilid3_struktural.py         (audit struktural OCR Jilid 3)
    ├── audit_jilid3_detail.py             (detail empty sections, hierarchy, weird chars)
    ├── audit_jilid123_struktur.py         (mapping struktur 18 bab Jilid 1-3)
    ├── extract_tokoh_jilid4.py            (ekstrak tokoh via regex Jilid 4)
    ├── map_struktur_jilid4.py             (mapping struktur 10 bab Jilid 4)
    ├── build_quality_report.py            (quality report semua bab)
    └── generate_medium_priority_enhanced.py (YAML enhanced untuk 32 bab)
```

## Quick Start

1. **Baca `ringkasan/INDEX.md`** untuk panduan navigasi 5 jilid
2. **Cari tokoh** di `ringkasan/master-tokoh.yaml` (250 tokoh, urut kronologis T001-T250)
3. **Pilih fase drama** berdasarkan periode:
   - Fase 1-3: Jilid 1-2 (prasejarah → Hindu-Buddha, 1,8 juta tahun lalu – abad 16 M)
   - Fase 4-6: Jilid 3 (Islamisasi, abad 7 – abad 16 M)
   - Fase 7-9: Jilid 4 (VOC awal, abad 15 – 1799 M)
   - Fase 10-12: Jilid 5 (kolonial 19, 1800-1900 M)
4. **Verifikasi fakta** di `audit/` (3 laporan cross-check ke sumber primer)
5. **Baca sumber primer** di `sumber-primer/jilid-X/` untuk detail lengkap

## Statistik

| Metrik | Angka |
|---|---|
| Total file di repo | 150 |
| Total kata (semua file) | ~1,46 juta |
| Total ringkasan | 106.680 kata (5 jilid + 3 suplemen, 38 bab) |
| Total tokoh (Master YAML) | 250 (77 lintas-jilid) |
| Total sumber primer | 78 file MD, 1.257.120 kata |
| Total audit | 3 laporan, 10.656 kata |
| Total task di worklog | 25 task IDs |
| Akurasi ringkasan | Jilid 4: 98,7% \| Jilid 5: ≥98% |

## Audit yang Telah Dilakukan

| Audit | Jilid | Metode | Hasil |
|---|---|---|---|
| Struktural OCR artifacts | Jilid 3 | Script Python (heading hierarchy, weird chars, empty sections) | 6 kategori, ~57 titik masalah |
| Cross-check klaim ke sumber primer | Jilid 4 | grep 228 klaim ke 10 bab sumber primer | 98,7% akurat, 1 kesalahan (38→68 perken) |
| Cross-check klaim ke sumber primer | Jilid 5 | grep 75+ klaim ke 7 bab sumber primer | ≥98% akurat, 0 kesalahan signifikan |
| Audit semua text repo | Semua | Script Python (encoding, YAML, Python, broken links, duplicates) | 150 file bersih, 0 encoding error, 0 broken link |

## Tokoh Lintas-Jilid Terpenting

| Tokoh | Jilid | Peran |
|---|---|---|
| Abd al-Ra'uf al-Sinkili | 3, 4, 5 | Kadi Aceh, khalifah Syattariyah |
| Sultan Agung | 3, 4 | Mataram Islam, penyerangan Batavia |
| Sultan Hasanuddin | 3, 4 | Gowa-Tallo, Perjanjian Bongaya |
| Eugène Dubois | 1, 5 | Pithecanthropus Trinil 1891 |
| Alfred Russel Wallace | 1, 5 | Garis Wallace, co-penemu seleksi alam |
| Raja Ali Haji | 4, 5 | Tuhfat al-Nafis, pujangga Pulau Penyengat |
| Mangkunegara IV | 4, 5 | Wedhatama, industrialis gula Colomadu |

## Sumber

- **Buku**: *Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global* (5 jilid)
- **Penerbit**: Kementerian Kebudayaan Republik Indonesia (2025)
- **URL**: https://pustakabudaya.id
- **Repo**: https://github.com/emailnyamahmud-afk/drama-nusantara

## Riwayat Pengerjaan

| Task ID | Deskripsi |
|---|---|
| 1-8 | Riset drama awal (10 era) + master YAML Mataram Kuno & Singasari |
| 9 | Audit struktural Jilid 3 Kemenbud 2025 |
| 10-A s/d 10-E | Ekstrak drama material Jilid 4 (5 subagent paralel) |
| 11 | Sintesis ringkasan Jilid 4 + setup GitHub |
| 12 | Audit cross-check Jilid 4 (228 klaim, 98,7% akurat) |
| 13-14 | Suplemen Jilid 4 (24 sub-bab + 420 tokoh tambahan) |
| 15-A s/d 15-D | Ekstrak drama material Jilid 5 (4 subagent paralel) |
| 15 | Audit Jilid 1, 2, 3 (80 sub-bab + 150 tokoh terlewat) |
| 16 | Ringkasan Jilid 5 + merge suplemen + INDEX |
| 17 | Audit Jilid 5 (≥98% akurat) + Master YAML 250 tokoh |
| Cleanup | Restrukturisasi repo: 1.496 → 150 file, hapus duplikasi, update path |
