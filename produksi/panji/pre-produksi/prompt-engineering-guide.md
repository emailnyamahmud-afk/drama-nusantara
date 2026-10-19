# T2I Prompt Engineering Guide — Panji: Asmara Bangun

## Untuk Google AI Studio (Nano Banana / Gemini Image API)

> **Koreksi penting (Oktober 2026):** Sebelumnya saya sebut "Imagen 3" — model itu **sudah deprecated dan di-shutdown Google**. Pengganti resmi: **Nano Banana** series. Dokumen ini sudah dikoreksi.
> **Sumber resmi**: https://ai.google.dev/gemini-api/docs/image-generation

---

## A. Model yang Tersedia (Oktober 2026)

| Model ID | Nama | Cocok untuk | Resolusi | Harga relatif |
|----------|------|-------------|----------|---------------|
| `gemini-nano-banana-2.1` | Nano Banana 2.1 | **Workhorse utama — pilihan default proyek ini** | 1K/2K/4K | Sedang |
| `gemini-3.1-flash-lite-image` | Nano Banana 2 Lite | Batch cepat & murah (TIDAK multi-reference, TIDAK multi-turn) | 1K/2K | Termurah |
| `gemini-3.1-flash-image` | Nano Banana 2 (previous gen) | Migrasi dari 2.5 | 1K/2K/4K | Sedang |
| `gemini-3-pro-image` | Nano Banana Pro | Tugas paling kompleks (brand consistency, knowledge tinggi) | 1K/2K/4K | Termahal |
| `gemini-2.5-flash-image` | Nano Banana (legacy) | **DEPRECATED** — jangan pakai | 1K | — |

**Rekomendasi proyek Panji:**
- **Step 1-2 (4 karakter ref + 5 lokasi ref)**: `gemini-nano-banana-2.1` (kualitas terbaik untuk ref yang akan dipakai berulang)
- **Step 3 (36 segmen)**: `gemini-nano-banana-2.1` (karena perlu reference image untuk konsistensi karakter)
- **Step 5 I2V**: pakai model video (Veo 3), bukan Nano Banana

---

## B. Workflow Konkret — Google AI Studio (Web UI)

```
1. Buka https://aistudio.google.com → sign in dengan Google account

2. Dapatkan API key:
   - Klik "Get API key" → "Create API key"
   - Simpan key di .env (JANGAN commit ke git)

3. Pilih model di dropdown:
   - "Nano Banana 2.1" (model ID: gemini-nano-banana-2.1)

4. Buat interaction baru:
   - Pilih "Interactions" (bukan "Chat" lama)
   - Pilih model: gemini-nano-banana-2.1
   - Tempel prompt (format 5 komponen — lihat section D)
   - Tambah reference image (klik + → upload PNG) — bisa hingga 14 gambar

5. Set image config (klik "Show advanced options"):
   - aspect_ratio: "9:16" (portrait ref) atau "16:9" (cinematic segmen)
   - resolution: "2K" (cukup untuk pilot) atau "4K" (production)
   - response_modalities: ["IMAGE", "TEXT"]

6. Run interaction → lihat output image
   - Klik download → simpan ke refs/C00X_base.png

7. Untuk iterasi:
   - Multi-turn: lanjutkan interaction dengan prompt revisi
   - "Make the lighting more dramatic" / "Change angle to low angle"
   - Interactions API menyimpan context, jadi karakter konsisten
```

---

## C. Workflow Programatik — Python SDK

### Instalasi

```bash
pip install google-genai Pillow
```

### Setup environment

```bash
# .env (JANGAN commit)
GEMINI_API_KEY=AIzaSy...your_key_here...
```

### Script: Generate 1 karakter ref dengan iterasi multi-turn

