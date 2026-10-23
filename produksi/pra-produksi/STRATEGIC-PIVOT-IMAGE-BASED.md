# Strategic Pivot — Image-Based Pipeline untuk Produksi Panjang

**Tanggal**: 2026-10-23
**Decision**: Pivot dari I2V-based ke **Image + TTS + ffmpeg (Ken Burns)** untuk produksi panjang
**Status**: PROPOSED — menunggu konfirmasi user

---

## 1. Mengapa Pivot Ini Strategis

### Problem dengan I2V-based pipeline:
- ❌ **Tidak skalabel**: 10 menit = 600cr = 12 hari Flow atau $10 Higgsfield
- ❌ **Mahal untuk series**: 6 episode × 30 menit = $180+ atau 6 bulan free tier
- ❌ **Unpredictable**: AI random, tidak bisa pixel-perfect control
- ❌ **Iteration cost**: kalau ada yang jelek, burn credits lagi
- ❌ **Cloud-dependent**: harus online, tergantung platform availability

### Solution: Image + TTS + ffmpeg (Ken Burns)
- ✅ **Skalabel unlimited**: 1 menit atau 1 jam, cost sama = $0
- ✅ **Predictable**: hasil deterministik, bisa plan tepat
- ✅ **Iteration gratis**: edit image, re-stitch lokal, tanpa burn credits
- ✅ **Lokal**: ffmpeg di MacBook, tidak tergantung cloud
- ✅ **Industry-proven**: channel YouTube besar pakai teknik ini (Kings and Generals, History Time, dll)

---

## 2. Arsitektur Pipeline Final

```
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 1: SUMBER PRIMER (DONE ✅)                                   │
│   83 file MD Jilid I-V Kemenbud 2025                              │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 2: MASTER ERA (DONE ✅)                                      │
│   16 era rewrite lengkap, ~220.000 kata, 1.496 klaim              │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 3: MASTER REFF T2I (DONE ✅)                                  │
│   220 file prompt v2.1 (K/L/A/F/S) per era                        │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 4: PRA-PRODUKSI JSON (RE-ARCHITECTED 🆕)                     │
│   - Plan skenario: series / dokumenter / short                     │
│   - Tulis naskah per episode                                        │
│   - Breakdown per segmen dengan SRT timing                          │
│   - JSON = source of truth:                                         │
│     * naskah per segmen                                             │
│     * T2I prompt per segmen                                         │
│     * TTS spec per segmen (voice, emotion, timing SRT)              │
│     * Ken Burns effect per segmen (zoom direction, speed)          │
│     * Transition antar segmen (cut/dissolve/fade)                   │
│     * BGM track per scene                                           │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 5: T2I PRODUCTION (DONE untuk prototype ✅)                   │
│   - Dola AI / Google Flow (FREE UNLIMITED)                          │
│   - Skill `batch-storyboard-generator` (Dola)                       │
│   - Generate master ref + storyboard frame per segmen               │
│   - Output: .jpg di produksi/t2i-output/                            │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 6: TTS PRODUCTION (EXPANDED 🆕 — gabung dengan Phase 7 lama)  │
│   - edge-tts (FREE UNLIMITED)                                       │
│   - Voice profile per karakter (id-ID-Ardi, etc)                    │
│   - Generate TTS per segmen berdasarkan SRT timing                  │
│   - Output: .mp3 per segmen di produksi/tts-output/                 │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ Phase 7: PASCA-PRODUKSI (EXPANDED 🆕 — gabung dengan Phase 8 lama)   │
│   - ffmpeg lokal di MacBook                                         │
│   - Composite:                                                       │
│     * Image storyboard per segmen (Ken Burns effect)                │
│     * TTS audio per segmen                                          │
│     * BGM track per scene                                           │
│     * SFX layer (kalau perlu)                                        │
│     * Transition antar segmen (cut/dissolve/fade)                  │
│     * Title card / subtitle overlay                                 │
│   - Output: 1 MP4 final per episode                                │
│   - Lokasi: produksi/final/                                         │
└─────────────────────────────────────────────────────────────────────┘
```

**PERUBAHAN UTAMA**:
- ~~Phase 6 I2V~~ → **REMOVED** untuk produksi panjang (keep only untuk short-form opsional)
- ~~Phase 7 TTS~~ + ~~Phase 8 Stitch~~ → **MERGED jadi Phase 6+7 baru**

---

## 3. JSON Schema v3.0 — Untuk Image-Based Production

