# DOLA AI SKILL SPEC — Batch Storyboard Generator

**Tujuan**: Skill untuk Dola AI (atau agen AI lain) yang membaca 1 file `dola-batch.json` dan menghasilkan semua image (master ref + storyboard frame) secara otomatis dalam 2 phase berurutan.

**Status**: Draft spec. User testing di Dola AI mode agen — implementasi tergantung fitur yang tersedia di Dola.

---

## 1. Input Skill Menerima

**Upload file**: `dola-batch.json` (24.9 KB)

Isi struktur JSON:
```json
{
  "schema_version": "1.0",
  "project": { "id","title","era","duration_target_seconds","resolution","fps","style","date_created" },
  "instructions_for_agent": {
    "phase_1_master_ref": { ... },
    "phase_2_storyboard_frame": { ... },
    "execution_order": "phase_1 → phase_2",
    "output_organization": { ... }
  },
  "phases": [
    {
      "phase_id": "phase_1_master_ref",
      "name": "Generate Master Reference Images",
      "parallel": true,
      "depends_on": null,
      "jobs": [ {job1}, {job2}, ... ]
    },
    {
      "phase_id": "phase_2_storyboard_frame",
      "name": "Generate Storyboard Frames",
      "parallel": true,
      "depends_on": "phase_1_master_ref",
      "jobs": [ {job1}, {job2}, ... ]
    }
  ],
  "total_jobs": 12,
  "summary": { ... }
}
```

### Job schema — Phase 1 (master_ref):
```json
{
  "job_id": "ref-C001",
  "phase": "master_ref",
  "asset_id": "C001",
  "asset_name": "Ken Arok",
  "asset_type": "character",
  "prompt_file": "2C-K002-ken-arok.txt",
  "prompt": "<full text prompt>",
  "model": "seedream-4.5",
  "aspect_ratio": "16:9",
  "include_inspiration": false,
  "ref_image_inputs": [],
  "output_path": "produksi/t2i-output/master-reff/2C/C001-2C-K002-ken-arok.jpg",
  "notes": "Character ref sheet 5-angle horizontal untuk Ken Arok"
}
```

### Job schema — Phase 2 (storyboard_frame):
```json
{
  "job_id": "frame-S001_seg01",
  "phase": "storyboard_frame",
  "segment_id": "S001_seg01",
  "scene_id": "S001",
  "scene_title": "Pengejaran di Hutan",
  "segment_notes": "Opening hook — establish chase & character",
  "prompt": "<full visual.prompt text>",
  "motion_prompt": "<for future I2V use>",
  "model": "seedream-4.5",
  "aspect_ratio": "16:9",
  "include_inspiration": true,
  "ref_image_inputs": [
    {
      "asset_id": "C001",
      "asset_name": "Ken Arok",
      "ref_image_path": "produksi/t2i-output/master-reff/2C/C001-2C-K002-ken-arok.jpg",
      "role": "character_consistency"
    }
  ],
  "output_path": "produksi/t2i-output/prototype-30s/S001_seg01.jpg",
  "duration_seconds": 5,
  "depends_on": ["C001"],
  "notes": "Storyboard frame untuk segment S001_seg01 (durasi 5s)"
}
```

---

## 2. Output Skill Harus Menghasilkan

- **12 file image** di lokasi sesuai `output_path` tiap job
- **Naming convention**: `{asset_id}-{prompt_file_basename}.jpg` untuk ref, `{segment_id}.jpg` untuk frame
- **Aspect ratio**:
  - Master ref character & location: **16:9 horizontal** (1920×1080)
  - Master ref prop: **1:1 square** (1080×1080)
  - Storyboard frame: **16:9 horizontal** (1920×1080)

---

## 3. Alur Eksekusi Skill

### Phase 1 — Generate Master Ref (parallel)
1. Baca semua job di `phases[0].jobs`
2. Untuk tiap job:
   - Pakai `prompt` sebagai text input
   - Set model = `seedream-4.5` (atau model terbaik yang tersedia)
   - Set aspect ratio sesuai job
   - Tidak perlu upload ref image (phase 1 input = text only)
3. Generate → pilih 1 variasi terbaik → download
4. Save ke `output_path`
5. Setelah semua job phase 1 selesai → lanjut phase 2

