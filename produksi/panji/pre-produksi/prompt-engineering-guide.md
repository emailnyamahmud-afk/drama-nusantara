# T2I Prompt Engineering Guide — Panji: Asmara Bangun

## Untuk Google Flow (https://flow.google.com)

> **Platform**: Google Flow adalah creative studio berbasis **WEB** (bukan API). Tidak perlu kode Python, tidak perlu API key. Login pakai Google account, langsung generate di browser.
> **URL**: https://flow.google.com
> **Model image yang dipakai Flow**: Nano Banana (Gemini 3.1 Flash Image series)
> **Sumber resmi**: https://flow.google.com + https://support.google.com/flow

---

## A. Setup — 3 Langkah

### 1. Login
- Buka https://flow.google.com
- Sign in pakai Google account
- Setelah login, masuk ke "Studio" / "Create"

### 2. Pilih Model
Di Flow, model dipilih via menu dropdown:
- **Nano Banana** → untuk image generation (yang kita pakai)
- **Veo 3.1** → untuk video (untuk Step 5 I2V nanti)
- **Gemini Omni** → untuk multimodal (image + video + text)

### 3. Pahami Credit System

| Tier | Harga | Credits Flow / bulan | Cocok untuk |
|------|-------|----------------------|-------------|
| **Free** | $0 | 50/hari (tidak menumpuk) | Eksperimen awal |
| **Google AI Plus** | $9.99/bln | 200/bln + 50/hari | Pilot kecil |
| **Google AI Pro** | $19.99/bln | 1.000/bln + 50/hari | **Pilot 3 menit (rekomendasi)** |
| **Google AI Ultra $100** | $99.99/bln | 10.000/bln | Mini-series |
| **Google AI Ultra $200** | $199.99/bln | 25.000/bln | Full series |

**Aturan penting credit:**
- 50 credit/hari hanya untuk eksperimen — tidak cukup untuk pilot lengkap
- Credit **tidak menumpuk** (yang tidak terpakai hilang)
- Credit bulanan refresh di awal billing cycle
- Veo 3.1 (video) mahal (~100 credit/generate), Nano Banana (image) murah (~5-10 credit)

**Estimasi untuk pilot Panji (45 image = 4 karakter + 5 lokasi + 36 segmen):**
- 45 image × ~10 credit = ~450 credit
- Rekomendasi: minimal **Google AI Pro** (1.050 credit total)

---

## B. Workflow Konkret di Web Flow

### Step 1 — Generate 4 Karakter Ref (C001-C004)

```
1. Buka https://flow.google.com → login

2. Klik "Create new" → pilih model "Nano Banana"

3. Setup project:
   - Project name: "Panji Pilot - Character Refs"
   - Model: Nano Banana
   - Aspect ratio: 9:16 (portrait untuk karakter ref)
   - Resolution: 2K (cukup untuk pilot)

4. Buka file prompt dari pre-produksi/prompts/C001_panji.txt
   Copy seluruh isi prompt

5. Paste ke chat box Flow

6. Klik "Generate" → tunggu ~30-60 detik
   → Flow akan kasih 1 image hasil

7. Review hasil:
   - Wajah Jawa? (bukan Chinese/Indian/Thai)
   - Kostum sesuai era 1100 CE?
   - Lighting sesuai mood?
   - Detail cukup?

8. Jika belum pas → pakai Multi-turn editing:
   - Jangan klik "Generate ulang" — pakai chat
   - Ketik feedback natural language di chat:
     "Make the lighting more dramatic. Increase contrast to 6:1.
      Add stronger rim light on left shoulder."
   - Flow akan edit image sebelumnya, bukan generate baru
   - Karakter tetap konsisten, hanya elemen yang disebut berubah

9. Iterasi 2-3x sampai quality gate (section F) lulus

10. Download image → simpan ke:
    /home/z/my-project/produksi/panji/refs/C001_base.png

11. Ulangi untuk C002, C003, C004
```

### Step 2 — Generate 5 Lokasi Ref (L001-L005)

