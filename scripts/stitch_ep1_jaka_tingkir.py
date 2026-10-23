#!/usr/bin/env python3
"""
Compile JSON final v3.1 EP1 + ffmpeg stitch → MP4 EP1 final.

Input:
- 24 storyboard frame images (1920x1080)
- 25 TTS MP3 files (1 segmen split jadi 2 voice)

Output:
- produksi/pra-produksi/jaka-tingkir-series/ep1-final-v3.1.json (SoT)
- produksi/final/jaka-tingkir-ep1.mp4 (12 menit, 1920x1080, 24fps, H.264+AAC)

Approach:
- 24 segmen, SRT deterministik, total 720s exact
- Setiap segmen: image (Ken Burns) + TTS audio (pad silence to cue_duration)
- SEG02 (Raden Patah + Narrator): gabung 2 TTS jadi 1 audio
- Concat 24 segmen → 1 MP4 final
"""
import json
import subprocess
import os
import shutil
from pathlib import Path

ROOT = Path("/home/z/my-project")
IMAGE_DIR = ROOT / "produksi/t2i-output/jaka-tingkir-ep1/storyboard-frame"
TTS_DIR = ROOT / "produksi/tts-output/jaka-tingkir-ep1"
OUT_DIR = ROOT / "produksi/final"
OUT_DIR.mkdir(parents=True, exist_ok=True)
FINAL_MP4 = OUT_DIR / "jaka-tingkir-ep1.mp4"
TEMP_DIR = ROOT / "download/jaka-tingkir-ep1-segments"
TEMP_DIR.mkdir(parents=True, exist_ok=True)
JSON_FINAL = ROOT / "produksi/pra-produksi/jaka-tingkir-ep1/ep1-final-v3.1.json"
JSON_FINAL.parent.mkdir(parents=True, exist_ok=True)


