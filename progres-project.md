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

## Sesi 2026-10-23 (lanjutan 4) — TAMBAH SUMBER JAKA TINGKIR + SERIES PLAN

**User share**: 5 URL blog Damar Shashangka (Puri Damar Shashangka, 2010) berisi kisah Jaka Tingkir lengkap dari kelahiran Mas Karebet (1499) sampai jadi Adipati Pajang (~1550).

**User request**: "masukan kisah Jaka Tingkir ini ke sumber, sebagai bahan untuk buat film Jaka Tingkir, atau series jaka tingkir. AI baca kisah jaka tingkir full agar paham konteks"

**AI eksekusi**:
1. WebFetch 5 URL parallel — extract teks asli lengkap (Indonesia + Jawa + dialog)
2. Simpan 5 file MD ke `riset/sumber-primer/supplementary/jaka-tingkir-damar-shashangka/`:
   - jaka-tingkir-1.md (Demak berdiri, Malaka jatuh, bunuh Suryawiyata)
   - jaka-tingkir-2.md (Fatahillah rebut Sunda Kelapa, Mas Karebet ke Demak)
   - jaka-tingkir-3.md (Adu banteng, pemberontakan Ki Ageng Sela, bunuh Dhadhung Awuk)
   - jaka-tingkir-4.md (Tapa di Pengging, Padepokan Banyu Biru, wahyu keprabhon Butuh)
   - jaka-tingkir-5.md TAMAT (Duel di Prawata, jadi Adipati Adiwijaya)
3. Bikin `master-era/JAKA-TINGKIR-damar-shashangka.md` (parsing sistematis):
   - Timeline kronologis 1478-1575 M
   - 20+ tokoh (protagonist, antagonist, pendukung)
   - 14+ lokasi (kerajaan, kadipaten, padepokan, pura)
   - 7 benda pusaka (keris Kyai Brongot Setan Kober, sadak, bendera Surya Majapahit, dll)
   - 5 tema utama (Putihan vs Abangan, Wahyu Keprabhon, Shiwa Buddha vs Islam, dll)
   - 6 episode breakdown
   - Klaim dengan sitasi ke file+baris sumber
4. Bikin `produksi/pra-produksi/jaka-tingkir-series/SERIES-PLAN.md`:
   - 6 episode × 10-15 menit = 75-95 menit total
   - Logline, tema, tone
   - Episode breakdown detail (story beats per episode)
   - Asset requirements (19 K + 14 L + 6 A + 3 F + 6 S = 48 file T2I baru)
   - Voice profiles per karakter (Jawa + Indonesia)
   - Cost $0 (reuse pipeline image-based)
   - Estimasi 30 jam kerja total series
5. Bikin `riset/sumber-primer/supplementary/README.md` — aturan pakai sumber supplementary

**Insight penting**:
- Sumber ini SEKUNDER (blog interpretasi), bukan primer Kemenbud 2025. Untuk produksi drama OK, untuk dokumenter akademis perlu verifikasi Babad Tanah Jawi orisinal.
- Continuity: prototype 30s KEN AROK (era 2C, abad 13) → Jaka Tingkir series (era Pajang, abad 16) → setup sequel "Arya Penangsang" (era Mataram awal).
- 6 episode sudah mapped, siap produksi dengan pipeline v3.1 yang sudah teruji di prototype 30s.

**Files added**:
- `riset/sumber-primer/supplementary/README.md`
- `riset/sumber-primer/supplementary/jaka-tingkir-damar-shashangka/jaka-tingkir-1.md` s/d `jaka-tingkir-5.md`
- `master-era/JAKA-TINGKIR-damar-shashangka.md`
- `produksi/pra-produksi/jaka-tingkir-series/SERIES-PLAN.md`

**Pending berikutnya**:
1. Mulai produksi EP1 "Demak Berdiri, Malaka Jatuh" (~12 menit)
2. Bikin master ref T2I baru untuk 48 karakter/lokasi/artefak Jaka Tingkir
3. Generate naskah EP1 dari master-era
4. Storyboard JSON v3.1 untuk EP1
5. Batch T2I + TTS + ffmpeg stitch → MP4 EP1

---

## Sesi 2026-10-23 (lanjutan 3) — STRATEGIC PIVOT: Image-Based Pipeline

**User insight kritis** (seusai test I2V di Dola + Flow):
1. I2V tidak skalabel: free tier max 30s-1min/hari. Untuk film panjang = mustahil
2. T2I storyboard sudah OK di Flow+Dola (free unlimited), tinggal rapihkan workflow
3. **Alternatif**: image + edge-tts + ffmpeg stitch = MP4 tanpa gen video. Cost $0 unlimited

**User refine workflow** (4 step konkret):
1. **Phase Pra-produksi JSON** = sumber ground of truth. Berisi: plan naskah, durasi + SRT, per segmen storyboard. User konfirmasi per segmen (mis. dialog Bahasa Jawa kurang ok = fix 1 segmen, bukan semua). edge-tts sudah support native Jawa: **Mas Neural** + **Siti Neural**.
2. **Batch T2I + Batch TTS** = kalau JSON sudah OK, jalankan batch generate (Dola/Flow untuk image, edge-tts untuk audio)
3. **Stitch lokal via ffmpeg** di MacBook. Atau AI bisa buat TUI (textual user interface) untuk tab-tab dan geser-geser
4. **Kalau ffmpeg ok = done**. Kalau belum, user edit manual di **DaVinci Resolve** (free)

