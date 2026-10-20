# Drama Nusantara — Riset & Master Era

> Riset sejarah untuk produksi drama/dokumenter Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## Alur Kerja (Phase)

```
Phase 1: RISET              → baca sumber primer, ringkasan, audit
   ↓
Phase 2: MASTER ERA         → tiap era = narasi + tokoh + latar (berdasar sumber primer)
   ↓
Phase 3: PRODUKSI (nanti)   → output format drama/dokumenter, storyboard, dll
```

**Status saat ini**: Phase 2 — Master Era (prasejarah 1A-1D sedang dikerjakan)

## Struktur Repo

```
drama-nusantara/
├── README.md                          ← file ini
├── worklog.md                         ← log semua task IDs
├── .gitignore
│
├── riset/                             ← PHASE 1: sumber primer + ringkasan + audit
│   ├── sumber-primer/                 ← 123 file MD, 1,257 juta kata
│   │   ├── jilid-1/                   ← 13 file (Akar Peradaban Nusantara)
│   │   ├── jilid-2/                   ← 15 file (Perjumpaan India-Tiongkok-Persia)
│   │   ├── jilid-3/                   ← 17 file (Timur Tengah / Islamisasi)
│   │   ├── jilid-4/                   ← 18 file (Interaksi Awal dengan Barat)
│   │   ├── jilid-5/                   ← 15 file (Negara Kolonial 1800-1900)
│   │   └── enhanced-chapters/         ← 38 YAML ontology per bab
│   │
│   ├── ringkasan/                    ← 10 file, 106.680 kata
│   │   ├── INDEX.md                   ← panduan navigasi 5 jilid
│   │   ├── master-tokoh.yaml         ← 250 tokoh lintas-jilid
│   │   ├── ringkasan-jilid-{1-5}-*.md ← 5 ringkasan utama
│   │   └── ringkasan-jilid-*-suplemen*.md ← 3 suplemen
│   │
│   ├── audit/                         ← 3 laporan cross-check
│   │   ├── audit-jilid3-kemenbud-2025.md
│   │   ├── audit-ringkasan-jilid4.md  (228 klaim cross-check, 98,7% akurat)
│   │   └── audit-ringkasan-jilid5.md  (≥98% akurat)
│   │
│   └── phase-1/                       ← riset drama awal (sebelum Kemenbud 2025)
│       ├── phase-1-mataram-kuno-master.yaml  (79 KB)
│       └── phase-2-singasari-master.yaml     (64 KB)
│
├── master-era/                        ← PHASE 2: master era (SEDANG dikerjakan)
│   ├── TEMPLATE-master-era.md        ← template wajib untuk semua era
│   ├── 1A-prasejarah-pleistosen-awal.md          ← ✅ 1,8 jt - 700 rb thn
│   ├── 1B-prasejarah-pleistosen-tengah-akhir.md  ← ✅ 700 rb - 12 rb thn
│   ├── 1C-prasejarah-holosen-neolitik.md         ⏳ 12 rb - 2.500 SM (berikutnya)
│   ├── 1D-prasejarah-logam-awal.md                ⏳ 2.500 SM - abad 5 M (berikutnya)
│   ├── 2A-hindu-buddha-awal.md                    ⏳ (Kutai, Tarumanagara)
│   ├── 2B-mataram-kuno.md                         ⏳ (abad 8-10 M)
│   ├── 2C-singasari-kediri.md                     ⏳ (abad 11-13 M)
│   ├── 2D-majapahit.md                            ⏳ (abad 13-16 M)
│   ├── 3A-islamisasi-awal.md                      ⏳ (Pasai, Malaka)
│   ├── 3B-demak-pajang.md                         ⏳ (abad 15-16 M)
│   ├── 3C-mataram-islam.md                        ⏳ (abad 17-18 M)
│   ├── 4A-voc-awal.md                             ⏳ (abad 17-18 M)
│   ├── 4B-kolonial-19.md                          ⏳ (1800-1900)
│   ├── 4C-pergerakan-kebangsaan.md                ⏳ (1900-1942)
│   ├── 4D-pendudukan-kemerdekaan.md               ⏳ (1942-1949)
│   └── 4E-orde-lama-baru.md                       ⏳ (1949-1998)
│
├── produksi/                          ← PHASE 3: output drama/dokumenter (nanti)
│   └── panji/                         ← (contoh — DITUNDA, bukan prioritas)
│       └── pre-produksi/
│
└── scripts/                           ← script Python pendukung
    ├── audit_*.py                     ← audit script
    ├── extract_*.py                   ← ekstraksi tokoh/struktur
    ├── koreksi_*.py                   ← koreksi massal
    └── update_*.py                    ← update massal
```

