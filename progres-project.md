# Progres Project — Drama Nusantara

> Tujuan file: catatan singkat progres **per sesi**. AI beku (tak punya ingatan antar sesi); file ini + `README.md` + `worklog.md` = konteks minimal yang WAJIB dibaca di awal setiap sesi baru. Sandbox bisa reset kapanpun — **tiap sesi wajib push GitHub**.

## Aturan Pakai

1. **Awal sesi**: baca berurutan `README.md` → `progres-project.md` → `worklog.md` (lihat entry terakhir).
2. **Akhir sesi**: append entry baru ke file ini (`## Sesi YYYY-MM-DD`), lalu push ke GitHub.
3. Format entry = ringkas, max 30 baris per sesi. Detail teknis tulis di `worklog.md`.
4. Setiap entry sebutkan: tanggal, eras yang dikerjakan, hal penting yang ditemukan/fix, hal yang masih pending.

---

## Sesi 2026-10-23 — Analisis Google Flow + Prototype 30s Schema v2

**Konteks**: User uji Google Flow (Storyboard Studio) — generate script + aset image + storyboard image FREE. User kirim JSON Flow v1.2 (56 MB, sample "KEN AROK: TAKDIR DARI TUMAPEL" — 4 scene, 21 frame, 16 asset). User minta: (1) analisis JSON Flow, (2) identifikasi yang bisa diadopsi, (3) prototype 30s/1min dengan JSON per segmen + adopsi workflow Flow.

**Task**:
1. Download & parse JSON Flow dari Drive (56 MB)
2. Extract struktur: 7 top-level keys, 16 asset (7 char + 3 loc + 6 prop), 21 frame, 5.381 char markdown script
3. VLM-analisis 1 sample frame (chase scene) — kualitas visual setara Dola AI
4. Tulis `analisis-google-flow.md` (16 KB, lengkap — adopsi + pengembangan)
5. User clarify: fokus adopsi saja, JSON per segmen + Flow optimization
6. Tulis `ADOPSI-Flow.md` (8 item adopsi ringkas, diff dari pilot Panji)
7. Generate `prototype-30s/storyboard.json` (12.5 KB, schema v2.0, 6 segmen × 5s = 30s, KEN AROK short)

**Hasil**:
- 7 item adopsi terverifikasi: 3-field asset schema, motion.prompt (I2V feeder), linked_asset_ids, include_inspiration flag, time_of_day, image_history (path-only), 16:9 (sudah ada)
- Prototype 30s: 2 karakter (Ken Arok + Dang Hyang Lohgawe), 2 lokasi (Hutan Tumapel + Pendopo), 2 prop (Sekantung Beras + Tombak)
- Schema v2.0 backward-compatible dengan pilot Panji lama (storyboard-pilot.json 36 segmen 3 menit)
- JSON size 12.5 KB (target < 500 KB) — base64 dipisah, aset di-gitignore

**File baru**:
- `produksi/pra-produksi/analisis-google-flow.md` — analisis lengkap
- `produksi/pra-produksi/ADOPSI-Flow.md` — ringkasan 8 item adopsi + schema diff
- `produksi/pra-produksi/prototype-30s/storyboard.json` — JSON schema v2.0
- `scripts/generate_prototype_30s.py` — generator script (reusable)

**Pending berikutnya**:
- Generate 6 T2I di Dola AI (atau Flow) untuk prototype 30s — verifikasi kualitas
- TTS 1 narasi gabungan via edge-tts
- Stitch 30s video via ffmpeg (Ken Burns effect untuk I2V opsional)
- Kalau OK → scale up ke pilot Panji lama (3 menit) atau produksi 10 menit
- 4C-4E masih BLOCKED (Jilid VI-X belum terbit)

---

## Sesi 2026-10-23 (lanjutan) — Dola AI Skill Jadi: `batch-storyboard-generator`

**Milestone**: Skill Dola AI pertama untuk pipeline kita — sudah jadi & tervalidasi.

**Yang Dola buat** (di environment Dola: `workspace/.user_skills/batch-storyboard-generator/`):
- `SKILL.md` (94 baris) — instruksi workflow 2-phase
- `scripts/parse_batch.py` — validator JSON + dependency graph (ditest, 12 job all ref resolve ✅)
- `scripts/make_contact_sheet.py` — bikin montage thumbnail 12 image untuk review cepat
- `references/batch-schema.md` — schema JSON v1.0 + mapping aspect ratio

