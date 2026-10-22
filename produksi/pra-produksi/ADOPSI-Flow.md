# ADOPSI Google Flow — Workflow Optimization untuk Pipeline Drama Nusantara

**Tanggal**: 2026-10-23
**Sumber**: `analisis-google-flow.md` (analisis lengkap 56MB JSON Flow v1.2)
**Tujuan**: Daftar ringkas **apa yang bisa langsung diadopsi** dari Google Flow ke schema pilot Panji yang sudah ada.

**Catatan user**:
- Flow dipakai sebatas storyboard image (image free, video berbayar)
- Fokus adopsi saja, bukan pengembangan
- Gen image/video fleksibel (Flow atau Dola)
- Riset kita jauh lebih dalam dari Flow → jangan kehilangan keunggulan
- Prototype 30 detik / 1 menit dulu
- JSON per segmen (sesuai plan awal) + tambah optimasi workflow Flow

---

## 1. Status Schema Saat Ini (Pilot Panji)

Sudah ada di `produksi/pra-produksi/panji-pilot/pre-produksi/storyboard-pilot.json`:

```json
{
  "episode": {"id","judul","era","durasi_target","resolusi","fps","style"},
  "characters[]": {"id","nama","peran","deskripsi","voice","status"},
  "locations[]": {"id","nama","deskripsi","status"},
  "acts[]": [{"id","judul","scenes[]": [{"id","judul","lokasi","mood","segments[]"}]}],
  "render_status": {"total_segments","draft","approved","image_generated",...}
}
```

**Segment schema**:
```json
{
  "id": "S001_seg01",
  "durasi": 5,
  "status": "draft",
  "visual": {"prompt": "Extreme wide aerial shot, Brantas river at dawn..."},
  "audio": {"type":"narration","tts_text":"...","tts_voice":"id-ID-Ardi","bgm":"..."},
  "characters_present": [],
  "notes": "Opening shot"
}
```

**Pilot stats**: 36 segmen × 5 detik = 180 detik = 3 menit

---

## 2. 8 Item Adopsi dari Flow ke Schema Kita

| # | Item Flow | Status schema kita | Aksi adopsi |
|---|---|---|---|
| 1 | **Asset 3-field** (physicalCharacteristics + clothingAccessories + backstory) | `characters[].deskripsi` = 1 field gabungan | **Pecah jadi 3 field** di characters[] |
| 2 | **Frame 3-description split** (visual + motion + audio) | Punya `visual.prompt` + `audio.*`, **tidak ada motion** | **Tambah `motion.prompt`** untuk I2V feeder |
| 3 | **linkedAssetIds** (multi-asset composition) | `characters_present[]` hanya karakter | **Extend jadi `linked_asset_ids[]`** (karakter + prop + location) |
| 4 | **includeInspirationInImageGen flag** | Tidak ada | **Tambah di asset library** (karakter utama=true, prop sekunder=false) |
| 5 | **location.timeOfDay** | Tidak ada | **Tambah field** di locations[] |
| 6 | **sceneId linkage** (HTML comment `<!-- scene-id -->`) | Pakai scene.id (S001) | **Pertahankan** — sudah lebih clean dari Flow |
| 7 | **imageHistory (versioning)** | Tidak ada | **Tambah per segment** (path-only, no base64) |
| 8 | **16:9 horizontal default** | Sudah 1920×1080 (16:9) | **Sudah adopsi** ✅ |

### Detail implementasi:

#### Adopsi #1: Asset 3-field (characters, locations, props)

**Sebelum** (pilot Panji):
```json
"characters": [{
  "id": "C001",
  "nama": "Panji Asmara Bangun",
  "deskripsi": "Pria Jawa 28 tahun, kulit cokelat keemasan, mata tajam, rambut hitam panjang, destar emas Jawa Kuno, kain batik biru tua-emas, keris pusaka"
}]
```