```python
# scripts/generate_character_ref.py
import os
import base64
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Load prompt dari characters.md
def load_prompt(char_id):
    # Parse prompt dari characters.md
    # (sederhananya: hardcode per karakter untuk pilot)
    prompts = {
        "C001": open("produksi/panji/pre-produksi/prompts/C001_panji.txt").read(),
        "C002": open("produksi/panji/pre-produksi/prompts/C002_candra_kirana.txt").read(),
        "C003": open("produksi/panji/pre-produksi/prompts/C003_patih.txt").read(),
        "C004": open("produksi/panji/pre-produksi/prompts/C004_mpu_dharmaja.txt").read(),
    }
    return prompts[char_id]

def generate_character(char_id, aspect_ratio="9:16", resolution="2K"):
    prompt = load_prompt(char_id)
    print(f"[{char_id}] Generating with model gemini-nano-banana-2.1...")

    interaction = client.interactions.create(
        model="gemini-nano-banana-2.1",
        input=prompt,
        config={
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
        },
    )

    output_path = Path(f"produksi/panji/refs/{char_id}_base.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(interaction.output_image.data))

    print(f"[{char_id}] Saved to {output_path}")
    return output_path

def iterate_character(char_id, feedback, aspect_ratio="9:16", resolution="2K"):
    """Iterasi dengan multi-turn — pakai reference image sebelumnya."""
    prev_image_path = Path(f"produksi/panji/refs/{char_id}_base.png")
    if not prev_image_path.exists():
        raise FileNotFoundError(f"Previous ref not found: {prev_image_path}")

    with open(prev_image_path, "rb") as f:
        image_bytes = f.read()

    interaction = client.interactions.create(
        model="gemini-nano-banana-2.1",
        input=[
            {"type": "text", "text": feedback},
            {
                "type": "image",
                "data": base64.b64encode(image_bytes).decode("utf-8"),
                "mime_type": "image/png",
            },
        ],
        config={
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
        },
    )

    # Overwrite previous ref
    with open(prev_image_path, "wb") as f:
        f.write(base64.b64decode(interaction.output_image.data))

    print(f"[{char_id}] Iterated ref saved to {prev_image_path}")


if __name__ == "__main__":
    # Step 1: Generate initial refs for all 4 characters
    for char_id in ["C001", "C002", "C003", "C004"]:
        generate_character(char_id)
```

### Script: Generate segmen dengan reference image (konsistensi karakter)

```python
# scripts/generate_segment.py
import os
import base64
import json
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def generate_segment(seg_id, prompt, char_refs, aspect_ratio="16:9", resolution="2K"):
    """Generate segmen dengan reference karakter untuk konsistensi.

    char_refs: list of paths ke character ref PNG (mis. ["refs/C001_base.png", "refs/C002_base.png"])
    """
    # Build input: prompt + up to 14 reference images
    input_parts = [{"type": "text", "text": prompt}]

    for ref_path in char_refs:
        with open(ref_path, "rb") as f:
            image_bytes = f.read()
        input_parts.append({
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        })

    interaction = client.interactions.create(
        model="gemini-nano-banana-2.1",
        input=input_parts,
        config={
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
        },
    )

    output_path = Path(f"produksi/panji/segments/{seg_id}/image.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(base64.b64decode(interaction.output_image.data))

    print(f"[{seg_id}] Saved to {output_path}")
    return output_path


if __name__ == "__main__":
    # Load storyboard
    with open("produksi/panji/pre-produksi/storyboard-pilot.json") as f:
        sb = json.load(f)

    # Map char_ref IDs to file paths
    REF_PATH = Path("produksi/panji/refs")
    ref_map = {
        "C001": REF_PATH / "C001_base.png",
        "C002": REF_PATH / "C002_base.png",
        "C003": REF_PATH / "C003_base.png",
        "C004": REF_PATH / "C004_base.png",
    }

    # Generate all 36 segments
    for act in sb["acts"]:
        for scene in act["scenes"]:
            for seg in scene["segments"]:
                prompt = seg["visual"]["prompt"]
                char_refs = [str(ref_map[c]) for c in seg.get("characters_present", []) if c in ref_map]

                # Skip if already generated
                output = Path(f"produksi/panji/segments/{seg['id']}/image.png")
                if output.exists():
                    print(f"[{seg['id']}] Skip — already exists")
                    continue

                try:
                    generate_segment(seg["id"], prompt, char_refs)
                except Exception as e:
                    print(f"[{seg['id']}] FAILED: {e}")
```

