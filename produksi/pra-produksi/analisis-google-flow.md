# Analisis Google Flow JSON v1.2 — Adopsi & Pengembangan untuk Pipeline Drama Nusantara

**Tanggal**: 2026-10-23
**Sumber**: `google-flow.json` (56.2 MB) dari Google Flow (Storyboard Studio)
**Project sample**: "KEN AROK: TAKDIR DARI TUMAPEL" — 4 scene, 21 frame, 16 asset

---

## 1. Ringkasan Struktur JSON Google Flow v1.2

### Top-level keys (7):
| Key | Type | Isi |
|---|---|---|
| `version` | str | `"1.2"` |
| `projectTitle` | str | Judul project |
| `fullMarkdown` | str | **Script storyboard lengkap** (~5.400 char) — action lines + dialogue dalam Bahasa Indonesia, scene header `### EXT/INT`, `<!-- scene-id: UUID -->` HTML comment sebagai penanda scene, `##### CUT TO:` transition |
| `globalStyle` | str | Style preset (mis. `"Realistic"`) |
| `customStyleLibrary` | dict | Kosong di sample ini |
| `assets` | list[16] | **Asset library** — character/location/prop |
| `frames` | list[21] | **Storyboard frames** — 1 frame = 1 generated image |

### Asset schema (per item):
```json
{
  "id": "UUID",
  "type": "character" | "location" | "prop",
  "name": "string",
  "supportingImages": [{"id": "UUID", "mediaId": "UUID", "base64": "~900KB JPEG"}],
  "includeInspirationInImageGen": true,    // ★ FLAG kontrol
  "physicalCharacteristics": "~350 char deskripsi fisik (EN)",
  "clothingAccessories": "~320 char pakaian + aksesori (character only)",
  "backstory": "~230 char latar belakang (character only)",
  "referenceImageId": "UUID",              // ★ pointer ke supportingImages canonical
  "timeOfDay": "midday" | "night"          // location only
}
```

### Frame schema (per item):
```json
{
  "id": "UUID",
  "sceneId": "UUID",                       // ★ link ke markdown <!-- scene-id -->
  "sceneNumber": "01".."04",
  "shotNumber": "01".."06",
  "sceneTitle": "Ext. Hutan Tumapel - Day",
  "title": "Chased Through Dense Woods",
  "visualDescription": "~420 char (EN) — APA yang dilihat",
  "motionDescription": "~120 char — GERAKAN kamera",
  "audioDescription": "~220 char — DESAIN audio + dialogue cue",
  "linkedAssetIds": ["UUID", "UUID", ...], // ★ multi-asset composition per frame
  "imageHistory": ["blob:URL", ...],       // history URL generasi sebelumnya
  "imageUrl": "blob:URL",                  // URL gambar final
  "base64": "~1.2MB JPEG",                 // ★ gambar storyboard jadi (1376×768, 16:9)
  "imageHistoryData": ["base64", ...]      // history gambar sebelumnya
}
```

### Distribusi konten sample:
- **4 scene** (3 scene berisi + 1 placeholder FADE TO BLACK)
- **21 frame** (6 + 6 + 6 + 3) — rata-rata ~6 shot per scene
- **16 asset**: 7 character, 3 location, 6 prop
- **Aspect ratio**: 1376×768 (~16:9 horizontal) — sama dengan standar v2.1 kita
- **Bahasa**: Markdown script = Indonesia; frame descriptions = English (campur)

---

## 2. APA YANG BISA DIADOPSI (Langsung dari Flow → Kita)

### ✅ 2.1 Asset Schema 3-field (physicalCharacteristics + clothingAccessories + backstory)

Ini **lebih kaya dari K-files kita** yang hanya punya 1 deskripsi fisik gabungan.

