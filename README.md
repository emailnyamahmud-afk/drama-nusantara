# Drama Nusantara — Riset & Master Era

> Riset sejarah untuk produksi drama/dokumenter Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## Alur Kerja (Phase)

```
Phase 1: RISET              → baca sumber primer, ringkasan, audit
   ↓
Phase 2: MASTER ERA         → tiap era = narasi + tokoh + latar (berdasar sumber primer)
   ↓
Phase 3: PRODUKSI           → T2I prompts (copy-paste ke Dola AI) + output drama/dokumenter
```

**Status saat ini**: Phase 2 — Master Era + T2I Prompts (pola hibrida: tiap selesai 1 era master → langsung buat T2I prompts)

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
├── master-era/                        ← PHASE 2: master era per periode
│   ├── TEMPLATE-master-era.md        ← template wajib untuk semua era
│   ├── 1A-prasejarah-pleistosen-awal.md          ✅ ~5.200 kata
│   ├── 1B-prasejarah-pleistosen-tengah-akhir.md ✅ ~8.500 kata
│   ├── 1C-prasejarah-holosen-neolitik.md         ✅ ~11.000 kata
│   ├── 1D-prasejarah-logam-awal.md                ✅ ~13.500 kata
│   ├── 2A-hindu-buddha-awal.md                    ✅ ~9.500 kata
│   ├── 2B-mataram-sriwijaya.md                    ✅ ~11.000 kata
│   └── 2C-singasari-kediri.md                       ✅ ~9.000 kata
│   ├── 2C-singasari-kediri.md                    ⏳ berikutnya
│   └── 2D-majapahit.md                              ✅ ~8.500 kata
│   ├── 3B-demak-pajang.md                         ⏳
│   ├── 3C-mataram-islam.md                        ⏳
│   ├── 4A-voc-awal.md                             ⏳
│   ├── 4B-kolonial-19.md                          ⏳
│   ├── 4C-pergerakan-kebangsaan.md                ⏳
│   ├── 4D-pendudukan-kemerdekaan.md               ⏳
│   └── 4E-orde-lama-baru.md                       ⏳
│
├── produksi/                          ← PHASE 3: T2I prompts + output
│   ├── t2i-prompts/                   ← T2I prompts per era (siap copy-paste ke Dola AI)
│   │   ├── GUIDE-dola-ai.md           ← panduan cara pakai Dola AI
│   │   ├── 1A-prasejarah-pleistosen-awal/prompts/         ✅ 10 file
│   │   ├── 1B-prasejarah-pleistosen-tengah-akhir/prompts/ ✅ 10 file
│   │   ├── 1C-prasejarah-holosen-neolitik/prompts/        ✅ 10 file
│   │   ├── 1D-prasejarah-logam-awal/prompts/              ✅ 12 file
│   │   ├── 2A-hindu-buddha-awal/prompts/                   ✅ 18 file
│   │   ├── 2B-mataram-sriwijaya/prompts/                  ✅ 37 file
│   │   └── 2D-majapahit/prompts/                           ✅ 17 file
│   └── panji/                         ← (contoh — DITUNDA, bukan prioritas)
│
└── scripts/                           ← script Python pendukung
    ├── audit_*.py                     ← audit script
    ├── extract_*.py                   ← ekstraksi tokoh/struktur
    ├── koreksi_*.py                   ← koreksi massal
    ├── regenerate_t2i_prompts.py      ← generate ulang 1A-1D prompts
    ├── generate_2B_prompts.py        ← generate 2B prompts
    ├── generate_2B_room_prompts.py    ← generate 2B ruang istana
    └── clean_humans_from_L.py         ← bersihkan manusia dari file L
