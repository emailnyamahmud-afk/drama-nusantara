# Drama Nusantara — Riset & Master Era

> Riset sejarah untuk produksi drama/dokumenter Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## Alur Kerja

```
1. SUMBER PRIMER          → baca Jilid 1-5 (Kemenbud 2025) — hanya file asli, no ringkasan
   ↓
2. MASTER ERA             → tiap era = parsing sistematis sumber primer → narasi + tokoh + latar
   ↓
3. T2I PROMPTS            → copy-paste ke Dola AI → output drama/dokumenter
```

**Status saat ini**: Era 1A-1D + 2D + 3A sudah di-rewrite/expand lengkap (parsing sistematis Bab terkait). Era 2A-2C + 3B sudah ditulis + dikoreksi parsing. T2I prompts sudah dibuat untuk 1A-3B.

## Struktur Repo

```
drama-nusantara/
├── README.md                              ← file ini
├── worklog.md                             ← log semua task
├── push-to-github.sh                      ← helper script untuk push
│
├── riset/
│   └── sumber-primer/                     ← SUMBER PRIMER: 83 file MD asli dari Kemenbud 2025
│       ├── jilid-1/                       ← 13 file (Akar Peradaban Nusantara)
│       ├── jilid-2/                       ← 15 file (Perjumpaan India-Tiongkok-Persia)
│       ├── jilid-3/                       ← 17 file (Timur Tengah / Islamisasi)
│       ├── jilid-4/                       ← 18 file (Interaksi Awal dengan Barat)
│       └── jilid-5/                       ← 15 file (Negara Kolonial 1800-1900)
│
├── master-era/                            ← MASTER ERA: parsing sistematis per periode
│   ├── TEMPLATE-master-era.md            ← template wajib untuk semua era
│   ├── 1A-prasejarah-pleistosen-awal.md          ✅ 1171 baris (rewrite lengkap)
│   ├── 1B-prasejarah-pleistosen-tengah-akhir.md   ✅ 1214 baris (rewrite lengkap)
│   ├── 1C-prasejarah-holosen-neolitik.md          ✅ 1205 baris (rewrite lengkap)
│   ├── 1D-prasejarah-logam-awal.md                  ✅ 1264 baris (rewrite lengkap)
│   ├── 2A-hindu-buddha-awal.md                       ✅ 831 baris
│   ├── 2B-mataram-sriwijaya.md                       ✅ 805 baris
│   ├── 2C-singasari-kediri.md                        ✅ 519 baris
│   ├── 2D-majapahit.md                                ✅ 816 baris (expand lengkap — Bab II+III+IV+V+VI Jilid 2)
│   ├── 3A-islamisasi-awal.md                          ✅ 815 baris (rewrite lengkap — semua 9 Bab Jilid III)
│   └── 3B-demak-pajang.md                             ✅ 756 baris (koreksi + 4 tokoh baru + 2 latar baru)
│
├── produksi/
│   ├── t2i-prompts/                       ← T2I prompts per era (siap copy-paste ke Dola AI)
│   │   ├── GUIDE-dola-ai.md              ← panduan cara pakai Dola AI
│   │   ├── 1A-prasejarah-pleistosen-awal/prompts/         ✅ 10 file
│   │   ├── 1B-prasejarah-pleistosen-tengah-akhir/prompts/ ✅ 10 file
│   │   ├── 1C-prasejarah-holosen-neolitik/prompts/        ✅ 10 file
│   │   ├── 1D-prasejarah-logam-awal/prompts/              ✅ 12 file
│   │   ├── 2A-hindu-buddha-awal/prompts/                   ✅ 18 file
│   │   ├── 2B-mataram-sriwijaya/prompts/                  ✅ 37 file
│   │   ├── 2C-singasari-kediri/prompts/                    ✅ 17 file
│   │   ├── 2D-majapahit/prompts/                           ✅ 17 file
│   │   ├── 3A-islamisasi-awal/prompts/                     ✅ 21 file
│   │   └── 3B-demak-pajang/prompts/                        ✅ 21 file
│   └── panji/                             ← pre-produksi Panji (DITUNDA)
│
└── scripts/                               ← script Python/JS pendukung
    ├── audit_*.py                         ← audit script
    ├── extract_*.py                       ← ekstraksi tokoh/struktur
    └── generate_*.py                     ← generate T2I prompts
```

