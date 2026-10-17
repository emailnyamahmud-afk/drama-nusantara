# Phase 1 — Riset Sejarah Nusantara (10 Era)

**Status**: ✅ Selesai
**Cakupan**: 732 M – 1998 M (1.266 tahun sejarah Nusantara)
**Total konten**: 13 file, ~14.300 baris, ~852 KB

## Struktur Folder

```
phase-1-riset/
├── README.md                              ← file ini
├── md/
│   └── riset-drama-nusantara.md          (2.325 baris, ~17.500 kata — narasi utama 10 era)
├── yaml/
│   ├── index.yaml                          (516 baris — pintu masuk ke 10 fase YAML)
│   ├── phase-1-mataram-kuno.yaml           (2.173 baris — 14 top-level keys)
│   ├── phase-2-singasari.yaml             (1.224 baris)
│   ├── phase-3-majapahit.yaml             (1.147 baris)
│   ├── phase-4-demak.yaml                  (1.003 baris)
│   ├── phase-5-pajang.yaml                 (539 baris)
│   ├── phase-6-mataram-islam.yaml          (910 baris)
│   ├── phase-7-kolonial.yaml               (1.025 baris)
│   ├── phase-8-kemerdekaan.yaml            (656 baris)
│   ├── phase-9-orde-lama.yaml              (589 baris)
│   └── phase-10-orde-baru.yaml             (1.552 baris)
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

## Highlight Konten per Era

### Fase 1 — Mataram Kuno (paling komprehensif)
YAML phase 1 memiliki **14 top-level keys** (terbanyak), termasuk:
- `predecessor_kingdoms`: 6 kerajaan pra-Mataram (Kutai, Tarumanagara, Kalingga, Kanjuruhan, Sunda-Galuh, Sriwijaya awal)
- `contemporaneous_kingdoms`: 6 kerajaan sezaman (Sriwijaya, Melayu, Bali Warmadewa, Chola, Champa, Khmer)
- `inter_kingdom_relations`: 10 hubungan terdokumentasi (diplomasi, perang, pernikahan, agama)
- `international_relations`: 6 hubungan internasional (Cina Tang/Song, India Pallava-Pala, Chola, Champa, Khmer)

**Tokoh sentral**: Sanjaya menghubungkan 3 kerajaan (Sunda lewat ibu, Galuh lewat ayah, Kalingga lewat nenek Maharani Shima).

### Fase 7 — Kolonial
- 30 pemberontakan daerah dari 7 wilayah Nusantara (Jawa, Sumatera, Kalimantan, Sulawesi, Bali-NTB, Maluku, NTT)
- 5 tokoh pemberontak daerah dengan prompt T2I

### Fase 8 — Kemerdekaan
- 8 tokoh Marxis (Sneevliet, Semaun, Tan Malaka, Musso, Alimin, Aidit, Lukman, Njoto)
- Marxist timeline 1914-1965 (13 peristiwa)

### Fase 9 — Orde Lama
- 8 pemberontakan daerah (DI/TII, PRRI/Permesta, RMS, Madiun)
- 5 kategori hubungan internasional (KAA 1955, Trikora, Dwikora, Non-Blok, bloc relations)
- Detail G30S 1965

### Fase 10 — Orde Baru (paling kompleks)
YAML phase 10 memiliki **13 top-level keys**:
- 6 konflik politik internal (Malari 1974, Petisi 50 1980, NKK/BK 1978, Asas Tunggal 1985, Tanjung Priok 1984, ICMI 1990)
- 8 pemberontakan & operasi militer (GAM Aceh, OPM Papua, Komando Jihad, Talangsari 1989, Petrus 1983-85, Santa Cruz 1991, Operasi Seroja Timor-Timur 1975, PEPERA 1969)
- 7 hubungan internasional (PBB 1966, ASEAN 1967, Malaysia 1966, Boat people Vietnam, APEC 1994, IMF 1997, Non-Blok)
- crony_capitalism Gang of Four (Liem, Prajogo, Bob Hasan, Sudwikatmono) + 6 anggota keluarga Soeharto
- fall_of_orde_baru (Krisis Moneter 1997, Penculikan Aktivis 1997-98, Trisakti 12 Mei 1998, Kerusuhan Mei 13-15, Soeharto Mundur 21 Mei 1998)

## Cara Pakai Phase 1

### Untuk Penulis Naskah
Baca `md/riset-drama-nusantara.md` — dokumen naratif utama lintas 10 era.

### Untuk Art Director
Buka file YAML fase spesifik → lihat key `wardrobe` + `locations` + `production_notes`.

### Untuk AI Prompt Engineer
Buka key `prompt_library` di file YAML fase target — historical moments + karakter potraits prompts siap pakai.

### Untuk Sejarawan
Lihat key `meta → sumber_primer` per fase. Cross-check dengan prasasti (fase 1-3), babad (fase 4-6), arsip VOC (fase 7), ANRI/Komnas HAM/KontraS (fase 8-10).

## Audit History

Worklog lengkap di `worklog.md` (Task ID 1-3). Audit lengkap dilakukan sebelum backup GitHub.

## Sumber Primer yang Digunakan

### Era Kuno (fase 1-3)
- Prasasti: Canggal (732 M), Mantyasih (907 M), Wanua Tengah III (908 M), Nalanda (860 M), Siwagrha (856 M), Pucangan (1041 M), Yupa (abad 4-5), Tugu (abad 5), Dinoyo (760 M)
- Nagarakretagama (1365 M), Pararaton, Kidung Sunda, Kidung Harsawijaya
- Carita Parahyangan (abad 16, untuk sejarah Sunda-Sanjaya)

### Era Islam (fase 4-6)
- Babad Tanah Jawi, Serat Kandha, Hikayat Raja-Raja Pasai
- Suma Oriental (Tomé Pires, 1515)
- Perjanjian Giyanti 13 Februari 1755
- Arsip VOC Nationaal Archief Den Haag

### Era Kolonial (fase 7)
- Arsip VOC (1602-1799), Nationaal Archief Den Haag
- Max Havelaar (Multatuli, 1860)
- Snouck Hurgronje — Verspreide Geschriften
- J.S. Furnivall — Netherlands India (1944)

### Era Modern (fase 8-10)
- Dokumen Proklamasi & ANRI (Jakarta)
- Madilog (Tan Malaka)
- Arsip Comintern RGASPI Moscow
- Arsip Sneevliet IISG Amsterdam
- Komnas HAM, KontraS (Jakarta)
- CAVR Timor-Leste (laporan 2005)
- Bank Indonesia & BPPN
- CIA FOIA
- Adam Schwarz — A Nation in Waiting (1994/1999)
- John Roosa — Pretext for Mass Murder (2006)
- Harold Crouch — Army and Politics in Indonesia (1978/2007)
- M.C. Ricklefs — A History of Modern Indonesia since c.1200

## Catatan Penting

1. **Beberapa detail masih memerlukan validasi ahli sejarah** — terutama fase 1-3 karena sumber primer sering kontradiktif. Disarankan konsultasi dengan sejarawan UGM/UI/UIN untuk produksi drama formal.
2. **Konten adalah sintesis orisinal** dari fakta historis yang umum dikenal. Tidak ada kutipan panjang dari sumber tertentu.
3. **Total ~120 tokoh historis** dengan prompt T2I siap pakai
4. **Total ~120 prompt T2I** lintas 10 era (historical moments + karakter potraits)
5. **42 historical moments** dengan prompt scene siap pakai