```

## Quick Start

1. **Baca `riset/ringkasan/INDEX.md`** untuk panduan navigasi 5 jilid
2. **Cari tokoh** di `riset/ringkasan/master-tokoh.yaml` (250 tokoh)
3. **Baca master era** di `master-era/<era>.md` (mulai dari 1A)
4. **Verifikasi fakta** di `riset/audit/` (3 laporan cross-check)
5. **Baca sumber primer** di `riset/sumber-primer/jilid-X/` untuk detail
6. **Generate image** di Dola AI: baca `produksi/t2i-prompts/GUIDE-dola-ai.md`
7. **Copy-paste prompt** dari `produksi/t2i-prompts/<era>/prompts/*.txt`

## Statistik

| Metrik | Angka |
|---|---|
| Total file di repo | 200+ |
| Sumber primer (5 jilid) | 1,257 juta kata |
| Ringkasan 5 jilid + suplemen | 106.680 kata |
| Master YAML tokoh | 250 (77 lintas-jilid) |
| Audit cross-check | 3 laporan, akurasi ≥98,7% |
| Master era selesai | 8 dari 17 (1A-1D + 2A-2D) |
| Master era dalam proses | 3A Islamisasi Awal (berikutnya) |
| T2I prompts selesai | 8 dari 17 era (131 prompt total) |
| T2I prompts dalam proses | 3A Islamisasi Awal (berikutnya) |
| Total kata master era | ~58.700 kata |
| Total T2I prompt file | 131 file .txt siap copy-paste |

## Status Master Era + T2I Prompts (Pola Hibrida)

Setiap selesai 1 era master → langsung buat prompt T2I komprehensif untuk era itu.

| Era | Periode | Master | T2I | File |
|-----|---------|--------|-----|------|
| 1A Pleistosen Awal | 1,8 jt – 700 rb thn lalu | ✅ ~5.200 kata | ✅ | 10 |
| 1B Pleistosen Tengah-Akhir | 700 rb – 12 rb thn lalu | ✅ ~8.500 kata | ✅ | 10 |
| 1C Holosen / Transisi Neolitik | 12 rb – 2.500 SM | ✅ ~11.000 kata | ✅ | 10 |
| 1D Logam Awal | 2.500 SM – abad 5 M | ✅ ~13.500 kata | ✅ | 12 |
| **TOTAL PRASEJARAH** | **1,8 jt thn – abad 5 M** | ✅ ~38.200 kata | ✅ | **42** |
| 2A Hindu-Buddha Awal | Abad 4-7 M | ✅ ~9.500 kata | ✅ | 18 |
| 2B Mataram-Sriwijaya | Abad 7-11 M | ✅ ~11.000 kata | ✅ | 37 |
| **TOTAL HINDU-BUDDHA AWAL** | **Abad 4-11 M** | ✅ ~20.500 kata | ✅ | **55** |
| 2C Singasari-Kediri | Abad 11-13 M | ✅ ~9.000 kata | ✅ | 17 prompt |
| 2D Majapahit | Abad 13-16 M | ✅ ~8.500 kata | ✅ | 17 prompt |
| 3A Islamisasi Awal | Abad 13-15 M | ⏳ | ⏳ | — |
| 3B Demak-Pajang | Abad 15-16 M | ⏳ | ⏳ | — |
| 3C Mataram Islam | Abad 17-18 M | ⏳ | ⏳ | — |
| 4A VOC Awal | Abad 17-18 M | ⏳ | ⏳ | — |
| 4B Kolonial 19 | 1800-1900 | ⏳ | ⏳ | — |
| 4C Pergerakan Kebangsaan | 1900-1942 | ⏳ | ⏳ | — |
| 4D Pendudukan-Kemerdekaan | 1942-1949 | ⏳ | ⏳ | — |
| 4E Orde Lama-Baru | 1949-1998 | ⏳ | ⏳ | — |

### T2I Prompts — Struktur per Era

Setiap folder `produksi/t2i-prompts/<era>/prompts/` berisi file `.txt` siap copy-paste ke Dola AI:

**Tipe file:**
- **K** = Karakter ref sheet (5 angle grid, clean cream studio background, 9:16)
- **L** = Latar/lokasi (scene historis, NO people, 9:16)
- **A** = Artefak (macro detail, 9:16)

**Format per file:**
- Flat natural-language prompt (siap paste langsung ke Dola AI chat box)
- Style keyword di awal ("Cinematic realistic...")
- Lighting konkret (Kelvin + arah + rasio kontras)
- Lensa spesifik (24mm-85mm, f/1.8-f/11)
- Color grading per era
- "Avoid:" section dengan negative prompt lengkap
- Semua file L: "No people, no characters, no humans — empty location reference"

**Naming convention (era 2B+):**
- `2B-K01-SRIWIJAYA-dapunta-hyang.txt` (Karakter, kerajaan, nama)
- `2B-L07-MATARAM-istana-eksterior-sindoro-sumbing.txt` (Lokasi, kerajaan, deskripsi)
- `2B-A02-MATARAM-borobudur-stupa.txt` (Artefak, kerajaan, objek)

### Dola AI Workflow

1. Buka https://dola.com/chat/create-image (login Google)
2. Pilih model Seedream 4.5
3. Buka file `.txt` dari repo
4. Copy seluruh isi (Ctrl+A, Ctrl+C)
5. Paste ke chat box Dola AI
6. Generate → pilih 1 dari variasi → download
7. Untuk konsistensi karakter: upload K (character ref) sebagai reference saat generate scene

**Panduan lengkap**: `produksi/t2i-prompts/GUIDE-dola-ai.md`

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
| Phase 2 | Restructure folder riset/master-era/produksi | ✅ |
| Phase 2 | Master Era 1A Pleistosen Awal + T2I prompts | ✅ |
| Phase 2 | Master Era 1B Pleistosen Tengah-Akhir + T2I prompts | ✅ |
| Phase 2 | Master Era 1C Holosen / Transisi Neolitik + T2I prompts | ✅ |
| Phase 2 | Master Era 1D Logam Awal + T2I prompts | ✅ |
| Phase 2 | Master Era 2A Hindu-Buddha Awal + T2I prompts (18 file) | ✅ |
| Phase 2 | Master Era 2B Mataram-Sriwijaya + T2I prompts (37 file) | ✅ |
| Phase 2 | Audit + bersihkan semua 97 file T2I (hapus manusia dari L, fix lensa, fix China architecture) | ✅ |
| Phase 2 | Rename file 2B dengan prefix MATARAM/SRIWIJAYA | ✅ |
| Phase 2 | Riset Dola AI + buat GUIDE-dola-ai.md | ✅ |
| Phase 2 | Master Era 2C Singasari-Kediri + T2I prompts | ⏳ Berikutnya |