**AI validasi 100%** dengan matematika kebrutalan:
- 10 menit video = 600cr Flow (12 hari) atau $10 Higgsfield
- 30 menit dokumenter = 1800cr (36 hari) atau $30
- Series 6 ep × 30 min = 10800cr (216 hari!) atau $180
- Image-based = $0 untuk any length, dipakai channel YouTube besar (Kings and Generals, History Time, dll)

**Update arsitektur pipeline** (8 phase → 7 phase):
- ~~Phase 6 I2V~~ → **REMOVED** untuk long-form (keep only untuk short ≤60s opsional)
- ~~Phase 7 TTS + Phase 8 Stitch~~ → **MERGED jadi Phase 6+7 baru**

**JSON schema v3.0** (backward compatible dengan v2.0):
- Tambahan field: `voice_profiles{}` (karakter → edge-tts voice setting, termasuk Jawa Neural)
- `image.ken_burns{}` (zoom/pan spec per image)
- `tts.srt_start` / `tts.srt_end` (timing sinkronisasi)
- `transition_out{}` (cut/dissolve/fade)
- `bgm_track` per scene
- `color_palette[]` per scene

**Voice profile edge-tts**:
- Narrator: id-ID-Ardi (default)
- Karakter perempuan: id-ID-Gadis
- Bahasa Jawa: jv-ID-MasNeural (laki-laki), jv-ID-SitiNeural (perempuan)

**Files updated**:
- README.md: workflow 7 phase image-based, "Mengapa Image-Based" section, industry references
- STRATEGIC-PIVOT-IMAGE-BASED.md: pivot strategis dengan matematika + arsitektur
- progres-project.md (file ini)

**Pending berikutnya**:
1. User konfirmasi pivot strategis
2. Pilih produksi pertama (saran: Ken Arok Series EP1 10 menit)
3. AI tulis JSON schema v3.0 spec lengkap
4. AI bikin `scripts/generate_series_json.py` + `generate_tts_batch.py` + `stitch_episode.py` + opsional `tui_editor.py`
5. AI tulis naskah EP1 dari master-era/2C-singasari-kediri.md
6. User review naskah + approve per segmen
7. Generate T2I + TTS + ffmpeg stitch → MP4 EP1 final

---

## Sesi 2026-10-23 (lanjutan 2) — PHASE 5 (T2I) SELESAI untuk Prototype 30s

**Milestone**: Pipeline end-to-end Phase 1-5 terbukti jalan. 12 image berhasil di-generate Dola AI.

**Eksekusi skill**:
- User trigger di Dola Brave browser: upload dola-batch.json + "jalankan batch storyboard"
- Skill auto-run: parse_batch.py → manifest valid (6 ref + 6 frame)
- Phase 1 generate 6 master ref ✅ — 2 karakter + 2 lokasi + 2 prop
- Gate check ✅ — all asset_id resolved
- Phase 2 generate 6 storyboard frame ✅ — pakai ref phase 1
- Issues di-auto-handle: download timeout, S001_seg01 missing, L001 truncated, S001_seg02 corrupt, RPC timeout 40s — semua di-retry background

**VLM analysis 4 sample (semua PASS)**:
- C001 Ken Arok: A-TIER, 5-angle konsisten, scar pipi kiri, leather armor, topknot
- S001_seg04 Prophecy (2 karakter): EXCELLENT — Ken Arok + Lohgawe both konsisten vs ref
- L001 Hutan Tumapel: PASS no-people, god rays, primal mood
- S001_seg01 Chase: PASS, Ken Arok konsisten, 3 prajurit + tombak

**Aspect ratio verification 100% sesuai spec**:
- 4 K/L ref: 1920×1080 (16:9) ✅
- 2 A prop: 1080×1080 (1:1) ✅
- 6 storyboard frame: 1920×1080 (16:9) ✅

**File tersimpan** (di-gitignore, lokal):
- `produksi/t2i-output/master-reff/2C/*.jpg` (6 file, ~9 MB)
- `produksi/t2i-output/prototype-30s/*.jpg` (6 file, ~10 MB)
- `produksi/t2i-output/prototype-30s/contact-sheet.png` (backup)

**Status Pipeline**:
- Phase 1-5 ✅ SELESAI
- Phase 6 (I2V): ⏳ Next — pakai motion.prompt
- Phase 7 (TTS): ⏳ Next — edge-tts id-ID-Ardi
- Phase 8 (Stitch): ⏳ Next — ffmpeg

**Pending berikutnya**:
- Pilih: iterate prompt / lanjut Phase 6 / Phase 7 / Phase 8 / scale-up
- Skill Dola siap dipakai untuk produksi lain (era 2A, pilot Panji 3 menit, dll)

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
