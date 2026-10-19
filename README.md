# Drama Nusantara — Riset Sejarah

> Riset sejarah untuk produksi drama Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## Struktur Repo

```
.
├── README.md                  ← file ini
├── worklog.md                ← log semua tugas (16 task IDs)
├── .gitignore
│
├── ringkasan/                 ← 5 ringkasan eksklusif (89.252 kata, 38 bab)
│   ├── INDEX.md               ← panduan navigasi + statistik
│   ├── master-tokoh.yaml      ← 250 tokoh lintas 5 jilid (77 lintas-jilid)
│   ├── ringkasan-jilid-1-akar-peradaban-nusantara.md      (9.438 kata)
│   ├── ringkasan-jilid-2-perjumpaan-india-tiongkok-persia.md (9.592 kata)
│   ├── ringkasan-jilid-3-timur-tengah.md                   (12.979 kata)
│   ├── ringkasan-jilid-4-interaksi-awal-barat.md           (40.861 kata)
│   ├── ringkasan-jilid-5-negara-kolonial-1800-1900.md      (16.382 kata)
│   ├── ringkasan-jilid-4-suplemen.md                       (referensi tambahan)
│   ├── ringkasan-jilid-4-suplemen-2-tokoh.md               (420 tokoh)
│   └── ringkasan-jilid-1-2-3-suplemen.md                   (150 tokoh + 80 sub-bab)
│
├── audit/                     ← laporan audit cross-check ke sumber primer
│   ├── audit-jilid3-kemenbud-2025.md     (struktural OCR artifacts)
│   ├── audit-ringkasan-jilid4.md         (228 klaim, 98,7% akurat)
│   └── audit-ringkasan-jilid5.md         (75+ klaim, ≥98% akurat)
│
├── sumber-primer/             ← sumber primer Kemenbud 2025 (78 file MD, 1,2 juta kata)
│   ├── jilid-1/               ← 13 file (Akar Peradaban Nusantara)
│   ├── jilid-2/               ← 15 file (Perjumpaan India-Tiongkok-Persia)
│   ├── jilid-3/               ← 17 file (Timur Tengah / Islamisasi)
│   ├── jilid-4/               ← 18 file (Interaksi Awal dengan Barat)
│   ├── jilid-5/               ← 15 file (Negara Kolonial 1800-1900)
│   └── enhanced-chapters/     ← YAML ontology per bab (38 file)
│
├── phase-1/                   ← riset drama awal (sebelum Kemenbud 2025)
│   ├── riset-drama-nusantara.md           (10 era, 14.277 kata)
│   ├── phase-1-mataram-kuno-master.yaml   (Mataram Kuno)
│   └── phase-2-singasari-master.yaml      (Singasari)
│
└── scripts/                   ← script Python persisten
    ├── audit_jilid3_struktural.py
    ├── audit_jilid3_detail.py
    ├── audit_jilid123_struktur.py
    ├── extract_tokoh_jilid4.py
    └── map_struktur_jilid4.py
```

## Quick Start

1. **Baca `ringkasan/INDEX.md`** untuk panduan navigasi 5 jilid
2. **Cari tokoh** di `ringkasan/master-tokoh.yaml` (250 tokoh, urut kronologis)
3. **Pilih fase drama** berdasarkan periode:
   - Fase 1-3: Jilid 1-2 (prasejarah → Hindu-Buddha)
   - Fase 4-6: Jilid 3 (Islamisasi)
   - Fase 7-9: Jilid 4 (VOC awal)
   - Fase 10-12: Jilid 5 (kolonial 19)
4. **Verifikasi fakta** di `audit/` (3 laporan cross-check ke sumber primer)

## Statistik

| Metrik | Angka |
|---|---|
| Total ringkasan | 89.252 kata (5 jilid, 38 bab) |
| Total tokoh (Master YAML) | 250 (77 lintas-jilid) |
| Total sumber primer | 78 file MD, ~1,2 juta kata |
| Audit dilakukan | 5 task (Jilid 3 struktural + Jilid 4 cross-check + Jilid 5 cross-check) |
| Akurasi ringkasan | Jilid 4: 98,7% | Jilid 5: ≥98% |

## Sumber

- **Buku**: *Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global* (5 jilid)
- **Penerbit**: Kementerian Kebudayaan Republik Indonesia (2025)
- **URL**: https://pustakabudaya.id