### Script: Iterasi multi-turn untuk refine segmen

```python
# scripts/iterate_segment.py
"""Iterasi segmen yang sudah ada dengan feedback natural language."""
import os
import base64
import sys
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def iterate_segment(seg_id, feedback):
    seg_path = Path(f"produksi/panji/segments/{seg_id}/image.png")
    if not seg_path.exists():
        raise FileNotFoundError(f"Segment not found: {seg_path}")

    with open(seg_path, "rb") as f:
        image_bytes = f.read()

    interaction = client.interactions.create(
        model="gemini-nano-banana-2.1",
        input=[
            {"type": "text", "text": feedback},
            {
                "type": "image",
                "data": base64.b64encode(image_bytes).decode("utf-8"),
                "mime_type": "image/png",
            },
        ],
        config={
            "aspect_ratio": "16:9",
            "resolution": "2K",
        },
    )

    # Backup old version
    backup = seg_path.with_name("image_prev.png")
    seg_path.rename(backup)

    # Save new version
    with open(seg_path, "wb") as f:
        f.write(base64.b64decode(interaction.output_image.data))

    print(f"[{seg_id}] Refined. Previous saved to {backup}")

if __name__ == "__main__":
    seg_id = sys.argv[1]
    feedback = sys.argv[2]
    iterate_segment(seg_id, feedback)

# Usage:
# python scripts/iterate_segment.py S001_seg01 "Make the lighting more dramatic, stronger rim light on Panji's left shoulder"
```

---

## D. Struktur Prompt — 5 Komponen (Rekomendasi Google)

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
5. **Negative prompt lengkap** (di section terpisah jika prompt tool mendukung): `modern clothing, western architecture, Chinese temple, Indian deity, anime, cartoon, 3D render, plastic skin, deformed hands, extra fingers, watermark, text, signature`
6. **Suhu lighting konkret**: 2700K (api), 5600K (bulan), 6500K (daylight), 2200K (api upacara)

---

## E. Audit Prompt Lama (Yang Masih Sampah)

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
| 1 | Tidak ada shot type | Nano Banana mungkin keluar wide shot |
| 2 | "Cinematic lighting" = sampah | Interpretasi bebas, hasil acak |
| 3 | Tidak ada mood konkret | "Tegas" tidak diterjemah ke visual |
| 4 | "Javanese Hindu palace" → ambigu | Bisa keluar kuil Bali/Thai |
| 5 | Tidak ada aspek rasio | Default 1:1 |
| 6 | Tidak ada referensi spesifik | Tidak sebut "Prambanan relief" |
| 7 | Negative prompt minim | Kurang |
| 8 | Tidak pakai struktur 5 komponen | Model tidak parse efisien |

**Yang sudah dilakukan:** Prompt C001-C004 dan L001-L005 sudah dirework ke format 5 komponen (lihat `characters.md` dan `visual-style.md`).

---

## F. Strategi Iterasi — Multi-Turn Editing

### Loop Iterasi (3 putaran maksimum)

```
Round 1: Generate dengan prompt awal
  ↓
Quality Gate (lihat section G)
  ↓
Round 2: Multi-turn edit dengan feedback natural language
  - "Make the lighting more dramatic, stronger rim light on left shoulder"
  - "The face looks too Chinese, make the nose broader and eyes less epicanthic"
  - "The kain batik pattern is wrong, use parang rusak diagonal pattern"
  ↓
Round 3: Final tweak + lock seed
  → Simpan sebagai refs/C00X_base.png
```

### Contoh Iterasi Multi-Turn