```json
{
  "schema_version": "3.0",
  "project": {
    "id": "P003-KEN-AROK-SERIES",
    "title": "Ken Arok: Takdir dari Tumapel — Series 6 Episode",
    "type": "series",
    "era": "2C Singasari-Kediri",
    "episodes": 6,
    "episode_duration_target_minutes": 10,
    "resolution": "1920x1080",
    "fps": 24
  },
  
  "voice_profiles": {
    "narrator": {"voice": "id-ID-Ardi", "speed": "1.0", "emotion": "neutral"},
    "ken_arok": {"voice": "id-ID-Ardi", "speed": "1.05", "emotion": "confident", "pitch": "+2"},
    "lohgawe": {"voice": "id-ID-Ardi", "speed": "0.95", "emotion": "wise", "pitch": "-3"},
    "tunggul_ametung": {"voice": "id-ID-Ardi", "speed": "0.95", "emotion": "cruel", "pitch": "-2"},
    "ken_dedes": {"voice": "id-ID-Gadis", "speed": "1.0", "emotion": "melancholic"}
  },
  
  "episodes": [
    {
      "episode_number": 1,
      "title": "Ramalan di Hutan Tumapel",
      "duration_target_seconds": 600,
      "scenes": [
        {
          "scene_id": "EP1-S001",
          "title": "Pengejaran di Hutan",
          "location_ref": "2C-L008-hutan-tumapel",
          "mood": "tense, defiant",
          "bgm_track": "tense_tribal_percussion.mp3",
          "color_palette": ["#8B4513", "#D2691E", "#F4A460"],
          "segments": [
            {
              "segment_id": "EP1-S001-SEG01",
              "duration_seconds": 8,
              
              "image": {
                "t2i_prompt": "Cinematic realistic extreme wide tracking shot, young Javanese man Ken Arok sprints through dense tropical teak forest...",
                "image_path": "produksi/t2i-output/ep1/S001-SEG01.jpg",
                "ken_burns": {
                  "effect": "zoom_in",
                  "start_zoom": 1.0,
                  "end_zoom": 1.15,
                  "pan_direction": "none",
                  "speed": "slow"
                }
              },
              
              "tts": {
                "speaker": "narrator",
                "text": "Tahun 1222 masa Saka. Seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel, membawa hasil curian dari istana.",
                "srt_start": "00:00:00,000",
                "srt_end": "00:00:08,000",
                "voice_profile": "narrator"
              },
              
              "transition_out": {
                "type": "cross_dissolve",
                "duration_seconds": 0.5
              }
            },
            // ... more segments
          ]
        }
      ]
    }
  ]
}
```

### Field baru di schema v3.0:
| Field | Fungsi |
|---|---|
| `voice_profiles{}` | Mapping karakter → voice setting edge-tts |
| `image.ken_burns{}` | Spec efek zoom/pan per image |
| `tts.srt_start` / `tts.srt_end` | Timing SRT untuk sinkronisasi |
| `tts.voice_profile` | Reference ke voice_profiles di atas |
| `transition_out{}` | Transition ke segmen berikutnya |
| `bgm_track` | Background music per scene |
| `color_palette[]` | Untuk color grading konsisten |

---

## 4. Hybrid Strategy — Kapan Pakai I2V vs Image-Based

| Skenario | Pakai I2V? | Alasan |
|---|---|---|
| Prototype 30 detik (sudah jadi) | ✅ Ya | Test pipeline, proof of concept |
| Trailer / teaser (60s) | ✅ Ya | High impact, low cost |
| TikTok / Reels / Shorts (<60s) | ✅ Ya | Native vertical format, social media |
| Intro / outro episode (10-15s) | ⚠️ Opsional | Kalau punya budget |
| Episode 10 menit | ❌ Tidak | Skalabilitas masalah |
| Dokumenter 30 menit | ❌ Tidak | Mahal, unpredictable |
| Series 6 episode | ❌ Tidak | Mustahil skalakan |
| Bulk production (10+ video/bulan) | ❌ Tidak | Cost prohibitive |

**Rule of thumb**: 
- ≤60s → I2V layak
- \>60s → image-based + Ken Burns

---

## 5. Update Workflow — Apa yang Sudah Jadi vs Perlu Baru

### ✅ Sudah Jadi (REUSE):
- Phase 1-3 (riset + master era + master reff) — semua reuse
- Phase 5 T2I skill Dola `batch-storyboard-generator` — reuse untuk image gen
- JSON schema v2.0 — base, perlu extend jadi v3.0
- 220 file prompt T2I per era — reuse
- 12 image prototype 30s — reuse sebagai sample untuk series

### 🆕 Perlu Dibuat:
1. **JSON schema v3.0** — tambah field SRT, Ken Burns, voice_profiles, transitions
2. **Script generator JSON v3.0** — `scripts/generate_series_json.py`
3. **Script edge-tts batch** — `scripts/generate_tts_batch.py` (loop per segmen)
4. **Script ffmpeg stitch** — `scripts/stitch_episode.py` (composite image + TTS + BGM + transitions)
5. **Library BGM tracks** — cari free music (YouTube Audio Library, Pixabay Music)
6. **Template naskah** per episode (10 menit standard struktur)

### 🆕 Skill Dola yang Perlu:
- ~~Skill I2V~~ → TIDAK PERLU (image-based, ffmpeg handle)
- Skill Dola T2I untuk **scene dengan multiple character** — bisa extend skill existing

