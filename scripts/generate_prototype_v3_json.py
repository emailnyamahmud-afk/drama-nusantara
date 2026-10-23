#!/usr/bin/env python3
"""
Generate prototype-30s-v3.json — JSON v3.0 sebagai single source of truth.
Berisi: naskah + SRT timing + T2I spec + TTS spec per segmen.

SRT timing deterministik — kunci waktu TTS start, tidak peduli rate TTS.
User review per segmen, fix 1 segmen kalau perlu tanpa redo semua.

Rate TTS: +25% (1.25x) — user ideal setelah feedback (1.0 terlalu lambat, 1.5 agak cepat)
"""

import json
from pathlib import Path

ROOT = Path("/home/z/my-project")
OUT = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.json"

# ============================================================
# Voice Profiles (rate +25% default)
# ============================================================
voice_profiles = {
    "narrator": {
        "edge_tts_voice": "id-ID-ArdiNeural",
        "language": "id",
        "default_rate": "+25%",  # 1.25x
        "default_pitch": "+0Hz",
        "purpose": "Narrator Indonesia netral, tempo 1.25x"
    },
    "ken_arok": {
        "edge_tts_voice": "jv-ID-DimasNeural",
        "language": "jv",
        "default_rate": "+25%",
        "default_pitch": "+2Hz",
        "purpose": "Ken Arok muda confident, Jawa halus, tempo 1.25x"
    },
    "lohgawe": {
        "edge_tts_voice": "jv-ID-DimasNeural",
        "language": "jv",
        "default_rate": "+25%",
        "default_pitch": "-4Hz",
        "purpose": "Dang Hyang Lohgawe tua bijak, Jawa halus, tempo 1.25x"
    }
}

# ============================================================
# Episode Meta
# ============================================================
episode = {
    "id": "P002-PROTOTYPE-30S-V3",
    "title": "Ken Arok: Takdir dari Tumapel — Prototype 30s (Image-Based v3.0)",
    "era": "2C Singasari-Kediri (abad 11-13 M)",
    "jilid_sumber": "2",
    "sumber_tambahan": "master-era/2C-singasari-kediri.md + Pararaton",
    "durasi_target_seconds": 30,
    "resolution": "1920x1080",
    "fps": 24,
    "style": "cinematic realistic, Javanese period drama",
    "schema_version": "3.0",
    "date_created": "2026-10-23",
    "tts_default_rate": "+25%",  # 1.25x
    "notes": "Prototype 30s dengan JSON v3.0 — naskah + SRT + T2I + TTS terintegrasi. Pipeline image-based (no I2V)."
}

# ============================================================
# Segments — SRT timing deterministik (5s per segmen)
# ============================================================
# SRT format: HH:MM:SS,mmm
def srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

segments = []
seg_duration = 5  # 5 detik per segmen

# Daftar segmen dengan naskah final
seg_data = [
    {
        "segment_id": "S001_seg01",
        "scene_title": "Chase Through Dense Woods",
        "scene_id": "S001",
        "tts_speaker": "narrator",
        "tts_text": "Tahun seribu dua ratus dua puluh dua masa Saka. Seorang pemuda bernama Ken Arok berlari menerobos hutan Tumapel, membawa hasil curian dari istana.",
        "t2i_image": "S001_seg01.jpg",
        "ken_burns": "zoom_in_slow"  # slow zoom-in untuk establish scene
    },
    {
        "segment_id": "S001_seg02",
        "scene_title": "Arok Taunts the Pursuers",
        "scene_id": "S001",
        "tts_speaker": "ken_arok",
        "tts_text": "Hanya segitu kecepatan prajurit istana? Kura-kura di rawa pun masih bisa mendahului kalian!",
        "t2i_image": "S001_seg02.jpg",
        "ken_burns": "zoom_in_medium"
    },
    {
        "segment_id": "S001_seg03",
        "scene_title": "Brahmana Halts the Conflict",
        "scene_id": "S001",
        "tts_speaker": "lohgawe",
        "tts_text": "Hentikan amarah kalian. Darah anak muda ini bukan untuk tumpah di tanah berlumpur ini.",
        "t2i_image": "S001_seg03.jpg",
        "ken_burns": "pan_up_slow"
    },
    {
        "segment_id": "S001_seg04",
        "scene_title": "A Prophecy Unveiled",
        "scene_id": "S001",
        "tts_speaker": "lohgawe",
        "tts_text": "Aku tidak menaruh kasihan, Ken Arok. Aku menaruh ramalan. Dewa Wisnu tidak mengirimmu ke dunia fana hanya untuk menjadi pencuri rendahan.",
        "t2i_image": "S001_seg04.jpg",
        "ken_burns": "arc_rotate_slow"
    },
    {
        "segment_id": "S001_seg05",
        "scene_title": "Arok Struck by Lightning",
        "scene_id": "S001",
        "tts_speaker": "narrator",
        "tts_text": "Mendengar ramalan itu, dadanya bergemuruh seolah dihantam halilintar. Sebuah ambisi gelap menyala dalam mata Ken Arok.",
        "t2i_image": "S001_seg05.jpg",
        "ken_burns": "zoom_in_fast"  # snap zoom feel
    },
    {
        "segment_id": "S001_seg06",
        "scene_title": "Title Card",
        "scene_id": "S001",
        "tts_speaker": "narrator",
        "tts_text": "Ken Arok: Takdir dari Tumapel.",
        "t2i_image": "S001_seg06.jpg",
        "ken_burns": "zoom_out_slow"
    }
]