| Field Flow | Karakter | Contoh isi |
|---|---|---|
| `physicalCharacteristics` | Tubuh, wajah, rambut, postur | "A Javanese man in his mid-20s possessing a rugged, athletic, and fiercely agile physique. He has warm golden-brown skin, an angular jawline..." |
| `clothingAccessories` | Pakaian, aksesori, sepatu | "Wears a faded crimson cloth headband... open earthy-brown sleeveless vest over a bare chest, indigo-patterned batik sarong..." |
| `backstory` | Motivasi, riwayat, arc | "Raised as an orphaned bandit and street thief in the jungles of Tumapel, he survives purely by his cunning..." |

**Rekomendasi adopsi**: Ubah K-files kita dari 1 field `description` jadi 3 field terpisah. Lebih modular — bisa reuse `physicalCharacteristics` saja di frame yang hanya perlu body reference, atau reuse `clothingAccessories` saja untuk wardrobe change scene.

### ✅ 2.2 Frame 3-description split (visualDescription + motionDescription + audioDescription)

Industry-standard storyboard format. Kita belum punya standar ini.

| Field | Untuk apa | Output pipeline ke mana |
|---|---|---|
| `visualDescription` | Komposisi visual frame | → T2I prompt |
| `motionDescription` | Camera movement (pan, tilt, push-in, tracking) | → I2V motion prompt |
| `audioDescription` | Sound design + dialogue cue | → TTS + SFX/music brief |

**Rekomendasi adopsi**: Wajib di Phase 4 `produksi.json`. Saat ini Phase 6 (I2V) kita belum punya sumber prompt — ini solusinya.

### ✅ 2.3 linkedAssetIds (multi-asset composition per frame)

Setiap frame link ke beberapa asset via UUID. Contoh Frame #14 "Seizing the Cursed Blade" link ke **6 asset**: Ken Arok + Empu Gandring + Keris + Palu + Tang Besi + Bengkel. Ini composition matrix yang clean.

**Rekomendasi adopsi**: Di `produksi.json` kita, setiap frame punya `linkedAssetIds: [...]` yang reference asset ID dari Phase 3 master T2I library (220 file K/L/A/F/S). Saat generate frame, sistem compose prompt dari deskripsi semua linked asset.

### ✅ 2.4 includeInspirationInImageGen flag

Boolean per asset: kalau `true`, ref image asset di-pass sebagai image input ke T2I; kalau `false`, hanya deskripsi teks yang dipakai. Pemisahan ini cerdik — asset "utama" (karakter di foreground) pakai ref image, asset "sekunder" (background prop) tidak.

**Rekomendasi adopsi**: Tambahkan flag ini di asset schema kita. Berguna untuk:
- Karakter utama → `includeInspirationInImageGen: true` (konsistensi wajah)
- Prop kecil / latar belakang → `false` (hemat token, lebih fleksibel)

### ✅ 2.5 sceneId linkage (markdown HTML comment ↔ frame.sceneId)

Script markdown pakai `<!-- scene-id: UUID -->` untuk segmentasi scene, dan `frame.sceneId` langsung reference UUID itu. Parse 1 file markdown → dapat scene structure.

**Rekomendasi adopsi**: Saat generate script Phase 4, embed `<!-- scene-id: ... -->` di markdown. Parser otomatis bisa assign frame ke scene tanpa perlu manual mapping.

### ✅ 2.6 imageHistory + imageHistoryData (versioning generated images)

Setiap frame menyimpan history semua generasi sebelumnya (URL + base64). Berguna untuk:
- Rollback ke versi sebelumnya
- A/B compare antar generasi
- Audit trail

**Rekomendasi adopsi**: Tambahkan `imageHistory: [{timestamp, prompt, model, params, path}]` per frame. Lokal path saja (bukan base64 — hemat storage).

### ✅ 2.7 Aspect ratio 16:9 horizontal default (1376×768)

Konfirmsi standar v2.1 kita sudah benar — Google Flow juga pakai 16:9 horizontal untuk storyboard.

### ✅ 2.8 Quality visual = bagus (validated via VLM)

