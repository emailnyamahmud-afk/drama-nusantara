# Riset Platform I2V (Image-to-Video) — Free Tier Comparison 2026

**Tanggal**: 2026-10-23
**Tujuan**: Cari platform I2V gratis terbaik untuk prototype 30s KEN AROK (6 segmen × 5 detik)

---

## 📊 Comparison Matrix — Free I2V Platforms 2026

| Platform | Free Limit | Per Video | Watermark | Quality | Sign-up | Notes |
|---|---|---|---|---|---|---|
| **Dola AI (Seedance 2.5)** | Berbayar (credits) | ~60-120 credits per 5s | ❌ No | 1080p | Google | Butuh skill baru. User bisa "Gmail method" unlimited via multiple accounts |
| **Google Flow (Veo)** | **50 credits/hari** | ~5-10 credits per 5s | ❌ No | 1080p | Google | 50 credits = ~5-10 video per hari. Cukup untuk prototype 6 video |
| **Higgsfield AI** | **150 credits one-time** (signup) | ~12-110 per 5s (model dependent) | ❌ No | 720p-4K | Email | 150 credits = 1-12 video tergantung model. Seedance 2.0 720p = 22cr/5s |
| **Leonardo AI** | **150 tokens/day** (reset daily) | Variable | ⚠️ Mungkin | 720p | Email | Token habis cepat untuk video. Better untuk image |
| **ReelCine** | Free trial, no signup | Variable | ❌ No | 1080p | Tidak perlu | Free Seedance 2.5 tanpa sign-up, no watermark. Limit unclear |
| **ApiPass** | Free starter credits | Variable | ❌ No | Up to 4K | Email | Konsolidasi multi-model. 30-70% lebih murah dari official |
| **Dreamina (CapCut)** | Free trial | Variable | ⚠️ Mungkin | 1080p | Email | Seedance 2.5 available. Limit free unclear |
| **LTX Studio** | Free tier | Limited | ❌ No | 720p | Email | Open source model, self-hostable |

---

## 🎯 Rekomendasi untuk Prototype 30s (6 video × 5 detik)

### Strategi Prioritas (multi-platform fallback):

```
1. Cek limit Dola I2V dulu (kalau ada free credits)
   ↓ kalau habis
2. Google Flow (50 credits/hari = cukup 6 video)
   ↓ kalau abis hari ini
3. Higgsfield (signup fresh account = 150 credits = cukup)
   ↓ kalau habis
4. ReelCine (free no signup, no watermark)
   ↓ kalau limit
5. Buat akun baru Gmail + Leonardo / Dola
```

### Quick Math untuk 6 video × 5 detik:

| Platform | Butuh | Punya | Cukup? |
|---|---|---|---|
| Dola Seedance 2.5 | 6 × ~60cr = 360cr | Tergantung akun | ⚠️ Cek dulu |
| Google Flow Veo | 6 × 5-10cr = 30-60cr | 50cr/hari | ✅ Cukup |
| Higgsfield (fresh signup) | 6 × 22cr (Seedance 720p) = 132cr | 150cr | ✅ Cukup |
| Leonardo | 6 × ~25-50 tokens = 150-300 tokens | 150 tokens/day | ⚠️ Marginal |
| ReelCine | Tidak jelas | "Free trial" | ⚠️ Test dulu |

---

## 🏆 TOP 3 REKOMENDASI

### #1 Google Flow (Veo) — PALING PRAKTIS
- ✅ 50 credits/hari = cukup 6 video prototype
- ✅ Sudah ada di user (sudah pernah pakai)
- ✅ No watermark
- ✅ Quality 1080p bagus
- ⚠️ Reset harian, jadi kalau habis harus nunggu besok

### #2 Higgsfield AI — BACKUP UTAMA
- ✅ 150 credits one-time signup (cukup 6-12 video)
- ✅ Multiple model: Seedance, Kling, Veo, Sora 2, Wan
- ✅ Pricing transparan, credit cost jelas per model
- ✅ Quality pilihan: 720p / 1080p / 4K
- ⚠️ One-time, habis harus signup akun baru

### #3 Dola AI + Skill Baru — INVESTASI WORKFLOW
- ✅ Skill bisa reuse pattern dari T2I skill (sangat efisien dev)
- ✅ Workflow konsisten dengan T2I (sudah teruji)
- ⚠️ I2V mungkin berbayar — perlu cek dulu
- ⚠️ Kalau berbayar: cost per video bisa mahal untuk 6 clip

---

## 💰 Estimasi Cost Kalau Berbayar

| Platform | Cost per 5s video | 6 video (30s total) |
|---|---|---|
| Dola Seedance 2.5 | ~$0.10-0.30 | $0.60-1.80 |
| Google Flow Veo | ~$0.15-0.30 | $0.90-1.80 |
| Higgsfield Seedance 720p | ~$0.10 (22cr × $5/100cr) | $0.60 |
| Higgsfield Seedance 1080p | ~$0.27 (60cr × $5/100cr) | $1.62 |
| ApiPass (multi-model) | 30-70% lebih murah | $0.40-1.20 |

**Kalau perlu bayar**: Higgsfield Seedance 720p paling murah ($0.60 untuk 6 video).

---

## 🔍 Insight Penting

### Dola I2V — Cek dulu limit gratis
Dari hasil search, Dola AI pakai **Seedance 2.5** untuk video. Limit free unclear — beberapa source bilang:
- Free users dapat daily credits (jumlah tidak konsisten disebut)
- "Gmail Full Method" untuk unlimited via multiple accounts
- Mungkin ada free credits starter saat signup

