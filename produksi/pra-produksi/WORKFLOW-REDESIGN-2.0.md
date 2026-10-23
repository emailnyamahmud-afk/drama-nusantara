# Workflow Redesign — Produksi Pipeline 2.0

**Tanggal**: 2026-10-23
**Trigger**: User feedback setelah EP1 final — silent gaps issue + workflow terlalu berat di sandbox Z.ai

---

## 🎯 Masalah yang Ditemukan

### Issue 1: Silent Gaps
- 24 segmen × ~15s silence = **360s silence dari 720s total (50% dead air)**
- Root cause: cue_duration = 30s (arbitrary), TTS actual = ~15s, pad 15s per segmen
- Audience experience: "kok banyak jeda sunyi?"

### Issue 2: Workflow Terlalu Berat di Sandbox Z.ai
- Z.ai sandbox: TTS generation (25 file) + ffmpeg stitch (24 segmen) = ~5 menit execution, sering timeout
- Resource limited (memory, CPU, time)
- User tidak bisa iterate cepat (harus tunggu AI eksekusi)

---

## 🏗️ Workflow Redesign 2.0 — Sesuai Usulan User

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1-3: Z.AI CHAT (creative direction)                       │
│                                                                 │
│ 1. Susun naskah dari master-era                                 │
│    → Output: draft naskah .md                                   │
│                                                                 │
│ 2. User validasi + edit naskah (terutama dialog Jawa)          │
│    → Output: naskah final .md                                   │
│                                                                 │
│ 3. AI generate JSON (source of truth):                          │
│    - Voice profiles (karakter → edge-tts voice + rate + pitch)  │
│    - T2I prompts (master ref: karakter, lokasi, properti)       │
│    - Storyboard frame prompts (visual per segmen)               │
│    - SRT timing (DETERMINISTIK, locked)                          │
│    - Ken Burns effect per frame                                 │
│    - BGM track per scene                                        │
│    - SFX cues per segmen                                        │
│    → Output: dola-batch-{episode}.json                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: DOLA / GOOGLE FLOW (T2I generation)                    │
│                                                                 │
│ 4. User upload JSON ke Dola/Flow                                │
│    - Dola skill `batch-storyboard-generator` auto-trigger       │
│    - Atau Google Flow copy-paste JSON                           │
│    → Output: N image (master ref + storyboard frame)            │
│    → User download image ke MacBook                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 5-7: MACBOOK LOKAL (rendering — TUI tool)                │
│                                                                 │
│ 5. User run TUI tool di MacBook:                                │
│    `python3 nusantara-render.py`                                │
│                                                                 │
│    TUI menu:                                                    │
│    [1] Generate TTS (edge-tts, baca JSON voice profiles)        │
│    [2] Stitch image + TTS (ffmpeg Ken Burns)                    │
│    [3] Add BGM (YouTube Audio Library MP3)                      │
│    [4] Add SFX (Freesound MP3)                                  │
│    [5] Preview segmen (quick check per segmen)                 │
│    [6] Render final (concat all → MP4)                          │
│    [7] Iterate (re-render 1 segmen kalau perlu)                 │
│                                                                 │
│ 6. Tool baca JSON final v3.1 (source of truth)                  │
│    - Auto-detect image di folder t2i-output/                    │
│    - Auto-detect TTS di folder tts-output/                      │
│    - Auto-detect BGM di folder bgm-library/                     │
│    - Auto-detect SFX di folder sfx-library/                     │
│                                                                 │
│ 7. Output: episode-N.mp4 (final, dengan BGM + SFX)              │
│                                                                 │
│ Alternatif: User edit manual di DaVinci Resolve (free)         │
│ - Import image sequence + TTS + BGM                             │
│ - Fine-tune transitions, color grading, audio mixing            │
│ - Export final MP4                                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ TUI Tool Design — `nusantara-render.py`

### Tech Stack
- **Python 3** (sudah ada di MacBook)
- **`textual`** library untuk TUI (modern, responsive, tab-based)
- **`edge-tts`** untuk TTS (pip install, free unlimited)
- **`ffmpeg`** (sudah ada di macOS via Homebrew)
- **`PIL/Pillow`** untuk image QC (opsional)

