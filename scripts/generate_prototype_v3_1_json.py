#!/usr/bin/env python3
"""
Generate prototype-30s-v3.1.json — JSON v3.1 sebagai TRUE single source of truth.

PERUBAHAN FUNDAMENTAL dari v3.0:
- v3.0 (SALAH): SRT 5s per segmen, TTS bebas → video ikut TTS = 37s (kompromi)
- v3.1 (BENAR): SRT per cue (bisa 4-7s), TTS ADAPTIF supaya FIT ke slot SRT

LOGIKA BARU:
1. SRT = GROUND TRUTH. Total = 30s exact.
2. TTS rate = ADAPTIF:
   - Default +25%
   - Kalau TTS@default > SRT slot → rate dinaikkan supaya muat
   - Kalau TTS@default < SRT slot → pakai default, pad silence di akhir
3. TTS TIDAK PERNAH dipotong. Kalau tidak muat walau rate +100%, split cue jadi 2.

SRT per cue (bukan rata 5s) — lebih natural untuk storytelling:
- seg01 (narasi panjang): 6s
- seg02 (dialog pendek): 4s
- seg03 (dialog pendek): 4s
- seg04 (ramalan panjang): 7s
- seg05 (narasi sedang): 5s
- seg06 (title card): 4s
Total: 30s exact
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
OUT = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.1.json"

# ============================================================
# Voice Profiles — TTS akan adaptive rate supaya fit ke SRT
# ============================================================
voice_profiles = {
    "narrator": {
        "edge_tts_voice": "id-ID-ArdiNeural",
        "language": "id",
        "default_rate": "+25%",
        "max_rate": "+100%",  # cap di 2x speed
        "default_pitch": "+0Hz"
    },
    "ken_arok": {
        "edge_tts_voice": "jv-ID-DimasNeural",
        "language": "jv",
        "default_rate": "+25%",
        "max_rate": "+100%",
        "default_pitch": "+2Hz"
    },
    "lohgawe": {
        "edge_tts_voice": "jv-ID-DimasNeural",
        "language": "jv",
        "default_rate": "+25%",
        "max_rate": "+100%",
        "default_pitch": "-4Hz"
    }
}

# ============================================================
# Episode Meta — SRT deterministik, total exactly 30s
# ============================================================
episode = {
    "id": "P002-PROTOTYPE-30S-V3.1",
    "title": "Ken Arok: Takdir dari Tumapel — Prototype 30s v3.1 (TRUE SoT)",
    "era": "2C Singasari-Kediri",
    "durasi_target_seconds": 30,  # EXACTLY 30s — no compromise
    "resolution": "1920x1080",
    "fps": 24,
    "schema_version": "3.1",
    "tts_strategy": "adaptive_rate",  # TTS rate adapt supaya fit ke SRT
    "notes": "JSON = TRUE source of truth. SRT deterministik. TTS adaptive. Video final = 30s exact."
}

# ============================================================
# SRT per cue (bukan rata 5s) — total 30s exact
# ============================================================
def srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# SRT plan: per cue natural (bukan rata 5s)
# Total must = 30s exact
seg_plan = [
    {"segment_id": "S001_seg01", "cue_duration": 6, "speaker": "narrator",  "ken_burns": "zoom_in_slow",     "scene_title": "Chase Through Dense Woods"},
    {"segment_id": "S001_seg02", "cue_duration": 4, "speaker": "ken_arok",  "ken_burns": "zoom_in_medium",   "scene_title": "Arok Taunts the Pursuers"},
    {"segment_id": "S001_seg03", "cue_duration": 4, "speaker": "lohgawe",   "ken_burns": "pan_up_slow",     "scene_title": "Brahmana Halts the Conflict"},
    {"segment_id": "S001_seg04", "cue_duration": 7, "speaker": "lohgawe",   "ken_burns": "arc_rotate_slow", "scene_title": "A Prophecy Unveiled"},
    {"segment_id": "S001_seg05", "cue_duration": 5, "speaker": "narrator",  "ken_burns": "zoom_in_fast",    "scene_title": "Arok Struck by Lightning"},
    {"segment_id": "S001_seg06", "cue_duration": 4, "speaker": "narrator",  "ken_burns": "zoom_out_slow",   "scene_title": "Title Card"}
]

# Verify total = 30s
total_srt = sum(s["cue_duration"] for s in seg_plan)
assert total_srt == 30, f"SRT total must be 30s, got {total_srt}s"

# ============================================================
# Naskah per segmen
# ============================================================
naskah = {
    "S001_seg01": "Tahun seribu dua ratus dua puluh dua masa Saka. Seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel, membawa hasil curian dari istana.",
    "S001_seg02": "Hanya segitu kecepatan prajurit istana? Kura-kura di rawa pun masih bisa mendahului kalian!",
    "S001_seg03": "Hentikan amarah kalian. Darah anak muda ini bukan untuk tumpah di tanah berlumpur ini.",
    "S001_seg04": "Aku tidak menaruh kasihan, Ken Arok. Aku menaruh ramalan. Dewa Wisnu tidak mengirimmu ke dunia fana hanya untuk menjadi pencuri rendahan.",
    "S001_seg05": "Mendengar ramalan itu, dadanya bergemuruh seolah dihantam halilintar. Ambisi gelap menyala dalam mata Ken Arok.",
    "S001_seg06": "Ken Arok: Takdir dari Tumapel."
}

# ============================================================
# Build segments
# ============================================================
segments = []
cumulative = 0
for sp in seg_plan:
    start_sec = cumulative
    end_sec = cumulative + sp["cue_duration"]
    cumulative = end_sec
    
    profile = voice_profiles[sp["speaker"]]
    
    segment = {
        "segment_id": sp["segment_id"],
        "scene_id": "S001",
        "scene_title": sp["scene_title"],
        "approved": False,
        
        # SRT TIMING — GROUND TRUTH, locked in JSON
        "srt_timing": {
            "start": srt_time(start_sec),
            "end": srt_time(end_sec),
            "cue_duration": sp["cue_duration"]
        },
        
        # TTS spec — adaptive rate akan dihitung saat generate
        "tts": {
            "speaker": sp["speaker"],
            "voice_profile": sp["speaker"],
            "edge_tts_voice": profile["edge_tts_voice"],
            "language": profile["language"],
            "default_rate": profile["default_rate"],
            "max_rate": profile["max_rate"],
            "pitch": profile["default_pitch"],
            "text": naskah[sp["segment_id"]],
            "actual_rate": None,  # akan diisi setelah test generate
            "actual_duration": None,  # akan diisi setelah generate
            "pad_silence_seconds": None,  # kalau TTS lebih pendek dari cue
            "output_path": f"produksi/tts-output/prototype-30s-v3.1/{sp['segment_id']}.mp3"
        },
        
        # T2I spec
        "t2i": {
            "image_path": f"produksi/t2i-output/prototype-30s/{sp['segment_id']}.jpg",
            "ken_burns": sp["ken_burns"],
            "resolution": "1920x1080"
        },
        
        # Audio layers
        "audio_layers": {
            "tts_volume": 1.0,
            "bgm_volume": 0.15,
            "sfx_volume": 0.30,
            "bgm_track": None,
            "sfx_track": None
        },
        
        "transition_out": {
            "type": "cross_dissolve",
            "duration_seconds": 0.3
        },
        
        "notes": f"SRT cue {sp['cue_duration']}s — TTS must FIT (adaptive rate)"
    }
    segments.append(segment)

# ============================================================
# Compile JSON
# ============================================================
prototype_v31 = {
    "schema_version": "3.1",
    "episode": episode,
    "voice_profiles": voice_profiles,
    "tts_strategy": {
        "method": "adaptive_rate",
        "default_rate": "+25%",
        "max_rate": "+100%",
        "logic": [
            "1. Generate TTS dengan default rate (+25%)",
            "2. Cek actual_duration vs srt_timing.cue_duration",
            "3. Kalau actual > cue: hitung rate_baru = (actual / cue) × 1.25, capped at 2.0 (max +100%)",
            "4. Re-generate TTS dengan rate_baru",
            "5. Kalau actual < cue: pad silence di akhir supaya = cue_duration",
            "6. Kalau walau rate +100% masih tidak muat → SPLIT cue jadi 2 (rare case)",
            "7. FINAL: TTS duration = cue_duration exact, no compromise"
        ]
    },
    "segments": segments,
    "render_status": {
        "total_segments": len(segments),
        "total_srt_duration": total_srt,
        "approved": 0,
        "tts_generated": 0,
        "video_stitched": False,
        "final_mp4_path": None,
        "final_mp4_duration": None  # MUST = 30s exact
    },
    "instructions": {
        "purpose": "JSON v3.1 = TRUE source of truth. SRT locked. TTS adaptive. Video final MUST = 30s.",
        "srt_is_ground_truth": "SRT timing DETERMINISTIK di JSON. TTS adjust dirinya supaya fit. Bukan sebaliknya.",
        "no_audio_cut": "TTS TIDAK PERNAH dipotong. Kalau text terlalu panjang, split cue atau speed up (capped 2x).",
        "no_overlap": "Kalau TTS lebih pendek dari cue, pad silence (fade out). Tidak ada audio overlap."
    }
}

# Write
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(prototype_v31, f, ensure_ascii=False, indent=2)

size_kb = OUT.stat().st_size / 1024
print(f"✅ Written: {OUT}")
print(f"   Size: {size_kb:.1f} KB")
print(f"   Schema: v3.1 (TRUE SoT — SRT deterministik, TTS adaptive)")
print(f"   Total SRT: {total_srt}s exact (target 30s) ✅")
print()
print("=== SRT TIMING PER CUE (not rata 5s) ===")
for s in segments:
    print(f"  {s['segment_id']:15s} {s['srt_timing']['start']} → {s['srt_timing']['end']} (cue={s['srt_timing']['cue_duration']}s) — {s['scene_title']}")
print()
print("=== STRATEGI TTS ADAPTIVE ===")
print("  Step 1: Generate TTS dengan rate +25% (default)")
print("  Step 2: Cek actual duration vs cue_duration")
print("  Step 3: Kalau TTS > cue → re-generate dengan rate = (tts/cue) × 1.25, capped 2.0")
print("  Step 4: Kalau TTS < cue → pad silence di akhir")
print("  Step 5: FINAL TTS duration = cue_duration exact")
