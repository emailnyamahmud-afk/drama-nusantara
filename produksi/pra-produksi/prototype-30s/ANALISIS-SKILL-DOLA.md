# Analisis Skill Dola `batch-storyboard-generator` — Hasil Backup

**Tanggal**: 2026-10-23
**Sumber**: zip dari Dola (4 file, 21.8 KB total)
**Backup location**: `scripts/dola-skill-backup/source/`
**Test result**: Parser diuji dengan `dola-batch.json` kita → BERFUNGSI sempurna ✅

---

## 1. Struktur File Skill

```
source/
├── SKILL.md                              (94 baris, 6 KB) — instruksi workflow
├── scripts/
│   ├── parse_batch.py                    (211 baris, 7.5 KB) — validator JSON
│   └── make_contact_sheet.py             (108 baris, 3.9 KB) — bikin montage thumbnail
└── references/
    └── batch-schema.md                   (86 baris, 4.4 KB) — schema reference
```

---

## 2. SKILL.md — Analisis

**Format**: Standard Agent Skill (YAML frontmatter + body markdown)

**Frontmatter**:
```yaml
name: batch-storyboard-generator
description: Two-phase batch image generation pipeline for storyboard production
  from a dola-batch.json manifest. Phase 1 generates master reference images
  (characters, locations, props) from text prompts; Phase 2 generates storyboard
  frames using the phase-1 images as consistency references. Use when the user
  uploads a dola-batch.json file (schema_version "1.0") or asks to batch-generate
  reference art plus storyboard frames, character-consistency storyboards,
  production concept-art batches, or any dependent-phase image generation manifest.
```

**Trigger keywords** (dari description — akan di-match Dola ke user query):
- "dola-batch.json" / "batch-generate"
- "reference art + storyboard frames"
- "character-consistency storyboards"
- "production concept-art batches"
- "dependent-phase image generation"

**Body**: 6 step workflow:
1. **Ingest and validate** — save file, run `parse_batch.py`, exit non-zero kalau invalid, buat output root dir
2. **Phase 1 — master ref (text-to-image)** — pakai `image_gen` tool, batch dalam 1 `request_list`, split jadi 4-6 job kalau >6
3. **Gate check before Phase 2** — verify semua asset_id punya URL, regenerate job gagal
4. **Phase 2 — storyboard frames (ref-guided)** — pakai `image_edit` tool dengan `image_reference_url_list`
5. **Quality check** — aspect ratio + character consistency + bikin contact sheet
6. **Deliver** — inline image URLs + NotifyHuman dengan folder + contact sheet

**Aturan yang ditanam** (sama dengan yang Dola bilang di chat):
- ✅ `motion_prompt` TIDAK ke image tool (reserved I2V)
- ✅ Aspect ratio mapping eksplisit (5 ratio: 16:9, 1:1, 9:16, 4:5, 3:4)
- ✅ Job gagal → regenerate job itu saja (split chunk jadi setengah)
- ✅ Phase-2 ref missing → STOP, jangan pakai placeholder
- ✅ Manifest invalid → lapor error, jangan guess

**Tool yang dipakai Dola**:
- `image_gen` — untuk phase 1 (text-to-image, no ref)
- `image_edit` — untuk phase 2 (ref-guided, pakai `image_reference_url_list`)
- `Read` tool — untuk QC visual konsistensi karakter
- `FileBatchUpload` — fallback kalau URL ref hilang, upload dari local file
- `NotifyHuman` — deliver hasil ke user

---

## 3. parse_batch.py — Analisis

**Fungsi**: Validator + execution plan printer untuk `dola-batch.json`.

**Yang dicek**:
1. Required top-level keys: `schema_version`, `project`, `phases`, `total_jobs`
2. `schema_version` harus `"1.0"`
3. Required phase keys: `phase_id`, `name`, `jobs`
4. Required job keys: `job_id`, `phase`, `prompt`, `model`, `aspect_ratio`, `output_path`
5. Required ref input keys: `asset_id`, `ref_image_path`, `role`
6. `aspect_ratio` harus known (5 ratio valid)
7. Build dependency map: asset_id → phase 2 jobs yang need it
8. Detect unresolved refs (asset_id di phase 2 tidak ada di phase 1)

**Output 2 mode**:
- Default: human-readable execution plan (print ke stdout)
- `--json`: machine-readable JSON (untuk programmatic use)

**Exit code**:
- 0 = valid
- Non-zero = error (message ke stderr)

### Test result dengan dola-batch.json kita:

```
======================================================================
PROJECT : Ken Arok: Takdir dari Tumapel — Prototype 30s (P002-PROTOTYPE-30S)
STYLE   : cinematic realistic, Javanese period drama, dark-fantasy tones
RES     : 1920x1080   target: 30s
TOTAL JOBS: 12  (phase1=6, phase2=6)
======================================================================

[PHASE 1] phase_1_master_ref — text-to-image (no refs)
  ref-C001 [character] 16:9 1920x1080  Ken Arok
  ref-C002 [character] 16:9 1920x1080  Dang Hyang Lohgawe
  ref-L001 [location]  16:9 1920x1080  Hutan Tumapel
  ref-L002 [location]  16:9 1920x1080  Pendopo Akuwu Tumapel
  ref-P001 [prop]      1:1  1080x1080  Sekantung Beras
  ref-P002 [prop]      1:1  1080x1080  Tombak Prajurit

[PHASE 2] phase_2_storyboard_frame — ref-guided image gen (depends_on: phase_1_master_ref)
  frame-S001_seg01  refs: C001(character_consistency)
  frame-S001_seg02  refs: C001(character_consistency)
  frame-S001_seg03  refs: C002(character_consistency)
  frame-S001_seg04  refs: C001+C002 (2 karakter!)
  frame-S001_seg05  refs: C001
  frame-S001_seg06  refs: C001

[DEPENDENCY MAP]
  C001 → seg01, seg02, seg04, seg05, seg06 (5 frame butuh Ken Arok)
  C002 → seg03, seg04 (2 frame butuh Lohgawe)

[OK] All phase-2 ref inputs resolve to phase-1 assets. ✅
```

**Parser berhasil**: 12 job, semua ref resolve, tidak ada unresolved.

---

## 4. make_contact_sheet.py — Analisis

**Fungsi**: Bikin montage thumbnail semua image hasil generate untuk review cepat.

**Cara pakai**:
```bash
python3 make_contact_sheet.py <image-dir-or-glob...> -o <output.png> [--cols N] [--thumb W]
```

**Fitur**:
- Scan directory rekursif untuk .jpg/.jpeg/.png/.webp/.bmp
- Tile lebar default 480px, label strip 36px
- Layout: 3 kolom default (--cols)
- Label: filename tanpa extension, auto-truncate kalau terlalu lebar
- Background gelap (24,24,28 RGB) — kontras dengan thumbnail
- Font: DejaVu Sans → Liberation Sans → fallback default
- Error image: tampilkan kotak merah dengan pesan error

**Estimasi output untuk 12 image kita**:
- 12 image / 3 cols = 4 rows
- Sheet size: ~1500 × ~2000 px (estimasi)
- Output: 1 PNG contact-sheet.png di output root

**Use case**: Setelah Dola selesai generate 12 image, otomatis bikin contact sheet → user bisa lihat semua dalam 1 view untuk cek konsistensi karakter.

---

## 5. batch-schema.md — Analisis

**Fungsi**: Dokumentasi lengkap schema `dola-batch.json` v1.0 — dibaca skill kalau ada field ambigu.

**Isi**:
- Top-level fields (6): schema_version, project, instructions_for_agent, phases, total_jobs, summary
- Phase object (5 fields): phase_id, name, parallel, depends_on, jobs
- Job common (9 fields): job_id, phase, prompt, model, aspect_ratio, include_inspiration, ref_image_inputs, output_path, notes
- Phase 1 extras (4): asset_id, asset_name, asset_type, prompt_file
- Phase 2 extras (5): segment_id, scene_id, scene_title, segment_notes, motion_prompt, duration_seconds, depends_on
- ref_image_inputs entry (4 fields): asset_id, asset_name, ref_image_path, role
- Aspect ratio mapping table (5 ratio)
- Naming conventions

**Field yang ditekankan**:
- `motion_prompt`: "Reserved for future image-to-video. Do NOT pass to image generation." ⭐
- `role`: `character_consistency` mandatory, `location_context` background tone, `prop_detail` object detail — semua diperlakukan sama oleh image tool, label cuma untuk QC

---

## 6. Verifikasi: Skill sesuai spec kita?

| Spec di DOLA-SKILL-SPEC.md | Implementasi di skill Dola | Match? |
|---|---|---|
| Baca dola-batch.json | parse_batch.py ✅ | ✅ |
| 2 phase berurutan | phases[] dengan depends_on ✅ | ✅ |
| Phase 1 text-only | image_gen tanpa ref ✅ | ✅ |
| Phase 2 pakai ref phase 1 | image_edit + image_reference_url_list ✅ | ✅ |
| motion_prompt tidak ke image tool | Eksplisit disebut di SKILL.md + batch-schema.md ✅ | ✅ |
| Aspect ratio mapping 16:9→1920×1080, 1:1→1080×1080 | Mapping 5 ratio di parse_batch.py + SKILL.md ✅ | ✅ |
| Job gagal → regenerate job itu saja | Error handling section ✅ | ✅ |
| Ref tidak resolve → stop + lapor | "never proceed with placeholder" ✅ | ✅ |
| Contact sheet untuk review | make_contact_sheet.py ✅ | ✅ |
| Output path preserve | "Recreate this directory structure" ✅ | ✅ |