**Action**: User cek di akun Dola sekarang — berapa credits yang tersedia. Kalau cukup 6 video, langsung pakai Dola dengan skill baru.

### Higgsfield — Paling Transparan
Pricing credit jelas:
- Seedance 2.0 720p: 22 credits per 5s
- Seedance 2.0 1080p: 60 credits per 5s  
- Kling 3.0 720p: 7 credits per 5s (paling murah!)
- Kling 3.0 1080p: 8 credits per 5s

**Untuk 6 video prototype**:
- Kling 3.0 720p: 6 × 7 = 42 credits (hemat!)
- Seedance 2.0 720p: 6 × 22 = 132 credits

Kling 3.0 720p paling worth — 42 credits saja untuk 6 video.

### Google Flow — Paling Familiar
User sudah pernah pakai Flow, jadi tidak perlu learning curve baru. 50 credits/hari = cukup untuk 5-10 video (tergantung model).

---

## 🛠️ Skill Design Recommendation

**Apakah perlu skill baru?** YA, dengan alasan:
1. Tool berbeda: image_gen → video_gen (atau video_edit)
2. Output berbeda: .jpg → .mp4
3. Parameter berbeda: tambah `duration_seconds`, `fps`, `motion_prompt`
4. Input berbeda: text + ref image → input image (dari T2I output)
5. Dependency berbeda: Phase 2 (T2I frame) → Phase 3 (I2V clip)

**Tapi konsep sama**: 1 batch JSON upload → skill generate semua video.

### Skill baru: `batch-video-generator`

**Reuse dari skill T2I**:
- ✅ parse_batch.py pattern (validator + dependency map)
- ✅ Phase-based execution (single phase untuk I2V — no dependency)
- ✅ Contact sheet (tapi untuk video → bikin contact GIF / thumbnail grid)
- ✅ Error handling (regenerate failed job)
- ✅ Output organization (path-based)

**Yang baru di skill I2V**:
- Input image dari `produksi/t2i-output/prototype-30s/*.jpg`
- Output video ke `produksi/i2v-output/prototype-30s/*.mp4`
- Parameter: `duration_seconds`, `fps`, `motion_prompt`, `input_image_path`
- QC: cek durasi video, file size, audio sync (kalau ada)

### Batch JSON I2V schema:

```json
{
  "schema_version": "1.0",
  "project": { ... },
  "phases": [{
    "phase_id": "phase_i2v",
    "name": "Generate Video Clips from Storyboard Frames",
    "parallel": true,
    "depends_on": null,
    "jobs": [
      {
        "job_id": "i2v-S001_seg01",
        "phase": "i2v",
        "segment_id": "S001_seg01",
        "input_image_path": "produksi/t2i-output/prototype-30s/S001_seg01.jpg",
        "motion_prompt": "Camera tracks rapidly backward ahead of Ken Arok, keeping him centered as foliage whips past frame edges",
        "duration_seconds": 5,
        "fps": 24,
        "model": "kling-3.0-720p",  // atau seedance-2.0-720p, atau pilihan user
        "output_path": "produksi/i2v-output/prototype-30s/S001_seg01.mp4",
        "notes": "Chase scene opening"
      },
      // ... 5 job lainnya
    ]
  }],
  "total_jobs": 6
}
```

---

## 📋 Action Plan

### Step 1 — Cek limit Dola I2V dulu
User buka akun Dola → cek credits available. Kalau cukup 6 video:
- Pakai Dola dengan skill baru (reuse pattern T2I)
- Investasi bikin skill, sekalian pakai untuk produksi lain

### Step 2 — Kalau Dola tidak cukup
Pilih berdasarkan prioritas:
1. **Google Flow** (kalau hari ini belum dipakai 50 credits)
2. **Higgsfield** signup fresh account (paling murah: Kling 3.0 720p)
3. **ReelCine** (free no signup, test limit)

### Step 3 — Generate I2V batch
Bikin `dola-batch-i2v.json` (atau `i2v-batch.json` platform-agnostic) + skill baru.

### Step 4 — Manual fallback (kalau skill belum siap)
Upload 6 image + motion prompt satu per satu ke platform pilihan.

---

## 🎯 Rekomendasi Final Saya

**Untuk prototype 30s KEN AROK** (6 video × 5 detik):

1. **CEK DOLA DULU** — kalau ada free credits ≥6 video, pakai Dola (skill baru, investasi workflow)
2. **Kalau Dola tidak cukup** → **Higgsfield fresh signup** + Kling 3.0 720p (42 credits total, paling hemat)
3. **Kalau malas signup** → **Google Flow** (kalau 50cr hari ini masih ada) atau **ReelCine** (test limit)

**Investasi skill baru**: WORTH IT kalau akan ada produksi panjang (pilot Panji 3 menit, era lain, dll). Skill T2I sudah terbukti hemat banyak waktu. Skill I2V dengan pattern sama bisa reuse 80% struktur.

---

## 📚 Sumber

- Dola AI: https://www.dola.com
- Higgsfield pricing: https://higgsfield.ai/pricing
- Higgsfield free: https://blog.segmind.com/higgsfield-ai-free-use
- Google Flow: https://flow.google.com
- Leonardo: https://leonardo.ai/pricing
- ReelCine (free no signup): https://reelcine.org
- ApiPass: https://apipass.dev
