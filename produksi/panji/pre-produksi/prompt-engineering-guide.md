# T2I Prompt Engineering Guide — Panji: Asmara Bangun

## Untuk Google AI Studio (Imagen 3 / Nano Banana)

> **Sumber**: Google's official prompting guide untuk image generation — struktur 5 komponen inti: **Subject → Setting → Lighting → Mood → Style/Material**.
> Dokumen ini menjelaskan workflow Google AI Studio + audit + rework prompt pre-produksi.

---

## A. Workflow Google AI Studio

### Langkah-Langkah Konkret

```
1. Buka https://aistudio.google.com → sign in pakai Google account

2. Pilih model:
   - Untuk gambar: pilih "Imagen 3" (atau "imagen-3.0-generate-002")
   - Untuk multimodal (teks + gambar): pilih "Gemini 2.5 Flash"
     (model "nano-banana" — bisa edit/restyle gambar)

3. Buat prompt baru:
   - Klik "Create Prompt" → "Image Generation"
   - Tempel prompt dari file pre-produksi (format 5 komponen)
   - Set parameter:
     • aspect_ratio: "9:16" untuk portrait / "16:9" untuk cinematic
     • sample_count: 4 (generate 4 variasi, pilih terbaik)
     • seed: catat seed yang bagus untuk reproducibility
     • guidance_scale: 7.5 (default, naikkan ke 10+ untuk prompt ketat)

4. Generate → review 4 hasil → pilih terbaik → download

5. Konsistensi karakter (referensi Imagen 3):
   - Setelah dapat ref image yang bagus, simpan URL file-nya
   - Untuk segmen berikutnya, sertakan referensi via "Image as input"
     (Imagen 3 + Gemini 2.5 Flash bisa pakai reference image)
   - Atau pakai LoRA training di Vertex AI untuk konsistensi penuh
```

### Tools Google Lain yang Bisa Dipakai

| Tool | URL | Cocok untuk |
|------|-----|-------------|
| **Google AI Studio** | aistudio.google.com | Prototype, eksperimen prompt |
| **Vertex AI Model Garden** | console.cloud.google.com/vertex-ai | Production batch generation |
| **Google Labs ImageFX** | labs.google/fx/tools/image-fx | Quick T2I tanpa coding |
| **Gemini API** | ai.google.dev | Pipeline programatik via Python SDK |

---

## B. Audit Prompt Lama (Yang Masih Sampah)

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

**Masalah:**

| # | Masalah | Konsekuensi |
|---|---------|-------------|
| 1 | Tidak ada shot type (medium close-up? full body?) | Imagen mungkin keluar wide shot, wajah kecil |
| 2 | "Cinematic lighting" = sampah | Imagen interpretasi bebas, hasil acak |
| 3 | Tidak ada mood konkret | "Tegas" tidak diterjemah ke visual |
| 4 | "Javanese Hindu palace" → Imagen bingung | Bisa keluar kuil Bali atau candi Thailand |
| 5 | Tidak ada aspek rasio | Default 1:1, tidak cocok untuk film 16:9 |
| 6 | Tidak ada referensi spesifik | Tidak sebut "Prambanan relief", "Penataran motif" |
| 7 | Negative prompt minim | Hanya "modern, western, building" — kurang |
| 8 | Tidak pakai struktur 5 komponen Google | Imagen tidak parse efisien |

---

## C. Struktur Prompt Baru (5 Komponen Google)

Setiap prompt T2I untuk proyek ini harus pakai format berikut:

```
[SUBJECT] + [SETTING] + [LIGHTING] + [MOOD] + [STYLE/MATERIAL]

SUBJECT   : Siapa/apa, shot type, pose, ekspresi, kostum detail
SETTING   : Lokasi konkret, era, elemen latar (candi, kanal, pasar)
LIGHTING  : Suhu warna (Kelvin), arah, intensitas, jenis (rim/key/fill)
MOOD      : Emosi/atmosfer (tegas, sakral, romantis, mencekam)
STYLE     : Reference visual, aspek rasio, technical specs (8K, hyperdetailed)
```

