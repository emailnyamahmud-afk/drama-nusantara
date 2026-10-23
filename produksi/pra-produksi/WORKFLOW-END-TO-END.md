# Workflow End-to-End — Pipeline Drama Nusantara (v3.1)

**Tanggal**: 2026-10-23
**Tujuan**: Jelasin workflow end-to-end supaya user paham alur lengkap dari idea → MP4 final.

---

## 🎯 Konsep Inti — JSON = Single Source of Truth

```
JSON (ground truth)
  ↓
  Berisi: naskah + SRT timing + T2I spec + TTS spec + audio layers + transitions
  ↓
  Output (T2I, TTS, MP4) = DERIVED dari JSON
  ↓
  Kalau output jelek = FIX JSON, bukan fix output
```

**Aturan emas**:
- ✅ JSON dulu, baru output
- ❌ Bukan output dulu, baru JSON di-adjust (kompromi)
- ❌ Bukan "TTS actual lebih panjang, ya udah video jadi 37s"

---

## 📊 Pipeline 7 Phase (image-based)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 1: SUMBER PRIMER ✅                                            │
│ 83 file MD Jilid I-V Kemenbud 2025                                  │
│ Status: Done. Tidak perlu sentuh lagi.                              │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 2: MASTER ERA ✅                                               │
│ 16 era rewrite lengkap, ~220.000 kata, 1.496 klaim dengan sitasi   │
│ Status: Done. Tinggal dipakai sebagai source naskah.                │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 3: MASTER REFF T2I ✅                                          │
│ 220 file prompt v2.1 (K/L/A/F/S) per era                            │
│ Status: Done. Dipakai saat Phase 5 (T2I batch).                     │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 4: PRA-PRODUKSI JSON ⭐ SINGLE SOURCE OF TRUTH                 │
│                                                                      │
│ JSON berisi (per segmen):                                            │
│ - Naskah (text dialog/narasi)                                       │
│ - SRT timing (cue_duration — DETERMINISTIK, locked)                 │
│ - T2I spec (image path + Ken Burns effect)                          │
│ - TTS spec (voice, rate adaptive, pitch)                            │
│ - Audio layers (TTS + BGM + SFX volume)                            │
│ - Transitions (cut/dissolve/fade)                                    │
│                                                                      │
│ User approve per segmen — fix 1 segmen = tidak redo semua           │
│ Status: Prototype 30s v3.1 done. Series EP1 todo.                   │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 5: T2I PRODUCTION (output dari JSON)                           │
│ Pakai Dola skill `batch-storyboard-generator` (atau Google Flow)    │
│ Generate image per segmen sesuai T2I spec di JSON                   │
│ Output: .jpg per segmen                                             │
│ Status: 12 image untuk prototype 30s sudah ada.                    │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 6: TTS PRODUCTION (output dari JSON, ADAPTIVE)                │
│ edge-tts (free unlimited, native Jawa: Dimas/Siti Neural)           │
│                                                                      │
│ ADAPTIVE RATE: TTS auto-adjust supaya FIT ke SRT cue:               │
│ 1. Generate dengan default rate (+25%)                              │
│ 2. Kalau TTS > cue → re-generate dengan rate lebih cepat           │
│    rate_new = (tts_actual / cue) × 1.25, capped at 2.0 (max +100%) │
│ 3. Kalau TTS < cue → pakai default, pad silence di akhir           │
│ 4. FINAL: TTS duration ≤ cue_duration, no cut, no overlap          │
│                                                                      │
│ Output: .mp3 per segmen                                             │
│ Status: 6 TTS untuk prototype 30s v3.1 done.                       │
└──────────────────────────────────────────────────────────────────────┘
                                ↓
┌──────────────────────────────────────────────────────────────────────┐
│ Phase 7: PASCA-PRODUKSI (output dari JSON + Phase 5 + 6)            │
│ ffmpeg lokal di MacBook                                             │
│                                                                      │
│ Per segmen:                                                          │
│ - Image (Phase 5) + Ken Burns effect (spec dari JSON)               │
│ - TTS audio (Phase 6) + pad silence supaya = cue_duration           │
│ - (Future: BGM + SFX layer)                                         │
│ - Transition out (cross_dissolve 0.3s)                              │
│ - Duration = cue_duration EXACT (sesuai SRT)                        │
│                                                                      │
│ Concat semua segmen → 1 MP4 final                                   │
│ FINAL duration = total SRT (30s exact untuk prototype)              │
│                                                                      │
│ Kalau perlu fine-tune → DaVinci Resolve (free)                      │
│ Status: Prototype 30s v3.1 done — 30.04s, 9 MB, 1920×1080.        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Logika SRT + TTS Adaptive — Detail

### v3.0 (LAMA — SALAH):
```
JSON: 6 segmen × 5s = 30s (SRT rata-rata)
  ↓
TTS generate dengan rate +25% (fixed)
  ↓
TTS actual: 7.46s, 5.95s, 5.78s, 9.02s, 6.43s, 2.52s (bebas)
  ↓
❌ Video duration = TTS actual + 0.3s padding (KOMPROMI)
  ↓
Hasil: 37.22s (BUKAN 30s sesuai SRT)
```