Saya VLM-analisis Frame #00 (chase scene). Hasil:
- ✅ Karakter konsisten dengan deskripsi (red headband, bare chest, brown vest, indigo sarong)
- ✅ Lokasi realistic (tropical teak forest, god rays, volumetric lighting)
- ✅ Aksi terbaca jelas (protagonis depan, antagonis kejar di belakang)
- ✅ Cinematic (depth of field, motion blur halus)
- ⚠️ AI artifacts kecil: anatomi tangan "meleleh", wajah figur sekunder generik, proporsi paha besar

**Insight**: Quality Google Flow setara dengan output Dola AI kita. Tidak ada keunggulan kualitas visual — keunggulan Flow ada di **workflow automation** (1 klik generate script+asset+storyboard).

---

## 3. APA YANG BISA DIKEMBANGKAN (Flow kurang → kita tambah)

### ❌ 3.1 TIDAK ada layer TTS (Text-to-Speech)

Flow hanya sampai storyboard image. **Tidak ada**:
- Voice profile per karakter (pitch, speed, accent, emotion)
- Dialogue-to-TTS mapping (line mana diucapkan karakter mana, di frame mana)
- Audio file output (`.wav` / `.mp3`)

**Pengembangan kita**: Phase 7 TTS — wajib tambah:
```json
"voiceProfiles": {
  "ken_arok": {"voice_id": "...", "pitch": "+2", "speed": "1.05", "emotion": "confident"},
  "ken_dedes": {"voice_id": "...", "pitch": "-3", "speed": "0.95", "emotion": "melancholic"}
}
```

### ❌ 3.2 TIDAK ada layer I2V (Image-to-Video)

Flow berhenti di image. Padahal `motionDescription` sudah ada di setiap frame — tapi tidak dipakai untuk apa-apa. **Peluang besar**: motionDescription itu sudah jadi prompt siap pakai untuk I2V model (Kling, Runway, LTX).

**Pengembangan kita**: Phase 6 I2V — `motionDescription` jadi input langsung ke I2V prompt.

### ❌ 3.3 TIDAK ada timeline/duration field

Tidak ada metadata: berapa detik frame ini ditampilkan? Total durasi video? Frame rate target?

**Pengembangan kita**: Tambah:
```json
"duration_seconds": 4.5,
"frame_rate": 24,
"in_point": "00:01:23.5",
"out_point": "00:01:28.0"
```

### ❌ 3.4 TIDAK ada shot metadata (focal length, framing, lens)

`motionDescription` hanya bilang "tracking shot", tapi tidak ada: shot size (WS/MS/CU/EWS), focal length (24mm/50mm/85mm), camera angle (eye-level/low/high/Dutch), lens type (prime/zoom/anamorphic).

**Pengembangan kita**: Tambah `shotSpec`:
```json
"shotSpec": {
  "size": "MCU",          // EWS/WS/MWS/MS/MCU/CU/ECU
  "angle": "eye-level",   // eye/low/high/dutch/overhead
  "lens_mm": 50,
  "lens_type": "prime"
}
```

### ❌ 3.5 TIDAK ada character consistency enforcement antar frame

Flow hanya pass ref image asset saat generate. Tapi T2I model tidak menjamin wajah Ken Arok di frame #00 = wajah Ken Arok di frame #14. Perlu **face lock** atau **character LoRA**.

**Pengembangan kita**:
- Opsional: latih LoRA per karakter utama (Ken Arok, Ken Dedes) dari 5-angle K-files
- Atau: pakai IP-Adapter / FaceID di ComfyUI workflow

### ❌ 3.6 TIDAK ada scene-level metadata

Scene (4 scene di markdown) tidak punya struktur JSON terpisah. Tidak ada field: mood, music theme, color palette, time of day, location reference.

**Pengembangan kita**: Tambah `scenes: [...]` array di top-level:
```json
"scenes": [
  {
    "id": "UUID",
    "number": "01",
    "title": "Ext. Hutan Tumapel - Day",
    "location_asset_id": "UUID",
    "time_of_day": "midday",
    "mood": "tense, defiant",
    "music_theme": "tribal percussion building",
    "color_palette": ["#8B4513", "#D2691E", "#F4A460"]
  }
]
```