### Struktur Folder di MacBook
```
drama-nusantara/  (repo lokal, sudah ada)
├── produksi/
│   ├── pra-produksi/
│   │   └── jaka-tingkir-series/
│   │       ├── EP1-NASKAH.md
│   │       ├── ep1-final-v3.1.json  ← SOURCE OF TRUTH
│   │       └── dola-batch-EP1-*.json
│   ├── t2i-output/  (di-gitignore, lokal)
│   │   └── jaka-tingkir-ep1/
│   │       ├── master-ref/  (15 image)
│   │       └── storyboard-frame/  (24 image)
│   ├── tts-output/  (di-gitignore, lokal)
│   │   └── jaka-tingkir-ep1/  (25 MP3)
│   ├── bgm-library/  ← NEW: BGM tracks dari YouTube Audio Library
│   │   ├── gamelan-ceremonial.mp3
│   │   ├── tense-tribal-percussion.mp3
│   │   ├── tragic-orchral.mp3
│   │   └── ominous-drone.mp3
│   ├── sfx-library/  ← NEW: SFX dari Freesound
│   │   ├── cannon-fire.mp3
│   │   ├── sword-clash.mp3
│   │   ├── crowd-shout.mp3
│   │   ├── heartbeat.mp3
│   │   └── gamelan-war.mp3
│   └── final/  (di-gitignore, lokal)
│       └── jaka-tingkir-ep1.mp4
├── scripts/
│   └── nusantara-render.py  ← TUI tool
└── nusantara-render.config.json  ← TUI config
```

### TUI Interface (textual-based)

```
┌─ Nusantara Render — EP1 Jaka Tingkir ──────────────────────────┐
│                                                                 │
│  [1] TTS Batch    [2] Image Stitch    [3] BGM Layer             │
│  [4] SFX Layer    [5] Preview         [6] Render Final          │
│  [7] Iterate      [8] Settings        [Q] Quit                  │
│                                                                 │
│  Status:                                                        │
│  ✓ Naskah: EP1-NASKAH.md (final, user edited)                   │
│  ✓ JSON: ep1-final-v3.1.json (24 segmen, 720s)                  │
│  ✓ Image: 24/24 storyboard frame ready                          │
│  ✓ TTS: 25/25 MP3 generated                                     │
│  ⚠ BGM: 0/4 tracks (need download from YouTube Audio Library)  │
│  ⚠ SFX: 0/5 effects (need download from Freesound)             │
│  ✗ Final: not rendered yet                                      │
│                                                                 │
│  > _                                                            │
└─────────────────────────────────────────────────────────────────┘
```

### Menu Details

#### [1] TTS Batch
```
Generate TTS per segmen dari JSON v3.1:
- Baca voice_profiles dari JSON
- Run edge-tts dengan adaptive rate (fit ke cue_duration)
- Output: tts-output/{episode}/*.mp3
- Status: 25/25 generated ✅

Options:
  [R] Re-generate single segmen (input segmen ID)
  [A] Re-generate all
  [V] Verify duration per segmen
```

#### [2] Image Stitch
```
Stitch image + TTS via ffmpeg Ken Burns:
- Baca ken_burns effect per segmen dari JSON
- Run ffmpeg per segmen (image + TTS + pad silence)
- Output: temp-segments/*.mp4
- Status: 24/24 segments built ✅

Options:
  [R] Re-build single segmen
  [A] Re-build all
  [P] Preview segmen (quick low-res render)
```

#### [3] BGM Layer
```
Add background music per scene:
- Baca bgm_track per scene dari JSON
- User select MP3 file from bgm-library/
- Mix: TTS (volume 1.0) + BGM (volume 0.15)
- Loop BGM if shorter than segmen
- Fade in/out per scene transition

Scene BGM mapping:
  Scene 1 (Pembuka): gamelan-ceremonial.mp3
  Scene 2 (Empat Putra): subtle-gamelan.mp3
  Scene 3 (Malaka Jatuh): tense-orchestral.mp3
  Scene 4 (Raden Yunus Serang): tribal-percussion.mp3
  Scene 5 (Raden Patah Wafat): solemn-gamelan.mp3
  Scene 6 (Kematian): ominous-drone.mp3
  Scene 7 (Cliffhanger): tense-drone.mp3

Options:
  [B] Browse bgm-library/
  [D] Download from YouTube Audio Library (link)
  [M] Manual mix settings (volume per track)
  [P] Preview with BGM
```

#### [4] SFX Layer
```
Add sound effects per segmen:
- Baca sfx_cues per segmen dari JSON
- User select MP3 file from sfx-library/
- Mix: TTS + BGM + SFX (volume 0.30)
- Position SFX at specific timestamp within segmen

SFX cues:
  EP1-S003-SEG01: cannon-fire.mp3 (at 5s)
  EP1-S004-SEG03: sword-clash.mp3 + cannon-fire.mp3
  EP1-S005-SEG03: heartbeat.mp3 (at 10s)
  EP1-S006-SEG01: mystical-drone.mp3

Options:
  [B] Browse sfx-library/
  [D] Download from Freesound (link)
  [M] Manual SFX placement
  [P] Preview with SFX
```