### Aturan Tambahan untuk Konsistensi Panji

1. **Selalu sebut "Javanese Hindu-Buddhist art, East Java 1100 CE"** — bukan "12th century Jenggala kingdom East Java" yang ambigu
2. **Sebut referensi visual konkret**: "Prambanan relief style", "Penataran temple motif", "wayang topeng Malang"
3. **Warna kerajaan eksplisit**: "blue-gold palette (Jenggala)" atau "red-gold palette (Kediri)"
4. **Aspek rasio wajib**: `16:9` untuk cinematic wide, `9:16` untuk portrait ref, `1:1` untuk thumbnail
5. **Negative prompt lengkap**: `modern clothing, western architecture, Chinese temple, Indian deity, anime, cartoon, 3D render, plastic skin, deformed hands, watermark, text, signature`
6. **Suhu lighting**: `2700K warm torch` (api), `5600K cool moonlight` (malam), `6500K daylight` (fajar)

---

## D. Prompt Rework — C001 (Panji Asmara Bangun) Versi Baru

```
SUBJECT: Medium close-up portrait of a 28-year-old Javanese crown
prince, three-quarter view facing camera left, calm determined
expression with slight confident smile, long black hair partially
tied in sanggul topknot with blue-gold destar headwrap, thin mustache,
golden brown skin, sharp dark brown eyes. Wearing dark blue Javanese
prince tunic with gold thread embroidery (kala-makara motif on chest,
foliate scrolls on shoulders), blue-gold batik kain (parang rusak
pattern) from waist down, gold keyura armlet on left upper arm, gold
kankana bracelets on both wrists, kris pusaka with golden hilt at
left waist.

SETTING: Interior of Javanese Hindu-Buddhist imperial palace, East
Java 1100 CE, Prambanan/Penataran temple relief style architecture.
Stone andesite pillars with carved kala-makara, palm fiber (ijuk)
roof visible at top, gold mesh curtains blowing softly in wind,
multiple bronze torches along corridor in background.

LIGHTING: Warm 2700K torch light from camera right (key light, warm
amber glow on face), cool 5600K moonlight from window left (fill
light, blue rim on hair and shoulder), low ambient 400K.

MOOD: Tegas, berkuasa, slightly contemplative — a prince who carries
the weight of two kingdoms.

STYLE: Cinematic realistic portrait, Javanese classical aesthetic
inspired by Chinese period drama, shallow depth of field f/2.0,
50mm lens equivalent, 8K hyperdetailed, photorealistic skin texture,
35mm film grain, color graded teal-orange shadows warm highlights.

Aspect ratio: 9:16 (portrait reference image)
Negative prompt: modern clothing, western architecture, Chinese
temple roof, Indian deity iconography, anime style, cartoon, 3D
render, plastic smooth skin, deformed hands, extra fingers,
watermark, text, signature, low resolution, blurry, oversaturated.
```

**Yang berubah dibanding versi lama:**

| Elemen | Lama | Baru |
|--------|------|------|
| Shot type | Tidak ada | "Medium close-up, three-quarter view facing camera left" |
| Pose | Tidak ada | "calm determined expression with slight confident smile" |
| Kostum | Generik "blue-dark tunic" | Spesifik "kala-makara motif on chest, foliate scrolls on shoulders" |
| Setting | "Javanese Hindu palace" | "Prambanan/Penataran temple relief style, stone andesite pillars, ijuk roof" |
| Lighting | "cinematic lighting" | "Warm 2700K torch key + cool 5600K moonlight fill" |
| Mood | Tidak ada | "Tegas, berkuasa, slightly contemplative" |
| Lensa | Tidak ada | "50mm, f/2.0, shallow DoF, 35mm film grain" |
| Aspect ratio | Tidak ada | "9:16 portrait" |
| Negative | Minim | Lengkap (12 item) |