**Verdict**: Skill 100% sesuai spec yang kita kirim. Dola tidak salah interpretasi satu pun.

---

## 7. Bug Ditemukan di dola-batch.json Kita (bukan di skill)

Saat test parser, saya nemu: semua `scene_title` di phase 2 = `"Pengejaran di Hutan"` (sama semua).

**Penyebab**: di `generate_dola_batch.py`, `scene["judul"]` diambil dari storyboard.json — dan semua 6 segmen memang di scene yang sama (S001 = "Pengejaran di Hutan"). Itu **bukan bug**, itu design — semua 6 segmen memang dalam 1 scene (Pengejaran di Hutan).

Tapi `scene_title` tidak menjelaskan **per-segment beat**. Lebih informatif kalau:
- `scene_title` = "Pengejaran di Hutan" (scene-level, sama untuk semua segmen di scene itu)
- `segment_notes` = beat description per segmen (sudah ada, tapi tidak ditampilkan parser)

**Saran**: tambah field `segment_title` per segmen di storyboard.json untuk distinguish (mis. "Chase Through Woods", "Taunt Pursuers", dll). Tapi ini opsional — skill sudah jalan dengan baik tanpa itu.

---

## 8. Workflow Lengkap dengan Skill Ini

```
[AI Z.ai chat]
  ↓
  scripts/generate_dola_batch.py
  ↓
  produksi/pra-produksi/prototype-30s/dola-batch.json (24.9 KB)
  ↓
[User upload JSON ke Dola AI]
  ↓
  Dola auto-trigger skill `batch-storyboard-generator`
  ↓
  1. parse_batch.py — validate + execution plan
  2. Phase 1: image_gen × 6 (parallel, text-only)
  3. Gate check
  4. Phase 2: image_edit × 6 (ref-guided, pakai phase 1 URL)
  5. QC: aspect ratio + character consistency + contact sheet
  6. Deliver: inline URLs + NotifyHuman with folder + contact sheet
  ↓
[User download 12 image + contact-sheet.png]
  ↓
[User save ke lokal]:
  produksi/t2i-output/master-reff/2C/*.jpg
  produksi/t2i-output/prototype-30s/*.jpg
  produksi/t2i-output/prototype-30s/contact-sheet.png
  ↓
[User share contact-sheet.png + 2-3 sample ke Z.ai]
  ↓
  Iterasi prompt kalau perlu
```

---

## 9. Reusable untuk Produksi Lain

Skill ini **reusable** untuk semua produksi ke depan:

1. Era 2A Hindu-Buddha awal (Kutai, Tarumanagara, Sriwijaya)
2. Era 2D Majapahit
3. Era 3A Islamisasi
4. Era 4A VOC
5. Pilot Panji 3 menit (yang lama, 36 segmen)
6. Dll.

**Cara reuse**:
1. Edit `storyboard.json` di folder pra-produksi baru
2. Pastikan ada master ref prompt `.txt` untuk tiap asset di Phase 3
3. Run `python3 scripts/generate_dola_batch.py` → output `dola-batch.json` baru
4. Upload ke Dola → trigger skill → 12+ image otomatis

**Estimasi effort per produksi baru**:
- Edit storyboard.json: 30 menit
- Bikin prompt ref baru kalau ada karakter/lokasi baru: 1-2 jam
- Run generator: 5 detik
- Upload + skill eksekusi: 5-10 menit
- Review & iterate: 30-60 menit
- **Total per produksi**: ~2-4 jam (vs manual 1-2 hari)

---

## 10. Kesimpulan

**Skill Dola `batch-storyboard-generator`**:
- ✅ Sesuai spec 100% — semua aturan kita ditanam dengan benar
- ✅ Parser diuji dengan dola-batch.json kita — BERFUNGSI sempurna
- ✅ 4 file komponen: SKILL.md + 2 Python script + 1 schema markdown
- ✅ Reusable untuk semua produksi ke depan
- ✅ Ada error handling (job gagal, ref missing, manifest invalid)
- ✅ Ada QC step + contact sheet untuk review cepat

**Action user berikutnya**:
1. Upload `dola-batch.json` ke Dola
2. Ketik: `jalankan batch storyboard`
3. Tunggu skill auto-trigger dan eksekusi 12 image
4. Download hasil + contact sheet
5. Share 3 sample ke Z.ai untuk review

**Estimasi waktu eksekusi**: 5-10 menit (12 image, parallel kalau Dola support).