#### [5] Preview
```
Quick preview per segmen (low-res, fast render):
- Input: segmen ID (e.g., EP1-S001-SEG02)
- Render: image + TTS + BGM + SFX (low quality, 10s)
- Output: temp-preview.mp4
- Auto-play with system player

Options:
  [N] Next segmen
  [P] Previous segmen
  [F] Full quality render (slower)
```

#### [6] Render Final
```
Render final MP4 (full quality):
- Concat all 24 segmen
- Output: produksi/final/{episode}.mp4
- Specs: 1920x1080, 24fps, H.264, AAC

Progress:
  [████████████████████████████████████████] 100%
  Rendering segmen 24/24...
  Concat all segments...
  Final MP4: jaka-tingkir-ep1.mp4 (76 MB, 12 menit)

Options:
  [O] Open output folder
  [S] Share to download/prototypes/ (for GitHub push)
```

#### [7] Iterate
```
Re-render single segmen after fix:
- Input: segmen ID
- Choose what to fix:
  [T] Re-generate TTS (edit text in JSON first)
  [I] Re-generate image (re-upload prompt to Dola/Flow)
  [B] Change BGM track
  [S] Change SFX
  [K] Change Ken Burns effect
- Re-build segmen + auto-replace in final MP4
```

---

## 🎵 Solusi Silent Gaps — BGM Fill Strategy

### Approach: BGM continuous + TTS on top

```
Audio timeline per segmen:
┌─────────────────────────────────────────────┐
│ BGM (volume 0.15) ──────────────────────── │  ← continuous, fills silence
│ TTS (volume 1.0) ──────────                │  ← on top, starts at 0s
│ Silence pad ────────────────────           │  ← covered by BGM
└─────────────────────────────────────────────┘
       0s                    TTS end    cue_duration
```

**Result**: Silence gap jadi "BGM only moment" — natural, professional. Tidak ada "dead air" lagi.

### BGM Track per Scene (EP1)

| Scene | Mood | BGM Track (search di YouTube Audio Library) |
|---|---|---|
| 1 (Pembuka) | Epic, ceremonial | "Gamelan Ceremonial" or "Asian Ambient" |
| 2 (Empat Putra) | Calm, character intro | "Subtle Gamelan" or "Meditative Drone" |
| 3 (Malaka Jatuh) | Tragic, urgent | "Tense Orchestral" or "Dramatic Strings" |
| 4 (Raden Yunus Serang) | Epic, heroic, tragic | "Tribal Percussion" or "War Drums" |
| 5 (Raden Patah Wafat) | Somber, transition | "Solemn Gamelan" or "Funeral Drone" |
| 6 (Kematian) | Mysterious, tense | "Ominous Drone" or "Dissonant Gamelan" |
| 7 (Cliffhanger) | Tense, anticipatory | "Tense Drone" or "Suspense Ambient" |

### SFX Cues per Segmen (EP1)

| Segmen | SFX | Timestamp | Volume |
|---|---|---|---|
| S003-SEG01 (Malaka attack) | cannon fire | 5s | 0.30 |
| S003-SEG02 (Hang Tuah gugur) | sword clash + scream | 3s | 0.25 |
| S004-SEG02 (Yunus rally) | crowd cheer | 0s | 0.30 |
| S004-SEG03 (Pertempuran) | cannon + sword + chaos | continuous | 0.35 |
| S005-SEG03 (Pembunuhan) | heartbeat + keris sheath | 10s | 0.25 |
| S006-SEG01 (3 versi kematian) | mystical drone | 0s | 0.20 |

---

## 📋 JSON v3.2 — Updated Schema (BGM + SFX support)

```json
{
  "schema_version": "3.2",
  "episode": {...},
  "voice_profiles": {...},
  "bgm_library": {
    "gamelan-ceremonial": {"path": "bgm-library/gamelan-ceremonial.mp3", "source": "youtube_audio_library"},
    "tense-orchestral": {"path": "bgm-library/tense-orchestral.mp3", "source": "youtube_audio_library"},
    "tribal-percussion": {"path": "bgm-library/tribal-percussion.mp3", "source": "youtube_audio_library"}
  },
  "sfx_library": {
    "cannon-fire": {"path": "sfx-library/cannon-fire.mp3", "source": "freesound"},
    "sword-clash": {"path": "sfx-library/sword-clash.mp3", "source": "freesound"},
    "heartbeat": {"path": "sfx-library/heartbeat.mp3", "source": "freesound"}
  },
  "scenes": [
    {
      "scene_id": "EP1-S001",
      "bgm_track": "gamelan-ceremonial",
      "bgm_volume": 0.15,
      "bgm_fade_in": 2.0,
      "bgm_fade_out": 2.0
    }
  ],
  "segments": [
    {
      "segment_id": "EP1-S001-SEG01",
      "srt_timing": {...},
      "tts": {...},
      "image": {...},
      "audio_layers": {
        "tts_volume": 1.0,
        "bgm_volume": 0.15,
        "sfx_cues": [
          {"sfx_id": "cannon-fire", "timestamp": 5.0, "volume": 0.30}
        ]
      }
    }
  ]
}
```