---

## E. Strategi Iterasi Prompt

### Loop Iterasi (3 putaran maksimum)

```
Round 1: Generate 4 sampel dengan prompt awal
  ↓
Review: Apakah wajah Jawa? Kostum candi? Lighting sesuai?
  ↓
Round 2: Tweak prompt berdasarkan masalah
  - Wajah terlalu Chinese? → tambah "Indonesian Javanese phenotype, 
    epicanthic fold minimal, broader nose, fuller lips"
  - Kostum terlalu India? → tambah "NOT Indian deity, NOT dhoti, 
    Javanese kain batik with parang pattern"
  - Lighting terlalu flat? → tambah "high contrast, strong key 
    shadow on right side of face"
  ↓
Round 3: Final tweak + lock seed
  → Catat seed untuk reproducibility
  → Simpan sebagai refs/C001_base.png
```

### Quality Gate Sebelum Lokcing Ref Image

Setiap ref image harus lulus checklist ini:

- [ ] Wajah terlihat Jawa (bukan Chinese/Indian/Thai)
- [ ] Kostum sesuai era (bukan Majapahit abad 14, bukan Mataram 17)
- [ ] Warna kerajaan benar (biru-emas Jenggala / merah-emas Kediri)
- [ ] Lighting sesuai mood babak
- [ ] Komposisi sesuai shot type
- [ ] Tidak ada elemen modern (kabel, kaca, dll)
- [ ] Detail tekstur cukup (kulit, kain, perhiasan)
- [ ] Aspek rasio sesuai target

Jika ada satu kotak tidak tercentang → prompt masih sampah → iterasi lagi.

---

## F. Pipeline Programatik (Opsional, via Vertex AI Python SDK)

Untuk batch generate 36 segmen + 4 karakter + 5 lokasi:

```python
# scripts/generate_assets_vertex.py (template)
from google.cloud import aiplatform
from google.cloud.aiplatform.v1beta1 import (
    PredictionServiceClient, GenerateImageRequest, Image
)

aiplatform.init(project="your-project", location="us-central1")

def generate_image(prompt, aspect_ratio="16:9", sample_count=4, seed=None):
    request = GenerateImageRequest(
        prompt=prompt,
        number_of_images=sample_count,
        aspect_ratio=aspect_ratio,
        guidance_scale=10.0,
        seed=seed,
    )
    response = client.generate_image(request=request)
    return response.images

# Loop segmen dari storyboard-pilot.json
import json
with open("storyboard-pilot.json") as f:
    sb = json.load(f)

for act in sb["acts"]:
    for scene in act["scenes"]:
        for seg in scene["segments"]:
            prompt = seg["visual"]["prompt"]
            images = generate_image(prompt, aspect_ratio="16:9")
            # Save best image
            images[0].save(f"segments/{seg['id']}/image.png")
```

---

## G. Checklist Sebelum Generate Massal

Sebelum eksekusi pipeline T2I untuk 45 asset (4 karakter + 5 lokasi + 36 segmen):

1. ✅ Semua prompt sudah pakai struktur 5 komponen (Subject/Setting/Lighting/Mood/Style)
2. ✅ Setiap prompt sebut "Javanese Hindu-Buddhist art, East Java 1100 CE"
3. ✅ Setiap prompt sebut warna kerajaan (biru-emas / merah-emas)
4. ✅ Aspect ratio ditentukan (9:16 ref, 16:9 segmen)
5. ✅ Negative prompt lengkap (12+ item)
6. ✅ Lighting konkret (Kelvin + arah)
7. ✅ Lensa/teknis spesifik (50mm, f/2.0, dll)
8. ✅ Reference visual disebut (Prambanan, Penataran, wayang Malang)
9. ✅ Mood konkret (bukan "cinematic" generik)
10. ✅ Quality gate checklist siap

Jika ada yang belum ✅, prompt masih sampah — jangan generate dulu.