### ❌ 3.7 TIDAK ada edit decision list (EDL)

Tidak ada urutan editing, transition antar shot, audio layering.

**Pengembangan kita**: Phase 8 pasca-produksi — tambah `editList: [...]`:
```json
"editList": [
  {"frame_id": "UUID", "transition_out": "hard_cut", "duration": 4.5},
  {"frame_id": "UUID", "transition_out": "cross_dissolve", "duration": 3.0}
]
```

### ❌ 3.8 Campur bahasa (Indonesia script + English descriptions)

Markdown script di Indonesia, tapi `visualDescription` / `motionDescription` / `audioDescription` di English. Ini confusing untuk TTS (Bahasa apa?) dan tidak konsisten.

**Pengembangan kita**: Wajib satu bahasa. Karena audience Indonesia → semua description Indonesia. Kecuali `style_keyword` di awal prompt T2I yang memang harus EN (`Cinematic realistic...`).

### ❌ 3.9 File 56 MB tidak manage-able (base64 embedded)

16 asset × ~900 KB + 21 frame × ~1.2 MB = ~41 MB raw → 56 MB after base64 inflation. Push ke GitHub? Tidak mungkin. Edit manual? Susah. Diff? Tidak terbaca.

**Pengembangan kita**: **JSON = source of truth, tapi aset dipisah**. JSON hanya berisi path/URL ke file gambar (di-gitignore), bukan base64 inline. JSON size target < 500 KB.

### ❌ 3.10 TIDAK ada multi-angle asset ref

Flow hanya 1 ref image per asset. K-files kita sudah punya 5 angle (front/side/back/3-quarter/top) — lebih kuat untuk konsistensi.

**Pertahankan** standar 5-angle kita.

### ❌ 3.11 TIDAK ada grup/kelompok asset (S-type)

Flow pakai linkedAssetIds untuk komposisi multi-karakter. Tapi tidak ada "master group" pre-defined. S-files kita (master kelompok, clean studio background, pakai K ref) lebih efisien untuk scene yang berulang (mis. "pasukan prajurit istana" muncul di banyak frame).

**Pertahankan** S-type dari Phase 3 kita.

### ❌ 3.12 TIDAK ada style library

`customStyleLibrary` kosong. Kita bisa pre-define style presets: `cinematic_realistic`, `wayang_inspired`, `colonial_painting`, `batik_texture`, dll. — reusable across project.

---

## 4. Rekomendasi Konkret untuk Pipeline Drama Nusantara

### 4.1 Phase 4 `produksi.json` schema (gabungan adopsi + pengembangan)

```json
{
  "version": "2.0",
  "projectTitle": "...",
  "globalStyle": "cinematic_realistic",
  "styleLibrary": {...},                    // custom presets
  
  "scenes": [
    {
      "id": "UUID",
      "number": "01",
      "title": "Ext. Hutan Tumapel - Day",
      "location_asset_id": "asset-uuid",
      "time_of_day": "midday",
      "mood": "tense",
      "music_theme": "tribal_percussion",
      "color_palette": [...]
    }
  ],
  
  "assets": [                               // ★ adopsi dari Flow, expand
    {
      "id": "UUID",
      "type": "character|location|prop|group|fauna",
      "name": "...",
      "slug": "...",
      "physicalCharacteristics": "...",    // ★ adopsi
      "clothingAccessories": "...",        // ★ adopsi
      "backstory": "...",                  // ★ adopsi
      "includeInspirationInImageGen": true,// ★ adopsi
      "ref_images": [                      // ★ expand: multi-angle
        {"angle": "front", "path": "K/..."},
        {"angle": "side", "path": "K/..."}
      ],
      "voice_profile": {                   // ★ pengembangan (character only)
        "voice_id": "...", "pitch": 0, "speed": 1.0, "emotion": "neutral"
      }
    }
  ],
  
  "frames": [
    {
      "id": "UUID",
      "scene_id": "UUID",                  // ★ adopsi
      "scene_number": "01",
      "shot_number": "01",
      "scene_title": "...",
      "shot_title": "...",
      "visualDescription": "...",          // ★ adopsi — feed ke T2I
      "motionDescription": "...",          // ★ adopsi — feed ke I2V
      "audioDescription": "...",           // ★ adopsi — feed ke TTS+SFX
      "linkedAssetIds": [...],             // ★ adopsi
      "shotSpec": {                        // ★ pengembangan
        "size": "MCU", "angle": "eye-level", "lens_mm": 50
      },
      "duration_seconds": 4.5,             // ★ pengembangan
      "dialogue_lines": [                  // ★ pengembangan
        {"character_id": "UUID", "text": "...", "emotion": "angry"}
      ],
      "imageHistory": [                    // ★ adopsi (tanpa base64)
        {"timestamp": "...", "model": "dola-v3", "path": "produksi/t2i-output/..."}
      ]
    }
  ],
  
  "editList": [...],                       // ★ pengembangan Phase 8
  "voiceProfiles": {...}                   // ★ pengembangan Phase 7
}
```