```
1. Buat project baru di Flow:
   - Project name: "Panji Pilot - Location Refs"
   - Model: Nano Banana
   - Aspect ratio: 16:9 (cinematic wide untuk landscape)
   - Resolution: 2K

2. Buka prompt dari visual-style.md (L001-L005)
   Copy ke chat Flow

3. Generate → review → iterate via chat

4. Quality gate untuk lokasi:
   - Arsitektur Jawa Hindu-Buddha? (bukan Chinese/Indian)
   - Skala imperial terbaca? (bukan desa kecil)
   - Multi-bangunan? (bukan satu candi tunggal)
   - Elemen maritime untuk L004/L005? (perahu, kanal, armada)

5. Download → simpan ke refs/L00X_base.png
```

### Step 3 — Generate 36 Segmen (Pakai Reference Image)

**INILAH KUNCI KONSISTENSI KARAKTER** — di Flow bisa upload reference image.

```
1. Buat project baru: "Panji Pilot - Segmen Images"
   - Model: Nano Banana
   - Aspect ratio: 16:9
   - Resolution: 2K

2. Untuk setiap segmen (36 total, lihat storyboard-pilot.json):

   a. Buka prompt segmen dari storyboard (mis. S001_seg01)
   b. Paste prompt ke chat Flow

   c. Upload reference image:
      - Klik icon "📎" / "Add image" di sebelah chat box
      - Upload refs/C001_base.png (jika segmen melibatkan Panji)
      - Upload refs/C002_base.png (jika Candra Kirana)
      - Bisa upload hingga 14 reference images sekaligus

   d. Generate → review
      - Karakter konsisten dengan ref? (wajah, kostum, warna)
      - Setting konsisten dengan lokasi ref?
      - Shot type sesuai storyboard?

   e. Iterate via chat:
      "Make Panji's face more like the reference, keep the lighting"
      "The crown should be smaller, more like the reference image"

   f. Download → segments/S001_seg01/image.png
```

### Step 4 — Generate Audio (TTS + BGM)

Audio tidak di-generate di Flow. Pakai:
- **TTS**: Google Cloud TTS atau ElevenLabs (untuk narator + dialog)
- **BGM**: Suno / Udio (untuk gamelan hybrid orchestra)
- **SFX**: Library gratis (freesound.org) — air, angin, obor, dll

### Step 5 — Generate Video (I2V)

```
1. Di Flow, ganti model dari "Nano Banana" ke "Veo 3.1"

2. Setup project:
   - Project name: "Panji Pilot - Video Segments"
   - Model: Veo 3.1
   - Aspect ratio: 16:9
   - Resolution: 1080p
   - Duration: 5 detik per segmen
   - Frame rate: 24fps

3. Untuk setiap segmen:
   a. Upload image segmen (dari Step 3) sebagai "First frame"
   b. Berikan prompt motion singkat:
      "Slow dolly forward, Panji stands up from throne"
   c. Generate → tunggu ~2-5 menit per segmen
   d. Veo 3.1 juga generate native audio (jangan di-mute)

4. Note: Veo 3.1 biaya ~100 credit per generate
   36 segmen × 100 credit = 3.600 credit
   ⚠️  Butuh Google AI Ultra ($100/bln) untuk 1 bulan production
   ATAU spread ke 4 bulanan Pro plan (1.000 credit/bulan)

5. Download → segments/SXX_segYY/video.mp4
```

### Step 6 — Assembly (Final Video)

```
1. Pakai video editor (DaVinci Resolve gratis, Adobe Premiere, FFmpeg)

2. Import 36 video segmen + audio (TTS + BGM + SFX)

3. Sequence per storyboard:
   - Babak 1: segmen 1-12 (1 menit)
   - Babak 2: segmen 13-24 (1 menit)
   - Babak 3: segmen 25-36 (1 menit)

4. Add transitions (crossfade antar segmen)

5. Color grading konsisten:
   - Babak 1: warm amber + deep blue shadows
   - Babak 2: golden orange + cool blue
   - Babak 3: fire orange + cool blue-black

6. Add subtitles (opsional, untuk dialog Bahasa Indonesia)

7. Export: episode_01_panji_pilot.mp4 (1920×1080, 24fps, H.264)

8. Upload ke /home/z/my-project/download/
```

---

## C. Struktur Prompt — 5 Komponen (Rekomendasi Google)

Setiap prompt T2I untuk proyek ini wajib pakai format:

```
[SUBJECT] + [SETTING] + [LIGHTING] + [MOOD] + [STYLE/MATERIAL]
```

### Penjelasan tiap komponen