---

## 🚀 Implementation Plan

### Step 1: Bikin TUI tool (AI Z.ai kerjakan, user run di MacBook)
- `scripts/nusantara-render.py` — TUI pakai `textual`
- Baca JSON v3.2 (source of truth)
- Menu: TTS batch, image stitch, BGM layer, SFX layer, preview, render final, iterate
- User run: `python3 scripts/nusantara-render.py`

### Step 2: Update JSON v3.2 schema (AI Z.ai kerjakan)
- Tambah field: `bgm_library`, `sfx_library`, `scenes[].bgm_track`, `segments[].audio_layers.sfx_cues`
- Backward compatible dengan v3.1 (field baru opsional)

### Step 3: Fix EP1 silent gaps (user run di MacBook)
- Download BGM dari YouTube Audio Library (4-7 tracks)
- Download SFX dari Freesound (5 effects)
- Run TUI tool → re-render EP1 dengan BGM + SFX
- Silent gaps hilang, replaced dengan BGM

### Step 4: Workflow untuk EP2-EP6
- Z.ai: susun naskah + generate JSON v3.2
- User: upload JSON ke Dola/Flow → generate image
- User: run TUI tool di MacBook → TTS + stitch + BGM + SFX → MP4 final
- Iterate kalau perlu, atau DaVinci Resolve untuk fine-tune

---

## 💰 Cost Analysis

| Komponen | Cost | Lokasi |
|---|---|---|
| Naskah + JSON (Z.ai) | $0 | Z.ai chat |
| T2I (Dola/Flow) | $0 | Dola/Flow |
| TTS (edge-tts) | $0 | MacBook lokal |
| ffmpeg stitch | $0 | MacBook lokal |
| BGM (YouTube Audio Library) | $0 | User download |
| SFX (Freesound) | $0 | User download |
| TUI tool (Python) | $0 | AI buat, user run |
| DaVinci Resolve | $0 (free version) | MacBook lokal |
| **Total per episode** | **$0** | |

---

## 🎯 Pilihan untuk User

### Opsi A — Bikin TUI tool sekarang (RECOMMENDED)
1. AI bikin `scripts/nusantara-render.py` (TUI pakai textual)
2. User download BGM + SFX
3. User run TUI tool di MacBook
4. Re-render EP1 dengan BGM → silent gaps hilang
5. Workflow siap untuk EP2-EP6

### Opsi B — Fix EP1 silent gaps dulu (quick fix)
1. Re-stitch EP1 dengan tighter cues (cue = TTS actual + 2s buffer)
2. Total durasi jadi ~400s (6.5 menit) — lebih pendek, tidak ada gap
3. Atau: tambah BGM manual via ffmpeg command (AI kasih script)
4. Tidak perlu TUI tool

### Opsi C — DaVinci Resolve manual
1. User import image sequence + TTS ke DaVinci
2. User add BGM + SFX manually
3. User export final MP4
4. Tidak perlu TUI tool, tapi user kerja manual

### Opsi D — Kombinasi
1. AI bikin TUI tool (Opsi A) — untuk workflow ke depan
2. Sambil itu, AI kasih ffmpeg script dengan BGM (Opsi B) — untuk fix EP1 sekarang
3. User pilih: pakai TUI tool atau DaVinci Resolve

---

## ❓ Pertanyaan untuk User

1. **Pilih opsi mana?** A (TUI tool), B (quick fix), C (DaVinci manual), D (kombinasi)
2. **BGM**: mau cari sendiri di YouTube Audio Library, atau AI kasih rekomendasi track + search keywords?
3. **SFX**: mau cari sendiri di Freesound, atau AI kasih list SFX yang dibutuhkan per segmen?
4. **TUI tool**: mau pakai `textual` (modern, responsive) atau `rich` (simpler, CLI-style)?
5. **Prioritas**: fix EP1 dulu, atau langsung setup workflow untuk EP2-EP6?

Saran: **Opsi D (kombinasi)** — AI bikin TUI tool sekaligus kasih ffmpeg script untuk fix EP1 sekarang. User bisa langsung test TUI tool dengan EP1, dan workflow siap untuk EP2-EP6.
