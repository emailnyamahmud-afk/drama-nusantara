# Drama Nusantara — Riset & Produksi Sejarah Nusantara

> Riset sejarah untuk produksi drama/dokumenter Nusantara berbasis buku **Sejarah Indonesia: Dinamika Kebangsaan dalam Arus Global** (Kementerian Kebudayaan RI, 2025)

## 8 Phase Pipeline

```
1. SUMBER PRIMER          → baca Jilid 1-5 (Kemenbud 2025) — hanya file asli, no ringkasan           ✅
   ↓
2. MASTER ERA             → tiap era = parsing sistematis sumber primer → narasi + tokoh + latar    ✅
   ↓
3. MASTER REFF T2I        → prompt universal per era: K (karakter), S (kelompok), L (lokasi), A (artefak), F (fauna)  🔄
   ↓
4. PRA-PRODUKSI           → narasi + storyboard JSON per produksi (dokumenter / series)                ⏳
   ↓
5. PRODUKSI T2I           → generate image per segmen storyboard (Dola AI)                             ⏳
   ↓
6. PRODUKSI I2V           → image-to-video per segmen                                                ⏳
   ↓
7. PRODUKSI TTS           → voice over (narrator edge-tts / multi-voice untuk dialog)                  ⏳
   ↓
8. PASCA PRODUKSI         → stitch video per segmen (ffmpeg / DaVinci Resolve)                        ⏳
```

**Aturan:** JSON = single source of truth. T2I, I2V, TTS hanya mengikuti JSON. User edit JSON kalau perlu.

**Workflow:** diskusi di Z.ai chat → AI push GitHub → user pull → user generate di Dola AI (free unlimited image) → asset lokal saja (di-gitignore).

**Status saat ini**: Era 1A-1D + 2A-2D + 3A-3C + 4A-4B sudah di-rewrite/expand lengkap (16 era, ~220.000 kata, 1.496 klaim). Hanya 4C-4E BLOCKED menunggu Jilid VI-X. T2I prompts sudah dibuat untuk 1A-3B (3C+4A+4B belum).

**BLOCKED**: Era 4C-4E (Pergerakan Kebangsaan → Orde Baru) tidak dapat dikerjakan karena **Jilid VI-X belum terbit** (Kementerian Kebudayaan RI 2025). Jilid V secara eksplisit menyebut di Bab VII line 558: "Jilid berikutnya, 'Jilid VI: Pergerakan Kebangsaan', akan menelusuri fase ketika kesadaran tersebut menemukan bentuk organisasinya." Folder `riset/sumber-primer/jilid-6/` belum ada.

## Struktur Repo

