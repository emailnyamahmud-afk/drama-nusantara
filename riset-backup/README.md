# 🎬 Drama Nusantara — Repository Utama

Dokumen riset, naskah, dan produksi untuk drama historis Nusantara lintas-zaman: dari Mataram Kuno (732 M) hingga Orde Baru (1998 M).

## 🗺️ Roadmap 4-Phase

```
Phase 1: Riset Sejarah          ✅ Selesai
   ↓
Phase 2: Naskah & Storyboard    ⏳ Pending
   ↓
Phase 3: LoRA Assets            ⏳ Pending (paralel dengan Phase 2)
   ↓
Phase 4: Produksi (T2I+TTS+I2V)  ⏳ Pending
```

### 📚 Phase 1 — Riset Sejarah Nusantara (10 Era) ✅

**Status**: Selesai (diperkaya dengan 5 jilid buku Kemenbud RI 2025)
**Cakupan**: 732 M – 1998 M (1.266 tahun sejarah Nusantara)
**Konten utama**: 13 file, ~14.300 baris, ~852 KB
**Sumber primer Kemenbud 2025**: 5 jilid, 78 bab, 5.204 halaman, **1.310.456 kata** (9.8 MB markdown)

Lihat: [`phase-1-riset/`](phase-1-riset/README.md)

**Sumber primer Kemenbud 2025** (folder [`phase-1-riset/sumber-primer/kemenbud-2025/`](phase-1-riset/sumber-primer/kemenbud-2025/)):
- Jilid 1: Akar Peradaban Nusantara (prasejarah–300 M)
- Jilid 2: Perjumpaan Budaya India, Tiongkok, Persia (abad 1 SM–16 M) — untuk **Fase 1-3 drama**
- Jilid 3: Timur Tengah (abad 7–16 M) — untuk **Fase 4-6 drama** (Bab 7 Wali Songo wajib baca)
- Jilid 4: Interaksi Awal dengan Barat (abad 16–awal 19 M) — untuk **Fase 6-7 drama** (Sultan Agung vs VOC)
- Jilid 5: Negara Kolonial 1800-1900 — untuk **Fase 7 drama** (Diponegoro, Cultuurstelsel)
- Index mapping: [`sumber-primer/kemenbud-2025-index.yaml`](phase-1-riset/sumber-primer/kemenbud-2025-index.yaml) — memetakan bab buku ke 10 fase drama

Ringkasan 10 era:
| # | Era | Periode |
|---|-----|---------|
| 1 | Mataram Kuno | 732-1016 M |
| 2 | Singasari | 1222-1292 M |
| 3 | Majapahit | 1293-1527 M |
| 4 | Demak | 1475-1548 M |
| 5 | Pajang | 1568-1587 M |
| 6 | Mataram Islam | 1587-1755 M |
| 7 | Kolonial | 1602-1942 M |
| 8 | Kemerdekaan | 1945-1949 M |
| 9 | Orde Lama | 1950-1965 M |
| 10 | Orde Baru | 1966-1998 M |

### ✍️ Phase 2 — Naskah & Storyboard ⏳

**Status**: Belum dimulai
**Tujuan**: Mengubah riset Phase 1 menjadi ratusan ide drama Nusantara, masing-masing dengan naskah + storyboard.yaml siap untuk pipeline produksi.

Lihat: [`phase-2-naskah-storyboard/`](phase-2-naskah-storyboard/README.md)

**9 Drama Anchor (draft)**:
1. Pralaya Mataram (1016 M) — Airlangga lari dari istana terbakar
2. Ken Arok: Tirani & Karma (1222 M) — pengkhianatan suci
3. Peristiwa Bubat (1357 M) — Gajah Mada vs Pajajaran
4. Walisongo: Sembilan Cahaya (1475-1548 M) — Islamisasi Jawa lewat budaya
5. Sultan Agung Serang Batavia (1628-1629 M) — heroisme tragis
6. Pangeran Diponegoro (1825-1830 M) — perang sufi melawan Belanda
7. Proklamasi (1945 M) — Soekarno-Hatta, harapan & revolusi
8. G30S: Malam Panjang (1965 M) — penculikan 7 jenderal
9. Reformasi: 9 Hari Mei (1998 M) — Trisakti → Soeharto mundur

### 🎨 Phase 3 — LoRA Assets ⏳

**Status**: Belum dimulai (paralel dengan Phase 2)
**Tujuan**: Dataset LoRA untuk karakter, lokasi, dan wardrobe yang dibutuhkan drama-drama.

Lihat: [`phase-3-lora-assets/`](phase-3-lora-assets/README.md)

**Prioritas pertama**: 12 tokoh LoRA (Airlangga, Ken Arok, Ken Dedes, Gajah Mada, Hayam Wuruk, Raden Patah, Sunan Kalijaga, Sultan Agung, Diponegoro, Soekarno, Soeharto, Gus Dur) + 10 lokasi LoRA (Borobudur, Prambanan, Trowulan, Demak Mosque, Keraton Mataram, Yogyakarta 1945, Lubang Buaya, BCA Plaza, Trisakti, Istana Negara).