**Cara kerja skill (6 langkah)**:
1. Ingest — upload dola-batch.json → parse_batch.py validasi + dependency map
2. Phase 1 — generate 6 master ref (text-only, batch 1 call) → asset_id → URL mapping
3. Gate check — pastikan semua phase 1 sukses sebelum lanjut
4. Phase 2 — generate 6 storyboard frame pakai image_edit + image_reference_url_list dari phase 1
5. QC — cek konsistensi karakter/lokasi + bikin contact sheet
6. Deliver — semua image + folder output via NotifyHuman

**Aturan penting yang ditanam Dola di skill**:
- `motion_prompt` TIDAK PERNAH dikirim ke tool image (reserved untuk I2V nanti) ✅
- Mapping aspect ratio: 16:9 → 1920×1080, 1:1 → 1080×1080 ✅
- Job gagal → regenerate job itu saja, bukan seluruh batch ✅
- Ref phase 2 tidak resolve → stop + lapor, jangan asal generate ✅

**Cara trigger skill**: upload `dola-batch.json` → ketik "jalankan batch storyboard" → skill auto-trigger.

**Pending berikutnya**:
- User trigger skill di Dola → eksekusi 12 image (6 ref + 6 storyboard frame)
- User download 12 image + contact sheet
- User share 3 sample balik ke Z.ai untuk review kualitas
- Kalau OK → lanjut Phase 6 (I2V) + Phase 7 (TTS) + Phase 8 (stitch)
- Kalau ada image perlu iterasi → edit prompt .txt → regenerate dola-batch.json → re-upload

---

## Sesi 2026-10-22 — Rewrite 2A Hindu-Buddha Awal

**Konteks awal sesi**: Sandbox sync dengan GitHub (HEAD `9b3649d`). User minta: (1) buat `progres-project.md` (file ini), (2) lanjut rewrite lengkap era 2A-2C dari pola "koreksi" ke "rewrite lengkap" (pola sama dengan 1A-1D, 3A-3C, 4A-4B yang sudah selesai sesi sebelumnya).

**Task**: Rewrite lengkap 2A (Hindu-Buddha Awal, abad 4-7 M).

**Sumber primer yang dibaca**:
- `jilid-2/06-bab-1.md` — Bab I: Masyarakat Nusantara dalam Perjumpaan Budaya dengan India, Tiongkok, dan Persia (religi pra-Hindu, struktur sosial desa-federasi, teknologi logam-pertanian-pelayaran, jaringan antarbangsa, kosmopolitan entrepôt)
- `jilid-2/07-bab-2.md` — Bab II: Persilangan Budaya — aksara Brahmi Akhir/Pallawa Tua, bahasa Melayu Kuno, agama Hindu (Waisnawa-Saiwa awal, dialog Hindu-Buddha), Buddha (Mahayana abad 5-15 M), penanggalan Saka, konsep raja (primus inter pares → dewaraja)
- `jilid-2/08-bab-3.md` — Bab III Section A.1: Kerajaan-kerajaan tertua abad 4-7 M (Kutai-Mulawarman, Tarumanagara-Purnawarman, Kan-to-li/Swarnadwipa awal, Kedatuan Sriwijaya-Dapunta Hyang)

**Hasil**: Lihat entry `worklog.md` untuk detail teknis. File `master-era/2A-hindu-buddha-awal.md` direwrite total dari 831 baris (koreksi) → target 1300+ baris (rewrite lengkap). Setiap klaim punya sitasi `jilid-2/NN-bab-M.md` Section line XXX-YYY.

**Pending berikutnya**: 
- Rewrite 2B Mataram-Sriwijaya (abad 8-11 M)
- Rewrite 2C Singasari-Kediri (abad 11-13 M)
- T2I prompts untuk 3C + 4A + 4B (belum dibuat)
- 4C-4E masih BLOCKED (Jilid VI-X belum terbit)

---

## Sesi 2026-10-20 — Final State (sesi sebelumnya, ringkas)

13 era selesai (1A-1D + 2D + 3A-3C + 4A-4B) dengan pola rewrite/expand lengkap. 3 era (2A-2C) masih di tahap koreksi parsing. 4 era (4C-4E) BLOCKED menunggu Jilid VI-X. Total: 12.010 baris master-era docs, ~154.000 kata, 1.176 klaim dengan sitasi sumber primer. T2I prompts: 10 era (173 file .txt). Detail lengkap lihat `README.md` dan `worklog.md`.

