# Nusantara Render — TUI Tool Plan

**Tujuan**: Python TUI tool yang user run di MacBook untuk generate TTS + stitch image + ffmpeg → MP4.

**Workflow**:
```
Z.ai chat → naskah + JSON (source of truth)
Dola/Flow → generate image
MacBook → TUI tool: TTS + stitch → MP4 → DaVinci Resolve (BGM/SFX/final)
```

---

## BGM/SFX — DaVinci Resolve Studio

**DaVinci Resolve Studio punya built-in Fairlight Sound Library**:
- Ribuan SFX (cannon, sword, ambient, crowd, heartbeat, dll)
- Music beds (royalty-free, berbagai mood)
- Foley sounds
- Akses: Fairlight tab → Sound Library panel → browse + drag to timeline
- Tidak perlu download external. Tidak perlu API. Langsung pakai.

**Untuk BGM eksternal** (opsional):
| Source | API? | Cara |
|---|---|---|
| **DaVinci Fairlight (built-in)** | N/A | Langsung di DaVinci, free |
| YouTube Audio Library | ❌ No API | Manual download via YouTube Studio |
| Pixabay Music | ✅ API | https://pixabay.com/api/docs/ |
| Freesound | ✅ API (token) | https://freesound.org/docs/api/ |
| Jamendo | ✅ API | https://developer.jamendo.com/ |

**Rekomendasi**: Pakai DaVinci Fairlight built-in saja. TUI tool fokus ke TTS + stitch. BGM/SFX di DaVinci.

---

## TUI Tool — `nusantara-render.py`

### Dependencies (MacBook)
```bash
# Install once
pip3 install edge-tts rich
brew install ffmpeg
```

### Run
```bash
cd drama-nusantara
python3 scripts/nusantara-render.py
```

### Menu
```
[1] Generate TTS (edge-tts, baca JSON voice profiles)
[2] Stitch image + TTS (ffmpeg Ken Burns)
[3] Render final MP4 (concat all segmen)
[4] Preview single segmen
[5] Re-render single segmen (iterate)
[Q] Quit
```

### Input: JSON v3.1 (source of truth)
TUI baca `produksi/pra-produksi/jaka-tingkir-ep1/ep1-final-v3.1.json`:
- segments[] dengan srt_timing, tts spec, image path, ken_burns
- voice_profiles{} (karakter → edge-tts voice + rate + pitch)

### Output
```
produksi/tts-output/jaka-tingkir-ep1/*.mp3  (TTS per segmen)
produksi/final/jaka-tingkir-ep1.mp4         (MP4 final)
```

### Silent Gaps Fix
- TUI pakai approach **tighter cues**: cue_duration = TTS actual + 2s buffer
- Total durasi = sum of (TTS + 2s) per segmen ≈ 400-450s (7-8 menit, bukan 12 menit)
- Tidak ada dead air. Natural pacing.
- Kalau mau 12 menit exact: tambah BGM di DaVinci (BGM fill gaps)

### Alternatif: DaVinci Resolve
- TUI export image sequence + TTS audio per segmen
- User import ke DaVinci → add BGM/SFX → fine-tune → export final
- Full creative control di DaVinci