### 🎬 Phase 4 — Produksi (T2I + TTS + I2V + Compose) ⏳

**Status**: Belum dimulai
**Tujuan**: Pipeline end-to-end mengubah storyboard.yaml menjadi video MP4 final.

Lihat: [`phase-4-produksi/`](phase-4-produksi/README.md)

**Pipeline**:
```
storyboard.yaml → [T2I] → images → [TTS] → voices → [I2V] → clips → [ffmpeg compose] → MP4
```

**Tools**: SDXL/Flux + LoRA (T2I), Edge TTS (voice), LTX-Video/CogVideoX/Kling AI (I2V), ffmpeg (compose).

## 📁 Struktur Folder

```
drama-nusantara/                          ← repo GitHub
├── README.md                              ← file ini
├── .gitignore
├── push-to-github.sh                      ← helper script untuk backup
│
├── phase-1-riset/                        ✅ SELESAI
│   ├── README.md
│   ├── md/
│   │   └── riset-drama-nusantara.md      (2.325 baris)
│   ├── yaml/
│   │   ├── index.yaml                     (516 baris)
│   │   ├── phase-1-mataram-kuno.yaml      (2.173 baris)
│   │   ├── phase-2-singasari.yaml        (1.224 baris)
│   │   ├── phase-3-majapahit.yaml        (1.147 baris)
│   │   ├── phase-4-demak.yaml            (1.003 baris)
│   │   ├── phase-5-pajang.yaml           (539 baris)
│   │   ├── phase-6-mataram-islam.yaml    (910 baris)
│   │   ├── phase-7-kolonial.yaml         (1.025 baris)
│   │   ├── phase-8-kemerdekaan.yaml      (656 baris)
│   │   ├── phase-9-orde-lama.yaml        (589 baris)
│   │   └── phase-10-orde-baru.yaml        (1.552 baris)
│   └── worklog.md                         (638 baris — Task ID 1-3)
│
├── phase-2-naskah-storyboard/            ⏳ PENDING
│   └── README.md                          (struktur + 9 drama anchor draft)
│
├── phase-3-lora-assets/                  ⏳ PENDING
│   └── README.md                          (struktur + 12 tokoh + 10 lokasi prioritas)
│
└── phase-4-produksi/                      ⏳ PENDING
    └── README.md                          (pipeline T2I→TTS→I2V→compose)
```

## 🚀 Cara Pakai Repo Ini

### Untuk Penulis Naskah / Skenario
1. Baca [`phase-1-riset/md/riset-drama-nusantara.md`](phase-1-riset/md/riset-drama-nusantara.md) — narasi utama 10 era
2. Pilih era + tokoh + peristiwa yang ingin diangkat jadi drama
3. (Phase 2) Buat folder `phase-2-naskah-storyboard/drama-XX-nama/` dengan template

### Untuk Art Director
1. Buka file YAML fase spesifik di [`phase-1-riset/yaml/`](phase-1-riset/yaml/)
2. Lihat key `wardrobe` + `locations` + `production_notes`

### Untuk AI Prompt Engineer (T2I)
1. Buka key `prompt_library` di file YAML fase target — historical moments + karakter potraits prompts siap pakai
2. (Phase 3) Train LoRA dengan dataset karakter/lokasi spesifik

### Untuk Sejarawan / Akademisi
1. Telusuri key `meta → sumber_primer` per fase
2. Cross-check dengan:
   - **Era kuno (fase 1-3)**: prasasti, Nagarakretagama, Pararaton
   - **Era Islam (fase 4-6)**: Babad Tanah Jawi, Hikayat, arsip VOC
   - **Era kolonial (fase 7)**: arsip VOC Den Haag, Max Havelaar
   - **Era modern (fase 8-10)**: ANRI, Komnas HAM, KontraS, CIA FOIA, IISG Amsterdam

## 🔐 Setup Backup ke GitHub

PAT (Personal Access Token) disimpan permanen di:
- `/home/z/.git-credentials` (git credential helper)
- `/home/z/my-project/.config/.git-credentials` (backup)

Untuk push update:
```bash
cd /home/z/my-project/riset-backup
bash push-to-github.sh "Pesan commit di sini"
```

## 📋 Audit History

Worklog lengkap di [`phase-1-riset/worklog.md`](phase-1-riset/worklog.md) (Task ID 1-3 audit history).

## 🌐 Info Repo

- **URL**: https://github.com/emailnyamahmud-afk/drama-nusantara
- **Visibility**: Public
- **Branch**: `main`
- **Bahasa**: Bahasa Indonesia
- **Update terakhir**: 17 Oktober 2026
- **Versi**: 1.1 (restrukturisasi 4-phase)