```python
# Initial generation
generate_character("C001")

# Iterasi 1: Lighting kurang dramatis
iterate_character("C001", "Make the lighting more dramatic — increase contrast ratio to 6:1, add stronger rim light on left shoulder, deepen the shadows on right side of face")

# Iterasi 2: Wajah terlalu Chinese
iterate_character("C001", "The face looks too East Asian. Make the nose broader and flatter, eyes with minimal epicanthic fold, lips fuller — typical Javanese phenotype")

# Iterasi 3: Pola batik salah
iterate_character("C001", "The batik pattern is wrong. Use parang rusak — diagonal broken knife pattern, not geometric squares. Blue and gold colors only")
```

---

## G. Quality Gate — Checklist Sebelum Locking Ref Image

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

Jika satu kotak tidak tercentang → prompt masih sampah → iterasi lagi.

---

## H. Konsistensi Karakter — Strategi Reference Image

### Pendekatan 3 Tier

```
Tier 1 (Pilot — 36 segmen):
  - Generate 4 karakter ref via Nano Banana 2.1
  - Untuk setiap segmen: sertakan karakter ref sebagai image input
  - Nano Banana bisa terima hingga 14 reference images
  - Cocok untuk pilot 3 menit (konsistensi 80-90%)

Tier 2 (Mini-series — 12 episode):
  - LoRA fine-tuning via Vertex AI (Model Garden)
  - Latih LoRA per karakter (4 LoRA files)
  - Konsistensi 95%+ di seluruh episode
  - Biaya: ~$50-100 per karakter training

Tier 3 (Full series — 24+ episode):
  - Custom model training via Vertex AI
  - Konsistensi 98%+
  - Biaya: ~$500-1000 per character
```

### Workflow Konsistensi untuk Pilot (Tier 1)

```python
# Saat generate segmen, sertakan karakter ref
generate_segment(
    seg_id="S001_seg04",
    prompt="Wide shot, Panji (C001) seated on stone throne in Javanese palace...",
    char_refs=["refs/C001_base.png"],  # ← karakter ref
    aspect_ratio="16:9"
)

# Saat dua karakter di frame, sertakan kedua ref
generate_segment(
    seg_id="S005_seg17",
    prompt="Medium two-shot, Panji (C001) and Candra Kirana (C002) facing each other...",
    char_refs=["refs/C001_base.png", "refs/C002_base.png"],  # ← dua ref
    aspect_ratio="16:9"
)
```

---

## I. Batasan Nano Banana yang Perlu Diketahui

| Batasan | Detail | Workaround |
|---------|--------|------------|
| **SynthID watermark** | Otomatis tertanam di setiap gambar (invisible) | Tidak bisa dihilangkan — accept this |
| **Max 14 reference images per request** | Cukup untuk 4 karakter + 5 lokasi + 5 ekstra | Jika perlu lebih, generate bertahap |
| **Resolution max 4K** | Cukup untuk pilot, mungkin kurang untuk IMAX | Upscale via Real-ESRGAN post-processing |
| **No explicit seed control** | Tidak bisa lock seed untuk reproducibility | Catat prompt + parameter, iterasi via multi-turn |
| **Output 1 image per request** | Tidak bisa batch-generate 4 variasi | Loop request 4x dengan prompt sama |
| **Rate limit** | Free tier: ~5 req/min | Batch dengan delay 12 detik antar request |
| **Aspect ratios supported** | 1:1, 3:4, 4:3, 9:16, 16:9 | Tidak ada 2.35:1 cinematic — gunakan 16:9 + crop post |
| **Image editing**: text + image input | Untuk iterasi multi-turn | Ini cara utama refine karakter |

---

## J. Cost Estimation untuk Pilot 3 Menit

### Asumsi
- 4 karakter ref × 3 iterasi rata-rata = 12 generate
- 5 lokasi ref × 3 iterasi = 15 generate
- 36 segmen × 2 iterasi = 72 generate
- Total ~99 generate image

### Estimasi biaya (Oktober 2026, perkiraan)

| Model | Per image (1K) | Per image (2K) | Per image (4K) | Total 99 image |
|-------|----------------|----------------|-----------------|-----------------|
| `gemini-3.1-flash-lite-image` | $0.031 | $0.038 | — | ~$3-4 |
| `gemini-nano-banana-2.1` | $0.039 | $0.046 | $0.078 | ~$4-8 |
| `gemini-3-pro-image` | $0.21 | $0.25 | $0.42 | ~$20-40 |