### v3.1 (BARU — BENAR):
```
JSON: SRT per cue (6s+4s+4s+7s+5s+4s) = 30s exact
  ↓
TTS generate dengan default rate +25%
  ↓
Cek TTS actual vs cue_duration:
  ↓
Kalau TTS > cue → ADAPTIVE: re-generate dengan rate = (tts_actual / cue) × 1.25
  Kalau TTS < cue → pakai default, pad silence
  ↓
TTS final: FIT ke cue_duration (no cut, no overlap)
  ↓
Video per segmen = cue_duration EXACT
  ↓
Concat → 30s EXACT (sesuai SRT)
```

### Hasil v3.1:
| Seg | Cue | TTS Default | TTS Adaptive Rate | TTS Actual | Pad | Status |
|---|---|---|---|---|---|---|
| 1 | 6s | 7.46s (+25%) | **+61%** | 5.81s | 0.19s | FIT ✅ |
| 2 | 4s | 5.95s (+25%) | **+96%** | 3.82s | 0.18s | FIT ✅ |
| 3 | 4s | 5.78s (+25%) | **+90%** | 3.82s | 0.18s | FIT ✅ |
| 4 | 7s | 9.02s (+25%) | **+66%** | 6.82s | 0.18s | FIT ✅ |
| 5 | 5s | 6.22s (+25%) | **+62%** | 4.80s | 0.20s | FIT ✅ |
| 6 | 4s | 2.52s (+25%) | +25% (default) | 2.52s | 1.48s | FIT ✅ |
| **Total** | **30s** | - | - | **27.58s** | **2.42s** | **30s exact** |

---

## 📁 File Final v3.1

| File | Lokasi | Size | Isi |
|---|---|---|---|
| JSON SoT | `produksi/pra-produksi/prototype-30s/prototype-30s-v3.1.json` | 10 KB | Source of truth |
| TTS adaptive | `produksi/tts-output/prototype-30s-v3.1/*.mp3` | 6 file, ~170 KB | Audio FIT ke cue |
| **MP4 final** | `produksi/final/prototype-30s-v3.1.mp4` | 9 MB | **30.04s, 1920×1080** |
| Review copy | `download/prototypes/prototype-30s-v3.1.mp4` | 9 MB | Bisa di-push ke GitHub |

---

## 🚀 Cara Pakai Pipeline (Reusable untuk Produksi Lain)

### Untuk prototype 30s (done):
```bash
# 1. Generate JSON v3.1 (single source of truth)
python3 scripts/generate_prototype_v3_1_json.py

# 2. Generate TTS adaptive
python3 scripts/generate_tts_adaptive_v3.1.py

# 3. Stitch final MP4
python3 scripts/stitch_prototype_v3.1.py

# Output: produksi/final/prototype-30s-v3.1.mp4 (30s exact)
```

### Untuk produksi panjang (Ken Arok Series EP1 10 menit):
```bash
# 1. Tulis naskah EP1 (AI dari master-era/2C)
# 2. Bikin JSON v3.1 dengan ~20 segmen × ~30s = 600s = 10 menit
# 3. Generate T2I via Dola skill (batch)
# 4. Generate TTS adaptive (auto-fit ke cue)
# 5. Stitch via ffmpeg → MP4 10 menit
# 6. Copy ke download/prototypes/ untuk review
# Cost: $0
# Estimasi: 2-4 jam per episode
```

---

## 🔧 Kalau Ada Yang Perlu Fix (Iterasi)

### Skenario 1: Naskah dialog kurang bagus
```bash
# Edit field tts.text di JSON v3.1 untuk segmen itu
# Re-generate TTS untuk segmen itu saja
python3 scripts/generate_tts_adaptive_v3.1.py  # (modify untuk run 1 segmen)
# Re-stitch
python3 scripts/stitch_prototype_v3.1.py
```

### Skenario 2: Image storyboard kurang baik
```bash
# Edit t2i_prompt di JSON
# Re-generate image via Dola skill (upload dola-batch.json)
# Re-stitch
```

### Skenario 3: TTS terlalu cepat (rate > +80% jadi ngebut)
```bash
# Split cue jadi 2 (rare case)
# Atau extend cue_duration di SRT (rebalance total ke 30s)
# Atau pendekkan naskah (edit text di JSON)
```

### Skenario 4: SRT timing perlu adjust (mis. seg04 terlalu padat)
```bash
# Edit cue_duration di JSON
# Verifikasi total tetap 30s
# Re-generate TTS adaptive (rate akan recalculate)
# Re-stitch
```

---

## 💡 Insight Penting

1. **JSON = ground truth, output mengikuti**. Bukan sebaliknya.
2. **SRT timing deterministik**. TTS yang adaptif supaya FIT ke SRT.
3. **TTS adaptive rate** memastikan tidak ada audio terpotong atau overlap.
4. **Per segmen approval** — fix 1 segmen tanpa redo semua.
5. **Cost $0** untuk any length. Skalabel untuk series panjang.
6. **Reusable scripts** — `generate_prototype_v3_1_json.py`, `generate_tts_adaptive_v3.1.py`, `stitch_prototype_v3.1.py` bisa dipakai untuk produksi lain.

---

## 🎯 Next Step

Setelah user review MP4 v3.1 (30s exact):

1. **Kalau OK** → scale up ke Ken Arok Series EP1 (10 menit)
2. **Kalau ada yang perlu adjust** → fix di JSON v3.1, re-generate TTS, re-stitch
3. **Kalau mau tambah BGM/SFX** → add bgm_track + sfx_track di JSON, modify stitch script untuk amix 3 layers

Sekarang JSON v3.1 + TTS adaptive + MP4 30s sudah konsisten. Workflow end-to-end terbukti jalan dengan logika yang benar.
