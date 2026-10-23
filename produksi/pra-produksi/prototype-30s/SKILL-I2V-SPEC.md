# Skill Spec — `batch-video-generator` (I2V)

**Tujuan**: Skill Dola AI (atau platform lain) untuk generate 6 video clip dari 6 storyboard frame yang sudah ada. Reuse pattern dari skill `batch-storyboard-generator` (T2I).

**Status**: Draft spec — perlu diimplementasikan setelah user pilih platform I2V.

---

## 1. Perbedaan dari Skill T2I

| Aspek | Skill T2I (existing) | Skill I2V (new) |
|---|---|---|
| Input | Text prompt (+ ref image optional) | Image (mandatory) + motion_prompt |
| Output | .jpg | .mp4 |
| Phases | 2 phase (master_ref → storyboard_frame) | 1 phase (semua parallel, no dependency) |
| Tool | image_gen / image_edit | video_gen / video_edit |
| QC | aspect ratio + character consistency | duration + file size + audio sync |
| Contact sheet | PNG montage | GIF thumbnail grid (opsional) |

---

## 2. Input Skill Menerima

**Upload file**: `i2v-batch.json` (9.8 KB)

### Job schema I2V:
```json
{
  "job_id": "i2v-S001_seg01",
  "phase": "i2v",
  "segment_id": "S001_seg01",
  "scene_id": "S001",
  "scene_title": "Pengejaran di Hutan",
  "segment_notes": "Opening hook — establish chase & character",
  
  "input_image_path": "produksi/t2i-output/prototype-30s/S001_seg01.jpg",
  
  "motion_prompt": "Camera tracks rapidly backward ahead of Ken Arok, keeping him centered as foliage whips past frame edges",
  "motion_camera": "rapid backward tracking, ahead of subject",
  "motion_speed": "fast",
  
  "audio_context": {
    "type": "ambience",
    "bgm": "tense tribal percussion building",
    "sfx": "heavy panting, twigs snapping, distant shouting"
  },
  
  "duration_seconds": 5,
  "fps": 24,
  "output_path": "produksi/i2v-output/prototype-30s/S001_seg01.mp4",
  
  "model_suggestion": "kling-3.0-720p",
  "resolution": "1280x720",
  
  "notes": "I2V untuk segment S001_seg01 — durasi 5s, speed fast"
}
```

---

## 3. Output Skill Harus Menghasilkan

- **6 file video** `.mp4` di `produksi/i2v-output/prototype-30s/`
- **Naming**: `{segment_id}.mp4` (mis. `S001_seg01.mp4`)
- **Durasi**: 5 detik per video (total 30s)
- **Resolution**: 1280×720 (720p default, hemat credit)
- **FPS**: 24 (cinema standard)
- **Audio**: native kalau model support (Seedance 2.5), skip kalau tidak (akan di-handle Phase 7 TTS)

---

## 4. Alur Eksekusi Skill

### Single Phase — I2V (semua parallel)

1. Baca semua job di `phases[0].jobs` (6 job)
2. Untuk tiap job:
   - **Upload input image** dari `input_image_path` (path lokal atau URL Dola)
   - Pakai `motion_prompt` sebagai text input untuk arah gerakan
   - Set model = `model_suggestion` (atau override kalau tidak available)
   - Set duration = `duration_seconds` (5s)
   - Set fps = `fps` (24)
   - Set resolution = `resolution` (720p)
3. Generate → download → save ke `output_path`
4. (Optional) Bikin contact grid GIF: 6 thumbnail video dalam 1 file

---

## 5. Implementasi per Platform

### Opsi A — Dola AI (kalau ada free credits I2V)

Skill baru `batch-video-generator` mirip dengan `batch-storyboard-generator`:

```
.user_skills/batch-video-generator/
├── SKILL.md                              # workflow 4-langkah (lebih simpel dari T2I)
├── scripts/
│   ├── parse_batch.py                    # reuse pattern dari T2I, modify untuk I2V schema
│   └── make_contact_grid.py              # thumbnail grid (atau .gif untuk video)
└── references/
    └── i2v-schema.md                     # field reference untuk i2v-batch.json v1.0
```

**SKILL.md workflow**:
1. Ingest — run parse_batch.py untuk validate i2v-batch.json
2. I2V generate — pakai video_gen tool dengan input_image + motion_prompt
3. QC — cek duration, file size, audio sync (kalau native audio)
4. Deliver — NotifyHuman dengan 6 .mp4 + optional contact grid

### Opsi B — Higgsfield AI (paling hemat credits)

Higgsfield punya API dan web UI. Implementasi:

1. Signup akun baru → dapat 150 credits free
2. Upload 6 input image + 6 motion prompt satu per satu di web UI
3. Pilih model Kling 3.0 720p (7 credits per video, paling hemat)
4. Generate 6 video × 5s = 42 credits total
5. Download 6 .mp4