| Komponen | Isi yang wajib ada | Contoh konkret |
|----------|---------------------|----------------|
| **SUBJECT** | Siapa/apa, shot type, pose, ekspresi, kostum detail (warna + motif + bahan) | "Medium close-up portrait of a 28-year-old Javanese crown prince, three-quarter view facing camera left, calm determined expression, wearing dark blue tunic with kala-makara gold embroidery" |
| **SETTING** | Lokasi konkret, era, elemen latar, referensi arsitektur | "Javanese Hindu-Buddhist imperial palace, East Java 1100 CE, Prambanan/Penataran temple relief style architecture, stone andesite pillars" |
| **LIGHTING** | Suhu warna (Kelvin), arah, intensitas, jenis, rasio kontras | "Warm 2700K torch light from camera right (key), cool 5600K moonlight from window left (fill), contrast ratio 4:1" |
| **MOOD** | Emosi/atmosfer konkret (bukan generik "cinematic") | "Tegas, berkuasa, slightly contemplative — a prince who carries the weight of two kingdoms" |
| **STYLE** | Reference visual, lensa, aspek rasio, technical specs, color grading | "Cinematic realistic portrait, Javanese classical aesthetic inspired by Chinese period drama, 50mm f/2.0, 8K hyperdetailed, 35mm film grain, color graded teal-orange shadows warm highlights, aspect ratio 9:16" |

### Aturan Tambahan untuk Konsistensi Panji

1. **Selalu sebut "Javanese Hindu-Buddhist art, East Java 1100 CE"** — bukan "12th century Jenggala kingdom" yang ambigu
2. **Sebut referensi visual konkret**: "Prambanan relief style", "Penataran temple motif", "wayang topeng Malang"
3. **Warna kerajaan eksplisit**: "blue-gold palette (Jenggala)" atau "red-gold palette (Kediri)"
4. **Aspek rasio wajib**: 9:16 portrait ref / 16:9 cinematic segmen
5. **Negative prompt** (di-embed di prompt, Flow tidak punya field terpisah): `Avoid: modern clothing, western architecture, Chinese temple, Indian deity, anime, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature`
6. **Suhu lighting konkret**: 2700K (api), 5600K (bulan), 6500K (daylight), 2200K (api upacara)

---

## D. Audit Prompt Lama (Yang Masih Sampah)

### Contoh Prompt C001 — Versi Lama (Sampah)

```
Handsome Javanese crown prince, 28 years old, golden brown skin, sharp
eyes, long black hair partly tied in topknot with destar headwrap, thin
mustache, regal bearing, wearing blue-dark Javanese prince tunic with
gold embroidery, blue-gold batik kain, gold necklace, kris at waist,
gold kairo bracelets, standing in Javanese Hindu palace, 12th century
Jenggala kingdom East Java, cinematic lighting, 8K, hyperdetailed,
realistic portrait
```

**8 masalah:**

| # | Masalah | Konsekuensi |
|---|---------|-------------|
| 1 | Tidak ada shot type | Flow mungkin keluar wide shot |
| 2 | "Cinematic lighting" = sampah | Interpretasi bebas, hasil acak |
| 3 | Tidak ada mood konkret | "Tegas" tidak diterjemah ke visual |
| 4 | "Javanese Hindu palace" → ambigu | Bisa keluar kuil Bali/Thai |
| 5 | Tidak ada aspek rasio | Default 1:1 |
| 6 | Tidak ada referensi spesifik | Tidak sebut "Prambanan relief" |
| 7 | Negative prompt minim | Kurang |
| 8 | Tidak pakai struktur 5 komponen | Model tidak parse efisien |

**Yang sudah dilakukan:** Prompt C001-C004 dan L001-L005 sudah dirework ke format 5 komponen (lihat `characters.md` dan `visual-style.md`). Prompt murni siap pakai ada di `prompts/C001_panji.txt` dst.

---

## E. Strategi Iterasi — Multi-Turn Editing di Flow

### Prinsip Utama

> **JANGAN klik "Generate ulang"** saat hasil belum pas. Itu akan bikin karakter baru berbeda.
> **GUNAKAN multi-turn chat** untuk edit image yang sama, karakter tetap konsisten.

### Loop Iterasi (3 putaran maksimum)