### Phase 2 — Generate Storyboard Frame (parallel, depends on phase 1)
1. Baca semua job di `phases[1].jobs`
2. Untuk tiap job:
   - Pakai `prompt` sebagai text input
   - **Upload ref image** dari `ref_image_inputs[*].ref_image_path` sebagai image input
     - Hanya asset dengan `include_inspiration=true` yang ada di list
     - Role `character_consistency` = wajib (Karakter utama — wajah harus konsisten)
     - Role `location_context` = opsional (lokasi sebagai background ref)
     - Role `prop_detail` = opsional (prop sebagai detail ref)
   - Set model = `seedream-4.5`
   - Set aspect ratio 16:9
3. Generate → pilih 1 variasi terbaik → download
4. Save ke `output_path`

---

## 4. Spec Implementasi di Dola AI (Mode Agen)

### Opsi A — Pakai "Skill Builder" Dola (kalau ada)
Buat skill baru dengan konfigurasi:
- **Trigger**: User upload file `.json` dengan `schema_version: "1.0"`
- **Action**: Parse JSON → jalankan 2 phase secara berurutan
- **Output**: Save image ke path yang ditentukan (atau download all sebagai zip)

### Opsi B — Manual Prompt di Chat Dola
Paste teks ini ke chat Dola mode agen + upload `dola-batch.json`:

```
Saya upload dola-batch.json. Tolong eksekusi sebagai berikut:

PHASE 1 (master_ref — 6 job, parallel):
- Untuk setiap job di phases[0].jobs:
  - Generate image dengan prompt dari field "prompt"
  - Model: seedream-4.5, aspect ratio sesuai field
  - Tidak perlu ref image input
  - Setelah selesai, beri nama file sesuai output_path
  - Kumpulkan semua 6 image

PHASE 2 (storyboard_frame — 6 job, parallel, setelah phase 1 selesai):
- Untuk setiap job di phases[1].jobs:
  - Generate image dengan prompt dari field "prompt"
  - Upload ref image dari ref_image_inputs[*].ref_image_path sebagai input
  - Model: seedream-4.5, aspect ratio 16:9
  - Setelah selesai, beri nama file sesuai output_path
  - Kumpulkan semua 6 image

OUTPUT: 12 image total, diberi nama sesuai output_path.
Tampilkan semua 12 image di akhir untuk saya download.
```

### Opsi C — Script Python pakai Dola API (kalau punya API key)
```python
# TODO: isi kalau user punya Dola API access
# Loop job phase 1, generate, save
# Loop job phase 2, generate dengan ref image, save
```

---

## 5. Quality Check

Setelah 12 image jadi, agent bisa otomatis cek:
- **Karakter konsistensi**: Bandingkan Ken Arok di frame 1, 2, 4, 5, 6 — wajah harus mirip
- **Lokasi konsistensi**: Bandingkan Hutan Tumapel di frame 1, 2, 3, 4 — tone/warna harus konsisten
- **Prop detail**: Sekantung beras & tombak harus sesuai deskripsi prompt ref
- **Aspect ratio**: Ref K/L = 16:9, ref A = 1:1, semua frame = 16:9

Kalau ada yang gagal, agent bisa regenerate job tersebut.

---

## 6. Iterasi & Refinement

Jika image hasil kurang baik, user bisa:
1. Edit prompt di file `.txt` di `produksi/master-reff-t2i-prompts/2C-*/prompts/`
2. Edit `visual.prompt` di `storyboard.json`
3. Re-run `scripts/generate_dola_batch.py` untuk regenerate `dola-batch.json`
4. Upload ulang ke Dola

---

## 7. Workflow Lengkap

```
[AI Z.ai chat]
  ↓
  scripts/generate_dola_batch.py
  ↓
  produksi/pra-produksi/prototype-30s/dola-batch.json (24.9 KB)
  ↓
[User upload JSON ke Dola AI mode agen]
  ↓
  Dola generate 6 ref image (phase 1)
  ↓
  Dola generate 6 storyboard frame (phase 2, pakai ref phase 1)
  ↓
  12 image di-download
  ↓
[User simpan di lokal]:
  produksi/t2i-output/master-reff/2C/*.jpg
  produksi/t2i-output/prototype-30s/*.jpg
  ↓
[User share sample ke AI Z.ai untuk review]
  ↓
  Iterasi prompt kalau perlu
```

---

## 8. Catatan

- **File 24.9 KB** cukup kecil untuk upload ke mana saja
- **Tidak ada base64 inline** — semua prompt adalah text plain, hemat space
- **Dependency graph jelas** — phase 2 tidak bisa mulai sebelum phase 1 selesai
- **Naming convention predictable** — mudah tracking file
- **Schema extensible** — bisa tambah phase 3 (I2V) nanti dengan format sama
