#!/usr/bin/env python3
"""
Stitch 6 image storyboard + 6 TTS jadi 1 MP4 final via ffmpeg.
- Image: pakai Ken Burns effect (zoom/pan per segmen)
- Audio: TTS langsung (no BGM/SFX dulu, untuk prototype review)
- Duration: variable per segmen (ikuti TTS duration)
- Total video: ~37s (bukan 30s, karena TTS actual > 5s di beberapa segmen)
"""
import json
import subprocess
import os
from pathlib import Path

ROOT = Path("/home/z/my-project")
JSON_PATH = ROOT / "produksi/pra-produksi/prototype-30s/prototype-30s-v3.json"
TTS_DIR = ROOT / "produksi/tts-output/prototype-30s-v3"
IMAGE_DIR = ROOT / "download/dola-results"  # backup images
OUT_DIR = ROOT / "produksi/final"
OUT_DIR.mkdir(parents=True, exist_ok=True)
FINAL_MP4 = OUT_DIR / "prototype-30s-v3.mp4"
TEMP_DIR = ROOT / "download/temp-segments"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# Ken Burns effect mapping
# ============================================================
def get_ken_burns_filter(effect, duration_sec, target_w=1920, target_h=1080):
    """Return ffmpeg filter string for Ken Burns effect."""
    frames = int(duration_sec * 24)
    
    if effect == "zoom_in_slow":
        # Slow zoom-in 1.0x → 1.10x
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0008,1.10)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    elif effect == "zoom_in_medium":
        # Medium zoom-in 1.0x → 1.15x
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0012,1.15)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    elif effect == "zoom_in_fast":
        # Fast zoom-in 1.0x → 1.25x (snap zoom feel)
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0025,1.25)':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    elif effect == "zoom_out_slow":
        # Slow zoom-out 1.15x → 1.0x
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='if(eq(on,0),1.15,max(zoom-0.0008,1.0))':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    elif effect == "pan_up_slow":
        # Pan up: dari bawah ke atas (image height 2x target, pan vertically)
        # Pakai zoompan dengan x fixed, y berubah
        return f"scale={target_w*2}:{target_h*4}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*4},zoompan=z=1.0:x='iw/2-{target_w}/2':y='(ih-{target_h})*on/{frames}':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    elif effect == "arc_rotate_slow":
        # Simulate arc rotation: pan horizontal slowly (simplified, no real 3D rotation)
        return f"scale={target_w*2}:{target_h*2}:force_original_aspect_ratio=increase,crop={target_w*2}:{target_h*2},zoompan=z='min(zoom+0.0005,1.08)':x='iw/2-{target_w}/2+(iw-{target_w})*on/{frames}/2':y='ih/2-{target_h}/2':d={frames}:s={target_w}x{target_h}:fps=24,format=yuv420p"
    
    else:
        # Default: static (no Ken Burns)
        return f"scale={target_w}:{target_h}:force_original_aspect_ratio=increase,crop={target_w}:{target_h},format=yuv420p"


# ============================================================
# Build per-segment MP4 (image + TTS)
# ============================================================
def build_segment_mp4(seg, tts_duration):
    """Build 1 segment MP4: image with Ken Burns + TTS audio."""
    seg_id = seg["segment_id"]
    image_path = IMAGE_DIR / seg["t2i"]["image_path"].split("/")[-1]
    tts_path = TTS_DIR / f"{seg_id}.mp3"
    output_path = TEMP_DIR / f"{seg_id}.mp4"
    
    if not image_path.exists():
        print(f"  ❌ Image not found: {image_path}")
        return None
    
    if not tts_path.exists():
        print(f"  ❌ TTS not found: {tts_path}")
        return None
    
    # Get Ken Burns filter
    kb_effect = seg["t2i"]["ken_burns"]
    video_filter = get_ken_burns_filter(kb_effect, tts_duration)
    
    # Build ffmpeg command
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(image_path),
        "-i", str(tts_path),
        "-filter_complex", f"[0:v]{video_filter}[v]",
        "-map", "[v]",
        "-map", "1:a",
        "-t", str(tts_duration),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-shortest",
        str(output_path)
    ]
    
    print(f"  Building {seg_id}.mp4 (dur={tts_duration:.2f}s, ken_burns={kb_effect})")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ❌ Error: {result.stderr[-300:]}")
        return None
    
    print(f"  ✅ {output_path.name} ({output_path.stat().st_size // 1024} KB)")
    return output_path