## Aturan Repo

1. **`riset/sumber-primer/`** = HANYA file asli dari buku Kemenbud 2025 (Jilid 1-5). Tidak ada ringkasan, tidak ada enhanced YAML, tidak ada audit JSON. Jika perlu cari info, baca langsung file asli.
2. **`master-era/`** = parsing sistematis dari sumber primer. Setiap klaim punya sitasi ke file + section sumber primer. Era 1A-1D + 2D + 3A sudah di-rewrite/expand lengkap (parsing sistematis Bab terkait). Era 2A-2C + 3B sudah ditulis + dikoreksi parsing, perlu audit coverage tambahan.
3. **`produksi/t2i-prompts/`** = file .txt siap copy-paste ke Dola AI. Format flat natural-language.

## Quick Start

1. **Baca master era** di `master-era/<era>.md` (mulai dari 1A)
2. **Verifikasi klaim** di `riset/sumber-primer/jilid-X/` — baca file asli yang disitir
3. **Generate image** di Dola AI: baca `produksi/t2i-prompts/GUIDE-dola-ai.md`
4. **Copy-paste prompt** dari `produksi/t2i-prompts/<era>/prompts/*.txt`

## Statistik

| Metrik | Angka |
|---|---|
| Sumber primer (5 jilid) | 83 file MD asli |
| Master era selesai | 10 dari 17 (1A-1D + 2D expand lengkap + 2A-2C + 3A rewrite lengkap + 3B) |
| T2I prompts selesai | 10 era (173 file .txt total) |
| Total kata master era | ~112.000 kata (9.964+ baris era docs) |
| Total file di repo | 345 |

## Status Master Era + T2I Prompts

| Era | Periode | Master | Baris | T2I | T2I file |
|-----|---------|--------|-------|-----|----------|
| 1A Pleistosen Awal | 1,8 jt – 700 rb thn lalu | ✅ rewrite | 1171 | ✅ | 10 |
| 1B Pleistosen Tengah-Akhir | 700 rb – 12 rb thn lalu | ✅ rewrite | 1214 | ✅ | 10 |
| 1C Holosen / Neolitik | 12 rb – 2.500 SM | ✅ rewrite | 1205 | ✅ | 10 |
| 1D Logam Awal | 2.500 SM – abad 5 M | ✅ rewrite | 1264 | ✅ | 12 |
| **TOTAL PRASEJARAH** | | | **4854** | | **42** |
| 2A Hindu-Buddha Awal | Abad 4-7 M | ✅ | 831 | ✅ | 18 |
| 2B Mataram-Sriwijaya | Abad 7-11 M | ✅ | 805 | ✅ | 37 |
| 2C Singasari-Kediri | Abad 11-13 M | ✅ | 519 | ✅ | 17 |
| 2D Majapahit | Abad 13-16 M | ✅ expand | 816 | ✅ | 17 |
| **TOTAL HINDU-BUDDHA** | | | **2930** | | **89** |
| 3A Islamisasi Awal | Abad 7-1511 M | ✅ rewrite | 815 | ✅ | 21 |
| 3B Demak-Pajang | Abad 15-16 M | ✅ koreksi | 756 | ✅ | 21 |
| **TOTAL ISLAM** | | | **1327** | | **42** |
| 3C Mataram Islam | Abad 17-18 M | ⏳ | — | ⏳ | — |
| 4A VOC Awal | Abad 17-18 M | ⏳ | — | ⏳ | — |
| 4B Kolonial 19 | 1800-1900 | ⏳ | — | ⏳ | — |
| 4C Pergerakan Kebangsaan | 1900-1942 | ⏳ | — | ⏳ | — |
| 4D Pendudukan-Kemerdekaan | 1942-1949 | ⏳ | — | ⏳ | — |
| 4E Orde Lama-Baru | 1949-1998 | ⏳ | — | ⏳ | — |

### Catatan: Rewrite vs Koreksi