---

## 6. Concrete Plan untuk Ken Arok Series (6 Episode × 10 Menit)

### Episode 1: Ramalan di Hutan Tumapel (10 menit = 600s)
- 4 scene, ~20 segmen × 30s rata-rata
- T2I: ~20 image storyboard + 6 master ref baru = 26 image (gratis Dola/Flow)
- TTS: ~20 narasi + dialog via edge-tts (gratis unlimited)
- BGM: 4 track (1 per scene) dari free library
- Stitch: 1 ffmpeg command di MacBook
- **Total cost**: $0
- **Estimasi waktu**: 2-3 hari kerja

### Episode 2-6: Reuse pattern
- Master ref (Ken Arok, Lohgawe, dll) sudah ada dari Episode 1
- Hanya generate storyboard frame baru per scene baru
- TTS per episode baru
- **Total cost per episode**: $0
- **Estimasi waktu per episode**: 1-2 hari kerja

### Series total (6 episode × 10 menit):
- **Total cost**: $0
- **Estimasi waktu**: 2-3 minggu kerja
- **Output**: 6 MP4 file, 60 menit total konten

### Perbandingan kalau pakai I2V untuk series ini:
- 6 ep × 600s = 3600s
- @ Flow 4cr/4s = 3600cr = 72 hari free tier atau ~$60 bayar
- @ Higgsfield = $60+
- **Image-based saves**: $60+ atau 72 hari kerja

---

## 7. Pertanyaan untuk User

Sebelum commit pivot ini, mohon konfirmasi:

1. **Setuju pivot ke image-based pipeline?**
   - I2V hanya untuk short-form opsional (trailer, teaser)
   - Image + TTS + ffmpeg jadi production approach utama

2. **Setuju dengan JSON schema v3.0?**
   - Add: voice_profiles, ken_burns, srt timing, transitions, bgm_track
   - Keep: existing schema v2.0 fields (linked_asset_ids, motion_prompt untuk reference, dll)

3. **Target produksi pertama**:
   - Episode 1 Ken Arok Series (10 menit)?
   - Atau dokumenter era 1A Prasejarah (10 menit)?
   - Atau scale up pilot Panji 3 menit dulu (sudah ada 36 segmen JSON)?

4. **Workflow naskah**:
   - AI Z.ai tulis naskah dari master-era docs?
   - User review + edit?
   - AI generate JSON v3.0 dari naskah final?

5. **BGM source**:
   - Pakai YouTube Audio Library (free)?
   - Pakai Pixabay Music (free)?
   - Generate AI music (Suno / Stable Audio)?

---

## 8. Next Actions (Kalau Setuju)

### Minggu ini:
1. ✅ Komit pivot strategis di repo (file ini)
2. 🆕 Tulis JSON schema v3.0 spec lengkap
3. 🆕 Bikin `scripts/generate_series_json.py` (template)
4. 🆕 Bikin `scripts/generate_tts_batch.py` (edge-tts loop)
5. 🆕 Bikin `scripts/stitch_episode.py` (ffmpeg composite)

### Minggu depan:
1. Pilih produksi pertama (Ken Arok Episode 1 atau yang lain)
2. Tulis naskah Episode 1 (AI Z.ai dari master-era/2C)
3. Generate JSON v3.0 dari naskah
4. Generate T2I via Dola skill (reuse)
5. Generate TTS via edge-tts
6. Stitch via ffmpeg
7. Review + iterate

### Series kerja (1-2 bulan):
- 6 episode Ken Arok Series jadi
- Pipeline terbukti skalabel
- Reusable untuk era lain (2A, 3A, 4A, dll)

---

## 9. Catatan Penting

- **Prototype 30s yang sudah jadi** (Dola seg01 + Flow seg04) = **bukan sia-sia**. Itu validasi pipeline Phase 1-5 berhasil. Skill Dola T2I terbukti jalan. JSON schema v2.0 terbukti bisa drive batch generation.
- **Skill Dola I2V** = **tidak dibuat**. Investasi waktu tidak worth untuk produksi panjang.
- **I2V platform research** = **keep sebagai reference**. Kalau nanti butuh trailer/teaser, bisa pakai Flow/Dola/Higgsfield.
- **JSON schema v3.0** = **backward compatible** dengan v2.0. Field lama tetap ada, field baru ditambahkan.

---

## 10. Kesimpulan

**User insight**: I2V tidak skalabel untuk produksi panjang. Image + TTS + ffmpeg adalah pendekatan industri-standard untuk dokumenter sejarah.

**AI agree 100%**. Matematika kebrutalan I2V tidak mendukung produksi panjang. Channel-channel besar (Kings and Generals, History Time) buktikan teknik image-based berjalan di scale.

**Action**: Komit pivot ini, mulai rancang JSON v3.0, plan produksi pertama.