# ============================================================
# 24 Segmen — SRT deterministik, total 720s
# ============================================================
def srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# SRT plan (sesuai naskah EP1)
SEGMENTS_PLAN = [
    # Scene 1 — Pembuka (90s)
    {"segment_id": "EP1-S001-SEG01", "cue_duration": 20, "scene": "S001", "speaker": "Narrator",
     "tts_files": ["EP1-S001-SEG01.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S001-SEG02", "cue_duration": 35, "scene": "S001", "speaker": "Raden Patah + Narrator",
     "tts_files": ["EP1-S001-SEG02.mp3", "EP1-S001-SEG02-narrator.mp3"], "ken_burns": "pan_right_slow"},
    {"segment_id": "EP1-S001-SEG03", "cue_duration": 35, "scene": "S001", "speaker": "Narrator",
     "tts_files": ["EP1-S001-SEG03.mp3"], "ken_burns": "zoom_in_slow"},
    # Scene 2 — Empat Putra (90s)
    {"segment_id": "EP1-S002-SEG01", "cue_duration": 30, "scene": "S002", "speaker": "Narrator",
     "tts_files": ["EP1-S002-SEG01.mp3"], "ken_burns": "pan_right_slow"},
    {"segment_id": "EP1-S002-SEG02", "cue_duration": 30, "scene": "S002", "speaker": "Narrator",
     "tts_files": ["EP1-S002-SEG02.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S002-SEG03", "cue_duration": 30, "scene": "S002", "speaker": "Narrator",
     "tts_files": ["EP1-S002-SEG03.mp3"], "ken_burns": "zoom_out_slow"},
    # Scene 3 — Malaka Jatuh (120s)
    {"segment_id": "EP1-S003-SEG01", "cue_duration": 30, "scene": "S003", "speaker": "Narrator",
     "tts_files": ["EP1-S003-SEG01.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S003-SEG02", "cue_duration": 30, "scene": "S003", "speaker": "Narrator",
     "tts_files": ["EP1-S003-SEG02.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S003-SEG03", "cue_duration": 30, "scene": "S003", "speaker": "Narrator",
     "tts_files": ["EP1-S003-SEG03.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S003-SEG04", "cue_duration": 30, "scene": "S003", "speaker": "Narrator",
     "tts_files": ["EP1-S003-SEG04.mp3"], "ken_burns": "zoom_in_slow"},
    # Scene 4 — Raden Yunus Serang (150s)
    {"segment_id": "EP1-S004-SEG01", "cue_duration": 30, "scene": "S004", "speaker": "Narrator",
     "tts_files": ["EP1-S004-SEG01.mp3"], "ken_burns": "pan_right_slow"},
    {"segment_id": "EP1-S004-SEG02", "cue_duration": 30, "scene": "S004", "speaker": "Raden Yunus",
     "tts_files": ["EP1-S004-SEG02.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S004-SEG03", "cue_duration": 40, "scene": "S004", "speaker": "Narrator",
     "tts_files": ["EP1-S004-SEG03.mp3"], "ken_burns": "zoom_in_fast"},
    {"segment_id": "EP1-S004-SEG04", "cue_duration": 30, "scene": "S004", "speaker": "Narrator",
     "tts_files": ["EP1-S004-SEG04.mp3"], "ken_burns": "zoom_out_slow"},
    {"segment_id": "EP1-S004-SEG05", "cue_duration": 20, "scene": "S004", "speaker": "Narrator",
     "tts_files": ["EP1-S004-SEG05.mp3"], "ken_burns": "zoom_out_slow"},
    # Scene 5 — Raden Patah Wafat (90s)
    {"segment_id": "EP1-S005-SEG01", "cue_duration": 30, "scene": "S005", "speaker": "Narrator",
     "tts_files": ["EP1-S005-SEG01.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S005-SEG02", "cue_duration": 30, "scene": "S005", "speaker": "Narrator",
     "tts_files": ["EP1-S005-SEG02.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S005-SEG03", "cue_duration": 30, "scene": "S005", "speaker": "Narrator",
     "tts_files": ["EP1-S005-SEG03.mp3"], "ken_burns": "zoom_in_slow"},
    # Scene 6 — Kematian Detail (120s)
    {"segment_id": "EP1-S006-SEG01", "cue_duration": 30, "scene": "S006", "speaker": "Narrator",
     "tts_files": ["EP1-S006-SEG01.mp3"], "ken_burns": "zoom_in_slow"},
    {"segment_id": "EP1-S006-SEG02", "cue_duration": 30, "scene": "S006", "speaker": "Narrator",
     "tts_files": ["EP1-S006-SEG02.mp3"], "ken_burns": "zoom_out_slow"},
    {"segment_id": "EP1-S006-SEG03", "cue_duration": 30, "scene": "S006", "speaker": "Narrator",
     "tts_files": ["EP1-S006-SEG03.mp3"], "ken_burns": "pan_right_slow"},
    {"segment_id": "EP1-S006-SEG04", "cue_duration": 30, "scene": "S006", "speaker": "Narrator",
     "tts_files": ["EP1-S006-SEG04.mp3"], "ken_burns": "zoom_in_slow"},
    # Scene 7 — Cliffhanger (60s)
    {"segment_id": "EP1-S007-SEG01", "cue_duration": 30, "scene": "S007", "speaker": "Narrator",
     "tts_files": ["EP1-S007-SEG01.mp3"], "ken_burns": "cross_fade"},
    {"segment_id": "EP1-S007-SEG02", "cue_duration": 30, "scene": "S007", "speaker": "Narrator",
     "tts_files": ["EP1-S007-SEG02.mp3"], "ken_burns": "pan_right_slow"},
]


def get_ken_burns_filter(effect, duration_sec, target_w=1920, target_h=1080):
    """Return ffmpeg filter string for Ken Burns effect."""
    frames = int(duration_sec * 24)
    
    if effect == "zoom_in_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0008,1.10)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_in_fast":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0025,1.25)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_out_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='if(eq(on,0),1.15,max(zoom-0.0008,1.0))':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "pan_right_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z=1.0:x='iw/2-{target_w}/2+(iw-{target_w})*on/{frames}/2':y='ih/2-{target_h}/2':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "cross_fade":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0005,1.08)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    else:
        return f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},format=yuv420p"


def concat_tts_files(tts_paths, output_path):
    """Concat multiple TTS files jadi 1 (untuk SEG02 yang punya 2 voice)."""
    if len(tts_paths) == 1:
        shutil.copy(tts_paths[0], output_path)
        return
    
    # Concat list
    list_path = output_path.parent / f"{output_path.stem}_concat_list.txt"
    with open(list_path, "w") as f:
        for p in tts_paths:
            f.write(f"file '{p}'\n")
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    list_path.unlink()
    return result.returncode == 0


def build_segment_mp4(seg, tts_combined_path, tts_duration):
    """Build 1 segment MP4: image (Ken Burns) + TTS audio + pad silence = cue_duration."""
    seg_id = seg["segment_id"]
    image_path = IMAGE_DIR / f"{seg_id}.jpg"
    output_path = TEMP_DIR / f"{seg_id}.mp4"
    
    cue_duration = seg["cue_duration"]
    
    if not image_path.exists():
        print(f"  ❌ Image not found: {image_path}")
        return None
    
    if not tts_combined_path.exists():
        print(f"  ❌ TTS not found: {tts_combined_path}")
        return None
    
    kb_effect = seg["ken_burns"]
    video_filter = get_ken_burns_filter(kb_effect, cue_duration)
    
    # Audio: pad silence di akhir supaya = cue_duration
    audio_filter = f"[1:a]apad=whole_dur={cue_duration}[a]"
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(image_path),
        "-i", str(tts_combined_path),
        "-filter_complex", f"[0:v]{video_filter}[v];{audio_filter}",
        "-map", "[v]",
        "-map", "[a]",
        "-t", str(cue_duration),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        str(output_path)
    ]
    
    print(f"  Building {seg_id} (cue={cue_duration}s, kb={kb_effect}, tts={tts_duration:.2f}s)")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ❌ Error: {result.stderr[-300:]}")
        return None
    
    # Verify duration
    verify = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(output_path)],
        capture_output=True, text=True
    )
    actual_dur = float(verify.stdout.strip()) if verify.stdout.strip() else 0
    size_kb = output_path.stat().st_size // 1024
    print(f"  ✅ {output_path.name} — actual={actual_dur:.2f}s, size={size_kb}KB")
    return output_path


def concat_segments(segment_paths, output_path):
    """Concat MP4 files."""
    list_path = TEMP_DIR / "concat_list.txt"
    with open(list_path, "w") as f:
        for p in segment_paths:
            f.write(f"file '{p}'\n")
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(list_path),
        "-c", "copy",
        str(output_path)
    ]
    
    print(f"\nConcat → {output_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def main():
    print("=" * 70)
    print("STITCH EP1 JAKA TINGKIR — 24 SEGMENTS → MP4 FINAL")
    print("=" * 70)
    print(f"Image dir: {IMAGE_DIR}")
    print(f"TTS dir: {TTS_DIR}")
    print(f"Output: {FINAL_MP4}")
    print(f"Target duration: 720s (12 menit)")
    print()
    
    # Step 1: Prepare TTS per segmen (concat kalau perlu)
    print("=== STEP 1: Prepare TTS per segmen ===")
    segment_paths = []
    srt_records = []
    cumulative = 0
    updated_json_segments = []
    
    for i, seg in enumerate(SEGMENTS_PLAN, 1):
        seg_id = seg["segment_id"]
        cue_duration = seg["cue_duration"]
        
        # Combine multiple TTS files kalau perlu
        tts_paths = [TTS_DIR / f for f in seg["tts_files"]]
        tts_combined = TEMP_DIR / f"{seg_id}_tts.mp3"
        
        if len(tts_paths) > 1:
            print(f"  [{i}/24] {seg_id} — concat {len(tts_paths)} TTS files")
            concat_tts_files(tts_paths, tts_combined)
        else:
            shutil.copy(tts_paths[0], tts_combined)
        
        # Get TTS duration
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(tts_combined)],
            capture_output=True, text=True
        )
        tts_duration = float(r.stdout.strip()) if r.stdout.strip() else 0
        
        # SRT timing
        start_sec = cumulative
        end_sec = start_sec + cue_duration
        cumulative = end_sec
        
        srt_records.append({
            "segment_id": seg_id,
            "start": srt_time(start_sec),
            "end": srt_time(end_sec),
            "duration": cue_duration,
            "tts_duration": tts_duration
        })
        
        print(f"  SRT: {srt_time(start_sec)} → {srt_time(end_sec)} (cue={cue_duration}s, tts={tts_duration:.2f}s)")
    
    # Step 2: Build each segment MP4
    print("\n=== STEP 2: Build segment MP4 (image + TTS + Ken Burns) ===")
    for i, seg in enumerate(SEGMENTS_PLAN, 1):
        seg_id = seg["segment_id"]
        cue_duration = seg["cue_duration"]
        tts_combined = TEMP_DIR / f"{seg_id}_tts.mp3"
        
        # Get TTS duration
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(tts_combined)],
            capture_output=True, text=True
        )
        tts_duration = float(r.stdout.strip()) if r.stdout.strip() else 0
        
        print(f"\n[{i}/24] {seg_id}")
        seg_path = build_segment_mp4(seg, tts_combined, tts_duration)
        if seg_path:
            segment_paths.append(seg_path)
    
    # Step 3: Concat all segments
    print(f"\n=== STEP 3: Concat {len(segment_paths)} segments ===")
    if concat_segments(segment_paths, FINAL_MP4):
        # Verify final
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_format", "-show_streams",
             "-of", "json", str(FINAL_MP4)],
            capture_output=True, text=True
        )
        final_info = json.loads(result.stdout)
        final_duration = float(final_info["format"]["duration"])
        final_size = int(final_info["format"]["size"])
        video = next(s for s in final_info["streams"] if s["codec_type"] == "video")
        audio = next(s for s in final_info["streams"] if s["codec_type"] == "audio")
        
        print()
        print("=" * 70)
        print("✅ FINAL MP4 — EP1 JAKA TINGKIR")
        print("=" * 70)
        print(f"  Path: {FINAL_MP4}")
        print(f"  Duration: {final_duration:.2f}s (target: 720s)")
        print(f"  Match SRT: {'✅ YES' if abs(final_duration - 720) < 1 else '❌ NO'}")
        print(f"  Size: {final_size // 1024 // 1024} MB ({final_size // 1024} KB)")
        print(f"  Resolution: {video['width']}x{video['height']}")
        print(f"  FPS: {video['r_frame_rate']}")
        print(f"  Video: {video['codec_name']}, Audio: {audio['codec_name']}")
        
        # Copy to download for user access
        review_path = ROOT / "download/prototypes/jaka-tingkir-ep1.mp4"
        shutil.copy(FINAL_MP4, review_path)
        print(f"\n📥 Review copy: {review_path}")
        
        # Save SRT updated
        srt_path = TEMP_DIR / "_final_srt.json"
        with open(srt_path, "w") as f:
            json.dump(srt_records, f, indent=2)
        print(f"📄 SRT records: {srt_path}")
        
        # Save JSON final v3.1
        json_final = {
            "schema_version": "3.1",
            "episode": {
                "id": "JT-S1-EP1",
                "title": "Jaka Tingkir EP1: Demak Berdiri, Malaka Jatuh",
                "era": "3B Demak-Pajang (1499-1550 M)",
                "duration_target_seconds": 720,
                "resolution": "1920x1080",
                "fps": 24,
                "schema_version": "3.1",
                "tts_strategy": "adaptive_rate",
                "date_created": "2026-10-23"
            },
            "segments": [
                {
                    "segment_id": s["segment_id"],
                    "srt_timing": {
                        "start": s["start"],
                        "end": s["end"],
                        "cue_duration": s["duration"]
                    },
                    "tts": {
                        "duration": s["tts_duration"],
                        "pad_silence": max(0, s["duration"] - s["tts_duration"])
                    },
                    "image": {
                        "path": f"produksi/t2i-output/jaka-tingkir-ep1/storyboard-frame/{s['segment_id']}.jpg",
                        "ken_burns": seg["ken_burns"]
                    }
                }
                for s, seg in zip(srt_records, SEGMENTS_PLAN)
            ],
            "render_status": {
                "total_segments": len(SEGMENTS_PLAN),
                "total_srt_duration": 720,
                "final_mp4_path": str(FINAL_MP4),
                "final_mp4_duration": final_duration,
                "rendered": True
            }
        }
        
        with open(JSON_FINAL, "w", encoding="utf-8") as f:
            json.dump(json_final, f, ensure_ascii=False, indent=2)
        print(f"\n📄 JSON final v3.1: {JSON_FINAL}")


if __name__ == "__main__":
    main()
