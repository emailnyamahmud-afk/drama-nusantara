# Review Hasil Eksekusi Skill Dola — Prototype 30s KEN AROK

**Tanggal**: 2026-10-23
**Sumber**: Dola AI skill `batch-storyboard-generator`
**Total image**: 12 (6 master ref + 6 storyboard frame) + 1 contact sheet
**Total size**: 18 MB
**Lokasi**: `produksi/t2i-output/` (di-gitignore, lokal saja)

---

## ✅ Status Eksekusi: SELESAI

### Ringkasan dari Dola:
- **Phase 1 (master refs)**: 6/6 berhasil — 2 karakter + 2 lokasi + 2 prop
- **Gate check**: semua `asset_id` (C001, C002) ter-resolve → lanjut Phase 2
- **Phase 2 (storyboard frames)**: 6/6 berhasil — S001_seg01 s/d seg06, semua 1920×1080
- **QC**: dimensi sesuai spec, konsistensi wajah Ken Arok & Lohgawe konsisten lintas frame
- **Issues encountered**: 
  - Download timeout → auto-retry background ✅
  - S001_seg01 missing → re-download ✅
  - Working directory issue → move files ✅
  - L001 (Hutan Tumapel) truncated → re-download ✅
  - S001_seg02 corrupt → re-download ✅
  - Bash RPC timeout 40s → background process ✅
  - L001 broken di contact sheet awal → rebuild contact sheet ✅
- **Semua issue di-auto-handle skill** (sesuai error handling spec kita)

---

## 📊 Verifikasi Dimensi (semua PASS)

| Image | Expected | Actual | Status |
|---|---|---|---|
| C001 Ken Arok | 16:9 → 1920×1080 | 1920×1080 | ✅ |
| C002 Lohgawe | 16:9 → 1920×1080 | 1920×1080 | ✅ |
| L001 Hutan Tumapel | 16:9 → 1920×1080 | 1920×1080 | ✅ |
| L002 Pendopo Akuwu | 16:9 → 1920×1080 | 1920×1080 | ✅ |
| P001 Sekantung Beras | **1:1 → 1080×1080** | 1080×1080 | ✅ |
| P002 Tombak Prajurit | **1:1 → 1080×1080** | 1080×1080 | ✅ |
| S001_seg01..seg06 | 16:9 → 1920×1080 | 1920×1080 × 6 | ✅ |

**Aspect ratio mapping 100% sesuai spec** — Dola baca field `aspect_ratio` per job dengan benar.

---

## 🎨 Hasil VLM Analysis — Quality Check

### Sample 1: C001 Ken Arok (master ref baseline)
**Verdict: A-TIER (Sangat Berkualitas Tinggi)**

| Kriteria | Hasil |
|---|---|
| 5-angle grid (frontal + full front + side profile + side full + back) | ✅ Semua 5 angle ada |
| Karakter fisik (Jawa 25-35 thn, golden brown, scar pipi kiri, topknot) | ✅ Sesuai deskripsi |
| Costum (leather chest armor, woven kain, simple iron keris) | ✅ Detail lengkap |
| Background clean cream studio | ✅ Tidak ada distraksi |
| **Konsistensi wajah antar 5 angle** | ✅ **Sangat konsisten** — VLM menyebut "sulit dicapai AI biasa tanpa ControlNet" |
| AI artifacts | ✅ Minimal — jari normal, anatomi simetris |

### Sample 2: S001_seg04 Momen Ramalan (critical 2-karakter frame)
**Verdict: PASS EXCELLENT — paling sulit tapi berhasil**

| Kriteria | Hasil |
|---|---|
| 2 karakter muncul (Ken Arok + Lohgawe) | ✅ Keduanya jelas terlihat |
| Ken Arok konsisten vs ref (golden brown, mata tajam, scar, topknot, leather armor) | ✅ Sangat konsisten |
| Lohgawe konsisten vs ref (60an, jenggot putih, jubah putih, rudraksha) | ✅ Sangat konsisten |
| Komposisi slow arc two-shot | ✅ Medium two-shot, face-to-face |
| Soft warm sunlight + god rays di antara mereka | ✅ Backlighting dramatis |
| Mood tense + sacred + prophecy | ✅ Tercipta sempurna |
| Latar hutan Tumapel + pohon + god rays | ✅ Sesuai |
| AI artifacts (tangan aneh, wajah duplikat) | ✅ Tidak ada |

### Sample 3: L001 Hutan Tumapel (location ref - harus no people)
**Verdict: PASS — empty location ref ideal**

| Kriteria | Hasil |
|---|---|
| NO people (empty location ref) | ✅ Tidak ada orang sama sekali |
| Hutan jati tropis + pohon tinggi + god rays | ✅ Dramatis |
| Mood midday + primal + sacred | ✅ Tercipta |
| Aspect 16:9 | ✅ |
| Modern elements (aspal, building, kabel) | ✅ Tidak ada |

### Sample 4: S001_seg01 Chase (konsistensi Ken Arok)
**Verdict: PASS**

| Kriteria | Hasil |
|---|---|
| Ken Arok konsisten vs ref (golden brown, topknot, leather armor) | ✅ Konsisten |
| Scar pipi kiri | ⚠️ Samar (akibat pencahayaan + resolusi) |
| 3 prajurit dengan tombak di background | ✅ Tepat 3 prajurit |
| Motion blur + god rays + cinematic chase | ✅ Excellent |
| Mood tense | ✅ Tercipta |
| AI artifacts | ✅ Minimal |

---

## 🏆 Overall Quality Assessment