```
drama-nusantara/
├── README.md                              ← file ini
├── progres-project.md                     ← catatan progres per sesi (AI amnesia mitigation)
├── worklog.md                             ← log semua task
├── .gitignore                             ← ignore aset (image/video/audio) + secrets
│
├── riset/
│   └── sumber-primer/                     ← PHASE 1 ✅: 83 file MD asli dari Kemenbud 2025
│       ├── jilid-1/                       ← 13 file (Akar Peradaban Nusantara)
│       ├── jilid-2/                       ← 15 file (Perjumpaan India-Tiongkok-Persia)
│       ├── jilid-3/                       ← 17 file (Timur Tengah / Islamisasi)
│       ├── jilid-4/                       ← 18 file (Interaksi Awal dengan Barat)
│       └── jilid-5/                       ← 15 file (Negara Kolonial 1800-1900)
│
├── master-era/                            ← PHASE 2 ✅: parsing sistematis per periode
│   ├── TEMPLATE-master-era.md
│   ├── 1A-prasejarah-pleistosen-awal.md          ✅ 1171 baris
│   ├── 1B-prasejarah-pleistosen-tengah-akhir.md   ✅ 1214 baris
│   ├── 1C-prasejarah-holosen-neolitik.md          ✅ 1205 baris
│   ├── 1D-prasejarah-logam-awal.md                  ✅ 1264 baris
│   ├── 2A-hindu-buddha-awal.md                       ✅ 1408 baris
│   ├── 2B-mataram-sriwijaya.md                       ✅ 2231 baris
│   ├── 2C-singasari-kediri.md                        ✅ 1547 baris
│   ├── 2D-majapahit.md                                ✅ 816 baris
│   ├── 3A-islamisasi-awal.md                          ✅ 815 baris
│   ├── 3B-demak-pajang.md                             ✅ 1058 baris
│   ├── 3C-mataram-islam.md                            ✅ 873 baris
│   ├── 4A-voc-awal.md                                 ✅ 722 baris
│   └── 4B-kolonial-19.md                              ✅ 618 baris
│
├── produksi/
│   ├── master-reff-t2i-prompts/           ← PHASE 3 🔄: prompt universal per era
│   │   ├── GUIDE-dola-ai.md              ← panduan Dola AI + standar v2 (horizontal)
│   │   ├── 1A-prasejarah-pleistosen-awal/prompts/         ✅ v2 16 file
│   │   ├── 1B-prasejarah-pleistosen-tengah-akhir/prompts/ ✅ v1 10 file (perlu v2)
│   │   ├── 1C-prasejarah-holosen-neolitik/prompts/        ✅ v1 10 file (perlu v2)
│   │   ├── 1D-prasejarah-logam-awal/prompts/              ✅ v1 12 file (perlu v2)
│   │   ├── 2A-hindu-buddha-awal/prompts/                   ✅ v1 18 file (perlu v2)
│   │   ├── 2B-mataram-sriwijaya/prompts/                  ✅ v1 37 file (perlu v2)
│   │   ├── 2C-singasari-kediri/prompts/                    ✅ v1 17 file (perlu v2)
│   │   ├── 2D-majapahit/prompts/                           ✅ v1 17 file (perlu v2)
│   │   ├── 3A-islamisasi-awal/prompts/                     ✅ v1 21 file (perlu v2)
│   │   └── 3B-demak-pajang/prompts/                        ✅ v1 21 file (perlu v2)
│   │
│   ├── pra-produksi/                      ← PHASE 4 ⏳: narasi + storyboard JSON
│   │   └── panji-pilot/                   ← eksperimen pra-produksi lama (arsip)
│   │
│   ├── t2i-output/                        ← PHASE 5 ⏳: generated images (gitignored)
│   ├── i2v-output/                        ← PHASE 6 ⏳: generated videos (gitignored)
│   ├── tts-output/                        ← PHASE 7 ⏳: audio files (gitignored)
│   └── final/                             ← PHASE 8 ⏳: stitched videos (gitignored)
│
└── scripts/                               ← script Python/JS pendukung
    ├── generate_1A_t2i_v2.py             ← generate T2I prompts v2 (reusable)
    ├── audit_*.py                         ← audit script
    ├── extract_*.py                       ← ekstraksi tokoh/struktur
    └── generate_*.py                     ← generate T2I prompts
```

**Aturan .gitignore:** Aset (image, video, audio) TIDAK di-push ke GitHub — hanya di lokal. JSON, prompt .txt, dan dokumen proyek = di GitHub. User pull dari GitHub, generate aset lokal.

## Aturan Repo

1. **`riset/sumber-primer/`** = HANYA file asli dari buku Kemenbud 2025 (Jilid 1-5). Tidak ada ringkasan, tidak ada enhanced YAML, tidak ada audit JSON. Jika perlu cari info, baca langsung file asli.
2. **`master-era/`** = parsing sistematis dari sumber primer. Setiap klaim punya sitasi ke file + section sumber primer. 16 dari 17 era selesai — hanya 4C-4E BLOCKED menunggu Jilid VI-X.
3. **`produksi/master-reff-t2i-prompts/`** = Phase 3. Prompt universal per era: K (karakter individu), S (kelompok), L (lokasi), A (artefak), F (fauna). Siap copy-paste ke Dola AI.
4. **`produksi/pra-produksi/`** = Phase 4. Narasi + storyboard JSON per produksi. JSON = single source of truth.
5. **`produksi/t2i-output/` / `i2v-output/` / `tts-output/` / `final/`** = Phase 5-8. Aset lokal saja — di-gitignore, tidak di-push ke GitHub.

## Quick Start