# ============================================================
# Concat all segments
# ============================================================
def concat_segments(segment_paths, output_path):
    """Concat MP4 files using ffmpeg concat demuxer."""
    # Create concat list file
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
    if result.returncode != 0:
        print(f"❌ Concat error: {result.stderr[-300:]}")
        return False
    
    print(f"✅ Final MP4: {output_path}")
    return True


# ============================================================
# Main
# ============================================================
def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)
    
    print("=" * 70)
    print("STITCH PROTOTYPE 30s V3 — Image + TTS → MP4")
    print("=" * 70)
    print(f"JSON source: {JSON_PATH}")
    print(f"Image dir: {IMAGE_DIR}")
    print(f"TTS dir: {TTS_DIR}")
    print(f"Output: {FINAL_MP4}")
    print(f"Total segments: {len(data['segments'])}")
    print()
    
    # Build each segment
    segment_paths = []
    cumulative_time = 0
    updated_srt = []
    
    print("=== BUILD SEGMENTS ===")
    for i, seg in enumerate(data["segments"], 1):
        seg_id = seg["segment_id"]
        tts_path = TTS_DIR / f"{seg_id}.mp3"
        
        # Get actual TTS duration
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(tts_path)],
            capture_output=True, text=True
        )
        tts_duration = float(result.stdout.strip()) if result.stdout.strip() else 5.0
        
        # Add 0.3s padding at end for breathing room
        seg_duration = tts_duration + 0.3
        
        # Update SRT timing
        start_sec = cumulative_time
        end_sec = start_sec + seg_duration
        cumulative_time = end_sec
        
        def srt_fmt(s):
            h = int(s // 3600); m = int((s % 3600) // 60); sec = int(s % 60); ms = int((s % 1) * 1000)
            return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
        
        updated_srt.append({
            "segment_id": seg_id,
            "start": srt_fmt(start_sec),
            "end": srt_fmt(end_sec),
            "duration_seconds": seg_duration,
            "tts_duration": tts_duration
        })
        
        print(f"\n[{i}/{len(data['segments'])}] {seg_id}")
        print(f"  SRT: {srt_fmt(start_sec)} → {srt_fmt(end_sec)} (dur={seg_duration:.2f}s, TTS={tts_duration:.2f}s)")
        
        seg_path = build_segment_mp4(seg, seg_duration)
        if seg_path:
            segment_paths.append(seg_path)
    
    # Concat all segments
    print("\n=== CONCAT SEGMENTS ===")
    if concat_segments(segment_paths, FINAL_MP4):
        # Get final MP4 specs
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_format", "-show_streams",
             "-of", "json", str(FINAL_MP4)],
            capture_output=True, text=True
        )
        final_info = json.loads(result.stdout)
        final_duration = float(final_info["format"]["duration"])
        final_size = int(final_info["format"]["size"])
        video_stream = next(s for s in final_info["streams"] if s["codec_type"] == "video")
        audio_stream = next(s for s in final_info["streams"] if s["codec_type"] == "audio")
        
        print()
        print("=" * 70)
        print("FINAL MP4 SPECS")
        print("=" * 70)
        print(f"  Path: {FINAL_MP4}")
        print(f"  Duration: {final_duration:.2f}s")
        print(f"  Size: {final_size // 1024 // 1024} MB ({final_size // 1024} KB)")
        print(f"  Resolution: {video_stream['width']}x{video_stream['height']}")
        print(f"  FPS: {video_stream['r_frame_rate']}")
        print(f"  Video codec: {video_stream['codec_name']}")
        print(f"  Audio codec: {audio_stream['codec_name']}")
        print(f"  Audio bitrate: {int(audio_stream.get('bit_rate', 0)) // 1000}kbps")
        
        print()
        print("=== UPDATED SRT TIMING (auto-adjusted ke TTS actual) ===")
        for s in updated_srt:
            print(f"  {s['segment_id']:15s} {s['start']} → {s['end']} (dur={s['duration_seconds']:.2f}s, TTS={s['tts_duration']:.2f}s)")
        
        # Save updated SRT to JSON
        with open(TEMP_DIR / "_final_srt.json", "w") as f:
            json.dump(updated_srt, f, indent=2)
        
        print(f"\n✅ SRT updated saved: {TEMP_DIR / '_final_srt.json'}")
        print(f"✅ Final MP4 ready for user review: {FINAL_MP4}")


if __name__ == "__main__":
    main()