### 4.2 Workflow adaptasi

1. **Pakai Flow sebagai prototype tool** untuk eksplorasi visual cepat (1 jam dari ide → storyboard image). Output JSON-nya bisa di-parse untuk diambil: asset descriptions + frame descriptions.
2. **Pindah ke pipeline kita** untuk production: TTS, I2V, editing, multi-scene consistency.
3. **Bridge**: tulis script konverter `flow_json → produksi_json.py` yang:
   - Ekstrak `assets[]` → isi `produksi.json.assets[]` (tambahkan `slug`, `voice_profile` placeholder)
   - Ekstrak `frames[]` → `produksi.json.frames[]` (tambahkan `shotSpec`, `duration_seconds`, `dialogue_lines`)
   - Tambahkan `scenes[]` dengan parse `<!-- scene-id -->` dari `fullMarkdown`
   - Pisahkan base64 image → file `.jpg` di `produksi/t2i-output/` (di-gitignore)
   - Output JSON < 500 KB, siap commit

### 4.3 Decision matrix: kapan pakai Flow vs pipeline kita

| Skenario | Pakai Flow | Pakai Pipeline Kita |
|---|---|---|
| Eksplorasi ide cepat, 1 scene | ✅ | ❌ (overkill) |
| Proof-of-concept untuk investor | ✅ | ❌ |
| Produksi dokumenter 10 menit | ❌ | ✅ |
| Produksi series 6 episode | ❌ | ✅ |
| Butuh TTS Bahasa Indonesia | ❌ (tidak ada) | ✅ |
| Butuh I2V motion | ❌ (tidak ada) | ✅ |
| Butuh multi-angle consistency | ❌ | ✅ |
| Konsistensi karakter cross-scene | ❌ (lemah) | ✅ |

---

## 5. Kesimpulan

**Google Flow adalah "storyboard studio" yang excellent untuk pre-production phase 1 (ide → script → storyboard image)**. Tapi itu **berhenti di sana** — tidak ada TTS, I2V, editing, atau production pipeline.

**3 hal paling berharga untuk diadopsi**:
1. Asset 3-field schema (physicalCharacteristics + clothingAccessories + backstory)
2. Frame 3-description split (visual + motion + audio) — siap pakai untuk T2I/I2V/TTS
3. linkedAssetIds composition + includeInspirationInImageGen flag

**3 hal paling berharga untuk dikembangkan**:
1. Layer TTS (voice profile per karakter, dialogue mapping) — Phase 7
2. Layer I2V (motionDescription → video prompt) — Phase 6
3. JSON size management (pisahkan base64 → file, JSON < 500 KB) — wajib untuk git

**Strategi**: Pakai Flow untuk prototyping cepat. Tulis converter untuk import Flow JSON ke `produksi.json` kita. Lanjutkan ke Phase 4-8 dengan schema yang sudah diperkaya.