```
Round 1: Generate dengan prompt awal (5 komponen)
  ↓
Quality Gate (lihat section F)
  ↓
Round 2: Multi-turn edit dengan feedback natural language di chat Flow:
  - "Make the lighting more dramatic — increase contrast ratio to 6:1,
     add stronger rim light on left shoulder, deepen the shadows on
     right side of face"
  - "The face looks too Chinese. Make the nose broader and flatter,
     eyes with minimal epicanthic fold, lips fuller — typical Javanese
     phenotype"
  - "The kain batik pattern is wrong. Use parang rusak — diagonal
     broken knife pattern, not geometric squares. Blue and gold only"
  ↓
Round 3: Final tweak via multi-turn
  - "Make the gold embroidery more intricate, add kala-makara motif
     (demon face with crocodile jaw) on chest"
  ↓
Lock → download → simpan sebagai refs/C00X_base.png
```

### Contoh Feedback Natural Language yang Efektif

**Tidak efektif (sampah):**
- ❌ "Make it better"
- ❌ "More cinematic"
- ❌ "Look more realistic"

**Efektif (presisi):**
- ✅ "Increase contrast ratio from 2:1 to 6:1"
- ✅ "Move key light from camera right to camera left at 45 degrees"
- ✅ "Add rim light on left shoulder using 5600K blue moonlight"
- ✅ "Make nose broader by 20%, reduce epicanthic fold, fuller lips"
- ✅ "Replace batik pattern with parang rusak (diagonal broken knife)"
- ✅ "Change tunic color from navy to deep midnight blue with subtle gold thread"

---

## F. Quality Gate — Checklist Sebelum Locking Ref Image

Setiap ref image harus lulus checklist ini sebelum dipakai untuk generate segmen:

### 1. Karakter Ref (C001-C004)
- [ ] Wajah terlihat Jawa (bukan Chinese/Indian/Thai) — verification: lebar hidung, lipatan epikantrik minimal, bibir penuh
- [ ] Kostum sesuai era 1100 CE (bukan Majapahit abad 14, bukan Mataram 17)
- [ ] Warna kerajaan benar (biru-emas Jenggala / merah-emas Kediri)
- [ ] Lighting sesuai mood babak
- [ ] Komposisi sesuai shot type
- [ ] Tidak ada elemen modern (kabel, kaca, listrik, plastik)
- [ ] Detail tekstur cukup (kulit dengan pori-pori, kain dengan serat)
- [ ] Aspek rasio sesuai target (9:16 portrait)
- [ ] Tangan tidak cacat (5 jari utuh, tidak ada jari tambahan)
- [ ] Tidak ada teks/watermark artefak

### 2. Lokasi Ref (L001-L005)
- [ ] Arsitektur Jawa Hindu-Buddha (bukan Chinese/Indian)
- [ ] Skala imperial terbaca (bukan desa kecil)
- [ ] Elemen maritime (untuk L004, L005): perahu, kanal, armada
- [ ] Multi-bangunan (bukan satu bangunan tunggal)
- [ ] Aspek rasio 16:9 cinematic
- [ ] Detail tekstur cukup (batu, kayu, genteng)
- [ ] Lighting konsisten dengan mood babak

### 3. Segmen (36 segmen)
- [ ] Karakter konsisten dengan ref image (wajah, kostum, warna)
- [ ] Setting konsisten dengan lokasi ref
- [ ] Lighting konsisten dengan mood babak di story bible
- [ ] Shot type sesuai storyboard
- [ ] Komposisi sesuai camera angle di storyboard
- [ ] Tidak ada elemen modern
- [ ] Tidak ada teks/watermark

Jika satu kotak tidak tercentang → prompt masih sampah → iterasi lagi via multi-turn chat.

---

## G. Konsistensi Karakter — Strategi Reference Image di Flow

### Cara Upload Reference Image di Flow

```
1. Buka project di Flow
2. Di chat box, klik icon "📎" / "Add image" / "Upload reference"
3. Pilih file PNG dari komputer (refs/C001_base.png)
4. Tambah prompt:
   "Generate wide shot of [karakter] seated on stone throne in
    Javanese palace, 16:9 cinematic, 8K hyperdetailed"
5. Generate

Flow akan menggunakan reference image sebagai panduan:
- Wajah karakter akan konsisten
- Kostum akan konsisten
- Hanya pose, angle, dan setting yang berubah sesuai prompt
```

### Bisa Upload Hingga 14 Reference Image Sekaligus