# Build segments with SRT timing
for i, sd in enumerate(seg_data):
    start_sec = i * seg_duration
    end_sec = start_sec + seg_duration
    
    profile = voice_profiles[sd["tts_speaker"]]
    
    segment = {
        "segment_id": sd["segment_id"],
        "scene_id": sd["scene_id"],
        "scene_title": sd["scene_title"],
        "approved": False,  # user approval flag
        
        # SRT timing — DETERMINISTIK, dikunci di sini
        "srt_timing": {
            "start": srt_time(start_sec),
            "end": srt_time(end_sec),
            "duration_seconds": seg_duration
        },
        
        # TTS spec
        "tts": {
            "speaker": sd["tts_speaker"],
            "voice_profile": sd["tts_speaker"],
            "edge_tts_voice": profile["edge_tts_voice"],
            "language": profile["language"],
            "rate": profile["default_rate"],
            "pitch": profile["default_pitch"],
            "text": sd["tts_text"],
            "output_path": f"produksi/tts-output/prototype-30s-v3/{sd['segment_id']}.mp3"
        },
        
        # T2I spec (image already generated)
        "t2i": {
            "image_path": f"produksi/t2i-output/prototype-30s/{sd['t2i_image']}",
            "backup_path": f"download/dola-results/{sd['t2i_image']}",  # sandbox backup
            "ken_burns": sd["ken_burns"],
            "resolution": "1920x1080"
        },
        
        # Audio layers (BGM + SFX untuk production)
        "audio_layers": {
            "tts_volume": 1.0,
            "bgm_volume": 0.15,  # subtle background
            "sfx_volume": 0.30,
            "bgm_track": None,  # to be added: download from YouTube Audio Library
            "sfx_track": None
        },
        
        # Transition
        "transition_out": {
            "type": "cross_dissolve" if i < len(seg_data) - 1 else "fade_to_black",
            "duration_seconds": 0.3
        },
        
        # Notes
        "user_notes": "",
        "production_notes": f"Segment {i+1}/6 — {sd['scene_title']}"
    }
    
    segments.append(segment)

# ============================================================
# Compile JSON
# ============================================================
prototype_v3 = {
    "schema_version": "3.0",
    "episode": episode,
    "voice_profiles": voice_profiles,
    "segments": segments,
    "render_status": {
        "total_segments": len(segments),
        "approved": 0,
        "tts_generated": 0,
        "video_stitched": False,
        "final_mp4_path": None
    },
    "instructions": {
        "purpose": "JSON v3.0 sebagai single source of truth. Naskah + SRT + T2I + TTS terintegrasi per segmen.",
        "approval_workflow": "User approve per segmen — fix 1 segmen tanpa redo semua",
        "srt_deterministic": "SRT timing dikunci di JSON. TTS start time = SRT start. Tidak peduli rate TTS.",
        "tts_rate": "+25% (1.25x) default — user ideal setelah feedback (1.0 lambat, 1.5 cepat)",
        "pipeline": [
            "1. Generate TTS per segmen (rate +25%)",
            "2. Stitch image + TTS via ffmpeg dengan Ken Burns effect",
            "3. Output final MP4 untuk review user",
            "4. Kalau ada segmen yang kurang, fix field di JSON, re-generate segmen itu saja"
        ]
    }
}

# Write
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(prototype_v3, f, ensure_ascii=False, indent=2)

# Stats
size_kb = OUT.stat().st_size / 1024
print(f"✅ Written: {OUT}")
print(f"   Size: {size_kb:.1f} KB")
print(f"   Segments: {len(segments)}")
print(f"   Total duration: {len(segments) * seg_duration}s = {len(segments) * seg_duration / 60:.1f} menit")
print(f"   TTS rate: +25% (1.25x)")
print()
print("=== SRT TIMING (DETERMINISTIK) ===")
for s in segments:
    print(f"  {s['segment_id']:15s} {s['srt_timing']['start']} → {s['srt_timing']['end']} ({s['srt_timing']['duration_seconds']}s) — {s['tts']['speaker']:10s} — {s['scene_title']}")
print()
print("=== NASKAH PER SEGMEN ===")
for s in segments:
    print(f"\n[{s['segment_id']}] {s['scene_title']}")
    print(f"  Speaker: {s['tts']['speaker']} ({s['tts']['edge_tts_voice']}, rate {s['tts']['rate']})")
    print(f"  Text: \"{s['tts']['text']}\"")
    print(f"  Image: {s['t2i']['image_path']}")
    print(f"  Ken Burns: {s['t2i']['ken_burns']}")