**Rekomendasi pilot:** Pakai `gemini-nano-banana-2.1` di 2K resolution → ~$5-8 total.

---

## K. Checklist Sebelum Eksekusi Pipeline

Sebelum run `generate_character_ref.py` + `generate_segment.py`:

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
11. ✅ API key diset di .env (TIDAK di-commit)
12. ✅ Model ID benar: `gemini-nano-banana-2.1` (bukan Imagen 3 yang deprecated)
13. ✅ Script `generate_character_ref.py` + `generate_segment.py` siap
14. ✅ Directory structure: `produksi/panji/refs/` + `produksi/panji/segments/`

Jika ada yang belum ✅, jangan eksekusi — perbaiki dulu.

---

## L. File yang Perlu Disiapkan Sebelum Generate

```
produksi/panji/
├── pre-produksi/
│   ├── story-bible.md          ✅
│   ├── characters.md           ✅ (sudah pakai format 5 komponen)
│   ├── visual-style.md         ✅ (sudah pakai format 5 komponen)
│   ├── storyboard-pilot.json   ✅ (36 segmen, prompt sudah diupdate)
│   ├── prompt-engineering-guide.md  ✅ (file ini)
│   └── prompts/                ← folder baru, perlu dibuat
│       ├── C001_panji.txt      ← prompt murni (tanpa markdown)
│       ├── C002_candra_kirana.txt
│       ├── C003_patih.txt
│       └── C004_mpu_dharmaja.txt
├── refs/                       ← folder baru, akan diisi script
│   ├── C001_base.png
│   ├── C002_base.png
│   ├── C003_base.png
│   ├── C004_base.png
│   ├── L001_base.png
│   ├── L002_base.png
│   ├── L003_base.png
│   ├── L004_base.png
│   └── L005_base.png
└── segments/                   ← folder baru, akan diisi script
    ├── S001_seg01/
    │   ├── image.png
    │   ├── image_prev.png      ← backup iterasi
    │   └── metadata.json
    └── ... (35 segmen lainnya)

scripts/
├── generate_character_ref.py   ✅ (lihat section C)
├── generate_segment.py         ✅
├── iterate_segment.py          ✅
└── ...
```

---

## M. Quick Reference — Kode Terpenting

### Generate 1 image dengan reference karakter

```python
from google import genai
import base64, os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Load Panji ref
with open("produksi/panji/refs/C001_base.png", "rb") as f:
    panji_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input=[
        {"type": "text", "text": "Wide shot, Panji seated on stone throne in Javanese palace, 16:9 cinematic, 8K hyperdetailed"},
        {
            "type": "image",
            "data": base64.b64encode(panji_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    config={
        "aspect_ratio": "16:9",
        "resolution": "2K",
    },
)

with open("produksi/panji/segments/S001_seg04/image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### Iterasi multi-turn untuk refine

```python
interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input=[
        {"type": "text", "text": "Make the lighting more dramatic. Increase contrast ratio to 6:1. Add stronger rim light on subject's left shoulder. Deepen shadows on right side of face."},
        {"type": "image", "data": prev_image_base64, "mime_type": "image/png"},
    ],
    config={"aspect_ratio": "16:9", "resolution": "2K"},
)
```

---

## N. Sumber Resmi

- **Google AI Image Generation Docs**: https://ai.google.dev/gemini-api/docs/image-generation
- **Model selection**: https://ai.google.dev/gemini-api/docs/image-generation#model-selection
- **Interactions API**: https://ai.google.dev/gemini-api/docs/interactions
- **Nano Banana Codelab (Consistent Imagery)**: https://codelabs.developers.google.com/gemini-consistent-imagery-notebook
- **Google AI Studio**: https://aistudio.google.com
- **API Keys**: https://aistudio.google.com/apikey
- **Pricing**: https://ai.google.dev/gemini-api/docs/rate-limits