Untuk segmen dengan dua karakter (mis. S005_seg17: Panji & Candra Kirana):
```
Upload:
- refs/C001_base.png (Panji)
- refs/C002_base.png (Candra Kirana)

Prompt:
"Medium two-shot, Panji (ref 1) and Candra Kirana (ref 2) facing each
 other at riverside, sunrise, mist, banyan tree, both in royal attire,
 12th century East Java, cinematic, 8K, hyperdetailed"
```

### Strategi 3 Tier Konsistensi

| Tier | Pakai untuk | Metode | Konsistensi |
|------|-------------|--------|-------------|
| 1 | **Pilot 3 menit** (saat ini) | Upload ref image per segmen | 80-90% |
| 2 | Mini-series 12 episode | Latih "Project" di Flow dengan asset library | 90-95% |
| 3 | Full series 24+ episode | Custom Tools di Flow (Vibe code) | 95%+ |

---

## H. Batasan Google Flow yang Perlu Diketahui

| Batasan | Detail | Workaround |
|---------|--------|------------|
| **SynthID watermark** | Otomatis tertanam di setiap gambar (invisible) | Tidak bisa dihilangkan — accept this |
| **Max 14 reference images per request** | Cukup untuk 4 karakter + 5 lokasi + 5 ekstra | Jika perlu lebih, generate bertahap |
| **Resolution max 4K** | Cukup untuk pilot, mungkin kurang untuk IMAX | Upscale via Real-ESRGAN post-processing |
| **No explicit seed control di web UI** | Tidak bisa lock seed untuk reproducibility | Catat prompt + iterasi via multi-turn chat |
| **1 image per generate di web** | Tidak bisa batch-generate 4 variasi sekaligus | Generate 4x dengan prompt sama, atau pakai "Variations" feature |
| **Rate limit** | Free tier: 50 credit/hari | Spread generation, atau upgrade ke Pro |
| **Aspect ratios supported** | 1:1, 3:4, 4:3, 9:16, 16:9 (terbatas) | Tidak ada 2.35:1 cinematic — gunakan 16:9 + crop post |
| **Credit tidak menumpuk** | Yang tidak terpakai hilang | Plan ahead, jangan boros credit |
| **Veo 3.1 mahal** | ~100 credit per generate | Generate 36 segmen = 3.600 credit → butuh Ultra plan |
| **Web only** | Tidak ada script lokal/CLI | Manual di browser, atau pakai Gemini API terpisah |

---

## I. Cost Estimation untuk Pilot 3 Menit via Flow

### Asumsi
- 4 karakter ref × 3 iterasi rata-rata = 12 generate
- 5 lokasi ref × 3 iterasi = 15 generate
- 36 segmen × 1 iterasi = 36 generate (kalau ref image dipakai, iterasi segmen lebih sedikit)
- Total ~63 image generate

### Estimasi Credit

| Komponen | Generate count | Credit per generate | Total credit |
|----------|----------------|---------------------|--------------|
| Karakter ref | 12 | ~10 | 120 |
| Lokasi ref | 15 | ~10 | 150 |
| Segmen image | 36 | ~10 | 360 |
| **Subtotal image** | 63 | — | **630** |
| Segmen video (Veo 3.1) | 36 | ~100 | 3.600 |
| **Grand total** | — | — | **4.230** |

### Pilihan Plan

| Plan | Credit bulanan | Cukup untuk? |
|------|----------------|--------------|
| Free (50/hari) | ~1.500/bulan | Image saja, video terbatas |
| AI Plus ($9.99) | 1.200/bulan + 50/hari | Image saja, video kurang |
| **AI Pro ($19.99)** | 1.050/bulan + 50/hari | Image pilot (630 credit) ✅ |
| AI Ultra $100 | 10.000/bulan | Image + video pilot ✅ |
| AI Ultra $200 | 25.000/bulan | Image + video + mini-series |

**Rekomendasi pilot:**
- **Fase 1 (image saja)**: AI Pro ($19.99/bulan) — cukup untuk 4 karakter + 5 lokasi + 36 segmen
- **Fase 2 (video)**: Upgrade ke AI Ultra $100 selama 1 bulan untuk generate 36 video segments

---

## J. Checklist Sebelum Mulai Generate di Flow

Sebelum buka flow.google.com dan generate:

1. ✅ Semua prompt sudah pakai struktur 5 komponen (Subject/Setting/Lighting/Mood/Style)
2. ✅ Setiap prompt sebut "Javanese Hindu-Buddhist art, East Java 1100 CE"
3. ✅ Setiap prompt sebut warna kerajaan (biru-emas / merah-emas)
4. ✅ Aspect ratio ditentukan (9:16 ref, 16:9 segmen)
5. ✅ Negative prompt lengkap (10+ item)
6. ✅ Lighting konkret (Kelvin + arah + rasio kontras)
7. ✅ Lensa/teknis spesifik (50mm, f/2.0, dll)
8. ✅ Reference visual disebut (Prambanan, Penataran, wayang Malang)
9. ✅ Mood konkret (bukan "cinematic" generik)
10. ✅ Quality gate checklist siap
11. ✅ Google account aktif
12. ✅ Subscribe ke plan yang cukup (minimal AI Pro $19.99 untuk image, AI Ultra $100 untuk video)
13. ✅ Folder tujuan siap: `produksi/panji/refs/` dan `produksi/panji/segments/`
14. ✅ File prompt siap di `produksi/panji/pre-produksi/prompts/C001-C004_*.txt`

---

## K. File yang Sudah Siap di Repo

```
produksi/panji/
├── pre-produksi/
│   ├── story-bible.md          ✅ (plot + sumber)
│   ├── characters.md           ✅ (profil + T2I prompt 5-komponen)
│   ├── visual-style.md         ✅ (lokasi + T2I prompt 5-komponen)
│   ├── storyboard-pilot.json   ✅ (36 segmen, prompt sudah diupdate)
│   ├── prompt-engineering-guide.md  ✅ (file ini)
│   └── prompts/                ✅ (4 prompt murni siap copy-paste ke Flow)
│       ├── C001_panji.txt
│       ├── C002_candra_kirana.txt
│       ├── C003_patih.txt
│       └── C004_mpu_dharmaja.txt
├── refs/                       ← akan diisi hasil download dari Flow
│   ├── C001_base.png
│   ├── C002_base.png
│   ├── C003_base.png
│   ├── C004_base.png
│   ├── L001_base.png s/d L005_base.png
└── segments/                   ← akan diisi hasil download dari Flow
    └── S001_seg01/ s/d S009_seg36/
        └── image.png + video.mp4
```

---

## L. Quick Reference — Cara Pakai Flow untuk Pilot

### Generate 1 Karakter Ref

```
1. Buka https://flow.google.com → login
2. Create new project → "Panji Pilot - Characters"
3. Pilih model: Nano Banana
4. Set: Aspect ratio 9:16, Resolution 2K
5. Buka file: produksi/panji/pre-produksi/prompts/C001_panji.txt
6. Copy seluruh isi → paste ke chat Flow
7. Klik Generate
8. Review, lalu iterate via multi-turn chat:
   "Make the lighting more dramatic, increase contrast to 6:1"
9. Setelah quality gate lulus → Download
10. Simpan ke: produksi/panji/refs/C001_base.png
```

### Generate 1 Segmen dengan Reference Image

```
1. Buka project "Panji Pilot - Segmen Images" di Flow
2. Buka file storyboard-pilot.json, cari segmen (mis. S001_seg04)
3. Copy prompt dari field "visual.prompt"
4. Paste ke chat Flow
5. Klik icon "📎" / "Add image" di sebelah chat box
6. Upload: produksi/panji/refs/C001_base.png
7. Set: Aspect ratio 16:9, Resolution 2K
8. Generate → review → iterate via chat
9. Download → simpan ke: produksi/panji/segments/S001_seg04/image.png
```

### Iterate via Multi-Turn Chat

```
Setelah generate pertama (image muncul di chat), jangan generate ulang.

Ketik feedback di chat box:
"Make the lighting more dramatic. Increase contrast ratio to 6:1.
 Add stronger rim light on left shoulder. Deepen shadows on right
 side of face."

Flow akan edit image sebelumnya, bukan generate baru.
Karakter tetap konsisten, hanya elemen yang disebut berubah.

Ulangi 2-3x sampai quality gate lulus.
```

---

## M. Sumber Resmi

- **Google Flow (Web App)**: https://flow.google.com
- **Google Flow Help Center**: https://support.google.com/flow
- **Google AI Plans (Pricing)**: https://one.google.com/about/google-ai-plans
- **Manage Flow credits**: https://support.google.com/flow/answer/16526234
- **Nano Banana model info**: https://aistudio.google.com/models/nano-banana
- **Nano Banana docs (image generation)**: https://ai.google.dev/gemini-api/docs/image-generation