**Catatan penting yang harus diingat**:
- AI pernah amnesia waktu garap 2D Majapahit → akibatnya master sebelumnya halu (Candi Sukuh ±1437 M, Meng Qi 1289, "100 keluarga"). Fix semua.
- Sumber primer = 83 file MD Jilid I-V (Jilid VI-X belum terbit).
- Pola "koreksi" tidak cukup — harus "rewrite lengkap" = baca semua Bab relevan + ekstrak semua tokoh/latar/klaim.

## Sesi 2026-10-22 (lanjutan) — T2I v2.1 Regenerate 1B-2B

**Task**: Regenerate T2I prompts era 1B, 1C, 1D, 2A, 2B dengan standar baru v2.1 (horizontal 16:9 + S pakai K ref).

**Hasil**:
- 1B: 10→17 files | 1C: 10→17 | 1D: 12→17 | 2A: 18→17 | 2B: 37→17
- Total v2.1: 101 files (1A-2B)
- Setiap era: K5-6 + L7 + A3 + F0-1 + S1
- 2B terbesar perubahan: 37→17 (hapus 20 file interior istana yang bukan master reff)

**Pending**:
- 2C Singasari-Kediri (perlu v2)
- 2D Majapahit (perlu v2)
- 3A Islamisasi Awal (perlu v2)
- 3B Demak-Pajang (perlu v2)
- 3C, 4A, 4B (belum ada T2I sama sekali)

## Sesi 2026-10-22 (lanjutan 2) — T2I v2.1 Regenerate 2C-2D + ERA HINDU-BUDDHA SELESAI

**Task**: Regenerate T2I 2C dan 2D + update dokumentasi setiap push.

**Hasil**:
- 2C: 17→17 v2.1 | 2D: 17→17 v2.1
- ERA HINDU-BUDDHA (2A-2D) T2I v2.1 selesai semua — 68 files
- Total v2.1: 135 files (1A-2D)
- Setiap push: update README + worklog + progres-project

**Pending**:
- 3A Islamisasi Awal (perlu v2)
- 3B Demak-Pajang (perlu v2)
- 3C, 4A, 4B (belum ada T2I)

## Sesi 2026-10-22 (lanjutan 3) — T2I v2.1 Regenerate 3A

**Hasil**: 3A Islamisasi Awal: 21→17 v2.1 (K6+L7+A3+S1)
Total v2.1: 152 files (1A-3A)
**Pending**: 3B (perlu v2), 3C/4A/4B (belum ada)

## Sesi 2026-10-22 (lanjutan 4) — T2I v2.1 SELESAI UNTUK SEMUA ERA YANG ADA (1A-3B)

**Hasil**: 3B Demak-Pajang: 21→17 v2.1 (K6+L7+A3+S1)
Total v2.1: 169 files (1A-3B) — semua era yang sudah ada T2I sebelumnya sudah di-regenerate ke v2.1
**Remaining**: 3C, 4A, 4B (belum ada T2I), 4C-4E BLOCKED

## Sesi 2026-10-22 (lanjutan 5) — T2I v2.1 era 3C (baru dari nol)

**Hasil**: 3C Mataram Islam: 0→17 v2.1 (K6+L7+A3+S1) — T2I pertama untuk era ini
Total v2.1: 186 files (1A-3C)
**Remaining**: 4A, 4B (belum ada T2I), 4C-4E BLOCKED

## Sesi 2026-10-22 (lanjutan 6) — T2I v2.1 era 4A VOC Awal

**Hasil**: 4A VOC Awal: 0→17 v2.1 (K6+L7+A3+S1)
Total v2.1: 203 files (1A-4A)
**Remaining**: 4B (belum ada T2I), 4C-4E BLOCKED

## Sesi 2026-10-22 (FINAL) — T2I v2.1 SELESAI UNTUK SEMUA ERA (1A-4B)

**Hasil**: 4B Kolonial 19: 0→17 v2.1 (K6+L7+A3+S1)
Total T2I v2.1: 220 files (13 era: 1A-4B)
*** PHASE 3 (MASTER REFF T2I) SELESAI ***

**Status Phase Pipeline:**
- Phase 1 (Sumber Primer): ✅ 83 file
- Phase 2 (Master Era): ✅ 16 era, ~220.000 kata
- Phase 3 (Master Reff T2I): ✅ 13 era, 220 file v2.1
- Phase 4-8: belum mulai

**BLOCKED**: 4C-4E (Jilid VI-X belum terbit)
