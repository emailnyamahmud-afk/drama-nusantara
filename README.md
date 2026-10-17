# Riset Drama Nusantara — 10 Era

Dokumen riset komprehensif untuk produksi drama historis Nusantara lintas-zaman: dari Mataram Kuno (732 M) hingga Orde Baru (1998 M). Materi dipecah menjadi (1) dokumen MD naratif tunggal untuk penulis naskah, (2) 10 file YAML master per fase untuk database T2I prompt generation.

## Struktur Folder

```
riset-backup/
├── README.md                              ← file ini (navigasi)
├── md/
│   └── riset-drama-nusantara.md          (2325 baris, ~17.500 kata — narasi utama)
├── yaml/
│   ├── index.yaml                          (516 baris — pintu masuk ke 10 fase)
│   ├── phase-1-mataram-kuno.yaml           (2173 baris — incl. 4 keys baru: predecessor_kingdoms, contemporaneous_kingdoms, inter_kingdom_relations, international_relations)
│   ├── phase-2-singasari.yaml             (1224 baris)
│   ├── phase-3-majapahit.yaml             (1147 baris)
│   ├── phase-4-demak.yaml                  (1003 baris)
│   ├── phase-5-pajang.yaml                 (539 baris)
│   ├── phase-6-mataram-islam.yaml          (910 baris)
│   ├── phase-7-kolonial.yaml               (1025 baris)
│   ├── phase-8-kemerdekaan.yaml            (656 baris)
│   ├── phase-9-orde-lama.yaml              (589 baris)
│   └── phase-10-orde-baru.yaml             (1552 baris)
└── worklog.md                              (638 baris — Task ID 1-3 audit history)
```

## Ringkasan 10 Era

| # | Era | Periode | File YAML | Baris |
|---|-----|---------|-----------|-------|
| 1 | Mataram Kuno | 732-1016 M | phase-1-mataram-kuno.yaml | 2.173 |
| 2 | Singasari | 1222-1292 M | phase-2-singasari.yaml | 1.224 |
| 3 | Majapahit | 1293-1527 M | phase-3-majapahit.yaml | 1.147 |
| 4 | Demak | 1475-1548 M | phase-4-demak.yaml | 1.003 |
| 5 | Pajang | 1568-1587 M | phase-5-pajang.yaml | 539 |
| 6 | Mataram Islam | 1587-1755 M | phase-6-mataram-islam.yaml | 910 |
| 7 | Kolonial | 1602-1942 M | phase-7-kolonial.yaml | 1.025 |
| 8 | Kemerdekaan | 1945-1949 M | phase-8-kemerdekaan.yaml | 656 |
| 9 | Orde Lama | 1950-1965 M | phase-9-orde-lama.yaml | 589 |
| 10 | Orde Baru | 1966-1998 M | phase-10-orde-baru.yaml | 1.552 |
| **Total** | | **732 M – 1998 M (1.266 tahun)** | **10 file + index** | **~14.300** |

## Highlight Konten

### Fase 1 — Mataram Kuno (paling komprehensif)
YAML phase 1 memiliki 14 top-level keys (terbanyak), termasuk:
- `predecessor_kingdoms`: 6 kerajaan pra-Mataram (Kutai, Tarumanagara, Kalingga, Kanjuruhan, Sunda-Galuh, Sriwijaya awal)
- `contemporaneous_kingdoms`: 6 kerajaan sezaman (Sriwijaya, Melayu, Bali Warmadewa, Chola, Champa, Khmer)
- `inter_kingdom_relations`: 10 hubungan terdokumentasi (diplomasi, perang, pernikahan, agama)
- `international_relations`: 6 hub. internasional (Cina Tang/Song, India Pallava-Pala, Chola, Champa, Khmer)

### Fase 7 — Kolonial
YAML phase 7 mencakup 30 pemberontakan daerah dari 7 wilayah Nusantara (Jawa, Sumatera, Kalimantan, Sulawesi, Bali-NTB, Maluku, NTT) + rebellion_characters dengan 5 tokoh pemberontak daerah.

### Fase 8 — Kemerdekaan
YAML phase 8 mencakup 8 tokoh Marxis (Sneevliet, Semaun, Tan Malaka, Musso, Alimin, Aidit, Lukman, Njoto) + marxist_timeline 1914-1965 (13 peristiwa).

### Fase 9 — Orde Lama
YAML phase 9 mencakup 8 pemberontakan daerah (DI/TII, PRRI/Permesta, RMS, Madiun) + 5 kategori hubungan internasional (KAA 1955, Trikora, Dwikora, Non-Blok, bloc relations) + detail G30S 1965.

### Fase 10 — Orde Baru (paling kompleks)
YAML phase 10 memiliki 13 top-level keys:
- 6 konflik politik internal (Malari 1974, Petisi 50 1980, NKK/BK 1978, Asas Tunggal 1985, Tanjung Priok 1984, ICMI 1990)
- 8 pemberontakan & operasi militer (GAM Aceh, OPM Papua, Komando Jihad, Talangsari 1989, Petrus 1983-85, Santa Cruz 1991, Operasi Seroja Timor-Timur 1975, PEPERA 1969)
- 7 hubungan internasional (PBB 1966, ASEAN 1967, Malaysia 1966, Boat people Vietnam, APEC 1994, IMF 1997, Non-Blok)
- crony_capitalism Gang of Four (Liem, Prajogo, Bob Hasan, Sudwikatmono) + 6 anggota keluarga Soeharto
- fall_of_orde_baru (Krisis Moneter 1997, Penculikan Aktivis 1997-98, Trisakti 12 Mei 1998, Kerusuhan Mei 13-15, Soeharto Mundur 21 Mei 1998)

## Cara Pakai

### Untuk Penulis Naskah
Baca `md/riset-drama-nusantara.md` — dokumen naratif utama lintas 10 era.

### Untuk Art Director
Buka file YAML fase spesifik → lihat key `wardrobe` + `locations` + `production_notes`.

### Untuk AI Prompt Engineer
Buka key `prompt_library` di file YAML fase target — historical moments + karakter potraits prompts siap pakai.

### Untuk Sejarawan
Lihat key `meta → sumber_primer` per fase. Cross-check dengan prasasti (fase 1-3), babad (fase 4-6), arsip VOC (fase 7), ANRI/Komnas HAM/KontraS (fase 8-10).

## Audit History

Lihat `worklog.md` untuk detail Task ID 1-3. Audit lengkap (Task ID 1-20) dilakukan sebelum backup — beberapa task ID 4-20 tidak tercatat di worklog ini karena sandbox reset.

## Catatan

- **Bahasa**: Bahasa Indonesia
- **Update terakhir**: 17 Oktober 2026
- **Versi**: 1.0
- **Total file**: 13 (1 MD + 11 YAML + 1 worklog)
- **Total ukuran**: ~852 KB

---

Backup ini dikirim ke GitHub dari sandbox Z.ai yang tidak permanen. Untuk pengembangan lebih lanjut, clone repo ini ke lingkungan lokal.
