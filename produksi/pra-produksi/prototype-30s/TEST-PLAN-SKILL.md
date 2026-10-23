# Test Plan — Eksekusi Skill `batch-storyboard-generator`

**Skill sudah jadi** di Dola environment: `workspace/.user_skills/batch-storyboard-generator/`

**Tujuan file ini**: Panduan step-by-step untuk trigger skill + verifikasi hasil 12 image.

---

## 1. Trigger Skill di Dola AI

### Langkah:
1. Buka Dola AI chat (lanjut sesi yang sama atau sesi baru)
2. Upload file `dola-batch.json` dari:
   ```
   drama-nusantara/produksi/pra-produksi/prototype-30s/dola-batch.json
   ```
3. Ketik pesan:
   ```
   jalankan batch storyboard
   ```
4. Skill `batch-storyboard-generator` harusnya auto-trigger

### Yang harus terjadi di chat Dola:
1. Dola jalankan `parse_batch.py` → print execution plan + dependency map
2. Output parser: "12 job valid, 6 ref phase 1, 6 frame phase 2, all refs resolve"
3. Dola mulai Phase 1 — generate 6 master ref (text-only)
4. Dola gate check — pastikan 6 ref sukses
5. Dola mulai Phase 2 — generate 6 storyboard frame pakai ref dari phase 1
6. Dola QC + bikin contact sheet (montage thumbnail 12 image)
7. Dola deliver — NotifyHuman dengan semua image + folder output

---

## 2. Saat Skill Berjalan — Yang Perlu Diawasi

### Warning signs (tidak masalah):
- Dola mungkin minta konfirmasi sebelum phase 2 → jawab "ya, lanjutkan"
- Dola mungkin generate ref 1 per 1 (sequential) meskipun spec bilang parallel → tidak masalah, cuma lebih lambat
- Dola mungkin tanya preferensi model → jawab "Seedream 4.5"

### Red flags (perlu perhatian):
- ❌ Dola generate semua 12 image tanpa bedakan phase 1 vs phase 2 → skill tidak jalan, manual prompt ulang
- ❌ Dola upload ref image untuk phase 1 (ref tidak punya dependency) → skill salah logic
- ❌ Dola kirim `motion_prompt` ke image_gen → skill abaikan rule "motion_prompt tidak ke image tool"
- ❌ Aspect ratio beda (mis. semua 1:1 atau semua 16:9) → skill tidak baca aspect_ratio per job
- ❌ Job gagal tapi Dola skip → skill tidak ada error recovery

Kalau ada red flag, share screenshot ke Z.ai untuk diagnose.

---

## 3. Setelah Skill Selesai — Verifikasi 12 Image

### Struktur output yang harus ada:
```
dola-output/  (atau folder yang Dola kasih)
├── master-ref/
│   ├── C001-2C-K002-ken-arok.jpg                    (16:9, 1920×1080)
│   ├── C002-2C-K007-dang-hyang-lohgawe.jpg           (16:9, 1920×1080)
│   ├── L001-2C-L008-hutan-tumapel.jpg               (16:9, 1920×1080)
│   ├── L002-2C-L009-pendopo-akuwu-tumapel.jpg        (16:9, 1920×1080)
│   ├── P001-2C-A004-sekantung-beras.jpg             (1:1, 1080×1080) ⚠️ BEDA
│   └── P002-2C-A005-tombak-prajurit.jpg              (1:1, 1080×1080) ⚠️ BEDA
├── storyboard-frame/
│   ├── S001_seg01.jpg    (5s, chase scene)
│   ├── S001_seg02.jpg    (5s, taunt scene)
│   ├── S001_seg03.jpg    (5s, sage appears)
│   ├── S001_seg04.jpg    (5s, prophecy — 2 karakter)
│   ├── S001_seg05.jpg    (5s, epiphany close-up)
│   └── S001_seg06.jpg    (5s, title card)
└── contact-sheet.png     (montage 12 thumbnail)
```

### Cek cepat (5 menit):
1. **Jumlah file**: 12 image + 1 contact sheet = 13 file
2. **Aspect ratio**: buka 2 file ref pertama (K vs A) → cek properties dimensi
   - K (Ken Arok): harus 1920×1080 (16:9)
   - A (Sekantung Beras): harus 1080×1080 (1:1)
3. **Contact sheet**: buka PNG montage → lihat 12 thumbnail, semua unik & sesuai deskripsi