**Sesudah adopsi Flow**:
```json
"characters": [{
  "id": "C001",
  "nama": "Panji Asmara Bangun",
  "peran": "Pangeran Mahkota Jenggala",
  "physical_characteristics": "Pria Jawa 28 tahun, kulit cokelat keemasan, mata tajam, rambut hitam panjang",
  "clothing_accessories": "Destar emas Jawa Kuno, kain batik biru tua-emas, keris pusaka",
  "backstory": "Putra mahkota Jenggala yang mencari cintanya, Candra Kirana, setelah dipisahkan oleh konflik dinasti",
  "voice": "id-ID-Ardi",
  "include_inspiration_in_image_gen": true,
  "ref_k_id": "2C-k003-panji-asmara-bangun",
  "status": "draft"
}]
```

**Lokasi juga**:
```json
"locations": [{
  "id": "L001",
  "nama": "Keraton Jenggala (Kahuripan)",
  "physical_characteristics": "Interior istana batu, pilar candi, atap ijuk, obor, bendera biru-emas (Jenggala)",
  "time_of_day": "day",
  "ref_l_id": "2C-l002-keraton-jenggala",
  "status": "draft"
}]
```

#### Adopsi #2: Tambah `motion.prompt` untuk I2V feeder

**Sebelum** (pilot Panji): segment cuma punya `visual.prompt` (T2I feeder) + `audio.*` (TTS feeder). Tidak ada feeder untuk I2V (Phase 6).

**Sesudah adopsi Flow**:
```json
"segments": [{
  "id": "S001_seg01",
  "durasi": 5,
  "status": "draft",
  "visual": {"prompt": "Extreme wide aerial shot, Brantas river at dawn..."},
  "motion": {
    "camera": "slow aerial pull-up, north-to-south",
    "prompt": "Camera cranes up slowly revealing the river valley, mist drifts rightward, distant royal boats glide leftward across frame",
    "speed": "slow"
  },
  "audio": {"type":"narration","tts_text":"...","tts_voice":"id-ID-Ardi","bgm":"..."},
  "linked_asset_ids": ["L002"],
  "notes": "Opening shot, no character"
}]
```

`motion.prompt` = siap pakai ke I2V (Flow video berbayar → Dola atau lainnya).

#### Adopsi #3: `linked_asset_ids[]` (multi-asset composition)

**Sebelum** (pilot Panji): `characters_present: ["C001","C002"]` — hanya karakter.

**Sesudah adopsi Flow**: gabung karakter + prop + location dalam 1 array.
```json
"linked_asset_ids": ["C001", "C002", "L002", "P001", "P003"]
```
Di mana `P001`, `P003` = ID prop (keris, tombak, dll). Location bisa tetap di `scene.lokasi` (level scene), tapi kalau dalam 1 scene ada sub-shot di lokasi berbeda, pakai linked_asset_ids.

#### Adopsi #4: `include_inspiration_in_image_gen` flag

Boolean per asset. Karakter utama (`C001` Panji, `C002` Candra) → `true` (ref image di-pass ke T2I untuk konsistensi wajah). Prop kecil atau figur sekunder → `false` (hemat token, lebih fleksibel).

```json
"characters": [
  {"id":"C001", "include_inspiration_in_image_gen": true, ...},  // Panji
  {"id":"C002", "include_inspiration_in_image_gen": true, ...},  // Candra Kirana
  {"id":"C005", "include_inspiration_in_image_gen": false, ...}  // Dayang sekunder
]
```

#### Adopsi #5: `time_of_day` di locations

Field sederhana tapi sangat berpengaruh ke T2I lighting.

```json
"locations": [
  {"id":"L001", "time_of_day":"day"},
  {"id":"L002", "time_of_day":"dawn"},
  {"id":"L003", "time_of_day":"night"}
]
```

#### Adopsi #6: sceneId linkage — pertahankan schema kita

Flow pakai `<!-- scene-id: UUID -->` HTML comment di markdown + `frame.sceneId = UUID`. Kita sudah pakai `scene.id = "S001"` yang lebih readable. **Tidak perlu adopsi**, schema kita lebih clean.