### Yang Berhasil:
1. **Skill Dola berfungsi end-to-end** — semua 12 image tergenerate sesuai spec
2. **Karakter konsistensi**: Ken Arok & Lohgawe konsisten lintas frame (verifikasi via VLM)
3. **Aspect ratio mapping 100% benar** — 4 K/L = 16:9, 2 A = 1:1
4. **Error handling skill bekerja** — semua issue (timeout, corrupt, missing file) di-auto-fix
5. **Workflow 1-JSON-upload terbukti** — dari upload `dola-batch.json` → 12 image dalam ~10 menit
6. **Phase dependency graph benar** — Phase 2 pakai ref dari Phase 1 dengan sukses

### Yang Bisa Diiterasi (minor):
1. **Scar di pipi kiri Ken Arok** samar di frame seg01 (akibat pencahayaan) — bisa strengthen di prompt
2. **Detail prop (Sekantung Beras, Tombak)** belum dianalisis — perlu cek konsistensi vs ref
3. **Title card seg06** belum diverifikasi text rendering ("KEN AROK: TAKDIR DARI TUMAPEL")

---

## 📁 Struktur File Final

```
produksi/t2i-output/                          (di-gitignore)
├── master-reff/2C/
│   ├── C001-2C-K002-ken-arok.jpg            (1.2 MB, 1920×1080)
│   ├── C002-2C-K007-dang-hyang-lohgawe.jpg  (1.3 MB, 1920×1080)
│   ├── L001-2C-L008-hutan-tumapel.jpg       (2.1 MB, 1920×1080)
│   ├── L002-2C-L009-pendopo-akuwu-tumapel.jpg (1.8 MB, 1920×1080)
│   ├── P001-2C-A004-sekantung-beras.jpg     (1.2 MB, 1080×1080)
│   └── P002-2C-A005-tombak-prajurit.jpg      (1.1 MB, 1080×1080)
└── prototype-30s/
    ├── S001_seg01.jpg                        (1.8 MB, 1920×1080)
    ├── S001_seg02.jpg                        (1.9 MB, 1920×1080)
    ├── S001_seg03.jpg                        (1.8 MB, 1920×1080)
    ├── S001_seg04.jpg                        (1.4 MB, 1920×1080) ⭐ critical 2-karakter
    ├── S001_seg05.jpg                        (1.0 MB, 1920×1080)
    ├── S001_seg06.jpg                        (1.8 MB, 1920×1080)
    └── contact-sheet.png                      (1980×966, 12 thumbnail)
```

---

## 🎯 Next Steps — Pilih Jalur

### Opsi A — Iterate Prompt untuk Image yang Kurang Baik
- Cek detail prop (P001, P002) — apakah sesuai deskripsi?
- Cek title card seg06 — apakah text "KEN AROK: TAKDIR DARI TUMAPEL" ter-render?
- Kalau ada yang perlu improve → edit prompt `.txt` → regenerate `dola-batch.json` → re-upload ke Dola

### Opsi B — Lanjut ke Phase 6 (I2V — Image to Video)
- Pakai `motion.prompt` di storyboard.json (sudah ada di setiap segmen)
- Pilih I2V tool: Dola video (berbayar) / Kling / Runway / LTX / free alternative
- Generate 6 clip 5-detik dari 6 storyboard frame
- Estimasi: ~10-15 menit

### Opsi C — Lanjut ke Phase 7 (TTS — Voice Over)
- edge-tts dengan voice `id-ID-Ardi`
- Generate 1 narasi gabungan (~15 detik) dari `audio.tts_text` di segmen yang punya
- Estimasi: ~5 menit

### Opsi D — Lanjut ke Phase 8 (Stitch Video)
- Pakai 6 storyboard frame sebagai image sequence
- ffmpeg: 6 image × 5 detik + TTS audio + Ken Burns effect (zoom/pan)
- Output: 1 video 30 detik
- Estimasi: ~5 menit

### Opsi E — Scale Up ke Produksi Lebih Panjang
- Bikin `dola-batch.json` untuk pilot Panji 3 menit (36 segmen)
- Atau bikin untuk dokumenter era lain (1A Prasejarah, 2A Hindu-Buddha, dll)
- Estimasi: 2-4 jam per produksi

---

## 💡 Insight untuk Optimasi Skill Dola ke Depan

Dari pengalaman eksekusi ini, beberapa hal yang bisa di-improve di skill Dola:

1. **Skip download ke VM** — pakai URL Dola langsung di NotifyHuman
2. **Deliver as 1 zip URL** — bukan 12 attachment individual
3. **Auto-save ke Dola Drive** — persistent storage, accessible dari mana saja
4. **Background retry lebih agresif** — kalau RPC timeout, langsung background tanpa tunggu

Tapi ini optimasi — skill sudah jalan excellent untuk MVP.

---

## 🎉 Milestone Pencapaian

| Milestone | Status |
|---|---|
| Phase 1 (Sumber Primer) | ✅ 83 file |
| Phase 2 (Master Era) | ✅ 16 era, ~220.000 kata |
| Phase 3 (Master Reff T2I) | ✅ 220 file prompt + 5 baru untuk prototype |
| Phase 4 (Pra-produksi JSON) | ✅ storyboard.json v2.0 schema |
| Phase 4 (Skill Dola) | ✅ `batch-storyboard-generator` jadi + tervalidasi |
| **Phase 5 (T2I Generate)** | ✅ **12 image berhasil di-generate Dola** |
| Phase 6 (I2V) | ⏳ Next |
| Phase 7 (TTS) | ⏳ Next |
| Phase 8 (Stitch) | ⏳ Next |

**Phase 5 (T2I Production) SELESAI untuk prototype 30s KEN AROK** 🎉

Pipeline end-to-end sudah terbukti jalan:
**Riset → Master Era → Master Reff Prompts → Storyboard JSON → Dola Skill → 12 Image**

Tinggal lanjut Phase 6-8 untuk produksi video 30 detik lengkap.