- **Rewrite lengkap** (1A-1D): Parsing sistematis semua entitas bernama dari sumber primer. Setiap tokoh, spesimen, situs, formasi geologi, biozona fauna diekstrak. Coverage 80-100%.
- **Koreksi parsing** (2D, 3A, 3B): Verifikasi langsung dari sumber primer, koreksi klaim yang salah, tambah tokoh/latar yang terlewat. Coverage 50-70% — perlu audit coverage tambahan.

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

| Tanggal | Task | Status |
|---------|------|--------|
| 2026-10-17 | Riset awal + struktur repo | ✅ |
| 2026-10-18 | Master era 1A-2B + T2I prompts | ✅ |
| 2026-10-19 | Master era 2C-2D + T2I prompts | ✅ |
| 2026-10-19 | Audit + bersihkan 97 file T2I | ✅ |
| 2026-10-20 | Master era 3A Islamisasi Awal + 21 T2I prompts | ✅ |
| 2026-10-20 | Master era 3B Demak-Pajang + 21 T2I prompts | ✅ |
| 2026-10-20 | Koreksi parsing: 2D Akt 6 (Ranawijaya), 3A (Demak 1481 M), 3B (Arya Penangsang + 4 tokoh baru + 2 latar baru) | ✅ |
| 2026-10-20 | **Rewrite lengkap 1A** — parsing sistematis (620→1171 baris, +551 baris) | ✅ |
| 2026-10-20 | **Rewrite lengkap 1B** — +10 tokoh +5 latar (1003→1214 baris) | ✅ |
| 2026-10-20 | **Rewrite lengkap 1C** — +18 latar baru (1020→1205 baris) | ✅ |
| 2026-10-20 | **Rewrite lengkap 1D** — +7 latar + bagian 4B primus inter pares (1098→1264 baris) | ✅ |
| 2026-10-20 | **Cleanup repo** — hapus 55 file sampah (ringkasan/audit/enhanced-chapters/phase-1), update README | ✅ |
| 2026-10-20 | **Expand lengkap 2D Majapahit** — Bab III A.4 + Bab IV-V-VI, 327→775 baris, 8.500→13.044 kata, 35→93 klaim, +9 tokoh +9 latar (Adityawarman, Wirabhumi, Kertabhumi, Ranawijaya, Patih Udara, Canggu, Trung, Daha/Kadiri, Candi Sukuh, pegunungan skriptoria) | ✅ |
| 2026-10-20 | **Audit halu 2D expand** — ditemukan + fixed: Candi Sukuh ±1437 M (tahun halu, hapus); Meng Qi utusan Mongol 1289 (tahun halu, hapus); '100 keluarga' → '100 anggota keluarga' (sesuai sumber primer); add Bab 2 Jilid II content (dharmadyaksa kasaiwan/karsian/kasogatan, Candi Brahu+Prasasti Alasantan Pu Sindok 861/939, Aksara Merapi-Merbabu/Prasasti Damalung 1371/1449, Aksara Arab Jawi-Pegon-Serang) → 775→816 baris, 93→112 klaim | ✅ |
| 2026-10-20 | **Rewrite lengkap 3A Islamisasi Awal** — parsing sistematis semua 9 Bab Jilid III (Bab 1-9), 571→815 baris, 7.903→15.167 kata, 64→136 klaim. Add: 3A periode diperluas jadi abad 7-1511 M (sebelumnya cuma abad 13-15); Bab 1 Bongal+koin Umayyah/Abbasiyah abad 7-10 M; Bab 4 Giri-Gresik+Minangkabau+Kutai; Bab 5 sistem transaksi+Undang-Undang Laut Melaka+syahbandar; Bab 6 gagasan politik+sultan+genealogi Iskandar Zulkarnain+hubungan Raja-Ulama-Elite+lembaga qadi/syaikh al-Islam/pakih najmuddin/Daengte Kaliya/Parewa Sara/Babato Akhirat; Bab 8 keraton+masjid Tipe Jawa 6 ciri Pijper+makam+nisan tipe Aceh/Demak-Troloyo/Bugis-Makasar/Ternate-Tidore/Plak Plieng; Bab 9 kosmopolis Sanskerta-Arab+Hikayat Amir Hamzah+Caritanira Amir+Sérat Menak Kartasura 1715+aksara Jawi-Pegon-Rambang-Serang-Buri Wolio | ✅ |