### Cek konsistensi karakter (10 menit):
Bandingkan wajah Ken Arok di:
- ref-C001 (master ref 5-angle) — baseline
- frame-S001_seg01 (chase) — harus wajah sama
- frame-S001_seg04 (prophecy, 2 karakter) — harus wajah sama dengan ref-C001
- frame-S001_seg06 (title card, walking away) — harus wajah sama

Begitu juga Dang Hyang Lohgawe:
- ref-C002 — baseline
- frame-S001_seg03 (sage appears) — harus sama
- frame-S001_seg04 (prophecy) — harus sama dengan ref-C002

---

## 4. Pindahkan Image ke Repo Lokal

Setelah verifikasi, pindahkan 12 image dari output Dola ke struktur repo:

```bash
# Di lokal repo drama-nusantara
mkdir -p produksi/t2i-output/master-reff/2C
mkdir -p produksi/t2i-output/prototype-30s

# Pindahkan (atau copy) dari Dola output:
cp <dola-output>/master-ref/*.jpg produksi/t2i-output/master-reff/2C/
cp <dola-output>/storyboard-frame/*.jpg produksi/t2i-output/prototype-30s/
cp <dola-output>/contact-sheet.png produksi/t2i-output/prototype-30s/
```

**Ingat**: folder `produksi/t2i-output/` di-gitignore (aset lokal saja, tidak di-push).

---

## 5. Share Sample ke Z.ai untuk Review

Pilih **3 sample** untuk share balik ke Z.ai chat:

1. **ref-C001 Ken Arok** — baseline karakter utama, paling penting untuk konsistensi
2. **frame-S001_seg04 Prophecy** — critical frame dengan 2 karakter sekaligus
3. **contact-sheet.png** — overview semua 12 image dalam 1 grid

Cara share:
- Buka Z.ai chat (lanjut sesi ini)
- Upload 3 file via attach button
- Tunggu review + iterate

---

## 6. Iterasi Jika Perlu

### Skenario A: Image bagus semua → lanjut phase berikutnya
- Lanjut Phase 6 (I2V) — pakai `motion.prompt` di storyboard.json untuk input video gen
- Lanjut Phase 7 (TTS) — pakai `audio.tts_text` + edge-tts
- Lanjut Phase 8 (stitch) — ffmpeg 6 clips + TTS → 30s video

### Skenario B: Beberapa image jelek → iterate prompt
- Edit prompt `.txt` di `produksi/master-reff-t2i-prompts/2C-*/prompts/`
- Atau edit `visual.prompt` di `produksi/pra-produksi/prototype-30s/storyboard.json`
- Re-run `python3 scripts/generate_dola_batch.py` untuk regenerate dola-batch.json
- Upload ulang ke Dola + trigger skill lagi

### Skenario C: Skill ada bug → fix skill
- Share screenshot error ke Z.ai
- Diagnose: apakah parser salah? aspect ratio mapping salah? ref resolve gagal?
- Tulis ulang bagian skill yang bermasalah di Dola
- Re-test

---

## 7. Tracking Progress

| Step | Status | Notes |
|---|---|---|
| Skill dibuat | ✅ | Dola selesai 2026-10-23 |
| Skill divalidasi | ✅ | quick_validate.py pass |
| Upload dola-batch.json | ⏳ | next user action |
| Trigger "jalankan batch storyboard" | ⏳ | next user action |
| Phase 1 generate (6 ref) | ⏳ | wait for Dola |
| Gate check | ⏳ | automatic |
| Phase 2 generate (6 frame) | ⏳ | wait for Dola |
| QC + contact sheet | ⏳ | automatic |
| Deliver via NotifyHuman | ⏳ | automatic |
| Verifikasi 12 image lokal | ⏳ | user cek |
| Pindahkan ke repo lokal | ⏳ | user cp |
| Share 3 sample ke Z.ai | ⏳ | user upload |
| Iterate / lanjut phase | ⏳ | based on review |

---

## 8. Catatan Tambahan

- **Skill folder tidak ada di GitHub** kita — hanya di environment Dola. Untuk backup, user bisa download folder `.user_skills/batch-storyboard-generator/` dari Dola lalu commit ke repo kalau perlu audit trail.
- **Skill ini reusable** — kalau nanti bikin produksi lain (mis. era 2A Hindu-Buddha), cukup generate dola-batch.json baru pakai script Python yang sama → upload ke Dola → skill auto-trigger.
- **motion_prompt di-reserve untuk Phase 6 I2V** — tidak ikut ke skill Dola (sudah ada rule di skill).
- **Total waktu estimasi**: 12 image × ~30 detik per image = ~6 menit. Kalau Dola parallel, bisa 2-3 menit.
