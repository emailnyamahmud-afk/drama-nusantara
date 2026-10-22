# Cara Pakai T2I Prompts di Dola AI

> **Platform**: Dola AI (https://dola.com/chat/create-image)
> **Model utama**: Seedream 4.5 (juga dukung Nano Banana 2/2 Lite/Pro, GPT Image 2/2.5, Seedream 5.0 Lite/Pro)
> **Tanggal**: 2026-10-22 (v2 — standar horizontal)
> **Sumber**: riset via WebSearch + WebFetch ke dola.com, dola-ai.com, dolai.video/how-to-use, fal.ai Seedream guide, BytePlus ModelArk docs

---

## ⚠️ Perubahan v2 (2026-10-22)

1. **Aspect ratio default berubah** — tidak lagi semua 9:16 portrait. Sekarang:
   - **K** (karakter ref sheet 5-angle SINGLE INDIVIDU): **16:9 horizontal** — 5 angle side-by-side lebih natural
   - **L** (latar/lokasi cinematic): **16:9 horizontal** — cinematic landscape untuk produksi
   - **A** (artefak macro detail): **1:1 square** — macro detail seimbang
   - **F** (fauna/cuaca): **16:9 horizontal** — cinematic animal scene
   - **S** (scene multi-karakter — tipe baru): **16:9 horizontal** — adegan untuk produksi
2. **Aturan K vs S** (penting!):
   - **K = SELALU single karakter** (1 individu, 5 angle turnaround di studio). Jangan pernah buat K dengan multiple karakter — Dola akan bingung.
   - **S = scene multi-karakter** (1 angle cinematic, komposisi grup dalam setting). Untuk adegan dengan 2+ karakter.
   - Kalau perlu ref sheet karakter individu → K. Kalau perlu adegan grup → S.
3. **Aturan costume/propriety** (penting untuk content filter):
   - Untuk anak/juvenile: SELALU tambahkan `"wearing a minimal barkcloth loincloth"` atau garment primitif sederhana — Dola AI content filter akan menolak gambar anak telanjang.
   - Untuk dewasa: boleh `"naked torso"` (bagian atas) tapi selalu pakai barkcloth wrap untuk bagian bawah.
4. **Style keyword wajib di awal**: `Cinematic realistic documentary...`
5. **Naming konsisten**: `{era}-{tipe}{nomor:03d}-{slug-lowercase}.txt`
   - Contoh: `1A-K001-homo-erectus-dewasa.txt`, `1A-L001-paparan-sunda.txt`, `1A-S001-kelompok-berburu.txt`
6. **Negative prompt** tetap di akhir dengan `Avoid:` prefix
7. **Semua file L**: "No people, no characters, no humans — empty location reference"

---

## A. Apa Itu Dola AI?

Dola AI adalah platform creative studio berbasis web yang menggabungkan:
- **Image generation** (text-to-image, image-to-image)
- **Video generation** (text-to-video, image-to-video)
- **Photo editor** (canvas multi-layer: inpainting, outpainting, blend)
- **Document tools** (PDF, spreadsheet, slides)

**URL utama**: https://dola.com/chat/create-image

**Login**: pakai Google account (tombol "Log In" di kanan atas)

**Sistem credit**:
- AI image generation pakai credit
- Manual editing + save project = tidak pakai credit
- Estimasi credit ditampilkan sebelum setiap generate
- Free credits tersedia saat signup

---

## B. 6 Langkah Konkret Pakai T2I Prompts di Dola AI

### Langkah 1 — Buka Dola AI + Pilih Mode

1. Buka browser → https://dola.com/chat/create-image
2. Login pakai Google account
3. Setelah login, di sebelah kiri ada opsi mode:
   - **Text-to-Image** ← mode utama untuk pakai prompt di repo
   - **Text-to-Video** ← pakai saat generate video
   - **Image-to-Image** ← pakai saat refine via reference image
4. Pilih **Text-to-Image** untuk awal

### Langkah 2 — Pilih Model

Di panel kanan, pilih model:
- **Seedream 4.5** (default — pilihan utama, kualitas terbaik)
- **Seedream 5.0 Lite** (lebih cepat, lebih murah)
- **Seedream 5.0 Pro** (kualitas tertinggi, lebih mahal)
- **Nano Banana 2** / **Nano Banana 2 Lite** / **Nano Banana Pro** (model Google, alternatif)
- **GPT Image 2** / **2.5** (model OpenAI)

**Rekomendasi untuk proyek prasejarah 1A-1D**:
- Default: **Seedream 4.5** (kualitas tinggi, photorealistic)
- Untuk portrait karakter: **Nano Banana Pro** (konsistensi wajah lebih baik)
- Untuk landscape cinematic: **Seedream 5.0 Pro** (detail tinggi)

### Langkah 3 — Adaptasi Prompt 5-Komponen ke Format Dola AI

Prompt di repo (`produksi/t2i-prompts/1A-1D/README.md`) sudah dalam format 5-komponen Google (Subject/Setting/Lighting/Mood/Style). Dola AI (Seedream 4.5) lebih optimal dengan prompt natural-language yang flat.

**Cara adaptasi — gabungkan 5 komponen jadi 1 paragraf flat:**

### Contoh: 1A-K001 (Homo erectus Dewala)

**Format 5-komponen di repo** (tidak langsung dipakai di Dola):
```
SUBJECT: Medium close-up portrait of an adult Homo erectus...
SETTING: Open savanna landscape of Paparan Sunda 1.8 million years ago...
LIGHTING: Warm 3500K late afternoon sun from camera left...
MOOD: Primitive survival, ancient wisdom...
STYLE: Cinematic realistic documentary portrait...
```

**Adaptasi ke Dola AI (flat prompt)**:
```
Cinematic realistic documentary portrait of an adult Homo erectus from
Pleistocene Awal Java, medium close-up, three-quarter view facing camera
left, calm vigilant expression looking toward horizon. Male, 30-40 years
old, 155 cm tall, golden brown weathered skin, deep-set dark brown eyes
under heavy supraorbital brow ridge, low sloping forehead, broad flat
nose, full lips, prognathic jaw. Long black coarse hair tangled, no
beard grooming. Naked torso, skin marked by natural exposure. Holding
a chert flake tool in right hand. Setting: open savanna landscape of
Paparan Sunda 1.8 million years ago, East Java, tropical grassland with
scattered acacia trees, meandering paleo-river, volcanic mountains on
horizon. Stegodon grazing in distance. Lighting: warm 3500K late
afternoon sun from camera left, golden amber on skin, high contrast 4:1.
Mood: primitive survival, ancient wisdom, first human presence in
Nusantara. Style: photorealistic skin texture with visible pores and
imperfections, weathered dirt and sweat, 35mm film grain, shallow depth
of field f/2.0, 50mm lens equivalent, 8K hyperdetailed, color graded
warm amber highlights cool blue shadows, National Geographic documentary
aesthetic, high detail, 4K, sharp focus.
```

**Aturan adaptasi:**
1. Hapus label `SUBJECT:`, `SETTING:`, `LIGHTING:`, `MOOD:`, `STYLE:`
2. Mulai dengan **style keyword** di awal (`Cinematic realistic documentary portrait of...`)
3. Gabungkan semua elemen jadi paragraf yang mengalir
4. Akhiri dengan **quality tag**: `high detail, 4K, sharp focus`
5. **Negative prompt**: masuk ke field terpisah "Negative prompt" di Dola AI (jika tersedia), atau gabungkan ke akhir prompt dengan `Avoid:` prefix

### Langkah 4 — Set Parameter

Di panel kanan Dola AI, set parameter:

| Parameter | Setting untuk proyek prasejarah |
|-----------|---------------------------------|
| **Model** | Seedream 4.5 (default) atau Nano Banana Pro (karakter) |
| **Ratio** | 9:16 portrait untuk karakter ref, 16:9 untuk cinematic, 1:1 untuk macro |
| **Style** | Pilih preset "Cinematic" atau "Photorealistic" jika tersedia, atau biarkan "Auto" |
| **Templates** | Pilih template "Portrait" / "Landscape" jika tersedia |
| **Number of outputs** | 4 (generate 4 variasi, pilih terbaik) |
| **Seed** | Catat seed yang bagus untuk reproducibility (kolom "Advanced settings") |

### Langkah 5 — Upload Reference Image (Untuk Konsistensi Karakter)

Untuk segmen yang melibatkan karakter yang sudah punya ref image:

1. Di bawah chat box, klik ikon **📎 (Upload)** atau drag-and-drop file
2. Upload hingga **10 reference image** sekaligus (format: jpg, png, jpeg, webp)
3. Untuk konsistensi karakter:
   - Upload `refs/1A-K001_homo_erectus.png` sebagai reference
   - Tambah prompt: "Use IMAGE 1 as the exact main character reference. Preserve the exact face, identity, body proportions."
4. Untuk **multi-image blending** (2 karakter di 1 scene):
   - Upload 2 reference image (mis. Panji + Candra Kirana)
   - Tambah prompt: "Combine [karakter 1 from ref 1] and [karakter 2 from ref 2] in same scene"

### Langkah 6 — Generate, Review, Iterate via Canvas

1. Klik **Generate** → tunggu 5-30 detik
2. Review 4 hasil → pilih yang terbaik
3. **Jangan Generate ulang** kalau belum pas — pakai **Canvas Editor** untuk refine:
   - **Inpainting**: pilih area spesifik (mis. wajah) → ganti prompt area itu saja
   - **Outpainting**: extend scene ke luar frame asli
   - **Multi-layer blend**: gabungkan 2-3 hasil generate jadi 1 komposisi
4. Iterasi via chat natural language:
   - "Make the lighting more dramatic, increase contrast"
   - "The brow ridge is too thin — make it thicker like Homo erectus"
   - "Add more Pleistocene fauna in the background"
5. Setelah quality gate lulus → **Download** (PNG atau JPEG)

---

## C. Template Adaptasi — Flat Prompt untuk Dola AI

Saya buat template konversi dari 5-komponen ke flat prompt Dola AI.

### Template Konversi

```
[STYLE_KEYWORD] [SHOT_TYPE] of [SUBJECT_DESCRIPTION],

[SETTING_DESCRIPTION],

[KEY_PROPS_AND_DETAILS],

Lighting: [LIGHTING_DESCRIPTION],

Mood: [MOOD_DESCRIPTION],

Style: [TECHNICAL_SPECS],

Aspect ratio [X:Y], high detail, 4K, sharp focus.

Avoid: [NEGATIVE_PROMPT_ITEMS]
```

### Contoh Konversi: 1D-L001 (Punden Berundak Gunung Padang)

**5-komponen di repo:**
```
SUBJECT: Wide cinematic aerial establishing shot of Punden Berundak
Gunung Padang, Cianjur, West Java, 200 BC. Massive stepped stone pyramid...

SETTING: Gunung Padang, Cianjur, West Java, 200 BC. Largest punden
berundak site in Indonesia...

LIGHTING: Warm 3500K morning sun from camera right...

MOOD: Sacred mountain, the monumental expression of ancestor worship...

STYLE: Cinematic realistic documentary aerial landscape...
```

**Flat prompt untuk Dola AI:**
```
Cinematic realistic documentary aerial landscape of Punden Berundak
Gunung Padang, Cianjur, West Java, 200 BC. Massive stepped stone pyramid
made of andesite blocks, multiple terraces rising from base to peak
(5+ terraces visible). Uppermost terrace has a menhir (standing stone).
Tropical rainforest covering surrounding hills. A small group of
perundagian community members (5-7 figures, tiny silhouettes) gathered
on middle terrace for ritual — one leader (primus inter pares)
addressing the group, others in deliberation. Distant volcanic mountains.

Setting: Gunung Padang, largest punden berundak site in Indonesia, 38
other sites in Cianjur area. Andesite stone, weathered and lichen-covered.

Lighting: warm 3500K morning sun from camera right, raking across
terraces revealing stone texture, long shadows, cool 6500K sky fill
from above, mid contrast 3:1, mist in valley.

Mood: sacred mountain, monumental expression of ancestor worship,
punden berundak as architectural form of megalithic belief.

Style: photorealistic andesite stone textures (weathered, lichen-covered),
35mm film grain, deep depth of field f/8, 16mm ultra-wide lens equivalent
for epic scale, 8K hyperdetailed, color graded warm earth tones (grey
andesite, green forest), BBC Earth documentary aesthetic.

Aspect ratio 16:9, high detail, 4K, sharp focus.

Avoid: modern buildings, modern tourism, modern researchers, modern
equipment, modern stairs/handrails, anime style, cartoon, 3D render,
watermark, text, signature, low resolution, blurry, oversaturated,
modern agricultural clearing.
```

---

## D. Strategi Pakai Reference Image di Dola AI

### Tier 1: Karakter Ref (Pilot)

1. Generate 1 karakter ref pertama (mis. 1A-K001 Homo erectus) tanpa reference image
2. Iterate sampai quality gate lulus (wajah Jawa, bukan modern)
3. Download → simpan ke `refs/1A-K001_homo_erectus.png`
4. Untuk segmen berikutnya yang melibatkan karakter yang sama:
   - Upload `1A-K001_homo_erectus.png` sebagai reference
   - Tambah prompt: "Use uploaded image as character reference. Maintain face, body, costume, but change pose and setting to [new scene]"

### Tier 2: Multi-Karakter Scene

Untuk scene dengan 2 karakter (mis. 1D-K001 primus inter pares + pengrajin):

1. Upload 2 reference image:
   - `refs/1D-K001_primus_inter_pares.png`
   - `refs/1D-K002_undagi.png`
2. Tambah prompt: "Combine character from ref 1 (primus inter pares, leader) with character from ref 2 (undagi, metal craftsman) in same scene. Both in their respective costumes. Ref 1 standing on terrace, ref 2 working at furnace below."

### Tier 3: Style Transfer (Untuk Konsistensi Visual Seluruh Era)

1. Setelah dapat 3-4 ref image untuk era tertentu (mis. 1A)
2. Upload semua 3-4 sebagai reference saat generate image baru di era yang sama
3. Tambah prompt: "Maintain visual style and color palette of uploaded references. New subject: [deskripsi]"

---

## E. Workflow Lengkap per Era

Untuk era 1A sebagai contoh:

```
STEP 1: Generate Karakter Ref (3-4 image)
  1A-K001 Homo erectus dewasa
  1A-K002 Anak Mojokerto
  1A-K003 Kelompok berburu
  
  → Pakai prompt flat (sesuaikan dari 5-komponen)
  → Model: Seedream 4.5 atau Nano Banana Pro
  → Ratio: 9:16 portrait
  → Generate 4 variasi, pilih terbaik
  → Iterate via canvas sampai quality gate lulus
  → Download ke refs/1A-K001_homo_erectus.png dst

STEP 2: Generate Latar Ref (4-5 image)
  1A-L001 Paparan Sunda
  1A-L002 Kubah Sangiran stratigrafi
  1A-L003 Lembah Bengawan Solo purba
  1A-L004 Bumiayu
  
  → Pakai prompt flat
  → Model: Seedream 5.0 Pro (kualitas tertinggi untuk landscape)
  → Ratio: 16:9 cinematic
  → Generate 4 variasi, pilih terbaik
  → Download ke refs/1A-L001_paparan_sunda.png dst

STEP 3: Generate Macro / Artefak (2-3 image)
  1A-P001 Alat batu serpih
  1A-P002 Tengkorak Trinil
  1A-F001 Stegodon + fauna
  
  → Pakai prompt flat
  → Model: Seedream 4.5
  → Ratio: 1:1 square macro
  → Generate 4 variasi, pilih terbaik
  → Download ke refs/1A-P001_alat_batu.png dst

STEP 4: Generate Scene dengan Karakter + Latar (kalau perlu)
  Untuk scene yang melibatkan karakter di latar:
  → Upload karakter ref + latar ref
  → Prompt: "Combine [karakter] from ref 1 in [latar] from ref 2"
  → Ratio: 16:9 cinematic

STEP 5: Quality Gate per Era
  Cek semua image di era tersebut:
  [ ] Wajah/wajah sesuai era (Homo erectus vs Homo sapiens)
  [ ] Kostum sesuai era (no clothing di 1A-1C, barkcloth di 1D)
  [ ] Latar period-akurat (Pleistosen vs Holosen vs Zaman Logam)
  [ ] Fauna pleistosen (Stegodon, bukan modern elephant)
  [ ] Tidak ada elemen modern
  [ ] Detail tekstur cukup
  [ ] Aspek rasio sesuai target
```

---

## F. Iterasi Multi-Turn di Dola AI

Dola AI mendukung iterasi via canvas editor + chat natural language. JANGAN klik Generate ulang untuk refine.

### Contoh Iterasi untuk 1A-K001 (Homo erectus)

**Round 1**: Generate dengan prompt flat
→ Review: wajah terlalu modern (high forehead, thin brow ridge)

**Round 2**: Pilih area wajah di canvas → inpaint dengan prompt:
```
Make this face more Homo erectus: heavier supraorbital brow ridge
(thick bone above eyes), lower sloping forehead, broader flat nose,
more prognathic jaw. Reduce chin projection. Ancient human features,
NOT modern Homo sapiens.
```

**Round 3**: Pilih area background → inpaint:
```
Add more Pleistocene fauna in distance — a herd of Stegodon
(extinct elephant with downward-curving tusks) grazing in far
background. Add antelopes and deer. Increase dust haze in air.
```

**Round 4**: Final tweak via chat:
```
Make the overall lighting more dramatic. Increase contrast to 6:1.
Add rim light on subject's left shoulder using cool 5600K blue
moonlight.
```

**Round 5**: Lock seed → catat seed untuk reproducibility
→ Download final → simpan ke `refs/1A-K001_homo_erectus.png`

---

## G. Tips Khusus Seedream 4.5 di Dola AI

Berdasarkan riset Seedream 4.5 (sumber: BytePlus ModelArk docs, fal.ai Seedream guide):

### 1. Struktur Prompt Optimal

```
[STYLE_KEYWORD]: [SUBJECT] [ENVIRONMENT] [LIGHTING] [MOOD] [TECHNICAL_SPECS]
```

Contoh:
```
Cinematic documentary: an adult Homo erectus in Pleistocene savanna,
warm golden hour lighting, primitive survival mood, 35mm film grain,
8K hyperdetailed, high detail, 4K, sharp focus.
```

### 2. Style Keyword di Awal

Seedream 4.5 responsif terhadap style keyword di awal prompt:
- `Cinematic:` → film-like lighting + depth of field
- `Photorealistic:` → hyperreal skin texture
- `Documentary:` → naturalistic, no stylization
- `Anime style:` → cartoonish
- `Studio Ghibli style:` → anime lembut

Untuk proyek prasejarah: selalu mulai dengan `Cinematic realistic documentary`

### 3. Quality Tag di Akhir

Selalu akhiri prompt dengan:
```
high detail, 4K, sharp focus, hyperdetailed
```

### 4. Multi-Image Blending

Seedream 4.5 dukung multi-image blending:
- Upload 2 image untuk blend
- Tambah prompt deskriptif tentang cara combine
- Specify style yang harus dipertahankan dari masing-masing source

### 5. Iterative Refinement

Lebih baik iterate 3-4 kali dengan prompt yang sedikit diubah, daripada 1x dengan prompt super kompleks. Pakai seed yang sama untuk compare perubahan.

---

## H. Perbandingan Dola AI vs Google Flow

| Aspek | Dola AI | Google Flow |
|-------|---------|-------------|
| URL | dola.com/chat/create-image | flow.google.com |
| Model | Seedream 4.5/5.0, Nano Banana series, GPT Image | Nano Banana 2.1, Veo 3.1 |
| Login | Google account | Google account |
| Reference image | Up to 10 file (jpg/png/jpeg/webp) | Up to 14 image |
| Multi-image blend | Ya (2 image per operasi) | Ya (chat natural language) |
| Canvas editor | Ya (inpaint, outpaint, multi-layer) | Ya (multi-turn chat) |
| Aspect ratio | 9:16, 16:9, 1:1 | 9:16, 16:9, 1:1, 3:4, 4:3 |
| Resolution | 4K max | 4K max |
| Credit | Pakai credit (free credits saat signup) | 50/hari free, 200-25000/bln berdasar plan |
| Negative prompt | Ya (field terpisah atau `Avoid:` prefix) | Tidak ada field terpisah (embed di prompt) |
| Iterasi | Canvas editor + chat | Multi-turn chat |
| Strength | Multi-layer canvas editor, banyak model pilihan | Konsistensi karakter via reference image, integrasi Veo |

**Rekomendasi**: Pakai Dola AI untuk pilot prasejarah 1A-1D karena:
- Canvas editor lebih powerful untuk iterative refinement
- Seedream 4.5 kualitas photorealistic lebih baik untuk Homo erectus
- Multi-image blending untuk scene multi-karakter
- Lebih ekonomis (free credits signup + tidak perlu subscription mahal)

---

## I. Checklist Sebelum Mulai Generate di Dola AI

Sebelum buka dola.com dan generate:

1. ✅ Sudah baca master-era untuk era yang mau digenerate (mis. 1A)
2. ✅ Sudah baca T2I prompts untuk era itu (`produksi/t2i-prompts/1A-prasejarah-pleistosen-awal/README.md`)
3. ✅ Sudah adaptasi prompt 5-komponen ke flat prompt Dola AI (lihat section C)
4. ✅ Sudah tentukan model: Seedream 4.5 (default) / Nano Banana Pro (karakter)
5. ✅ Sudah tentukan aspect ratio: 9:16 (karakter) / 16:9 (cinematic) / 1:1 (macro)
6. ✅ Sudah siap folder output: `refs/1A-K001_homo_erectus.png` dst
7. ✅ Sudah siap quality gate checklist per era
8. ✅ Sudah login Google account di dola.com

---

## J. Sumber Riset

| Sumber | URL | Dipakai untuk |
|--------|-----|---------------|
| Dola AI (official) | https://dola.com/chat/create-image | URL utama, interface |
| Dola AI How-To Guide | https://www.dolai.video/how-to-use | 6 langkah pakai, prompt tips |
| Dola-AI.com | https://dola-ai.com | Daftar fitur lengkap |
| Seedream 4.5 Prompt Guide (BytePlus) | https://docs.byteplus.com/en/docs/ModelArk/1829186 | Struktur prompt optimal |
| Seedream v4.5 Prompt Guide (fal.ai) | https://fal.ai/learn/devs/seedream-v4-5-prompt-guide | Multi-image blending, troubleshooting |
| Seedream 4.5 Complete Guide (WaveSpeed) | https://wavespeed.ai/blog/posts/seedream-4-5-complete-guide-2026 | Perbandingan model, best practices |
| Twelve Tools — Dola AI review | https://twelve.tools/dolai-pro | Info credit, fitur |