Tapi pertimbangkan: kalau nanti import JSON dari Flow, perlu mapping `UUID → S001`. Buat helper `flow_uuid_to_scene_id.py` saat dibutuhkan.

#### Adopsi #7: `image_history[]` per segment

```json
"segments": [{
  "id": "S001_seg01",
  "image_history": [
    {"timestamp": "2026-10-23T15:00", "model": "dola-seedream-4.5", "path": "produksi/t2i-output/S001_seg01_v1.jpg", "notes": "first attempt"},
    {"timestamp": "2026-10-23T15:15", "model": "dola-seedream-4.5", "path": "produksi/t2i-output/S001_seg01_v2.jpg", "notes": "fix lighting"}
  ]
}]
```

**PENTING**: path-only, **tidak ada base64** (Flow's mistake — file 56MB tidak manageable). Aset di-gitignore, JSON tetap < 500KB.

#### Adopsi #8: 16:9 horizontal default ✅ SUDAH

Pilot Panji pakai `1920×1080` = 16:9. Sama dengan Flow (1376×768). Pertahankan.

---

## 3. Schema Upgrade — `storyboard-pilot.json` v2

```json
{
  "episode": {
    "id": "P001",
    "judul": "Panji: Asmara Bangun — Prototype 30s",
    "era": "Kediri abad 12",
    "jilid_sumber": 2,
    "sumber_tambahan": "UNESCO Memory of the World (Panji Tales, 2017) + Kakawin Smaradahana (Mpu Dharmaja)",
    "durasi_target": 30,            // ★ turun dari 180 → 30 (prototype)
    "resolusi": "1920x1080",        // 16:9 horizontal (adopsi #8)
    "fps": 24,
    "style": "cinematic realistic, Chinese period drama aesthetic + Nusantara Hindu-Buddha"
  },
  
  "characters": [                  // ★ adopsi #1 + #4
    {
      "id": "C001",
      "nama": "Panji Asmara Bangun",
      "peran": "Pangeran Mahkota Jenggala",
      "physical_characteristics": "Pria Jawa 28 tahun, kulit cokelat keemasan, mata tajam, rambut hitam panjang",
      "clothing_accessories": "Destar emas Jawa Kuno, kain batik biru tua-emas, keris pusaka",
      "backstory": "Putra mahkota Jenggala yang mencari cintanya Candra Kirana",
      "voice": "id-ID-Ardi",
      "include_inspiration_in_image_gen": true,
      "ref_k_id": "2C-k003-panji-asmara-bangun",
      "status": "draft"
    }
    // ... 3 karakter lainnya sama formatnya
  ],
  
  "locations": [                    // ★ adopsi #1 + #5
    {
      "id": "L001",
      "nama": "Keraton Jenggala (Kahuripan)",
      "physical_characteristics": "Interior istana batu, pilar candi, atap ijuk, obor, bendera biru-emas",
      "time_of_day": "day",
      "ref_l_id": "2C-l002-keraton-jenggala",
      "status": "draft"
    }
    // ... 2 lokasi lainnya
  ],
  
  "props": [                        // ★ BARU (tidak ada di pilot Panji, adopsi dari Flow)
    {"id":"P001", "nama":"Keris pusaka", "physical_characteristics":"...", "ref_a_id":"2C-a002-keris", "include_inspiration_in_image_gen": true},
    {"id":"P002", "nama":"Tombak kerajaan", "physical_characteristics":"...", "ref_a_id":"2C-a005-tombak", "include_inspiration_in_image_gen": false}
  ],
  
  "acts": [
    {
      "id": "A1",
      "judul": "Dua Kerajaan, Satu Sungai",
      "scenes": [
        {
          "id": "S001",
          "judul": "Fajar di Brantas",
          "lokasi": "L002",
          "mood": "tegas, kuasa, sedikit tegang",
          "segments": [
            {
              "id": "S001_seg01",
              "durasi": 5,
              "status": "draft",
              "visual": {
                "prompt": "Extreme wide aerial shot, Brantas river at dawn, 12th century East Java..."
              },
              "motion": {              // ★ adopsi #2
                "camera": "slow aerial pull-up, north-to-south",
                "prompt": "Camera cranes up slowly revealing the river valley, mist drifts rightward",
                "speed": "slow"
              },
              "audio": {
                "type": "narration",
                "tts_text": "Tahun 1182 masa Saka. Sungai Brantas membelah Jawa Timur menjadi dua kerajaan.",
                "tts_voice": "id-ID-Ardi",
                "bgm": "gamelan soft opening, strings"
              },
              "linked_asset_ids": ["L002"],   // ★ adopsi #3 (sebelumnya characters_present[])
              "image_history": [],             // ★ adopsi #7
              "notes": "Opening shot, no character"
            }
            // ... 5 segmen lainnya untuk total 30 detik
          ]
        }
      ]
    }
  ],
  
  "render_status": {
    "total_segments": 6,                  // 30 detik / 5s = 6 segmen
    "draft": 6, "approved": 0, "image_generated": 0,
    "audio_generated": 0, "video_generated": 0,
    "rendered": 0, "failed": 0
  }
}
```

**Diff dari pilot Panji → v2**:
| Field | Sebelum | Sesudah |
|---|---|---|
| `characters[].deskripsi` | 1 string | Pecah jadi `physical_characteristics` + `clothing_accessories` + `backstory` |
| `characters[].include_inspiration_in_image_gen` | (tidak ada) | `true` untuk karakter utama |
| `characters[].ref_k_id` | (tidak ada) | Link ke Phase 3 master T2I prompts |
| `locations[].deskripsi` | 1 string | Pecah + `time_of_day` + `ref_l_id` |
| `props[]` | (tidak ada) | Array baru — prop library |
| `segments[].motion` | (tidak ada) | `{camera, prompt, speed}` — feeder I2V |
| `segments[].characters_present[]` | Karakter only | Ubah jadi `linked_asset_ids[]` (karakter+prop+lokasi) |
| `segments[].image_history[]` | (tidak ada) | Path-only versioning (no base64) |

---

## 4. Prototype 30 Detik — 6 Segmen Pilot

**Tujuan**: Validasi end-to-end pipeline (T2I → I2V → TTS → stitch) dalam 30 detik, sebelum commit ke produksi panjang.

**Konsep prototype**: Babak pembuka Panji — 6 segmen × 5 detik.

| Seg# | ID | Durasi | Visual hook | Asset link |
|---|---|---|---|---|
| 1 | S001_seg01 | 5s | Extreme wide aerial, Brantas dawn, 2 keraton (Jenggala vs Kediri) | L002 only |
| 2 | S001_seg02 | 5s | Medium shot Panji di balkon keraton, menatap ke arah Kediri | C001 + L001 |
| 3 | S001_seg03 | 5s | Close-up keris pusaka di tangan Panji, kilau senja | C001 + P001 |
| 4 | S001_seg04 | 5s | Cut: Candra Kirana di keraton seberang, menatap arah berlawanan | C002 + L003 |
| 5 | S001_seg05 | 5s | Wide shot: 2 perahu kerajaan bersilangan di tengah sungai | (none — silhouette shot) |
| 6 | S001_seg06 | 5s | Title card: "PANJI: ASMARA BANGUN" di atas sunrise river | (typography overlay) |

**Output yang diharapkan**:
- 6 T2I images (Dola AI free) — 1 per segmen
- 6 I2V clips 5 detik (opsional: Dola atau Flow kalau free trial, atau skip untuk prototype awal)
- 1 TTS narrator (edge-tts, 1 narasi gabungan ~15 detik total)
- 1 final video 30 detik (ffmpeg stitch)

**Kriteria validasi**:
- [ ] Konsistensi karakter Panji: wajah sama di segmen 2 & 3?
- [ ] Konsistensi lokasi Brantas: tone warna senja konsisten di segmen 1 & 5?
- [ ] Flow narasi: 6 segmen bercerita koheren dalam 30 detik?
- [ ] Quality image: cukup baik untuk dipakai sebagai sample ke investor?

---

## 5. Workflow Hybrid (Flow + Dola + Pipeline Kita)

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 4: PRA-PRODUKSI                                           │
│  ├─ Riset: master-era/2C-singasari-kediri.md (riset kita)     │
│  ├─ Asset lib: produksi/master-reff-t2i-prompts/2C-*/prompts/   │
│  │             K003-panji.txt, L002-keraton.txt, A002-keris.txt│
│  └─ Storyboard JSON: pra-produksi/prototype-30s/storyboard.json │
│      (schema v2 dengan adopsi Flow #1-#7)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Phase 5: T2I                                                    │
│  Opsi A: Dola AI (free unlimited, pakai prompt dari JSON)      │
│  Opsi B: Flow (free image, upload asset ref dari Phase 3)      │
│  └─ Output: 6 .jpg di produksi/t2i-output/ (gitignored)        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Phase 6: I2V (OPSIONAL untuk prototype awal)                   │
│  Opsi A: Dola (kalau ada)                                      │
│  Opsi B: Flow trial (kalau free credits cukup)                │
│  Opsi C: Skip — pakai Ken Burns effect di ffmpeg saja         │
│  └─ Output: 6 .mp4 5-detik di produksi/i2v-output/            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Phase 7: TTS                                                    │
│  edge-tts (free, voice id-ID-Ardi)                             │
│  └─ Output: 1 .mp3 narasi di produksi/tts-output/              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Phase 8: PASCA-PRODUKSI                                         │
│  ffmpeg: stitch 6 clips + audio + title card                   │
│  └─ Output: prototype-30s.mp4 di produksi/final/               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Yang TIDAK Diadopsi (Flow kurang, kita pertahankan)

| Item Flow | Status kita | Keputusan |
|---|---|---|
| `customStyleLibrary` kosong | Tidak ada | **Tidak adopsi** — kita pakai style keyword di prompt saja |
| Base64 embedded (file 56MB) | Tidak ada | **Tidak adopsi** — path-only (JSON < 500KB) |
| 1 ref image per asset | 5-angle K-files | **Tidak adopsi** — kita lebih kaya |
| UUID scene-id | "S001" string | **Tidak adopsi** — kita lebih readable |
| TTS layer | Tidak ada | Flow tidak punya — kita tetap pakai edge-tts |
| I2V layer | Tidak ada | Flow tidak punya — kita tetap pakai Dola/opsi lain |
| Timeline/duration field | Punya `durasi` | Flow tidak punya — kita lebih kaya |
| Shot metadata (size/lens) | Tidak ada | Flow juga tidak ada — skip untuk prototype, pertimbangkan di produksi panjang |

---

## 7. Next Steps

1. **Implementasi schema v2** — buat `prototype-30s/storyboard.json` baru dengan 6 segmen, pakai schema adopsi di atas.
2. **Ambil asset dari Phase 3 yang sudah ada** — karakter/lokasi/prop dari `2C-singasari-kediri/prompts/` yang sudah ada.
3. **Generate 6 T2I di Dola** (atau Flow) — verifikasi kualitas image sebelum lanjut ke I2V.
4. **Skip I2V untuk prototype awal** — pakai Ken Burns ffmpeg effect saja (free, cepat).
5. **TTS 1 narasi** via edge-tts.
6. **Stitch jadi 1 video 30 detik** via ffmpeg.
7. **Review + iterate** — kalau OK, scale up ke 3 menit (36 segmen pilot Panji lama) atau langsung ke produksi 10 menit.

**Tetap menjaga keunggulan riset kita**: setiap klaim dalam storyboard JSON wajib bisa ditelusuri ke `master-era/2C-singasari-kediri.md` dan sitasi `jilid-2/NN-bab-M.md`. Flow tidak punya riset sejarah — kita punya.
