#!/usr/bin/env python3
"""
Stitch MP4 final untuk v3.1 — exactly 30s sesuai SRT.
Setiap segment: image (Ken Burns) + TTS audio + pad silence supaya = cue_duration.
"""
import json
import subprocess
from pathlib import Path

ROOT = Path("/home/z/my-project")
JSON_PATH = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.1.json"
TTS_DIR = ROOT / "produksi/tts-output/prototype-30s-v3.1"
IMAGE_DIR = ROOT / "download/dola-results"
OUT_DIR = ROOT / "produksi/final"
OUT_DIR.mkdir(parents=True, exist_ok=True)
FINAL_MP4 = OUT_DIR / "prototype-30s-v3.1.mp4"
TEMP_DIR = ROOT / "download/temp-segments-v3.1"
TEMP_DIR.mkdir(parents=True, exist_ok=True)


def get_ken_burns_filter(effect, duration_sec, target_w=1920, target_h=1080):
    """Return ffmpeg filter string for Ken Burns effect."""
    frames = int(duration_sec * 24)
    
    if effect == "zoom_in_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0008,1.10)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_in_medium":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0012,1.15)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_in_fast":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0025,1.25)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "zoom_out_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='if(eq(on,0),1.15,max(zoom-0.0008,1.0))':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "pan_up_slow":
        return f"scale={target_w*2}:{target_h*4}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*4},zoompan=z=1.0:x='iw/2-{target_w}/2':y='(ih-{target_h})*on/{frames}':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    elif effect == "arc_rotate_slow":
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0005,1.08)':x='iw/2-{target_w}/2+(iw-{target_w})*on/{frames}/2':y='ih/2-{target_h}/2':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    else:
        return f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},format=yuv420p"


def build_segment_mp4(seg):
    """Build 1 segment MP4 with exactly cue_duration."""
    seg_id = seg["segment_id"]
    image_path = IMAGE_DIR / seg["t2i"]["image_path"].split("/")[-1]
    tts_path = TTS_DIR / f"{seg_id}.mp3"
    output_path = TEMP_DIR / f"{seg_id}.mp4"
    
    cue_duration = seg["srt_timing"]["cue_duration"]
    tts_duration = seg["tts"]["actual_duration"]
    pad_silence = seg["tts"].get("pad_silence_seconds", 0)
    
    if not image_path.exists() or not tts_path.exists():
        print(f"  ❌ Missing files for {seg_id}")
        return None
    
    # Ken Burns filter
    kb_effect = seg["t2i"]["ken_burns"]
    video_filter = get_ken_burns_filter(kb_effect, cue_duration)
    
    # Audio filter: pad silence di akhir supaya = cue_duration
    # Kalau TTS < cue: append silence (apad)
    # Kalau TTS ≈ cue: no pad needed
    if pad_silence > 0:
        # Audio: TTS + silence pad → exactly cue_duration
        audio_filter = f"[1:a]apad=whole_dur={cue_duration}[a]"
    else:
        # TTS already ≈ cue, just use as is, but trim to exactly cue_duration
        audio_filter = f"[1:a]atrim=duration={cue_duration}[a]"
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(image_path),
        "-i", str(tts_path),
        "-filter_complex", f"[0:v]{video_filter}[v];{audio_filter}",
        "-map", "[v]",
        "-map", "[a]",
        "-t", str(cue_duration),  # EXACTLY cue_duration
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        str(output_path)
    ]
    
    print(f"  Building {seg_id}.mp4 (cue={cue_duration}s, tts={tts_duration:.2f}s, pad={pad_silence:.2f}s)")
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
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)
    
    print("=" * 70)
    print("STITCH V3.1 — EXACTLY 30s (SRT = GROUND TRUTH)")
    print("=" * 70)
    print(f"Target duration: 30s exact (no compromise)")
    print()
    
    print("=== BUILD SEGMENTS (each = cue_duration exact) ===")
    segment_paths = []
    total_actual = 0
    for i, seg in enumerate(data["segments"], 1):
        print(f"\n[{i}/{len(data['segments'])}] {seg['segment_id']}")
        seg_path = build_segment_mp4(seg)
        if seg_path:
            segment_paths.append(seg_path)
            # Get actual
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(seg_path)],
                capture_output=True, text=True
            )
            total_actual += float(result.stdout.strip())
    
    print(f"\n=== CONCAT ALL SEGMENTS ===")
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
        print("✅ FINAL MP4 — EXACTLY 30s (SRT GROUND TRUTH)")
        print("=" * 70)
        print(f"  Path: {FINAL_MP4}")
        print(f"  Duration: {final_duration:.2f}s (target: 30s)")
        print(f"  Match SRT: {'✅ YES' if abs(final_duration - 30) < 0.5 else '❌ NO'}")
        print(f"  Size: {final_size // 1024 // 1024} MB ({final_size // 1024} KB)")
        print(f"  Resolution: {video['width']}x{video['height']}")
        print(f"  FPS: {video['r_frame_rate']}")
        print(f"  Video: {video['codec_name']}, Audio: {audio['codec_name']}")
        
        # Copy to download/prototypes/ for user access
        review_path = ROOT / "download/prototypes/prototype-30s-v3.1.mp4"
        import shutil
        shutil.copy(FINAL_MP4, review_path)
        print(f"\n📥 Review copy: {review_path}")


if __name__ == "__main__":
    main()