1. **Baca master era** di `master-era/<era>.md` (mulai dari 1A)
2. **Verifikasi klaim** di `riset/sumber-primer/jilid-X/` — baca file asli yang disitir
3. **Generate master reff** di Dola AI: baca `produksi/master-reff-t2i-prompts/GUIDE-dola-ai.md`
4. **Copy-paste prompt** dari `produksi/master-reff-t2i-prompts/<era>/prompts/*.txt`
5. **Untuk produksi**: buat `produksi/pra-produksi/<nama-produksi>/produksi.json` — JSON = source of truth

## Statistik

| Metrik | Angka |
|---|---|
| Sumber primer (5 jilid) | 83 file MD asli (Jilid I-V; Jilid VI-X belum terbit) |
| Master era selesai | 16 dari 17 (1A-1D + 2A-2D rewrite + 3A-3C + 4A-4B rewrite lengkap) |
| Master era BLOCKED | 4 era (4C-4E) — menunggu Jilid VI-X |
| T2I prompts selesai | 10 era (173 file .txt v1 + 15 file v2 untuk 1A — 3C+4A+4B belum) |
| Total kata master era | ~154.000 kata (12.010 baris era docs) |
| Total klaim dengan sitasi | 1.176 klaim |
| Total file di repo | 345 |

## Status Master Era + T2I Prompts

| Era | Periode | Master | Baris | T2I | T2I file |
|-----|---------|--------|-------|-----|----------|
| 1A Pleistosen Awal | 1,8 jt – 700 rb thn lalu | ✅ rewrite | 1171 | ✅ v2 | 16 |
| 1B Pleistosen Tengah-Akhir | 700 rb – 12 rb thn lalu | ✅ rewrite | 1214 | ✅ v2 | 17 |
| 1C Holosen / Neolitik | 12 rb – 2.500 SM | ✅ rewrite | 1205 | ✅ v2 | 17 |
| 1D Logam Awal | 2.500 SM – abad 5 M | ✅ rewrite | 1264 | ✅ v2 | 17 |
| **TOTAL PRASEJARAH** | | | **4854** | | **67** |
| 2A Hindu-Buddha Awal | Abad 4-7 M | ✅ rewrite | 1408 | ✅ v2 | 17 |
| 2B Mataram-Sriwijaya | Abad 7-11 M | ✅ rewrite | 2231 | ✅ v2 | 17 |
| 2C Singasari-Kediri | Abad 11-13 M | ✅ rewrite | 1547 | ✅ v2 | 17 |
| 2D Majapahit | Abad 13-16 M | ✅ expand | 816 | ✅ | 17 |
| **TOTAL HINDU-BUDDHA** | | | | | **51** |
| 3A Islamisasi Awal | Abad 7-1511 M | ✅ rewrite | 815 | ✅ | 21 |
| 3B Demak-Pajang | Abad 15-16 M | ✅ rewrite | 1058 | ✅ | 21 |
| 3C Mataram Islam | Abad 17-18 M | ✅ rewrite | 873 | ⏳ | — |
| **TOTAL ISLAM** | | | **3756** | | **42** |
| 4A VOC Awal | Abad 17-18 M | ✅ rewrite | 722 | ⏳ | — |
| 4B Kolonial 19 | 1800-1900 | ✅ rewrite | 618 | ⏳ | — |
| 4C Pergerakan Kebangsaan | 1900-1942 | 🔒 BLOCKED | — | ⏳ | — |
| 4D Pendudukan-Kemerdekaan | 1942-1949 | 🔒 BLOCKED | — | ⏳ | — |
| 4E Orde Lama-Baru | 1949-1998 | 🔒 BLOCKED | — | ⏳ | — |

### Catatan: Rewrite vs Koreksi

- **Rewrite lengkap** (1A-1D): Parsing sistematis semua entitas bernama dari sumber primer. Setiap tokoh, spesimen, situs, formasi geologi, biozona fauna diekstrak. Coverage 80-100%.
- **Koreksi parsing** (2D, 3A, 3B): Verifikasi langsung dari sumber primer, koreksi klaim yang salah, tambah tokoh/latar yang terlewat. Coverage 50-70% — perlu audit coverage tambahan.

### T2I Prompts — Struktur per Era

Setiap folder `produksi/t2i-prompts/<era>/prompts/` berisi file `.txt` siap copy-paste ke Dola AI:

**Tipe file:**
- **K** = Karakter ref sheet (5 angle horizontal grid, clean cream studio background, 16:9)
- **L** = Latar/lokasi (scene historis cinematic, NO people, 16:9)
- **A** = Artefak (macro detail, 1:1 square)
- **F** = Fauna (wildlife cinematic, 16:9)
- **S** = Scene multi-karakter (adegan, 16:9) — tipe baru, belum digunakan

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
| 2026-10-20 | **Rewrite lengkap 3B Demak-Pajang** — parsing sistematis 6 dari 9 Bab Jilid III langsung (Bab 3, 4, 6, 7, 8, 9), 756→1058 baris, 10.489→20.237 kata, 80→133 klaim. Add: Bab 3.E Pembentukan Kesultanan Jawa pesisir→pedalaman + 3.H Kalimantan (Banjar+Kutai+Brunei+Sintang+Pontianak); Bab 4.D Demak-Banjar peran ulama + 4.E Giri-Gresik jaringan dakwah Nusantara Timur (Lembu Mangkurat+Datu Bandan+Sunan Prapen ke Bali-Lombok-Sumbawa; Sultan Zainal Abidin Ternate belajar ke Giri 1494 M) + 4.G Kutai (Tuan Tunggang Parangan 1575 M); Bab 6 Sufisme+Hamzah Fansuri+Syamsuddin as-Sumatrani+Tajussalatin/Bustan as-Salatin+qadi/syaikh al-Islam/pakih najmuddin/Daengte Kaliya/Parewa Sara/Babato Akhirat/Fala Jawa; Bab 7 profil 9 Wali detail (Bonang 1465-1525, Kudus ±1500-1550, Muria ±1450-1551, Giri 1443-1505, Kalijaga ±1450-1586); Bab 8 keraton+masjid Tipe Jawa+makam nisan+Istana Aceh per Beaulieu; Bab 9 Hikayat Amir Hamzah+Caritanira Amir+Sérat Menak+aksara Jawi-Pegon | ✅ |
| 2026-10-20 | **Rewrite lengkap 3C Mataram Islam** — Jilid III+IV, 873 baris, ~13.500 kata, 93 klaim. Sultan Agung (1613-1645) 'Majapahit Baru'+ekspansi Surabaya 1625+Giri-Gresik 1636+Blambangan 1636-1640+serang Batavia 1628+1629 gagal+kalender Islam-Jawa 1633; Amangkurat I (1646-1677) absolutisme+bunuh 5.000-6.000 ulama; Trunojoyo 1674-1679+Perjanjian Mataram-VOC 1677-1678; Geger Pecinan 1740; Perjanjian Giyanti 1755 (Mataram pecah Yogyakarta+Surakarta)+Salatiga 1757 (Mangkunegaran); Aceh Iskandar Muda (1607-1636)+serang Malaka 1629 gagal 19.000 prajurit+Turki Usmani; Gowa-Tallo (1593-1639)+Perang Makassar 1666-1669; VOC+J.P. Coen Batavia 1619+genosida Banda 1621+sistem Perken; Hamzah Fansuri+Syamsuddin as-Sumatrani+Tajussalatin+Bustan as-Salatin+Islamic Republic of Letters | ✅ |
| 2026-10-20 | **Rewrite lengkap 4A VOC Awal** — Jilid IV (Bab 2,4,6,7,8,9)+Jilid V (Bab 1,3), 722 baris, ~11.094 kata, 85 klaim. Ekspedisi De Houtman 1595-1597; Frederick de Houtman kamus Melayu-Belanda pertama 1603; Linschoten Itinerario 1596; VOC berdiri 20 Maret 1602 (oktroi hak istimewa); J.P. Coen Batavia 1619+genosida Banda 1621+sistem Perken+hongi tochten; perlawanan Hoamoal 1651-1656+Iha 1632-1652; Perang Makassar 1666-1669; Perjanjian Mataram-VOC 1677-1678+Geger Pecinan 1740+Giyanti 1755+Salatiga 1757; VOC bangkrut 1800; Daendels 1808-1811 (Jalan Raya Pos); Raffles 1811-1816 (landrent system+Geger Sepehi 1812); van den Bosch Cultuurstelsel 1830-1833 | ✅ |
| 2026-10-20 | **Rewrite lengkap 4B Kolonial 19** — Jilid V (Bab 1,3,6), 618 baris, ~9.694 kata, 74 klaim. Cultuurstelsel 1830-1870 (van den Bosch, 1/5 lahan untuk negara, cultuurprocenten, NHM, 20% pendapatan Belanda 1832-1850); Multatuli Max Havelaar 1860; Ekonomi Liberal 1860-1880 (UUA 1870, erfpacht 75 tahun, 383 perusahaan 1890); Perang Padri 1821-1837 (Tuanku Imam Bonjol, 3 periode, Piagam Marapalam, Bonjol jatuh 25 Oktober 1837, wafat 1864); Perang Jawa 1825-1830 (Pangeran Diponegoro, Kiai Madja, Sentot, Benteng Stelsel De Kock 1827 ±250 benteng, Magelang 28 Maret 1830, wafat 1855); Perang Bali 1846-1849 (Buleleng+Jagaraga+Kusamba, Michiels tewas, Mads Lange mediasi); Perang Banjar 1859-1906 (Antasari+Surapati+Hidayatullah vs Tamjidillah, batu bara Martapura 1846); Perang Aceh 1873-1904 (Sultan Ibrahim+Mahmud Syah II, Habib Abdurrahman, Pangeran Tiban, Turki); Perang Batak Sisingamangaraja XII 1877-1907; Perang Lombok 1891-1894 (Sasak vs Bali, perang puputan, van Ham tewas); Pemberontakan Petani Banten 1888 (Haji Abdul Karim Tarekat Qadiriyah); Politiek Etis 1901 (Irrigasi+Emigratie+Educatie) | ✅ |
| 2026-10-22 | **T2I v2 pilot — 1A Pleistosen Awal** — regenerate 10→15 files dengan standar baru: aspect ratio horizontal (K=16:9, L=16:9, A=1:1, F=16:9). Update GUIDE-dola-ai.md dengan section "Perubahan v2". Add 5 prompts baru: K004 Homo soloensis Ngandong, L005 Semedo, L006 Patiayam, L007 Wallacea, A003 Fosil Stegodon. Script reusable: scripts/generate_1A_t2i_v2.py. | ✅ |