**Estimasi waktu manual**: 15-20 menit untuk 6 video.
**Tidak butuh skill** — manual upload lebih cepat untuk 6 video saja.

### Opsi C — Google Flow (kalau 50 credits hari ini belum dipakai)

User sudah pernah pakai Flow. Workflow:

1. Buka Flow, upload 6 input image + 6 motion prompt
2. Pilih model Veo (Fast = 5-10 credits per 5s)
3. Generate 6 video, total ~30-60 credits
4. Kalau 50cr habis di tengah, sisa nunggu besok

**Estimasi**: 15-20 menit untuk 6 video.

### Opsi D — ReelCine (free no signup)

Test dulu limit ReelCine:
1. Buka https://reelcine.org
2. Pilih model Seedance 2.5
3. Upload 1 image + motion prompt → generate → cek apakah benar-benar free
4. Kalau OK, ulang untuk 5 video lainnya

**Tidak perlu signup, langsung pakai.** Kalau ternyata limitnya bagus, ini paling praktis.

---

## 6. Quality Check

### Setelah 6 video jadi:

1. **Durasi check** — tiap video harus ±0.5s dari `duration_seconds` (5s)
2. **File size** — minimum 1MB per .mp4 (sanity check, bukan corrupt)
3. **Audio sync** — kalau model support native audio (Seedance 2.5), verify audio match `audio_context`
4. **Visual consistency** — karakter/lokasi harus konsisten dengan T2I input image
5. **Motion matching** — arah gerakan harus sesuai `motion_prompt`

### Kalau ada video yang gagal/kurang baik:
- Regenerate job itu saja (tidak perlu semua 6 video)
- Edit motion_prompt kalau perlu → update i2v-batch.json → re-upload

---

## 7. Estimasi Total Effort per Platform

| Platform | Skill Required? | Manual Time | Estimasi Cost | Reusable untuk Produksi Lain? |
|---|---|---|---|---|
| Dola AI (kalau free credits) | ✅ Bikin skill baru (~30-60 mnt) | 5 menit (auto via skill) | Free kalau credits ada | ✅ Sangat reusable |
| Higgsfield AI | ❌ Manual | 15-20 menit | 42 credits (free signup) | ⚠️ Manual per produksi |
| Google Flow | ❌ Manual | 15-20 menit | 30-60 credits (50/hari) | ⚠️ Manual per produksi |
| ReelCine | ❌ Manual | 15-20 menit | Free (limit unclear) | ⚠️ Test limit dulu |

---

## 8. Rekomendasi untuk Prototype 30s

**Untuk prototype ini saja** (6 video):
- **Cek Dola I2V dulu** → kalau ada free credits, pakai Dola
- Kalau Dola tidak punya → **Higgsfield fresh signup** (paling hemat 42 credits)
- Kalau malas signup → **Google Flow** (kalau 50cr masih ada)

**Untuk produksi panjang ke depan** (pilot Panji 3 menit = 36 video, era lain = lebih banyak):
- **Investasi bikin skill Dola I2V** — sekali bikin, reuse berkali-kali
- Atau investasi Python script untuk API Higgsfield (kalau punya API key)

---

## 9. Next Action Items

### Sekarang:
1. User cek di akun Dola → berapa I2V credits available?
2. Share ke saya → kalau ≥6 video, bikin skill baru Dola
3. Kalau <6 → lanjut ke opsi lain (Higgsfield / Flow / ReelCine)

### Kalau Dola ada free credits:
1. Bikin skill `batch-video-generator` di Dola AI
2. Pattern sama dengan skill T2I (parse_batch.py + SKILL.md)
3. Upload `i2v-batch.json` → trigger skill → 6 video otomatis
4. Total waktu: ~30-60 menit bikin skill + 5 menit generate

### Kalau Dola tidak ada free credits:
1. Higgsfield signup fresh account (5 menit)
2. Manual upload 6 image + motion prompt di web UI Higgsfield
3. Generate 6 video × 5s dengan Kling 3.0 720p
4. Total waktu: ~20-30 menit manual

---

## 10. Files Generated

- `produksi/pra-produksi/prototype-30s/i2v-batch.json` (9.8 KB) — siap upload ke skill atau manual
- `produksi/pra-produksi/prototype-30s/RESEARCH-I2V-PLATFORMS.md` — comparison matrix lengkap
- `produksi/pra-produksi/prototype-30s/SKILL-I2V-SPEC.md` — spec ini
- `scripts/generate_i2v_batch.py` — reusable generator

---

## 11. Catatan Penting

- **motion_prompt yang tadinya "reserved" di skill T2I** sekarang DIPAKAI di skill I2V
- **Audio native** kalau model support (Seedance 2.5) — kalau tidak, audio akan di-handle Phase 7 TTS via edge-tts
- **File I2V (.mp4) di-gitignore** — sama seperti T2I, aset lokal saja
- **Skill Dola I2V bisa reuse 80% struktur T2I** — parse_batch.py, contact sheet pattern, error handling semua sama
