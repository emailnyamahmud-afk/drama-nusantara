# Progres Project — Drama Nusantara

> **Tujuan file ini**: Progress tracker per sesi. Sandbox Z.ai bisa reset kapan saja — file ini + README + GitHub = memori permanen.
> **Aturan**: Update file ini di akhir setiap sesi sebelum push GitHub.

---

## Sesi Terakhir: 2026-10-21 (Sesi 3 — BERLANGSUNG)

### Yang sudah dikerjakan sesi ini:
- ✅ Cek sync sandbox ↔ GitHub: ✅ SINKRON (HEAD: `9b3649d`)
- ✅ Buat file `progres-project.md` (progress tracker per sesi)
- ✅ Fix file refs di 2A-2C: bare refs (`08-bab-3.md`) → prefixed (`jilid-2/08-bab-3.md`)
- ✅ Baca semua Bab Jilid II untuk persiapan rewrite 2A-2C:
  - Bab 1: Perjumpaan awal (religi pra-Hindu, penguburan, gunung sebagai orientasi, arwah nenek moyang, monumen tegak, interaksi budaya asing)
  - Bab 2: Aksara Brahmi Akhir/Pallawa + Hindu di Nusantara (Wolters localization, Pollock Sanskrit Cosmopolis, Acri) + Buddha di Nusantara (konsep dasar, candi/stupa/wihara, stupika+dharani, percandian Buddha Nusantara)
  - Bab 3: Kutai (Yupa, Mulawarman, Hindu Awal/Weda) + Tarumanagara (Purnawarman, 5 prasasti, kanal Gomati-Candrabhaga) + Kan-to-li (Varanarendra, Saba-la-na-lin-da, 455-563 M) + Malayu awal + Ho Ling + Sriwijaya (Dapunta Hyang, siddhayatra, Kedatuan federasi, mandala, kemunduran Chola)
  - Bab 4: Orang asing di Nusantara (India, Persia, Arab, Tiongkok — pengaturan pajak)
  - Bab 5: Maritim (Austronesia 5000 SM, Ko Ying, Si Tao, Barus) + agrikultur + literasi (Yupa, Pallawa, Kawi, Yijing di Sriwijaya)
- ✅ Commit + push: `c1ce21d` (progres-project.md + fix file refs)

### Yang tersisa untuk sesi ini / sesi berikutnya:
- 🔄 Rewrite 2A Hindu-Buddha Awal — bahan sudah dibaca semua, tinggal tulis file
- ⏳ Rewrite 2B Mataram-Sriwijaya
- ⏳ Rewrite 2C Singasari-Kediri
- ⏳ T2I prompts untuk 3C+4A+4B
- 🔒 BLOCKED: 4C-4E (Jilid VI belum terbit)

---

## Riwayat Sesi

### Sesi 1: 2026-10-17 → 2026-10-19
- Setup repo, struktur folder, baca Jilid I-V
- Tulis master era 1A-2D + T2I prompts (10 era, 173 file)
- Audit + bersihkan 97 file T2I

### Sesi 2: 2026-10-20
- Rewrite lengkap 1A-1D (prasejarah) — pola parsing sistematis
- Expand 2D Majapahit + audit halu (4 halu fixed)
- Rewrite lengkap 3A (Islamisasi Awal) + 3B (Demak-Pajang) + 3C (Mataram Islam)
- Rewrite lengkap 4A (VOC Awal) + 4B (Kolonial 19)
- Update dokumentasi: BLOCKED 4C-4E (Jilid VI belum terbit)
- **Total akhir sesi 2**: 13 era selesai, ~154.000 kata, 1.176 klaim

### Sesi 3: 2026-10-21 (sesi ini — BERLANGSUNG)
- Cek sync sandbox ↔ GitHub: ✅ sinkron
- Buat `progres-project.md`
- Fix file refs di 2A-2C (tambah prefix `jilid-2/`)
- Baca semua Bab Jilid II untuk persiapan rewrite 2A-2C
- Commit: `c1ce21d` (progres-project.md + fix file refs)
- **SEDANG MENGERJAKAN**: Rewrite 2A — bahan sudah dibaca, siap tulis

---

## State Saat Ini

| Era | Status | Baris | Klaim | T2I | Catatan |
|-----|--------|-------|-------|-----|---------|
| 1A | ✅ rewrite | 1171 | 83 | ✅ 10 | |
| 1B | ✅ rewrite | 1214 | 47 | ✅ 10 | |
| 1C | ✅ rewrite | 1205 | 57 | ✅ 10 | |
| 1D | ✅ rewrite | 1264 | 84 | ✅ 12 | |
| 2A | 🔄 rewrite | 831 | 45 | ✅ 18 | BAHAN SUDAH DIBACA — SIAP TULIS |
| 2B | 🔄 rewrite | 805 | 45 | ✅ 37 | BERIKUTNYA SETELAH 2A |
| 2C | 🔄 rewrite | 519 | 41 | ✅ 17 | BERIKUTNYA SETELAH 2B |
| 2D | ✅ expand | 816 | 112 | ✅ 17 | Audit halu: 4 fixed |
| 3A | ✅ rewrite | 815 | 136 | ✅ 21 | |
| 3B | ✅ rewrite | 1058 | 133 | ✅ 21 | |
| 3C | ✅ rewrite | 873 | 93 | ⏳ | T2I belum |
| 4A | ✅ rewrite | 722 | 85 | ⏳ | T2I belum |
| 4B | ✅ rewrite | 618 | 74 | ⏳ | T2I belum |
| 4C | 🔒 BLOCKED | — | — | — | Jilid VI belum terbit |
| 4D | 🔒 BLOCKED | — | — | — | Jilid VII/VIII belum terbit |
| 4E | 🔒 BLOCKED | — | — | — | Jilid IX/X belum terbit |

---

## Catatan Penting untuk AI Sesi Berikutnya

1. **Baca 3 file ini dulu**: `README.md` (konteks project) → `progres-project.md` (progress) → `worklog.md` (detail task)
2. **Cek sync sandbox ↔ GitHub** dengan `git fetch origin && git rev-parse HEAD && git rev-parse origin/main`
3. **Token PAT**: cek apakah masih valid. Kalau tidak → minta user PAT baru
4. **Jilid VI**: cek `ls riset/sumber-primer/jilid-6/` — kalau ada, mulai era 4C
5. **Aturan emas**: setiap klaim harus punya sitasi sumber primer (file+section+line). Tidak boleh ada klaim tanpa sumber. Tidak boleh ada halu (tahun/nama yang tidak ada di sumber primer).
6. **Push GitHub wajib di akhir sesi** — sandbox bisa reset kapan saja
7. **File refs**: selalu pakai prefix `jilid-X/` (contoh: `jilid-2/08-bab-3.md`), bukan bare refs (`08-bab-3.md`)
8. **Rewrite 2A-2C**: bahan Jilid II sudah dibaca di sesi 3. Bab yang relevan:
   - 2A: Bab 1 (perjumpaan awal) + Bab 2 (aksara+Hindu+Buddha) + Bab 3.A.1 (Kutai+Taruma+Kan-to-li+Ho Ling+Sriwijaya awal) + Bab 4 (orang asing) + Bab 5 (maritim+agrikultur+literasi)
   - 2B: Bab 3.B (Mataram+Kanjuruhan+Bali Kuno+Sriwijaya puncak) + Bab 5 (puncak pencapaian) + Bab 6 (keruntuhan)
   - 2C: Bab 3 (lanjutan: Singasari+Kediri) + Bab 5 (sastra+literasi) + Bab 6 (keruntuhan)