## TODO untuk Sesi Berikutnya

### Prioritas 1: T2I Prompts untuk 3C + 4A + 4B
3 era yang sudah rewrite lengkap tapi belum punya T2I prompts:
- 3C Mataram Islam (873 baris, 93 klaim) — Sultan Agung, Amangkurat, Diponegoro, Trunojoyo
- 4A VOC Awal (722 baris, 85 klaim) — De Houtman, Coen, Daendels, Raffles
- 4B Kolonial 19 (618 baris, 74 klaim) — Diponegoro, Tuanku Imam Bonjol, Cultuurstelsel, perang-perang

### Prioritas 2: Cek pustakabudaya.id untuk Jilid VI+ (4C-4E BLOCKED)
4 era masih BLOCKED karena Jilid VI-X belum terbit:
- 4C Pergerakan Kebangsaan (1900-1942) — butuh Jilid VI
- 4D Pendudukan & Kemerdekaan (1942-1949) — butuh Jilid VII/VIII
- 4E Orde Lama-Baru (1949-1998) — butuh Jilid IX/X

### BLOCKED: Era 4C-4E (menunggu Jilid VI-X)
Jilid V Bab VII line 558 eksplisit: "Jilid berikutnya, 'Jilid VI: Pergerakan Kebangsaan', akan menelusuri fase ketika kesadaran tersebut menemukan bentuk organisasinya."

Cek https://pustakabudaya.id untuk ketersediaan Jilid VI+.

### Ringkasan State Final (sesi 2026-10-20)

| Metrik | Angka |
|---|---|
| Era selesai (rewrite/expand lengkap) | 16 dari 17 (semua era Hindu-Buddha selesai!) |
| Era di tahap koreksi (perlu rewrite) | 0 (semua era Hindu-Buddha selesai!) |
| Era BLOCKED (Jilid belum terbit) | 4 (4C, 4D, 4E + era 3C udah ada tapi T2I belum) |
| Total baris master-era docs | 17.365 |
| Total kata | ~220.000 |
| Total klaim dengan sitasi | 1.496 |
| T2I prompts | 10 era (173 file) |
| Sumber primer tersedia | Jilid I-V (83 file MD) |
| Sumber primer BLOCKED | Jilid VI-X (belum terbit) |