## Quick Start

1. **Baca `riset/ringkasan/INDEX.md`** untuk panduan navigasi 5 jilid
2. **Cari tokoh** di `riset/ringkasan/master-tokoh.yaml` (250 tokoh)
3. **Baca master era** di `master-era/<era>.md` (mulai dari 1A)
4. **Verifikasi fakta** di `riset/audit/` (3 laporan cross-check)
5. **Baca sumber primer** di `riset/sumber-primer/jilid-X/` untuk detail

## Statistik

| Metrik | Angka |
|---|---|
| Total file di repo | 150+ |
| Sumber primer (5 jilid) | 1,257 juta kata |
| Ringkasan 5 jilid + suplemen | 106.680 kata |
| Master YAML tokoh | 250 (77 lintas-jilid) |
| Audit cross-check | 3 laporan, akurasi ≥98,7% |
| Master era selesai | 2 dari 17 (1A, 1B) |
| Master era dalam proses | 1C, 1D (prasejarah) |

## Master Era yang Telah Dikerjakan

| Era | Periode | Status | Kata |
|---|---|---|---|
| 1A Pleistosen Awal | 1,8 juta – 700 ribu thn lalu | ✅ Selesai | ~5.200 |
| 1B Pleistosen Tengah-Akhir | 700 ribu – 12 ribu thn lalu | ✅ Selesai | ~8.500 |
| 1C Holosen / Transisi Neolitik | 12 ribu – 2.500 SM | ⏳ Berikutnya | — |
| 1D Logam Awal | 2.500 SM – abad 5 M | ⏳ Berikutnya | — |

## Sumber

- **Buku**: *Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global* (5 jilid)
- **Penerbit**: Kementerian Kebudayaan Republik Indonesia (2025)
- **URL**: https://pustakabudaya.id
- **Repo**: https://github.com/emailnyamahmud-afk/drama-nusantara

## Riwayat Pengerjaan (Ringkas)

| Phase | Task | Status |
|-------|------|--------|
| Phase 1 | Riset drama awal (10 era) + master YAML Mataram Kuno & Singasari | ✅ |
| Phase 1 | Audit struktural Jilid 3 Kemenbud 2025 | ✅ |
| Phase 1 | Ekstrak drama material Jilid 4 (5 subagent paralel) | ✅ |
| Phase 1 | Sintesis ringkasan Jilid 4 | ✅ |
| Phase 1 | Audit cross-check Jilid 4 (228 klaim, 98,7% akurat) | ✅ |
| Phase 1 | Suplemen Jilid 4 (24 sub-bab + 420 tokoh) | ✅ |
| Phase 1 | Ekstrak drama material Jilid 5 (4 subagent paralel) | ✅ |
| Phase 1 | Audit Jilid 1, 2, 3 (80 sub-bab + 150 tokoh) | ✅ |
| Phase 1 | Ringkasan Jilid 5 + merge suplemen + INDEX | ✅ |
| Phase 1 | Audit Jilid 5 (≥98% akurat) + Master YAML 250 tokoh | ✅ |
| Cleanup | Restrukturisasi repo: 1.496 → 150 file | ✅ |
| Phase 3 (ditunda) | Pre-produksi Panji (story bible + characters + visual style + storyboard) | ✅ Dibuat, lalu ditunda |
| Phase 2 | Master Era 1A Pleistosen Awal | ✅ |
| Phase 2 | Master Era 1B Pleistosen Tengah-Akhir | ✅ |
| Phase 2 | Restructure folder riset/master-era/produksi | ✅ |
