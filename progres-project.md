# Progres Project — Drama Nusantara

> **Tujuan file ini**: Progress tracker per sesi. Sandbox Z.ai bisa reset kapan saja — file ini + README + GitHub = memori permanen.
> **Aturan**: Update file ini di akhir setiap sesi sebelum push GitHub.

---

## Sesi Terakhir: 2026-10-21 (Sesi 3)

### Yang dikerjakan:
- Cek sync sandbox ↔ GitHub: ✅ SINKRON (HEAD: `9b3649d`)
- Buat file `progres-project.md` ini
- Mulai rewrite 2A-2C (3 era Hindu-Buddha yang masih di tahap "koreksi")

### Yang tersisa untuk sesi berikutnya:
- Lanjut rewrite 2A-2C (atau cek apakah sudah selesai di sesi ini)
- Kalau 2A-2C selesai → T2I prompts untuk 3C+4A+4B
- Kalau Jilid VI sudah terbit → cek pustakabudaya.id → mulai era 4C

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

### Sesi 3: 2026-10-21 (sesi ini)
- Cek sync sandbox ↔ GitHub: ✅ sinkron
- Buat `progres-project.md`
- Mulai rewrite 2A-2C

---

## State Saat Ini (update实时 saat sesi berjalan)

| Era | Status | Baris | Klaim | T2I | Catatan |
|-----|--------|-------|-------|-----|---------|
| 1A | ✅ rewrite | 1171 | 83 | ✅ 10 | |
| 1B | ✅ rewrite | 1214 | 47 | ✅ 10 | |
| 1C | ✅ rewrite | 1205 | 57 | ✅ 10 | |
| 1D | ✅ rewrite | 1264 | 84 | ✅ 12 | |
| 2A | 🔄 rewrite | 831 | 45 | ✅ 18 | SEDANG DIKERJAKAN |
| 2B | 🔄 rewrite | 805 | 45 | ✅ 37 | SEDANG DIKERJAKAN |
| 2C | 🔄 rewrite | 519 | 41 | ✅ 17 | SEDANG DIKERJAKAN |
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
